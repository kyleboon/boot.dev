from leafnode import LeafNode
from parentnode import ParentNode
import unittest

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        self.assertEqual(
            ParentNode("div", [LeafNode("p", "This is a paragraph of text.")]).to_html(), "<div><p>This is a paragraph of text.</p></div>")
        self.assertEqual(ParentNode("div", [
            LeafNode("p", "This is a paragraph of text."),
            LeafNode("p", "This is another paragraph of text.")]).to_html(), "<div><p>This is a paragraph of text.</p><p>This is another paragraph of text.</p></div>")
        self.assertEqual(ParentNode("div", [LeafNode("p", "This is a paragraph of text."), LeafNode("p", "This is another paragraph of text.")], {"class": "container"}).to_html(), "<div class=\"container\"><p>This is a paragraph of text.</p><p>This is another paragraph of text.</p></div>")
        self.assertEqual(ParentNode("div", [ParentNode("div", [LeafNode("p", "This is a paragraph of text."), LeafNode("p", "This is another paragraph of text.")])]).to_html(), "<div><div><p>This is a paragraph of text.</p><p>This is another paragraph of text.</p></div></div>")

        with self.assertRaises(ValueError):
            ParentNode(None, [ParentNode("p", ["This is a paragraph of text."])]).to_html()
        with self.assertRaises(ValueError):
            ParentNode("div", [], {"class": "container"}).to_html()

if __name__ == "__main__":
    unittest.main()
