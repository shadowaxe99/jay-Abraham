
import unittest
from scripts import data_preprocessing

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        self.data_preprocessor = data_preprocessing.DataPreprocessor()

    def test_clean_text(self):
        text = "Hello, World! This is a test."
        expected_output = "hello world this is a test"
        self.assertEqual(self.data_preprocessor.clean_text(text), expected_output)

    def test_tokenize_text(self):
        text = "hello world this is a test"
        expected_output = ['hello', 'world', 'this', 'is', 'a', 'test']
        self.assertEqual(self.data_preprocessor.tokenize_text(text), expected_output)

    def test_build_vocab(self):
        tokens = ['hello', 'world', 'this', 'is', 'a', 'test']
        expected_output = {'hello': 0, 'world': 1, 'this': 2, 'is': 3, 'a': 4, 'test': 5}
        self.assertEqual(self.data_preprocessor.build_vocab(tokens), expected_output)

if __name__ == '__main__':
    unittest.main()
