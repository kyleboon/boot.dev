from extract_markdown_images import extract_markdown_images
import unittest

class TestExtractMarkdownImages(unittest.TestCase):
    def testExtractMarkdownImages(self):
        self.assertEqual(
            extract_markdown_images("![alt text](https://www.google.com)"),
            [('alt text', 'https://www.google.com')])
        self.assertEqual(
            extract_markdown_images("![alt text](https://www.google.com) and some text and another link ![alt text](https://www.google.com)"),
            [('alt text', 'https://www.google.com'), ('alt text', 'https://www.google.com')])
