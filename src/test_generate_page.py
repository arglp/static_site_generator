import unittest
from generate_page import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
    
    def test_extract_title2(self):
        self.assertEqual(extract_title("First line\n# Hello"), "Hello")