from pydub import AudioSegment
import speech_recognition as sr

def transcribe_audio(audio_segment, recognizer):
    with sr.AudioFile(audio_segment.export(format="wav")) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return ""

def main(video):
    audio = AudioSegment.from_file(video, format="mp4")

    recognizer = sr.Recognizer()
    transcribed_text = transcribe_audio(audio, recognizer)

    return transcribed_text
