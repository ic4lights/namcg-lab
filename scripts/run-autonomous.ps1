[CmdletBinding()]
param(
    [string]$Target = 'auto',
    [int]$Items = 5,
    [int]$Rounds = 4,
    [int]$MaxTurns = 600,
    [switch]$Sandboxed   # pass only inside a container/VM: adds --dangerously-skip-permissions
)
# Launch one autonomous research run. Stops itself at a milestone/stop condition and writes reports/run-*.md.
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) { throw 'Claude Code CLI not found on PATH (npm i -g @anthropic-ai/claude-code).' }
if (git status --porcelain) { throw 'Working tree is dirty. Commit or stash first.' }

$cmdText = (Get-Content .claude\commands\run-cycle.md -Raw) -replace '(?s)^---.*?---\s*', ''
$prompt  = $cmdText.Replace('$ARGUMENTS', "$Target --items $Items --rounds $Rounds")

$stamp = Get-Date -Format 'yyyyMMdd-HHmm'
$log   = "reports\run-$stamp.log"
$argsList = @('-p', $prompt, '--max-turns', $MaxTurns, '--output-format', 'text')
if ($Sandboxed) { $argsList += '--dangerously-skip-permissions' } else { $argsList += @('--permission-mode', 'acceptEdits') }

& claude @argsList 2>&1 | Tee-Object -FilePath $log
Write-Host "`nLog: $log`nDigest: reports\run-*.md (branch: $(git branch --show-current))"
