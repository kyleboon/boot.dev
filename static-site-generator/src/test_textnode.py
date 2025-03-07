from logging import warn
import unittest

from textnode import TextNode, split_nodes_delimiter
from textnode import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        node = TextNode("text", "bold", "url")
        node2 = TextNode("text", "bold", "url")

        self.assertEqual(node, node2)

        node = TextNode("text", "bold", "url")
        node2 = TextNode("text2", "bold", "url")

        self.assertNotEqual(node, node2)

        node = TextNode("text", "bold", "url")
        node2 = TextNode("text", "bold2", "url")

        self.assertNotEqual(node, node2)

        node = TextNode("text", "bold", "url")
        node2 = TextNode("text", "bold", "url2")

        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node(self):
        node = TextNode("This is a paragraph of text.", "text")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<p>This is a paragraph of text.</p>")

        node = TextNode("Click me!", "link", "https://www.google.com")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

        node = TextNode("This is a paragraph of text.", "bold")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<b>This is a paragraph of text.</b>")

        node = TextNode("This is a paragraph of text.", "italic")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<i>This is a paragraph of text.</i>")

        node = TextNode("This is a paragraph of text.", "code")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<code>This is a paragraph of text.</code>")

        node = TextNode("This is a paragraph of text.", "image", "https://www.google.com")
        self.assertEqual(text_node_to_html_node(node).to_html(), "<img src=\"https://www.google.com\" alt=\"This is a paragraph of text.\"></img>")

        with self.assertRaises(ValueError):
            node = TextNode("This is a paragraph of text.", "list")
            text_node_to_html_node(node).to_html()

    def test_split_nodes_delimiter(self):
        node = TextNode("This is a **paragraph** of text.", "text")
        split_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(split_nodes, [TextNode("This is a ", "text"), TextNode("paragraph", "bold"), TextNode(" of text.", "text")])

        node = TextNode("**This** is a **paragraph** of text.", "text")
        split_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(split_nodes, [TextNode("This", "bold"), TextNode(" is a ", "text"), TextNode("paragraph", "bold"), TextNode(" of text.", "text")])

        with self.assertRaises(ValueError):
            node = TextNode("****This** is a **paragraph** of text.", "text")
            split_nodes = split_nodes_delimiter([node], "**", "bold")


if __name__ == "__main__":
    unittest.main()
