
import unittest
from scripts.ai_conversation import AIConversation

class TestAIConversation(unittest.TestCase):

    def setUp(self):
        self.ai_conversation = AIConversation()

    def test_response(self):
        input_text = "What is the strategy of preeminence?"
        response = self.ai_conversation.get_response(input_text)
        self.assertIsNotNone(response)

    def test_transcription(self):
        input_text = "What is the strategy of preeminence?"
        self.ai_conversation.get_response(input_text)
        transcription = self.ai_conversation.get_transcription()
        self.assertIn(input_text, transcription)

if __name__ == '__main__':
    unittest.main()

