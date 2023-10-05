#Terminal Caption Generator

Terminal Caption Generator is a Python project that uses the power of AI language models to generate captions for social media posts based on transcribed text from a video. It combines the functionality of three modules: terminal.py, mp4totxt.py, and ai_gen.py.

##How it Works

The project follows a simple workflow:

    The mp4totxt.py module extracts transcribed text from a video file in MP4 format using the Google Speech Recognition API. It converts the audio from the video into text.

    The ai_gen.py module leverages OpenAI's GPT-3.5 Turbo model to generate captions. It takes the transcribed text from step 1 and a system instruction as input and generates a relevant caption.

    The terminal.py script ties everything together. It provides an interactive terminal interface where you can input a video, receive generated captions, and edit the system instruction for caption generation.