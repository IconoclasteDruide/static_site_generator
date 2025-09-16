import unittest

from src.textnode_to_htmlnode import text_node_to_html_node
from src.htmlnode import LeafNode
from src.textnode import TextNode, TextType

class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()