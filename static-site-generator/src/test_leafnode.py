from leafnode import LeafNode
import unittest

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        self.assertEqual(LeafNode("p", "This is a paragraph of text.").to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
        self.assertEqual(LeafNode(None, "value", {}).to_html(), 'value')
        with self.assertRaises(ValueError):
            LeafNode("tag", None, {}).to_html()


if __name__ == "__main__":
    unittest.main()

