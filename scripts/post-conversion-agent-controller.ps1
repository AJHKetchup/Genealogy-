param(
    [string]$Root = ".",
    [int]$MaxWorkers = 3,
    [int]$QueueLimit = 12,
    [int]$PollSeconds = 90,
    [int]$RunMinutes = 0,
    [int]$StaleMinutes = 360,
    [switch]$Once,
    [switch]$DryRun,
    [switch]$NoRefresh,
    [switch]$NoWorkers,
    [switch]$AllowPromotion,
    [switch]$PromotionOnly,
    [string]$CodexPath = "",
    [switch]$WaitForWorkers,
    [int]$WorkerTimeoutMinutes = 50
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = (Resolve-Path -LiteralPath $Root).Path
$env:PYTHONPATH = (Join-Path $Root "src")
$QueueDir = Join-Path $Root "research\_agent-queues"
$PromptDir = Join-Path $QueueDir "post-conversion-worker-prompts"
$LogDir = Join-Path $QueueDir "post-conversion-worker-logs"
$StatePath = Join-Path $QueueDir "post-conversion-controller-state.json"
$IdentityQueuePath = Join-Path $QueueDir "identity-analysis.json"
$ReviewQueuePath = Join-Path $QueueDir "proof-review.json"
$PromotionQueuePath = Join-Path $QueueDir "wiki-promotion.json"
$LockPath = Join-Path $QueueDir "post-conversion-controller.lock.json"
$Script:ResolvedCodexPath = $null
New-Item -ItemType Directory -Force -Path $QueueDir, $PromptDir, $LogDir | Out-Null

function ConvertTo-Array {
    param([object]$Value)
    if ($null -eq $Value) { return @() }
    if ($Value -is [System.Array]) { return @($Value) }
    return @($Value)
}

function Read-JsonFile {
    param([string]$Path, [object]$Default)
    if (-not (Test-Path -LiteralPath $Path)) { return $Default }
    $raw = Get-Content -LiteralPath $Path -Raw
    if ([string]::IsNullOrWhiteSpace($raw)) { return $Default }
    return $raw | ConvertFrom-Json
}

function Write-JsonFile {
    param([string]$Path, [object]$Value, [int]$Depth = 12)
    $Value | ConvertTo-Json -Depth $Depth | Set-Content -LiteralPath $Path -Encoding UTF8
}

function Resolve-UnderRoot {
    param([string]$Path)
    if ([string]::IsNullOrWhiteSpace($Path)) { return "" }
    if ([System.IO.Path]::IsPathRooted($Path)) { return $Path }
    return Join-Path $Root $Path
}

function ConvertTo-RelativePath {
    param([string]$Path)
    $full = [System.IO.Path]::GetFullPath($Path)
    $base = [System.IO.Path]::GetFullPath($Root)
    if (-not $base.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
        $base += [System.IO.Path]::DirectorySeparatorChar
    }
    $baseUri = [Uri]$base
    $pathUri = [Uri]$full
    return [Uri]::UnescapeDataString($baseUri.MakeRelativeUri($pathUri).ToString()).Replace("\", "/")
}

function New-Slug {
    param([string]$Value)
    $slug = $Value.ToLowerInvariant() -replace '[^a-z0-9]+', '-'
    $slug = $slug.Trim('-')
    if ([string]::IsNullOrWhiteSpace($slug)) { return "task" }
    return $slug
}

function Quote-Arg {
    param([string]$Value)
    if ($Value -notmatch '[\s"]') { return $Value }
    return '"' + ($Value -replace '"', '\"') + '"'
}

function Add-CodexCandidate {
    param(
        [System.Collections.Generic.List[string]]$Candidates,
        [string]$Path
    )
    if ([string]::IsNullOrWhiteSpace($Path)) { return }

    $candidate = $Path
    if (-not [System.IO.Path]::IsPathRooted($candidate)) {
        $command = Get-Command $candidate -ErrorAction SilentlyContinue | Select-Object -First 1
        if ($null -eq $command -or [string]::IsNullOrWhiteSpace($command.Source)) { return }
        $candidate = [string]$command.Source
    }

    if ($candidate -match '\\WindowsApps\\OpenAI\.Codex_') { return }
    if ($candidate.EndsWith(".ps1", [System.StringComparison]::OrdinalIgnoreCase)) {
        $cmdShim = [System.IO.Path]::ChangeExtension($candidate, ".cmd")
        if (Test-Path -LiteralPath $cmdShim -PathType Leaf) {
            $candidate = $cmdShim
        }
        else {
            return
        }
    }
    elseif ($candidate -notmatch '\.(cmd|exe|bat)$') {
        $cmdShim = "$candidate.cmd"
        if (Test-Path -LiteralPath $cmdShim -PathType Leaf) {
            $candidate = $cmdShim
        }
        else {
            return
        }
    }

    if (-not (Test-Path -LiteralPath $candidate -PathType Leaf)) { return }
    if (-not $Candidates.Contains($candidate)) { $Candidates.Add($candidate) | Out-Null }
}

function Resolve-CodexExecutable {
    if (-not [string]::IsNullOrWhiteSpace($Script:ResolvedCodexPath)) {
        return $Script:ResolvedCodexPath
    }

    $candidates = [System.Collections.Generic.List[string]]::new()
    Add-CodexCandidate -Candidates $candidates -Path $CodexPath
    Add-CodexCandidate -Candidates $candidates -Path $env:CODEX_CLI_PATH
    Add-CodexCandidate -Candidates $candidates -Path (Join-Path $env:APPDATA "npm\codex.cmd")
    if ($null -ne (Get-Command where.exe -ErrorAction SilentlyContinue)) {
        foreach ($path in (& where.exe codex.cmd 2>$null)) { Add-CodexCandidate -Candidates $candidates -Path $path }
        foreach ($path in (& where.exe codex 2>$null)) { Add-CodexCandidate -Candidates $candidates -Path $path }
    }
    foreach ($command in (Get-Command codex -All -ErrorAction SilentlyContinue)) {
        Add-CodexCandidate -Candidates $candidates -Path ([string]$command.Source)
    }

    if ($candidates.Count -eq 0) {
        throw "No runnable Codex CLI was found. Install the npm CLI with 'npm i -g @openai/codex' or set CODEX_CLI_PATH to a runnable codex.cmd/codex.exe. The Microsoft Store WindowsApps package path is intentionally ignored because it cannot be launched directly by automation."
    }

    $Script:ResolvedCodexPath = $candidates[0]
    return $Script:ResolvedCodexPath
}

function Invoke-GenealogyWiki {
    param([string[]]$Arguments)
    $oldPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = "Continue"
        $commandOutput = & python -m historic_doc_ingest.genealogy_wiki @Arguments 2>&1
        $exitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $oldPreference
    }
    foreach ($line in $commandOutput) { Write-Host $line }
    if ($exitCode -ne 0) {
        $tail = (($commandOutput | Select-Object -Last 12) -join " | ").Trim()
        throw "genealogy-wiki failed: $($Arguments -join ' '): $tail"
    }
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

function Apply-TaskState {
    param([hashtable]$Task, [hashtable]$TaskState)
    $taskId = [string]$Task.task_id
    if (-not $TaskState.ContainsKey($taskId)) { return $Task }
    $state = $TaskState[$taskId]
    foreach ($prop in $state.PSObject.Properties) {
        $Task[$prop.Name] = $prop.Value
    }
    return $Task
}

function Get-StatusCounts {
    param([object[]]$Tasks)
    $counts = [ordered]@{}
    foreach ($task in $Tasks) {
        $status = [string]$task.status
        if ([string]::IsNullOrWhiteSpace($status)) { $status = "unknown" }
        if (-not $counts.Contains($status)) { $counts[$status] = 0 }
        $counts[$status] += 1
    }
    return $counts
}

function Get-QueueStatusCountsFromFile {
    param([string]$Path)
    $payload = Read-JsonFile -Path $Path -Default ([pscustomobject]@{ status_counts = [pscustomobject]@{} })
    if ($null -eq $payload -or $null -eq $payload.PSObject.Properties["status_counts"]) {
        return [ordered]@{}
    }
    return $payload.status_counts
}

function Test-ProcessAlive {
    param([int]$ProcessId)
    return $null -ne (Get-Process -Id $ProcessId -ErrorAction SilentlyContinue)
}

function Try-AcquireLock {
    if ($DryRun) { return $true }
    $existing = Read-JsonFile -Path $LockPath -Default $null
    if ($null -ne $existing -and $null -ne $existing.pid) {
        $pidValue = [int]$existing.pid
        if (Test-ProcessAlive -ProcessId $pidValue) { return $false }
    }
    Write-JsonFile -Path $LockPath -Value ([ordered]@{
        pid = $PID
        started = [DateTime]::UtcNow.ToString("s") + "Z"
        root = $Root
    }) -Depth 4
    return $true
}

function Release-Lock {
    if (-not $DryRun -and (Test-Path -LiteralPath $LockPath)) {
        try {
            Remove-Item -LiteralPath $LockPath -Force -ErrorAction Stop
        }
        catch {
            # Another controller cleanup path may already have removed it.
        }
    }
}

function Update-TaskState {
    param([string]$Action, [string[]]$TaskIds, [string]$Agent, [string]$Note)
    if ($DryRun -or $TaskIds.Count -eq 0) { return }
    Invoke-GenealogyWiki -Arguments (@("agent-task", $Action) + $TaskIds + @(
        "--root", $Root,
        "--agent", $Agent,
        "--note", $Note,
        "--no-refresh"
    ))
}

function New-ProofReviewPrompt {
    param([string]$RelativePath)
    return @"
# Proof Review Task

Use `$genealogy-proof-review`.

You are a proof-review worker for this exact workspace:

`$Root = "$Root"`

You are not alone in the codebase. Other workers may be handling separate staged drafts. Own only this staged draft and do not edit raw sources, converted Markdown, chunks, or canonical wiki pages.

## Assignment

- Role: `claim_reviewer`
- Staged draft: `$RelativePath`
- Output area: `research/_staging/reviews/`

## Rules

- Read the staged draft and only the referenced converted file, chunk, page image, source packet, QA note, or source page needed to verify it.
- Check literal support, uncertainty, source reliability, conversion confidence, claim confidence, identity risk, relationship jumps, conflicts, relevance, and claim probability.
- Treat proof as a scored judgment, not a promoted/not-promoted binary. Include `source_quality_score`, `conversion_confidence_score`, `evidence_quantity_score`, `agreement_score`, `identity_confidence_score`, `claim_probability`, `relevance_level`, `relevance_confidence`, and `canonical_readiness`.
- Maintain the hard boundary between verification context and source transcription. "Please double-check whether this is Dario" is allowed; "change this to Dario" is forbidden unless the visible source itself supports that reading.
- If support is missing or the referenced conversion/chunk is unavailable, mark the item `hold` or `revise`; do not guess.
- Write a review note under `research/_staging/reviews/` that references this exact staged draft.
- Do not promote to `research/claims`, `research/relationships`, `wiki/people`, `wiki/families`, or other canonical folders.

## Done When

- A review note exists under `research/_staging/reviews/`.
- The note includes probability/evidence scoring plus `canonical_readiness`.
- The note lists blockers first, then evidence strengths and next action.
"@
}

function New-PromotionPrompt {
    param([object[]]$ReadyReviews)
    $readyLines = @()
    foreach ($review in @($ReadyReviews)) {
        $readyLines += "- `$($review.staged_draft)` ($($review.canonical_readiness); review: `$($review.review_file)`)"
    }
    if ($readyLines.Count -eq 0) {
        $readyLines = @("- No proof-review notes are currently marked `canonical_readiness: ready` or `ready_with_caveats`.")
    }
    $readySection = ($readyLines -join "`n")
    return @"
# Reviewed Promotion Task

Use `$genealogy-proof-review` as the review contract and act as the `wiki_promoter` only for items already reviewed as promotion-ready.

You are a promotion worker for this exact workspace:

`$Root = "$Root"`

## Assignment

- Role: `wiki_promoter`
- Review folder: `research/_staging/reviews/`
- Promotion command: `python -m historic_doc_ingest.genealogy_wiki promote-staged --root "$Root"`

## Review-Ready Inputs

$readySection

## Rules

- Promote only staged material with explicit review notes showing strong source support, conservative scores, and `canonical_readiness: ready`.
- Preserve probability, source quality, conflicts, and uncertainty in canonical pages; promotion is an operational state, not a truth binary.
- Preserve the distinction between literal transcription and interpretation. Do not convert a suspected reading into canonical fact unless the review says the visible source supports it.
- Living-family privacy is not a standalone hold for this internal family project; user approval was recorded in `research/_automation/post-conversion-architecture.json`. Still require reviewed evidence, source support, and conservative confidence/status labels.
- Do not promote drafts with missing converted/chunk evidence, open conversion QA holds, unresolved identity conflicts, low claim probability, or `canonical_readiness` below `ready`.
- Run a dry run first and inspect skipped items before any real promotion.
- After promotion, run `python -m historic_doc_ingest.genealogy_wiki lint --root "$Root"` and update `research/log.md`.

## Done When

- A promotion manifest exists under `research/_staging/promotions/`, or the task writes a review note explaining why nothing was safe to promote.
"@
}

function Get-ReviewFrontmatterValue {
    param([string]$Text, [string]$Name)
    $match = [regex]::Match($Text, "(?ms)^---\s*\r?\n(.*?)\r?\n---")
    if (-not $match.Success) { return "" }
    $frontmatter = $match.Groups[1].Value
    $pattern = "(?im)^\s*" + [regex]::Escape($Name) + "\s*:\s*(.+?)\s*$"
    $valueMatch = [regex]::Match($frontmatter, $pattern)
    if (-not $valueMatch.Success) { return "" }
    return $valueMatch.Groups[1].Value.Trim().Trim("`"")
}

function Normalize-ReviewReadiness {
    param([string]$Value)
    return (($Value.Trim().Trim("``").ToLowerInvariant() -replace "[-\s]+", "_") -replace "[^a-z0-9_]", "")
}

function Test-ReviewReadyForPromotion {
    param([string]$Value)
    $normalized = Normalize-ReviewReadiness -Value $Value
    return $normalized -in @("ready", "ready_with_caveats", "ready_to_promote", "promote", "approved")
}

function Test-StagedDraftCanBePromoted {
    param([string]$StagedDraft)
    $relative = ($StagedDraft -replace "\\", "/").Trim().Trim("``").Trim('"').Trim("'")
    if ([string]::IsNullOrWhiteSpace($relative)) { return $false }
    $path = Resolve-UnderRoot -Path $relative
    if (-not (Test-Path -LiteralPath $path)) { return $false }
    $text = Get-Content -LiteralPath $path -Raw
    $type = (Get-ReviewFrontmatterValue -Text $text -Name "type").Trim().ToLowerInvariant()
    if ($type -notin @("claim", "relationship_candidate", "source_packet", "staged_source_packet")) {
        return $false
    }
    $recommendation = (Get-ReviewFrontmatterValue -Text $text -Name "promotion_recommendation").Trim().ToLowerInvariant()
    if ($recommendation -in @("reject", "rejected", "do_not_promote")) {
        return $false
    }
    return $true
}

function Get-ReadyPromotionReviews {
    $reviewDir = Join-Path $Root "research\_staging\reviews"
    if (-not (Test-Path -LiteralPath $reviewDir)) { return @() }
    $ready = @()
    foreach ($file in (Get-ChildItem -LiteralPath $reviewDir -Filter "*.md" -File | Sort-Object FullName)) {
        $text = Get-Content -LiteralPath $file.FullName -Raw
        $staged = Get-ReviewFrontmatterValue -Text $text -Name "staged_draft"
        if ([string]::IsNullOrWhiteSpace($staged)) {
            $taskId = Get-ReviewFrontmatterValue -Text $text -Name "task_id"
            if ($taskId.StartsWith("proof-review:")) {
                $staged = $taskId.Substring("proof-review:".Length)
            }
        }
        if ([string]::IsNullOrWhiteSpace($staged)) {
            $match = [regex]::Match($text, "(?im)^\s*-?\s*Reviewed staged draft:\s*``([^``]+)``")
            if ($match.Success) { $staged = $match.Groups[1].Value.Trim() }
        }
        if ([string]::IsNullOrWhiteSpace($staged)) {
            $match = [regex]::Match($text, "(?im)^\s*-?\s*Review task id:\s*``proof-review:([^``]+)``")
            if ($match.Success) { $staged = $match.Groups[1].Value.Trim() }
        }
        $readiness = Get-ReviewFrontmatterValue -Text $text -Name "canonical_readiness"
        if ([string]::IsNullOrWhiteSpace($readiness)) {
            $match = [regex]::Match($text, "(?im)^\s*-?\s*canonical_readiness:\s*``?([^``\r\n]+)``?")
            if ($match.Success) { $readiness = $match.Groups[1].Value.Trim() }
        }
        if ([string]::IsNullOrWhiteSpace($staged) -or -not (Test-ReviewReadyForPromotion -Value $readiness)) { continue }
        if (-not (Test-StagedDraftCanBePromoted -StagedDraft $staged)) { continue }
        $ready += [pscustomobject]@{
            staged_draft = ($staged -replace "\\", "/").Trim().Trim("``")
            canonical_readiness = $readiness
            review_file = ConvertTo-RelativePath -Path $file.FullName
        }
    }
    return @($ready)
}

function Get-PromotionFingerprint {
    param([object[]]$ReadyReviews)
    if ($ReadyReviews.Count -eq 0) { return "none" }
    $joined = (@($ReadyReviews) | Sort-Object staged_draft, review_file | ForEach-Object {
        "$($_.staged_draft)|$($_.canonical_readiness)|$($_.review_file)"
    }) -join "`n"
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($joined)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        $hashBytes = $sha.ComputeHash($bytes)
    }
    finally {
        $sha.Dispose()
    }
    return ([System.BitConverter]::ToString($hashBytes).Replace("-", "").ToLowerInvariant()).Substring(0, 12)
}

function Write-ProofReviewQueue {
    param([hashtable]$TaskState)
    $tasks = @()
    $stagingRoot = Join-Path $Root "research\_staging"
    $folders = @("source-packets", "claims", "relationships", "identity", "conflicts", "identity-analysis")
    $promptRoot = Join-Path $QueueDir "prompts\proof-review"
    if (-not $DryRun) { New-Item -ItemType Directory -Force -Path $promptRoot | Out-Null }

    foreach ($folder in $folders) {
        $dir = Join-Path $stagingRoot $folder
        if (-not (Test-Path -LiteralPath $dir)) { continue }
        foreach ($file in (Get-ChildItem -LiteralPath $dir -Filter "*.md" -File | Sort-Object FullName)) {
            $rel = ConvertTo-RelativePath -Path $file.FullName
            $taskId = "proof-review:$rel"
            $promptPath = Join-Path $promptRoot "$(New-Slug $taskId).md"
            $task = [ordered]@{
                task_id = $taskId
                queue = "proof-review"
                role = "claim_reviewer"
                skill = "genealogy-proof-review"
                status = "todo"
                staged_draft = $rel
                prompt_path = ConvertTo-RelativePath -Path $promptPath
            }
            $taskHash = @{}
            foreach ($key in $task.Keys) { $taskHash[$key] = $task[$key] }
            Apply-TaskState -Task $taskHash -TaskState $TaskState | Out-Null
            $tasks += [pscustomobject]$taskHash
            if (-not $DryRun) {
                New-ProofReviewPrompt -RelativePath $rel | Set-Content -LiteralPath $promptPath -Encoding UTF8
            }
        }
    }

    $payload = [ordered]@{
        created = [DateTime]::UtcNow.ToString("yyyy-MM-dd")
        queue = "proof-review"
        task_count = $tasks.Count
        status_counts = Get-StatusCounts -Tasks $tasks
        tasks = @($tasks)
    }
    if (-not $DryRun) { Write-JsonFile -Path $ReviewQueuePath -Value $payload -Depth 12 }
    return $payload
}

function New-IdentityAnalysisPrompt {
    param([string]$RelativePath, [string]$Kind)
    return @"
# Identity And Conflict Analysis Task

Use `$genealogy-proof-review` as the evidence contract, but act as the `identity_researcher`.

You are an identity/conflict analysis worker for this exact workspace:

`$Root = "$Root"`

You are not alone in the codebase. Other workers may be handling separate staged drafts. Own only this staged identity/conflict analysis and do not edit raw sources, converted Markdown, chunks, or canonical wiki pages.

## Assignment

- Role: `identity_researcher`
- Staged `$Kind` draft: `$RelativePath`
- Output area: `research/_staging/identity-analysis/`

## Rules

- Compare same-person, duplicate-person, name-variant, relationship-conflict, and chronology-conflict evidence only from staged drafts, referenced converted/chunk/source files, reviewed notes, and existing canonical wiki pages.
- Do not perform external research.
- Do not run document conversion or edit conversion outputs.
- Do not merge people, rename canonical pages, or promote facts.
- Keep literal source readings separate from interpretation. Family-context hints can justify a double-check, not a silent correction.
- Preserve multiple hypotheses when identity is uncertain.
- Score identity confidence, conflict severity, evidence quality, conversion confidence, claim probability, relevance, and canonical readiness.
- Write one analysis note under `research/_staging/identity-analysis/` that references the exact staged draft.

## Done When

- An identity/conflict analysis note exists under `research/_staging/identity-analysis/`.
- The note lists blockers first, then evidence supporting each hypothesis, conflicts, probability/confidence scores, and recommended next action.
"@
}

function Write-IdentityAnalysisQueue {
    param([hashtable]$TaskState)
    $tasks = @()
    $stagingRoot = Join-Path $Root "research\_staging"
    $folders = @("identity", "conflicts")
    $promptRoot = Join-Path $QueueDir "prompts\identity-analysis"
    if (-not $DryRun) {
        New-Item -ItemType Directory -Force -Path $promptRoot | Out-Null
        New-Item -ItemType Directory -Force -Path (Join-Path $stagingRoot "identity-analysis") | Out-Null
    }

    foreach ($folder in $folders) {
        $dir = Join-Path $stagingRoot $folder
        if (-not (Test-Path -LiteralPath $dir)) { continue }
        foreach ($file in (Get-ChildItem -LiteralPath $dir -Filter "*.md" -File | Sort-Object FullName)) {
            $rel = ConvertTo-RelativePath -Path $file.FullName
            $taskId = "identity-analysis:$rel"
            $promptPath = Join-Path $promptRoot "$(New-Slug $taskId).md"
            $kind = if ($folder -eq "conflicts") { "conflict" } else { "identity" }
            $task = [ordered]@{
                task_id = $taskId
                queue = "identity-analysis"
                role = "identity_researcher"
                skill = "genealogy-proof-review"
                status = "todo"
                staged_draft = $rel
                output_dir = "research/_staging/identity-analysis"
                prompt_path = ConvertTo-RelativePath -Path $promptPath
            }
            $taskHash = @{}
            foreach ($key in $task.Keys) { $taskHash[$key] = $task[$key] }
            Apply-TaskState -Task $taskHash -TaskState $TaskState | Out-Null
            $tasks += [pscustomobject]$taskHash
            if (-not $DryRun) {
                New-IdentityAnalysisPrompt -RelativePath $rel -Kind $kind | Set-Content -LiteralPath $promptPath -Encoding UTF8
            }
        }
    }

    $payload = [ordered]@{
        created = [DateTime]::UtcNow.ToString("yyyy-MM-dd")
        queue = "identity-analysis"
        task_count = $tasks.Count
        status_counts = Get-StatusCounts -Tasks $tasks
        tasks = @($tasks)
    }
    if (-not $DryRun) { Write-JsonFile -Path $IdentityQueuePath -Value $payload -Depth 12 }
    return $payload
}

function Write-PromotionQueue {
    param([hashtable]$TaskState)
    $promptRoot = Join-Path $QueueDir "prompts\wiki-promotion"
    $readyReviews = @(Get-ReadyPromotionReviews)
    $fingerprint = Get-PromotionFingerprint -ReadyReviews $readyReviews
    $promptPath = Join-Path $promptRoot "wiki-promotion-reviewed-ready-$fingerprint.md"
    $task = [ordered]@{
        task_id = "wiki-promotion:reviewed-ready:$fingerprint"
        queue = "wiki-promotion"
        role = "wiki_promoter"
        skill = "genealogy-proof-review"
        status = if (-not $AllowPromotion) { "disabled_requires_allow_promotion" } elseif ($readyReviews.Count -gt 0) { "todo" } else { "blocked_no_reviewed_ready" }
        ready_review_count = $readyReviews.Count
        ready_review_fingerprint = $fingerprint
        prompt_path = ConvertTo-RelativePath -Path $promptPath
    }
    $taskHash = @{}
    foreach ($key in $task.Keys) { $taskHash[$key] = $task[$key] }
    Apply-TaskState -Task $taskHash -TaskState $TaskState | Out-Null
    $tasks = @([pscustomobject]$taskHash)
    $payload = [ordered]@{
        created = [DateTime]::UtcNow.ToString("yyyy-MM-dd")
        queue = "wiki-promotion"
        task_count = $tasks.Count
        status_counts = Get-StatusCounts -Tasks $tasks
        tasks = $tasks
    }
    if (-not $DryRun) {
        New-Item -ItemType Directory -Force -Path $promptRoot | Out-Null
        New-PromotionPrompt -ReadyReviews $readyReviews | Set-Content -LiteralPath $promptPath -Encoding UTF8
        Write-JsonFile -Path $PromotionQueuePath -Value $payload -Depth 12
    }
    return $payload
}

function Read-QueueTasks {
    param([string]$QueueName, [string]$Path)
    $payload = Read-JsonFile -Path $Path -Default ([pscustomobject]@{ tasks = @() })
    $tasks = @()
    foreach ($task in (ConvertTo-Array $payload.tasks)) {
        $task | Add-Member -NotePropertyName "_queue_file" -NotePropertyValue $Path -Force
        $tasks += $task
    }
    return @($tasks)
}

function Get-ActiveWorkers {
    $state = Read-JsonFile -Path $StatePath -Default ([pscustomobject]@{ active_workers = @() })
    $taskState = Get-TaskStateMap
    $active = @()
    foreach ($worker in (ConvertTo-Array $state.active_workers)) {
        if ($null -eq $worker.PSObject.Properties["pid"]) { continue }
        if (Test-ProcessAlive -ProcessId ([int]$worker.pid)) {
            $active += $worker
        }
        else {
            $taskIds = @((ConvertTo-Array $worker.task_ids) | ForEach-Object { [string]$_ })
            $releasableTaskIds = @()
            foreach ($taskId in $taskIds) {
                if (-not $taskState.ContainsKey($taskId)) { continue }
                $status = [string]$taskState[$taskId].status
                if ($status -in @("claimed", "in_progress")) {
                    $releasableTaskIds += $taskId
                }
            }
            Update-TaskState -Action "release" -TaskIds $releasableTaskIds -Agent ([string]$worker.worker) -Note "post-conversion worker exited before completion"
        }
    }
    return @($active)
}

function Get-AvailableTasks {
    param([object[]]$ActiveWorkers)
    $activeTaskIds = @{}
    foreach ($worker in $ActiveWorkers) {
        foreach ($taskId in (ConvertTo-Array $worker.task_ids)) {
            $activeTaskIds[[string]$taskId] = $true
        }
    }

    if ($PromotionOnly) {
        if (-not $AllowPromotion) { return @() }
        $queuePaths = @(
            @{ name = "wiki-promotion"; path = $PromotionQueuePath }
        )
    }
    else {
        $queuePaths = @(
            @{ name = "conversion-qa"; path = Join-Path $QueueDir "conversion-qa.json" },
            @{ name = "evidence-extraction"; path = Join-Path $QueueDir "evidence-extraction.json" },
            @{ name = "identity-analysis"; path = $IdentityQueuePath },
            @{ name = "proof-review"; path = $ReviewQueuePath }
        )
    }
    if ($AllowPromotion -and -not $PromotionOnly) {
        $queuePaths += @{ name = "wiki-promotion"; path = $PromotionQueuePath }
    }

    $tasksByQueue = @{}
    foreach ($queue in $queuePaths) {
        $ready = @()
        foreach ($task in (Read-QueueTasks -QueueName $queue.name -Path $queue.path)) {
            $taskId = [string]$task.task_id
            $status = [string]$task.status
            if ($activeTaskIds.ContainsKey($taskId)) { continue }
            if ($status -notin @("todo", "released")) { continue }
            $ready += $task
        }
        $tasksByQueue[$queue.name] = @($ready)
    }

    $selected = [System.Collections.ArrayList]::new()
    $selectedTaskIds = @{}
    function Add-ReadyTasksFromQueue {
        param([string]$QueueName, [int]$Limit)
        if ($Limit -le 0 -or $selected.Count -ge $QueueLimit) { return }
        if (-not $tasksByQueue.ContainsKey($QueueName)) { return }
        $taken = 0
        foreach ($task in @($tasksByQueue[$QueueName])) {
            if ($selected.Count -ge $QueueLimit -or $taken -ge $Limit) { break }
            $taskId = [string]$task.task_id
            if ($selectedTaskIds.ContainsKey($taskId)) { continue }
            [void]$selected.Add($task)
            $selectedTaskIds[$taskId] = $true
            $taken += 1
        }
    }

    if ($PromotionOnly) {
        Add-ReadyTasksFromQueue -QueueName "wiki-promotion" -Limit $QueueLimit
        return @($selected)
    }

    # Avoid starving extraction behind a large QA backlog. The canonical tree grows only
    # after extraction -> proof review -> promotion, so each run reserves slots for that path.
    $reviewQuota = [Math]::Max(1, [int][Math]::Ceiling($QueueLimit * 0.25))
    $evidenceQuota = [Math]::Max(1, [int][Math]::Ceiling($QueueLimit * 0.60))
    $qaQuota = [Math]::Max(1, [int][Math]::Floor($QueueLimit * 0.25))

    Add-ReadyTasksFromQueue -QueueName "proof-review" -Limit $reviewQuota
    Add-ReadyTasksFromQueue -QueueName "identity-analysis" -Limit 1
    Add-ReadyTasksFromQueue -QueueName "evidence-extraction" -Limit $evidenceQuota
    Add-ReadyTasksFromQueue -QueueName "conversion-qa" -Limit $qaQuota
    if ($AllowPromotion) {
        Add-ReadyTasksFromQueue -QueueName "wiki-promotion" -Limit 1
    }

    $fillOrder = @("proof-review", "identity-analysis", "evidence-extraction", "conversion-qa")
    if ($AllowPromotion) { $fillOrder += "wiki-promotion" }
    while ($selected.Count -lt $QueueLimit) {
        $before = $selected.Count
        foreach ($queueName in $fillOrder) {
            Add-ReadyTasksFromQueue -QueueName $queueName -Limit 1
            if ($selected.Count -ge $QueueLimit) { break }
        }
        if ($selected.Count -eq $before) { break }
    }
    return @($selected)
}

function Write-WorkerPrompt {
    param([object]$Task, [string]$WorkerName)
    $promptPath = Join-Path $PromptDir "$WorkerName.md"
    $taskJson = $Task | ConvertTo-Json -Depth 20
    $body = ""
    $taskPromptPath = ""
    if ($null -ne $Task.PSObject.Properties["prompt_path"]) {
        $taskPromptPath = Resolve-UnderRoot ([string]$Task.prompt_path)
    }
    if ($taskPromptPath -and (Test-Path -LiteralPath $taskPromptPath)) {
        $body = Get-Content -LiteralPath $taskPromptPath -Raw
    }
    elseif ($null -ne $Task.PSObject.Properties["prompt"]) {
        $body = [string]$Task.prompt
    }
    else {
        $body = "# Post-Conversion Task`n`nTask details are in the JSON below."
    }

    $taskId = [string]$Task.task_id
    $promptTemplate = @'
__BODY__

## Controller Contract

This task was dispatched by `scripts/post-conversion-agent-controller.ps1`.

- Worker: `__WORKER_NAME__`
- Task id: `__TASK_ID__`

You are not alone in the codebase. Do not revert or overwrite unrelated edits. Own only this task's output paths.
Do not perform external research. Do not run source preparation or document conversion. Do not edit raw sources, converted Markdown, chunks, or conversion job page Markdown.

When the task is complete, run:

~~~powershell
python -m historic_doc_ingest.genealogy_wiki agent-task complete "__TASK_ID__" --root "__ROOT__" --agent "__WORKER_NAME__" --no-refresh
~~~

If the task cannot be completed safely, run:

~~~powershell
python -m historic_doc_ingest.genealogy_wiki agent-task release "__TASK_ID__" --root "__ROOT__" --agent "__WORKER_NAME__" --note "<short blocker>" --no-refresh
~~~

Task JSON:

~~~json
__TASK_JSON__
~~~
'@
    $prompt = $promptTemplate.
        Replace("__BODY__", $body).
        Replace("__WORKER_NAME__", $WorkerName).
        Replace("__TASK_ID__", $taskId).
        Replace("__ROOT__", $Root).
        Replace("__TASK_JSON__", $taskJson)
    if (-not $DryRun) { $prompt | Set-Content -LiteralPath $promptPath -Encoding UTF8 }
    return $promptPath
}

function Start-PostConversionWorker {
    param([object]$Task)
    $timestamp = [DateTime]::UtcNow.ToString("yyyyMMddHHmmssfff")
    $queueName = if ($null -ne $Task.PSObject.Properties["queue"]) { [string]$Task.queue } else { "post-conversion" }
    $workerName = "postconv-$queueName-$timestamp"
    $taskId = [string]$Task.task_id

    if (-not $NoWorkers) {
        Update-TaskState -Action "claim" -TaskIds @($taskId) -Agent $workerName -Note "post-conversion controller claim"
        Update-TaskState -Action "start" -TaskIds @($taskId) -Agent $workerName -Note "post-conversion controller start"
    }
    $promptPath = Write-WorkerPrompt -Task $Task -WorkerName $workerName
    $stdoutPath = Join-Path $LogDir "$WorkerName.jsonl"
    $stderrPath = Join-Path $LogDir "$WorkerName.err.log"
    $lastMessagePath = Join-Path $LogDir "$WorkerName.last.md"

    if ($DryRun -or $NoWorkers) {
        return [ordered]@{
            worker = $workerName
            pid = 0
            task_ids = @($taskId)
            queue = $queueName
            prompt = $promptPath
            stdout = $stdoutPath
            stderr = $stderrPath
            last_message = $lastMessagePath
            dry_run = $true
            started = [DateTime]::UtcNow.ToString("s") + "Z"
        }
    }

    $codexArgs = @(
        "exec",
        "-C", $Root,
        "--dangerously-bypass-approvals-and-sandbox",
        "--output-last-message", $lastMessagePath,
        "--json",
        "-"
    )
    $argumentLine = ($codexArgs | ForEach-Object { Quote-Arg ([string]$_) }) -join " "
    $codexExecutable = Resolve-CodexExecutable
    try {
        $process = Start-Process -FilePath $codexExecutable -ArgumentList $argumentLine -RedirectStandardInput $promptPath -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath -WindowStyle Hidden -PassThru
    }
    catch {
        Update-TaskState -Action "release" -TaskIds @($taskId) -Agent $workerName -Note "Codex worker failed to launch: $($_.Exception.Message)"
        throw
    }
    return [ordered]@{
        worker = $workerName
        pid = $process.Id
        task_ids = @($taskId)
        queue = $queueName
        codex = $codexExecutable
        prompt = $promptPath
        stdout = $stdoutPath
        stderr = $stderrPath
        last_message = $lastMessagePath
        started = [DateTime]::UtcNow.ToString("s") + "Z"
    }
}

function Wait-ForWorkerDrain {
    param([object[]]$Workers)
    if (-not $WaitForWorkers -or $DryRun -or $NoWorkers) { return @($Workers) }

    $deadline = (Get-Date).AddMinutes([Math]::Max(1, $WorkerTimeoutMinutes))
    $active = @($Workers)
    while ($active.Count -gt 0 -and (Get-Date) -lt $deadline) {
        Start-Sleep -Seconds $PollSeconds
        try {
            $active = @(Get-ActiveWorkers)
            Save-ControllerState -Workers $active -Summary $summary
        }
        catch {
            $summary.blockers += "worker drain status check failed: $($_.Exception.Message)"
            break
        }
    }

    if ($active.Count -gt 0) {
        foreach ($worker in $active) {
            $taskIds = @((ConvertTo-Array $worker.task_ids) | ForEach-Object { [string]$_ })
            try {
                Update-TaskState -Action "release" -TaskIds $taskIds -Agent ([string]$worker.worker) -Note "post-conversion worker timed out in hosted runner"
            }
            catch {
                $summary.blockers += "worker timeout release failed for $($worker.worker): $($_.Exception.Message)"
            }
            try {
                Stop-Process -Id ([int]$worker.pid) -Force -ErrorAction Stop
            }
            catch {
                $summary.blockers += "worker timeout cleanup failed for $($worker.worker): $($_.Exception.Message)"
            }
        }
        $summary.blockers += "timed out waiting for $($active.Count) worker(s)"
        return @()
    }
    return @($active)
}

function Save-ControllerState {
    param([object[]]$Workers, [object]$Summary)
    if ($DryRun) { return }
    Write-JsonFile -Path $StatePath -Value ([ordered]@{
        updated = [DateTime]::UtcNow.ToString("s") + "Z"
        root = $Root
        max_workers = $MaxWorkers
        allow_promotion = [bool]$AllowPromotion
        active_workers = @($Workers)
        last_summary = $Summary
    }) -Depth 14
}

function Invoke-Refresh {
    if ($NoRefresh) { return @("skipped") }
    Invoke-GenealogyWiki -Arguments @("conversion-qc", "--root", $Root)
    Invoke-GenealogyWiki -Arguments @("agent-queues", "--root", $Root, "--stale-minutes", [string]$StaleMinutes, "--post-conversion-only")
    Invoke-GenealogyWiki -Arguments @("source-status", "--root", $Root, "--no-refresh-index", "--no-source-prep-task-refresh")
    Invoke-GenealogyWiki -Arguments @("source-relevance", "sync-review-holds", "--root", $Root)
    Invoke-GenealogyWiki -Arguments @("source-relevance", "restore-review-assets", "--root", $Root, "--limit", "12")
    return @("conversion-qc", "agent-queues", "source-status", "source-relevance-review-holds", "source-relevance-review-assets")
}

$summary = [ordered]@{
    started = [DateTime]::UtcNow.ToString("s") + "Z"
    root = $Root
    dry_run = [bool]$DryRun
    allow_promotion = [bool]$AllowPromotion
    promotion_only = [bool]$PromotionOnly
    fatal = $false
    refresh = @()
    queues = [ordered]@{}
    active_workers_before = 0
    active_workers_after = 0
    launched = @()
    blockers = @()
}

if (-not (Try-AcquireLock)) {
    $summary.blockers += "post-conversion controller lock is held by an active process"
    $summary.finished = [DateTime]::UtcNow.ToString("s") + "Z"
    Write-Host "post-conversion-controller | summary"
    $summary | ConvertTo-Json -Depth 12
    exit 0
}

$controllerStart = Get-Date
$activeWorkers = @()
try {
    do {
        try {
            $activeWorkers = @(Get-ActiveWorkers)
        }
        catch {
            $summary.blockers += "active worker scan: $($_.Exception.Message)"
            $activeWorkers = @()
        }

        try {
            if ($activeWorkers.Count -ge $MaxWorkers -and -not $Once) {
                $summary.refresh = @("skipped_active_workers_at_capacity")
            }
            else {
                $summary.refresh = @(Invoke-Refresh)
                $taskState = Get-TaskStateMap
                $identityQueue = Write-IdentityAnalysisQueue -TaskState $taskState
                $reviewQueue = Write-ProofReviewQueue -TaskState $taskState
                $promotionQueue = Write-PromotionQueue -TaskState $taskState
                $summary.queues["conversion-qa"] = Get-QueueStatusCountsFromFile -Path (Join-Path $QueueDir "conversion-qa.json")
                $summary.queues["evidence-extraction"] = Get-QueueStatusCountsFromFile -Path (Join-Path $QueueDir "evidence-extraction.json")
                $summary.queues["identity-analysis"] = $identityQueue.status_counts
                $summary.queues["proof-review"] = $reviewQueue.status_counts
                $summary.queues["wiki-promotion"] = $promotionQueue.status_counts
            }
        }
        catch {
            $summary.blockers += "refresh: $($_.Exception.Message)"
        }

        $summary.active_workers_before = $activeWorkers.Count
        $slots = if ($NoWorkers) { 0 } else { [Math]::Max(0, $MaxWorkers - $activeWorkers.Count) }
        if ($slots -gt 0) {
            $available = @(Get-AvailableTasks -ActiveWorkers $activeWorkers)
            foreach ($task in ($available | Select-Object -First $slots)) {
                $taskIdForLog = if ($null -ne $task.PSObject.Properties["task_id"]) { [string]$task.task_id } else { "unknown-task" }
                try {
                    $worker = Start-PostConversionWorker -Task $task
                    $summary.launched += $worker
                    if (-not $DryRun -and -not $NoWorkers) {
                        $activeWorkers += $worker
                    }
                }
                catch {
                    $summary.blockers += "worker launch failed for ${taskIdForLog}: $($_.Exception.Message)"
                }
            }
        }
        $summary.active_workers_after = $activeWorkers.Count
        try {
            Save-ControllerState -Workers $activeWorkers -Summary $summary
        }
        catch {
            $summary.blockers += "save controller state: $($_.Exception.Message)"
        }

        if ($Once) { break }
        if ($RunMinutes -gt 0 -and ((Get-Date) - $controllerStart).TotalMinutes -ge $RunMinutes) { break }
        Start-Sleep -Seconds $PollSeconds
    } while ($true)
}
catch {
    $summary.fatal = $true
    $summary.blockers += "controller fatal: $($_.Exception.Message)"
}
finally {
    try {
        $activeWorkers = @(Wait-ForWorkerDrain -Workers $activeWorkers)
    }
    catch {
        $summary.fatal = $true
        $summary.blockers += "worker drain fatal: $($_.Exception.Message)"
    }
    try {
        Release-Lock
    }
    catch {
        $summary.blockers += "release lock: $($_.Exception.Message)"
    }
}

$summary.finished = [DateTime]::UtcNow.ToString("s") + "Z"
try {
    Save-ControllerState -Workers $activeWorkers -Summary $summary
}
catch {
    $summary.fatal = $true
    $summary.blockers += "final save controller state: $($_.Exception.Message)"
}
Write-Host "post-conversion-controller | summary"
$summary | ConvertTo-Json -Depth 14
if ($summary.fatal) {
    exit 1
}
