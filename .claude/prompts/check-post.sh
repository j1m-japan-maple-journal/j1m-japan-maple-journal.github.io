#!/bin/bash
PROMPT=$(cat /home/j1m/j1m.github.io/.claude/prompts/blog-proofreader.md)
POST=$(cat "$1")
claude "${PROMPT/\{FILE_CONTENT\}/$POST}"
