from htmlnode import HtmlNode
import unittest

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        self.assertEqual(HtmlNode("tag", "value", [], {"key": "value"}).props_to_html(), 'key="value"')
        self.assertEqual(HtmlNode("tag", "value", [], {"key": "value", "key2": "value2"}).props_to_html(), 'key="value" key2="value2"')
        self.assertEqual(HtmlNode("tag", "value", [], {}).props_to_html(), '')

if __name__ == "__main__":
    unittest.main()
