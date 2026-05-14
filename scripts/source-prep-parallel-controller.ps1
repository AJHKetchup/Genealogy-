param(
    [string]$Root = "C:\Users\Big Al\Documents\Genealogy",
    [int]$MaxWorkers = 4,
    [int]$BatchPages = 4,
    [int]$QueueLimit = 40,
    [int]$PollSeconds = 90,
    [int]$RunMinutes = 0,
    [int]$StaleMinutes = 180,
    [int]$FastLaneLimit = 250,
    [int]$FastLaneScanLimit = 2500,
    [switch]$SkipFastLane,
    [switch]$Once
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = (Resolve-Path -LiteralPath $Root).Path
$env:PYTHONPATH = (Join-Path $Root "src")
$QueueDir = Join-Path $Root "research\_agent-queues"
$PromptDir = Join-Path $QueueDir "parallel-worker-prompts"
$LogDir = Join-Path $QueueDir "parallel-worker-logs"
$StatePath = Join-Path $QueueDir "parallel-controller-state.json"
New-Item -ItemType Directory -Force -Path $PromptDir, $LogDir | Out-Null

function Invoke-GenealogyWiki {
    param([string[]]$Arguments)
    $commandOutput = & python -m historic_doc_ingest.genealogy_wiki @Arguments 2>&1
    $exitCode = $LASTEXITCODE
    foreach ($line in $commandOutput) {
        Write-Host $line
    }
    if ($exitCode -ne 0) {
        throw "genealogy-wiki failed: $($Arguments -join ' ')"
    }
}

function Read-JsonFile {
    param([string]$Path, [object]$Default)
    if (-not (Test-Path -LiteralPath $Path)) {
        return $Default
    }
    $raw = Get-Content -LiteralPath $Path -Raw
    if ([string]::IsNullOrWhiteSpace($raw)) {
        return $Default
    }
    return $raw | ConvertFrom-Json
}

function Save-ControllerState {
    param([object[]]$Workers)
    $payload = [ordered]@{
        updated = [DateTime]::UtcNow.ToString("s") + "Z"
        root = $Root
        max_workers = $MaxWorkers
        active_workers = @($Workers)
    }
    $payload | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $StatePath -Encoding UTF8
}

function Get-TaskStateMap {
    $statePath = Join-Path $QueueDir "task-state.json"
    $payload = Read-JsonFile -Path $statePath -Default ([pscustomobject]@{ tasks = [pscustomobject]@{} })
    $map = @{}
    if ($null -ne $payload.tasks) {
        foreach ($prop in $payload.tasks.PSObject.Properties) {
            $map[$prop.Name] = $prop.Value
        }
    }
    return $map
}

function ConvertTo-Array {
    param([object]$Value)
    if ($null -eq $Value) {
        return @()
    }
    if ($Value -is [System.Array]) {
        return @($Value)
    }
    return @($Value)
}

function Resolve-UnderRoot {
    param([string]$Path)
    if ([System.IO.Path]::IsPathRooted($Path)) {
        return $Path
    }
    return (Join-Path $Root $Path)
}

function Release-UnfinishedWorkerTasks {
    param([object]$Worker)
    $taskState = Get-TaskStateMap
    $unfinished = @()
    foreach ($taskId in (ConvertTo-Array $Worker.task_ids)) {
        if (-not $taskState.ContainsKey($taskId)) {
            continue
        }
        $state = $taskState[$taskId]
        $status = [string]$state.status
        $agent = [string]$state.agent
        if (($status -eq "claimed" -or $status -eq "in_progress") -and $agent -eq [string]$Worker.worker) {
            $unfinished += [string]$taskId
        }
    }
    if ($unfinished.Count -gt 0) {
        Invoke-GenealogyWiki -Arguments (@(
            "agent-task", "release"
        ) + $unfinished + @(
            "--root", $Root,
            "--agent", [string]$Worker.worker,
            "--note", "parallel worker process ended before completion; released for retry",
            "--no-refresh"
        ))
    }
}

function Prune-Workers {
    param([object[]]$Workers)
    $active = @()
    foreach ($worker in $Workers) {
        if ($null -eq $worker -or $null -eq $worker.PSObject.Properties["pid"]) {
            continue
        }
        $pidValue = [int]$worker.pid
        $process = Get-Process -Id $pidValue -ErrorAction SilentlyContinue
        if ($null -ne $process -and $process.ProcessName -like "codex*") {
            $active += $worker
            continue
        }
        Release-UnfinishedWorkerTasks -Worker $worker
    }
    return @($active)
}

function Quote-Arg {
    param([string]$Value)
    if ($Value -notmatch '[\s"]') {
        return $Value
    }
    return '"' + ($Value -replace '\\(?=")', '\\' -replace '"', '\"') + '"'
}

function Write-WorkerPrompt {
    param([object]$Batch, [string]$WorkerName)
    $promptPath = Join-Path $PromptDir "$WorkerName.md"
    $batchJson = $Batch | ConvertTo-Json -Depth 20
    $taskIds = @((ConvertTo-Array $Batch.task_ids) | ForEach-Object { [string]$_ })
    $pageLines = @()
    foreach ($page in (ConvertTo-Array $Batch.pages)) {
        $pageLines += "- Page $($page.page): image `$(Resolve-UnderRoot ([string]$page.page_image))`; output `$(Resolve-UnderRoot ([string]$page.output_path))`; crops `$(Resolve-UnderRoot ([string]$page.image_output_dir))`."
    }
    $taskList = ($taskIds | ForEach-Object { '"' + $_ + '"' }) -join " "
    $taskIdLines = ($taskIds | ForEach-Object { "- $_" }) -join [Environment]::NewLine
    $pageLineText = $pageLines -join [Environment]::NewLine
    $skillSourcePrep = Join-Path $Root ".agents\skills\source-prep-pipeline\SKILL.md"
    $skillConversion = Join-Path $Root ".agents\skills\historical-document-conversion\SKILL.md"
    $promptTemplate = @'
You are a parallel source-prep conversion worker for this exact workspace:

`$Root = "__ROOT__"`

You are not alone in the codebase. Other workers may be converting different pages at the same time. Own only the task ids below; do not edit any other page files, raw sources, canonical wiki pages, or unrelated files.

Read these skills before converting:
- __SKILL_SOURCE_PREP__
- __SKILL_CONVERSION__

Task ids already claimed and started for you:
__TASK_ID_LINES__

Pages:
__PAGE_LINES__

Rules:
- Use the attached page image files as the conversion authority.
- OCR, PDF text layers, old Markdown, and old crops are hints only.
- Every completed page must have the required source-prep sections, full-page Markdown, extracted visual crops when present, uncertainty notes, genealogy leads, and a completeness audit.
- If a page is too dense, damaged, handwritten, table-heavy, or family-critical for accurate batch work, complete only the pages you can do accurately and release or fail the others with a note.
- Do not run global `prepare-sources`, `conversion-qc`, `agent-queues`, or `source-status`; the controller handles that.

Validation command pattern:
`$env:PYTHONPATH = "__PYTHONPATH__"`
`python -c "from pathlib import Path; from historic_doc_ingest.genealogy_wiki import review_source_prep_page_output; import sys; paths=[Path(p) for p in sys.argv[1:]]; bad=[]; [bad.append((str(p), review_source_prep_page_output(p))) for p in paths if review_source_prep_page_output(p).get('status')!='done']; print(bad); sys.exit(1 if bad else 0)" <output paths...>`

When a page passes validation, mark only that page done:
`python -m historic_doc_ingest.genealogy_wiki agent-task complete __TASK_LIST__ --root "__ROOT__" --agent "__WORKER_NAME__" --no-refresh`

If a page cannot be completed accurately:
`python -m historic_doc_ingest.genealogy_wiki agent-task release <task-id> --root "__ROOT__" --agent "__WORKER_NAME__" --note "<why>" --no-refresh`

Batch JSON:
```json
__BATCH_JSON__
```
'@
    $prompt = $promptTemplate.
        Replace("__ROOT__", $Root).
        Replace("__SKILL_SOURCE_PREP__", $skillSourcePrep).
        Replace("__SKILL_CONVERSION__", $skillConversion).
        Replace("__TASK_ID_LINES__", $taskIdLines).
        Replace("__PAGE_LINES__", $pageLineText).
        Replace("__PYTHONPATH__", $env:PYTHONPATH).
        Replace("__TASK_LIST__", $taskList).
        Replace("__WORKER_NAME__", $WorkerName).
        Replace("__BATCH_JSON__", $batchJson)
    $prompt | Set-Content -LiteralPath $promptPath -Encoding UTF8
    return $promptPath
}

function Start-Worker {
    param([object]$Batch)
    $timestamp = [DateTime]::UtcNow.ToString("yyyyMMddHHmmssfff")
    $workerName = "overnight-parallel-$timestamp-p$($Batch.first_page)-p$($Batch.last_page)"
    $taskIds = @((ConvertTo-Array $Batch.task_ids) | ForEach-Object { [string]$_ })

    Invoke-GenealogyWiki -Arguments (@(
        "agent-task", "claim"
    ) + $taskIds + @(
        "--root", $Root,
        "--agent", $workerName,
        "--note", "parallel controller claim",
        "--no-refresh"
    ))
    Invoke-GenealogyWiki -Arguments (@(
        "agent-task", "start"
    ) + $taskIds + @(
        "--root", $Root,
        "--agent", $workerName,
        "--note", "parallel controller start",
        "--no-refresh"
    ))

    $promptPath = Write-WorkerPrompt -Batch $Batch -WorkerName $workerName
    $stdoutPath = Join-Path $LogDir "$workerName.jsonl"
    $stderrPath = Join-Path $LogDir "$workerName.err.log"
    $lastMessagePath = Join-Path $LogDir "$workerName.last.md"
    $codexArgs = @(
        "exec",
        "-C", $Root,
        "--dangerously-bypass-approvals-and-sandbox",
        "--output-last-message", $lastMessagePath,
        "--json"
    )
    foreach ($page in (ConvertTo-Array $Batch.pages)) {
        $imagePath = Resolve-UnderRoot ([string]$page.page_image)
        if (Test-Path -LiteralPath $imagePath) {
            $codexArgs += @("-i", $imagePath)
        }
    }
    $codexArgs += "-"
    $argumentLine = ($codexArgs | ForEach-Object { Quote-Arg ([string]$_) }) -join " "
    $process = Start-Process -FilePath "codex" -ArgumentList $argumentLine -RedirectStandardInput $promptPath -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath -WindowStyle Hidden -PassThru
    return [ordered]@{
        worker = $workerName
        pid = $process.Id
        batch_id = [string]$Batch.task_id
        task_ids = @($taskIds)
        prompt = $promptPath
        stdout = $stdoutPath
        stderr = $stderrPath
        last_message = $lastMessagePath
        started = [DateTime]::UtcNow.ToString("s") + "Z"
    }
}

function Get-AvailableBatches {
    param([object[]]$ActiveWorkers)
    $batchPath = Join-Path $QueueDir "source-prep-batches.json"
    $payload = Read-JsonFile -Path $batchPath -Default ([pscustomobject]@{ tasks = @() })
    $taskState = Get-TaskStateMap
    $activeTaskIds = @{}
    foreach ($worker in $ActiveWorkers) {
        foreach ($taskId in (ConvertTo-Array $worker.task_ids)) {
            $activeTaskIds[[string]$taskId] = $true
        }
    }

    $available = @()
    foreach ($batch in (ConvertTo-Array $payload.tasks)) {
        $ids = @((ConvertTo-Array $batch.task_ids) | ForEach-Object { [string]$_ })
        if ($ids.Count -eq 0) {
            continue
        }
        $blocked = $false
        foreach ($taskId in $ids) {
            if ($activeTaskIds.ContainsKey($taskId)) {
                $blocked = $true
                break
            }
            if ($taskState.ContainsKey($taskId)) {
                $status = [string]$taskState[$taskId].status
                if ($status -eq "claimed" -or $status -eq "in_progress" -or $status -eq "done" -or $status -eq "failed") {
                    $blocked = $true
                    break
                }
            }
        }
        if (-not $blocked) {
            $available += $batch
        }
    }
    return @($available)
}

$controllerStart = Get-Date
$activeWorkers = @()
if (Test-Path -LiteralPath $StatePath) {
    $savedState = Read-JsonFile -Path $StatePath -Default ([pscustomobject]@{ active_workers = @() })
    $activeWorkers = @(ConvertTo-Array $savedState.active_workers)
}

do {
    Invoke-GenealogyWiki -Arguments @(
        "source-prep-batches",
        "--root", $Root,
        "--max-pages", [string]$BatchPages,
        "--limit", [string]$QueueLimit,
        "--stale-minutes", [string]$StaleMinutes
    )

    $activeWorkers = @(Prune-Workers -Workers $activeWorkers)
    $slots = [Math]::Max(0, $MaxWorkers - $activeWorkers.Count)
    if ($slots -gt 0) {
        $batches = Get-AvailableBatches -ActiveWorkers $activeWorkers
        foreach ($batch in ($batches | Select-Object -First $slots)) {
            $activeWorkers += (Start-Worker -Batch $batch)
        }
    }
    Save-ControllerState -Workers $activeWorkers

    if (-not $SkipFastLane -and $FastLaneLimit -gt 0 -and $FastLaneScanLimit -gt 0) {
        Invoke-GenealogyWiki -Arguments @(
            "source-prep-fastlane",
            "--root", $Root,
            "--limit", [string]$FastLaneLimit,
            "--scan-limit", [string]$FastLaneScanLimit,
            "--agent", "overnight-fastlane",
            "--stale-minutes", [string]$StaleMinutes
        )
    }

    if ($Once) {
        break
    }
    if ($RunMinutes -gt 0 -and ((Get-Date) - $controllerStart).TotalMinutes -ge $RunMinutes) {
        break
    }
    Start-Sleep -Seconds $PollSeconds
} while ($true)

Write-Host "parallel-controller | active_workers=$($activeWorkers.Count) state=$StatePath"
