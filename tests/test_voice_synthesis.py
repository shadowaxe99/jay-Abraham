
import unittest
from scripts.voice_synthesis import synthesize_voice

class TestVoiceSynthesis(unittest.TestCase):

    def setUp(self):
        self.text = "Hello, I am Jay Abraham."

    def test_synthesize_voice(self):
        output = synthesize_voice(self.text)
        self.assertIsNotNone(output)

if __name__ == '__main__':
    unittest.main()
