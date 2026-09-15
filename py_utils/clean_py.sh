#!/bin/bash

echo "Find and remove __pycache__" 
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null

echo "Find and remove .mypy_cache..." 
find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null

if [ "$1" == "all" ]; then
    echo "Delete main.py from subfolders (keeping root main.py)"
    find . -mindepth 2 -type f -name "main.py" -delete 2>/dev/null
fi