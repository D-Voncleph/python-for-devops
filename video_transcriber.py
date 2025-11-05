import os
import sys
from pathlib import Path
import yt_dlp
import assemblyai as aai
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

# Configure AssemblyAI API key
aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')

def download_video(url: str, output_path: str = 'temp_video') -> str:
    """
    Download a YouTube video using yt-dlp
    Returns the path to the downloaded file
    """
    ydl_opts = {
        'format': 'bestaudio/best',  # We only need audio for transcription
        'outtmpl': f'{output_path}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return f"{output_path}.mp3"
    except Exception as e:
        print(f"Error downloading video: {str(e)}")
        sys.exit(1)

def transcribe_audio(file_path: str) -> str:
    """
    Transcribe audio file using AssemblyAI
    """
    try:
        # Create a transcriber
        config = aai.TranscriptionConfig(
            language_detection=True,  # Automatically detect language
        )
        transcriber = aai.Transcriber(config=config)
        
        # Start transcription
        print("Uploading audio file to AssemblyAI...")
        transcript = transcriber.transcribe(file_path)
        
        # Wait for transcription to complete
        while transcript.status != 'completed':
            print(f"Transcription status: {transcript.status}")
            if transcript.status == 'error':
                raise Exception("Transcription failed")
            time.sleep(3)
            transcript = transcriber.get_transcript(transcript.id)
        
        return transcript.text
        
    except Exception as e:
        print(f"Error transcribing audio: {str(e)}")
        return None
    finally:
        # Clean up the audio file
        try:
            os.remove(file_path)
            print(f"Cleaned up temporary file: {file_path}")
        except:
            print(f"Warning: Could not delete temporary file: {file_path}")

def main():
    if not os.getenv('ASSEMBLYAI_API_KEY'):
        print("Error: ASSEMBLYAI_API_KEY not found in environment variables")
        print("Please create a .env file with your AssemblyAI API key:")
        print("ASSEMBLYAI_API_KEY=your-api-key-here")
        sys.exit(1)

    # Get video URL from command line argument or prompt
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Please enter the YouTube video URL: ")

    print("Downloading video...")
    audio_file = download_video(url)
    
    print("Transcribing audio...")
    transcript = transcribe_audio(audio_file)
    
    if transcript:
        # Save transcript to file
        output_file = "transcript.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcript)
        print(f"\nTranscript saved to: {output_file}")

if __name__ == "__main__":
    main()