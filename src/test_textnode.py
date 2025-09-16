import unittest

from src.textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Testing printing", TextType.ITALIC)
        print_node = node.__repr__()
        self.assertEqual(print_node, f"TextNode({node.text}, {node.text_type.value}, {node.url})")

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url_none(self):
        node = TextNode("Testsing empty url", TextType.LINK)
        self.assertEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()
