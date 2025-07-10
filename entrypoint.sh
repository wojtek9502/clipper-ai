#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieve LLAMA3 model..."
ollama pull steamdj/llama3.1-cpu-only
echo "🟢 Done!"

# Wait for Ollama process to finish.
wait $pid