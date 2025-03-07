from extract_markdown_links import extract_markdown_links
import unittest

class TestExtractMarkdownLinks(unittest.TestCase):
    def testExtractMarkdownLinks(self):
        self.assertEqual(
            extract_markdown_links("[link text](https://www.google.com)"),
            [('link text', 'https://www.google.com')])
        self.assertEqual(
            extract_markdown_links("[link text](https://www.google.com) and some text and another link [link text](https://www.google.com)"),
            [('link text', 'https://www.google.com'), ('link text', 'https://www.google.com')])
