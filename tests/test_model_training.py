
import unittest
from scripts import model_training
from tensorflow.keras.models import load_model

class TestModelTraining(unittest.TestCase):

    def setUp(self):
        self.model_training = model_training.ModelTraining()

    def test_train_nlp_model(self):
        self.model_training.train_nlp_model()
        model = load_model('models/nlp_model.h5')
        self.assertIsNotNone(model)

    def test_train_voice_model(self):
        self.model_training.train_voice_model()
        model = load_model('models/voice_model.h5')
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
