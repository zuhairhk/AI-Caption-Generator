# Terminal Caption Generator

Terminal Caption Generator is a Python project I created that uses the power of AI to generate captions for social media posts based on transcribed text from a video.

## How it Works

The project follows a simple workflow:

1. The mp4totxt.py module extracts transcribed audio from a video file in MP4 format using the Google Speech Recognition API. It converts the audio from the video into text.

2. The ai_gen.py module leverages OpenAI's GPT-3.5 Turbo model to generate captions. It takes the transcribed text and system prompts to generate a relevant caption.

3. The final step gives front-end users the option to enter additional prompts and tailor the caption to their preference.