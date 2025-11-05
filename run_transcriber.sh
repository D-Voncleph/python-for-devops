#!/bin/bash

# Activate virtual environment
source /home/voncleph/Projects/python-for-devops/.venv/bin/activate

# Export the AssemblyAI API key
export ASSEMBLYAI_API_KEY=4f0db627842446dba9cd4c233de727a0

# Run the transcriber script with all arguments passed to this script
python video_transcriber.py "$@"

# Deactivate virtual environment
deactivate