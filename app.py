from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
import json
import re
import os
from typing import Dict, Any

# Configure Gemini API
genai.configure(api_key="YOUR_API_KEY_HERE")
model = genai.GenerativeModel('gemini-2.0-flash-exp')

app = FastAPI()

def extract_youtube_id(url: str) -> str:
    """Extract YouTube video ID from URL"""
    try:
        if "youtube.com/watch?v=" in url:
            return url.split("v=")[1].split("&")[0]
        elif "youtu.be/" in url:
            return url.split("/")[-1].split("?")[0]
        else:
            raise ValueError("Invalid YouTube URL format")
    except Exception as e:
        raise ValueError(f"Could not extract video ID from URL: {str(e)}")

def fetch_youtube_transcript(video_id: str) -> str:
    """Fetch transcript from YouTube video ID"""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_transcript = ""
        for entry in transcript:
            full_transcript += entry['text'] + " "
        return full_transcript.strip()
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def send_to_gemini(transcript_text: str) -> Dict[str, str]:
    """Send transcript to Gemini for processing"""
    try:
        # Simple prompt for better results
        prompt = f"""Summarize this YouTube video transcript in 2 parts:
1. Topic (5-6 words max)
2. Summary (2-3 sentences)

Transcript: {transcript_text[:3000]}"""
        
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        
        # Split by lines and extract
        lines = [line.strip() for line in response_text.split('\n') if line.strip()]
        
        # Default values
        topic_name = "Video Summary"
        topic_summary = "Summary not available"
        
        # Simple extraction
        if len(lines) >= 2:
            topic_name = lines[0].replace('1.', '').replace('Topic:', '').replace('**', '').strip()
            topic_summary = ' '.join(lines[1:]).replace('2.', '').replace('Summary:', '').replace('**', '').strip()
        elif len(lines) == 1:
            topic_summary = lines[0]
            
        # Clean up
        topic_name = topic_name.replace('"', '').replace("'", "")[:50]
        topic_summary = topic_summary.replace('"', '').replace("'", "")
        
        return {
            "topic_name": topic_name,
            "topic_summary": topic_summary
        }
        
    except Exception as e:
        print(f"Error calling Gemini: {e}")
        return {
            "topic_name": "Processing Error",
            "topic_summary": f"Failed to generate summary: {str(e)}"
        }

@app.get("/summarize")
def get_summary(url: str) -> Dict[str, str]:
    """Get summary from YouTube URL"""
    try:
        # Extract video ID
        video_id = extract_youtube_id(url)
        
        # Fetch transcript
        transcript = fetch_youtube_transcript(video_id)
        
        if not transcript:
            return {
                "topic_name": "Transcript Error",
                "topic_summary": "Could not fetch transcript for this video. The video might not have captions available."
            }
        
        # Generate summary using Gemini
        summary = send_to_gemini(transcript)
        
        return summary
        
    except ValueError as e:
        return {
            "topic_name": "URL Error",
            "topic_summary": str(e)
        }
    except Exception as e:
        return {
            "topic_name": "Processing Error",
            "topic_summary": f"Failed to process video: {str(e)}"
        }

# Optional: Add a health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "YouTube Summarizer"}

# Additional utility functions (kept for compatibility)
def summarize_transcript_with_gemini(transcript):
    """Summarize transcript using Gemini (legacy function)"""
    gemini_response = send_to_gemini(transcript)
    if gemini_response:
        return gemini_response
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
