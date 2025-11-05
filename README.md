# YouTube Video Transcriber

A Python script that downloads YouTube videos and generates accurate transcripts using AssemblyAI's transcription service.

## Features

- Downloads YouTube videos using yt-dlp
- Extracts audio in MP3 format
- Transcribes audio using AssemblyAI's advanced AI
- Automatically cleans up temporary files
- Simple shell script for easy execution

## Requirements

- Python 3.x
- ffmpeg
- AssemblyAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/D-Voncleph/python-for-devops.git
cd python-for-devops
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install required packages:
```bash
pip install -r requirements-transcribe.txt
```

4. Create a `.env` file with your AssemblyAI API key:
```bash
echo "ASSEMBLYAI_API_KEY=your-api-key-here" > .env
```

## Usage

Use the provided shell script:
```bash
./run_transcriber.sh https://youtu.be/YOUR-VIDEO-ID
```

Or run manually:
```bash
source .venv/bin/activate
python video_transcriber.py https://youtu.be/YOUR-VIDEO-ID
deactivate
```

The transcript will be saved as `transcript.txt` in the current directory.

## How it Works

1. The script uses yt-dlp to download the video and extract its audio in MP3 format
2. The audio is sent to AssemblyAI's API for transcription
3. The transcript is saved to a text file
4. All temporary files are automatically cleaned up

## Notes

- Make sure you have ffmpeg installed on your system
- The AssemblyAI API key is required for transcription
- The script automatically handles video download and audio extraction
- Temporary files are automatically cleaned up after transcription

This repository serves as a collection of Python scripts and projects developed as part of my DevOps learning journey. The goal of these scripts is to demonstrate key concepts in automation, data handling, and system interaction using Python.

## Scripts

- **`fizzbuzz.py`**: A classic script that iterates from 1 to 100, demonstrating the use of `for` loops and conditional logic.

- **`validate_input.py`**: A script that asks for user input and validates whether it is a number or a string, showcasing user interaction and string methods.

- **`data_generator.py`**: A script that generates a list of dictionaries, with each dictionary representing a customer and containing a unique ID, name, and email. This project demonstrates the use of lists, dictionaries, and loops to generate structured data.

- **`parse_log.py`**: A script that reads a text file and prints out only the lines containing the word "error," demonstrating file handling and string searching.

- **`user_profile.py`**: A script that creates a dictionary and uses a `for` loop to print each key-value pair, demonstrating the use of dictionaries and the `.items()` method.

- **`stock_fetcher.py`**: A script that contains a reusable function to fetch real-time stock price data from a public API, demonstrating how to use the `requests` library and `JSON` data.

- **`zigzag.py`**: A personal project that creates a simple console animation, demonstrating the use of an infinite `while` loop and conditional logic.

---

### Connect with me

[LinkedIn](https://www.linkedin.com/in/voncleph) | [GitHub](https://github.com/D-Voncleph)