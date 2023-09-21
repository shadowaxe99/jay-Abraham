
import tensorflow as tf
from tensorflow import keras
from nltk.tokenize import word_tokenize
from gtts import gTTS
import speech_recognition as sr
import os

class AI_Conversation:
    def __init__(self):
        self.nlp_model = keras.models.load_model('models/nlp_model.h5')
        self.voice_model = keras.models.load_model('models/voice_model.h5')
        self.recognizer = sr.Recognizer()

    def transcribe(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            audio = self.recognizer.record(source)
        text = self.recognizer.recognize_google(audio)
        return text

    def respond(self, text):
        tokens = word_tokenize(text)
        prediction = self.nlp_model.predict(tokens)
        response = ' '.join(prediction)
        return response

    def synthesize_voice(self, text):
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save('response.mp3')
        os.system('mpg321 response.mp3')

    def converse(self, audio_file):
        transcription = self.transcribe(audio_file)
        with open('data/transcriptions.txt', 'a') as file:
            file.write(transcription + '\n')
        response = self.respond(transcription)
        self.synthesize_voice(response)

if __name__ == "__main__":
    ai = AI_Conversation()
    ai.converse('input.mp3')
