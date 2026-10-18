$env:ANTHROPIC_AUTH_TOKEN="ollama"
$env:ANTHROPIC_API_KEY="null"
$env:ANTHROPIC_BASE_URL="http://10.0.0.143:11434"

# $env:CLAUDE_CODE_MAX_CONTEXT_TOKENS=65536
# $env:CLAUDE_CODE_AUTO_COMPACT_WINDOW=65536
# $env:CLAUDE_CODE_MAX_OUTPUT_TOKENS=65536


# # 3. PERFORMANCE & CONTEXT BREAKERS (Solves Classifier Timeouts & VRAM Spikes)
# $env:LOCAL_LIGHTWEIGHT_MODE   = "true"
# $env:CLAUDE_CODE_MAX_TOKENS   = "2048"

# # 4. TIMEOUT & PROTOCOL HARDENING
$env:API_TIMEOUT_MS                            = "90000"
# $env:CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS    = "1"
# $env:CLAUDE_CODE_AUTO_MODE_SERVER              = "0"

# In PowerShell: Explicitly override the default compaction trigger percentage
# Triggers compaction at 90% utilization instead of defaulting down prematurely
$env:CLAUDE_AUTOCOMPACT_PCT_OVERRIDE = "90"


claude --model futuretea/deepseek-r1-tools:32b @args
