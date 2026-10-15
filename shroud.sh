#!/bin/bash

export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
export ANTHROPIC_BASE_URL=http://10.0.0.143:11434

claude --model rafw007/qwen35-claude-coder:9b
