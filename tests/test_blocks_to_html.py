import unittest

from src.markdown_to_html_node import markdown_to_html_node

class TestMDBlockIntoHTMLWithChildren(unittest.TestCase):
    def test_para_block(self):
        md = """This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>")

    def test_code_block(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>\nThis is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_header_block(self):
        md = """

## This is an h2 header

# This is an h1 header **with bold**!

Followed by an important

- list
- listing
- items"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, 
            "<div><h2>This is an h2 header</h2><h1>This is an h1 header <b>with bold</b>!</h1><p>Followed by an important</p><ul><li>list</li><li>listing</li><li>items</li></ul></div>"
            )
        
    def test_blockq_block_and_ordered_list(self):
        md = """

> Someone important said something important.

1. list
2. listing
4. items"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, 
            "<div><blockquote>Someone important said something important.</blockquote><ol><li>list</li><li>listing</li><li>items</li></ol></div>"
            )
    def test_blocks_with_single_text(self):
        md = """# **This is a bold header**

- This is a list where whole items are a single text node
- [nhl.com](https://nhl.com)
- _italics are for cools_"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, 
            '<div><h1><b>This is a bold header</b></h1><ul><li>This is a list where whole items are a single text node</li><li><a href="https://nhl.com">nhl.com</a></li><li><i>italics are for cools</i></li></ul></div>'
            )