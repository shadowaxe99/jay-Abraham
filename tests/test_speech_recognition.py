
import unittest
import speech_recognition as sr
from scripts.speech_recognition import transcribe_audio

class TestSpeechRecognition(unittest.TestCase):

    def setUp(self):
        self.recognizer = sr.Recognizer()
        self.audio_file = "test_audio.wav"

    def test_transcribe_audio(self):
        transcript = transcribe_audio(self.recognizer, self.audio_file)
        self.assertIsInstance(transcript, str)

if __name__ == '__main__':
    unittest.main()
