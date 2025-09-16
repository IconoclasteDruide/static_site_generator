from src.htmlnode import LeafNode, ParentNode, HTMLNode
from src.block_to_block_type import BlockType, block_to_block_type
from src.markdown_to_blocks import markdown_to_blocks
from src.md_to_textnodes import md_to_textnodes

def markdown_to_html_node(markdown: str) -> HTMLNode:
    top_node = HTMLNode()
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        new_node = HTMLNode(block_type, block)
    return 