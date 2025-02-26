#!/bin/bash

# Local and remote paths
LOCAL_PATH="/Users/vkroz/workplace/vkroz/neural-machines/"
REMOTE_PATH="clouddesk:/home/vkroz/workplace/vkroz/neural-machines/"

echo "Starting sync script..."
echo "Monitoring: $LOCAL_PATH"

# Run rsync on file changes
fswatch -o "$LOCAL_PATH" | while read -r event; do
    echo "Change detected: $event"
    rsync -avz --delete --exclude='.git' "$LOCAL_PATH" "$REMOTE_PATH"
    echo "Synced at $(date)"
done
