
import unittest
from scripts import data_preprocessing, model_training, voice_synthesis, speech_recognition, ai_conversation

class TestMain(unittest.TestCase):

    def test_data_preprocessing(self):
        self.assertEqual(data_preprocessing.process_data("jay_abraham_teachings.txt"), True)

    def test_model_training(self):
        self.assertEqual(model_training.train_model(), True)

    def test_voice_synthesis(self):
        self.assertEqual(voice_synthesis.synthesize_voice("Hello, I am Jay Abraham."), True)

    def test_speech_recognition(self):
        self.assertEqual(speech_recognition.recognize_speech("Hello, AI Mentor."), True)

    def test_ai_conversation(self):
        self.assertEqual(ai_conversation.start_conversation(), True)

if __name__ == '__main__':
    unittest.main()
