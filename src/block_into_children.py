from src.htmlnode import LeafNode
from src.md_to_textnodes import md_to_textnodes
from src.textnode_to_htmlnode import text_node_to_html_node

def block_into_children(block: str) -> list[LeafNode]:
    nodes = md_to_textnodes(block)
    html_nodes = []
    for node in nodes:
        text_node = text_node_to_html_node(node)
        text_node.value = text_node.value.replace('\n', ' ')
        html_nodes.append(text_node)
    if not html_nodes:
        raise ValueError("Html nodes from md block should not be empty.")
    return html_nodes