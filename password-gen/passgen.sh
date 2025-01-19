#!/bin/bash
# Linux wrapper script for password generator
# Usage: 
# 1. Make executable: chmod +x passgen.sh
# 2. Run: ./passgen.sh [-n NUM] [-l LENGTH] [-s]

SCRIPT_DIR=$(dirname "$0")
python3 "${SCRIPT_DIR}/password_gen.py" "$@"
