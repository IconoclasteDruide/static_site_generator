import re

from src.htmlnode import ParentNode, LeafNode
from src.block_to_block_type import BlockType
from src.block_into_children import block_into_children

from src. test_for_single_plain_html_node import is_single_plain_html_node

L_ITEM_TAG = 'li'

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
        if is_single_plain_html_node(list_item_children):
            list_node = LeafNode(L_ITEM_TAG, list_item_children[0].value)
        else:
            list_node = ParentNode(L_ITEM_TAG, list_item_children)
        html_list.append(list_node)
    return html_list