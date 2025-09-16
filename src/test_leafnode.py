import unittest

from src.htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self) -> None:
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self) -> None:
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")

    def test_leaf_to_html_with_props(self) -> None:
        node = LeafNode("h1", "Hello, world!", {'color': 'blue', 'size': 'big'})
        self.assertEqual(node.to_html(), """<h1 color="blue" size="big">Hello, world!</h1>""")
