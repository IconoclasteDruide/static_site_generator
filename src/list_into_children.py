import re

from src.htmlnode import ParentNode, LeafNode
from src.block_to_block_type import BlockType
from src.block_into_children import block_into_children

def list_into_children(list_block: str, list_type: BlockType) -> list[LeafNode, ParentNode]:
    list_items = list_block.split("\n")
    html_list = []
    for list_item in list_items:
        match list_type:
            case BlockType.UNORD:
                only_text = list_item.lstrip('- ')
            case BlockType.ORD:
                only_text = re.sub(r'^\d+\. ', '', list_item)
        list_item_children = block_into_children(only_text)
        if len(list_item_children) == 1:
            list_item_children = None
            list_node = LeafNode('li', only_text)
        else:
            list_node = ParentNode(list_type, list_item_children)
        html_list.append(list_node)
    return html_list