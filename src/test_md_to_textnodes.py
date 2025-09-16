import unittest

from src.md_to_textnodes import md_to_textnodes
from src.textnode import TextNode, TextType

class TestMDToTextNodes(unittest.TestCase):
    def test_md_to_textNodes(self):
        nodes = md_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertListEqual(nodes, [
    TextNode("This is ", TextType.PLAIN),
    TextNode("text", TextType.BOLD),
    TextNode(" with an ", TextType.PLAIN),
    TextNode("italic", TextType.ITALIC),
    TextNode(" word and a ", TextType.PLAIN),
    TextNode("code block", TextType.CODE),
    TextNode(" and an ", TextType.PLAIN),
    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", TextType.PLAIN),
    TextNode("link", TextType.LINK, "https://boot.dev"),
])


if __name__ == "__main__":
    unittest.main()