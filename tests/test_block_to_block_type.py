import unittest

from src.block_to_block_type import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type1(self):
        block = '```python\ntest = "4"\ntest.isdigit()\n# True\n```'
        b_type = block_to_block_type(block)
        self.assertEqual(BlockType.CODE, b_type)

    def test_block_to_block_type2(self):
        block = '1. How does direct speech begin?\n2. How does it end?\nHow do participles modify verbs of speaking?'
        b_type = block_to_block_type(block)
        self.assertEqual(BlockType.ORD, b_type)

    def test_block_to_block_type2(self):
        block = '- Look for or perceive naturally occurring sections in the text\n- Correctly group texts together that have been inadvertently separated by chapter divisions\n- Read the Bible undistracted by numbers and superscripts which are not inspired\n- Experience the text as in a communal reading\n- Think beyond individual verses to thinking the message of the larger context\n- etc.'
        b_type = block_to_block_type(block)
        self.assertEqual(BlockType.UNORD, b_type)

    def test_block_to_block_type3(self):
        block = '2.1 children per woman is the fertility rate required to maintain a stable population.'
        b_type = block_to_block_type(block)
        self.assertEqual(BlockType.PARA, b_type)

    def test_block_to_block_type4(self):
        block = '### Purpose of the Speech Act'
        b_type = block_to_block_type(block)
        self.assertEqual(BlockType.HEAD, b_type)

    def test_block_to_block_type5(self):
        block = '>Thus _He_ declared all foods clean. (NASB1995)'
        b_type = block_to_block_type(block)
        self.assertEqual(BlockType.QUOTE, b_type)
