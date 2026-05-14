param(
    [string]$Root = "C:\Users\Big Al\Documents\Genealogy",
    [string]$Message = "",
    [switch]$DryRun,
    [switch]$NoPush
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$Root = (Resolve-Path -LiteralPath $Root).Path
Push-Location -LiteralPath $Root
try {
    $repoRoot = (& git rev-parse --show-toplevel 2>$null)
    if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($repoRoot)) {
        throw "Not inside a Git repository: $Root"
    }

    & git diff --cached --quiet
    if ($LASTEXITCODE -ne 0) {
        throw "Refusing to sync because staged changes already exist. Commit or unstage them first."
    }

    $includePaths = @(
        "raw/source-prep-manifest.json",
        "raw/converted",
        "raw/chunks",
        "research",
        "wiki"
    )
    $existingIncludePaths = @($includePaths | Where-Object { Test-Path -LiteralPath $_ })
    if ($existingIncludePaths.Count -eq 0) {
        Write-Host "github-database-sync | nothing to add; include paths do not exist"
        return
    }

    if ($DryRun) {
        & git add --dry-run -A -- @existingIncludePaths
        if ($LASTEXITCODE -ne 0) {
            throw "git add dry-run failed"
        }
        Write-Host "github-database-sync | dry run only; no commit created"
        return
    }

    & git add -A -- @existingIncludePaths
    if ($LASTEXITCODE -ne 0) {
        throw "git add failed"
    }

    $staged = @(& git diff --cached --name-only)
    if ($staged.Count -eq 0) {
        Write-Host "github-database-sync | no database changes to commit"
        return
    }

    $forbiddenPrefixes = @(
        "raw/sources/",
        "raw/codex-conversion-jobs/",
        "raw/assets/",
        "research/_agent-queues/",
        ".genealogy/",
        "obsidian-offline/"
    )
    $forbidden = @(
        $staged | Where-Object {
            $path = ($_ -replace "\\", "/")
            foreach ($prefix in $forbiddenPrefixes) {
                if ($path.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)) {
                    return $true
                }
            }
            return $false
        }
    )
    if ($forbidden.Count -gt 0) {
        & git restore --staged -- @forbidden | Out-Null
        throw "Refusing to commit laptop-only paths: $($forbidden -join ', ')"
    }

    if ([string]::IsNullOrWhiteSpace($Message)) {
        $stamp = Get-Date -Format "yyyy-MM-dd HH:mm"
        $Message = "Sync genealogy GitHub database $stamp"
    }

    & git commit -m $Message
    if ($LASTEXITCODE -ne 0) {
        throw "git commit failed"
    }

    if (-not $NoPush) {
        & git push
        if ($LASTEXITCODE -ne 0) {
            throw "git push failed; commit is local and needs manual push or rebase"
        }
    }

    Write-Host "github-database-sync | committed $($staged.Count) database path change(s)"
}
finally {
    Pop-Location
}
