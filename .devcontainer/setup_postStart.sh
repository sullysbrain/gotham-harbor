#!/bin/bash
set -e

echo "[postStart] Checking venv..."
if [ ! -f /opt/venv/bin/python ]; then
  echo "[postStart] Creating venv and syncing dependencies..."
  uv venv /opt/venv
  UV_PROJECT_ENVIRONMENT=/opt/venv uv sync
else
  echo "[postStart] Venv already exists, skipping sync."
fi

if [ ! -f /tmp/.main_ran ]; then
  echo "[postStart] Running src/main.py..."
  touch /tmp/.main_ran
  /opt/venv/bin/python src/main.py
else
  echo "[postStart] main.py already ran this session, skipping."
fi
