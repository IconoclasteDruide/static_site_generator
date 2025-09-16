import unittest

from src.markdown_to_blocks import markdown_to_blocks

class TestMDToBlocks(unittest.TestCase):
    def test_md_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_md_with_whspace_to_blocks(self):
        md = '''


\t *This is a header after unneeded spacing.

This is plain text. \t


 - This is an unordered list.\t
  - This a list item. 
- Should be a pretty serious test.

'''