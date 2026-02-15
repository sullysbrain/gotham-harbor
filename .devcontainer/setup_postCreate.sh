#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -x /opt/venv/bin/python ]; then
    echo "Creating virtual environment..."
    uv venv /opt/venv
fi

# Sync dependencies
echo "Syncing dependencies..."
UV_PROJECT_ENVIRONMENT=/opt/venv uv sync

# Add venv activation to shell rc files
ACTIVATE_LINE='[ -f /opt/venv/bin/activate ] && source /opt/venv/bin/activate'
for rcfile in ~/.bashrc ~/.zshrc; do
    if [ -f "$rcfile" ] && ! grep -qxF "$ACTIVATE_LINE" "$rcfile"; then
        echo "Adding venv activation to $rcfile..."
        echo "$ACTIVATE_LINE" >> "$rcfile"
    elif [ ! -f "$rcfile" ]; then
        echo "$ACTIVATE_LINE" > "$rcfile"
    fi
done