import regex as re

from src.htmlnode import ParentNode, LeafNode
from src.block_to_block_type import block_to_block_type, BlockType
from src.markdown_to_blocks import markdown_to_blocks
from src.block_into_children import block_into_children
from src.list_into_children import list_into_children

from src.test_for_single_plain_html_node import is_single_plain_html_node

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    new_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.CODE:
                inner_node = LeafNode(block_type, block.strip('```'))
                new_node = ParentNode('pre', children=[inner_node])
                new_nodes.append(new_node)
            case BlockType.ORD | BlockType.UNORD:
                new_node = ParentNode(block_type, list_into_children(block, block_type))
                new_nodes.append(new_node)
            case BlockType.PARA:
                children = block_into_children(block)
                if is_single_plain_html_node(children):
                    new_node = LeafNode(block_type, children[0].value)
                else:
                    new_node = ParentNode(block_type, children)
                new_nodes.append(new_node)
            case BlockType.QUOTE :
                block = block.lstrip('>').lstrip()
                children = block_into_children(block)
                if is_single_plain_html_node(children):
                    new_node = LeafNode(block_type, children[0].value)
                else:
                    new_node = ParentNode(block_type, children)
                new_nodes.append(new_node)
            case 'h1'|'h2'|'h3'|'h4'|'h5'|'h6':
                block = block.lstrip('#').lstrip()
                children = block_into_children(block)
                if is_single_plain_html_node(children):
                    new_node = LeafNode(block_type, children[0].value)
                else:
                    new_node = ParentNode(block_type, children)
                new_nodes.append(new_node)

    top_node = ParentNode('div', new_nodes)
    return top_node