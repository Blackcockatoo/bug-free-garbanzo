#!/usr/bin/env bash
set -euo pipefail

echo "=== TamaOS Kernel setup ==="
if ! command -v python3 >/dev/null 2>&1; then
  sudo apt-get update -y && sudo apt-get install -y python3 python3-venv python3-pip
fi
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. Run: source .venv/bin/activate && python -m tamaos.main"
