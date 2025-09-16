import unittest

from src.textnode import TextNode, TextType
from src.split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_bold_node_del(self):
        node = TextNode("Test with **bold** text.", TextType.PLAIN)
        newNodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(newNodes, [TextNode('Test with ', TextType.PLAIN), TextNode('bold', TextType.BOLD), TextNode(' text.', TextType.PLAIN)])

    def test_ital_node_del(self):
        node = TextNode("Test with _italic_ text _here_ and _there._", TextType.PLAIN)
        newNodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(newNodes, [TextNode('Test with ', TextType.PLAIN), TextNode('italic', TextType.ITALIC), TextNode(' text ', TextType.PLAIN), TextNode('here', TextType.ITALIC), TextNode(' and ', TextType.PLAIN), TextNode('there.', TextType.ITALIC)])

    def test_longer_bold_node_del(self):
        node  = TextNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", TextType.PLAIN)
        newNodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(newNodes, [TextNode('This is ', TextType.PLAIN), TextNode('text', TextType.BOLD), TextNode(' with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)', TextType.PLAIN)])


if __name__ == "__main__":
    unittest.main()
