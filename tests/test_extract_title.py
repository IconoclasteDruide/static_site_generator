import unittest

from src.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_basic_title(self):
        md = """# Hello World

This is a markdown file with **booooooooold**."""
        h1_header = extract_title(md)
        self.assertEqual(h1_header, 'Hello World')
    def test_many_titles(self):
        md = """## Hello World

This is a markdown file with **booooooooold**.

# And an h1 header here.   
"""
        h1_header = extract_title(md)
        self.assertEqual(h1_header, 'And an h1 header here.')