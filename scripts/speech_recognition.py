
import speech_recognition as sr

def transcribe_audio(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    return text

if __name__ == "__main__":
    audio_file = "path_to_your_audio_file"
    print(transcribe_audio(audio_file))
