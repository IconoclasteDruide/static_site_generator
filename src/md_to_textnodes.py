from src.textnode import TextNode, TextType
from src.split_img_and_links import split_nodes_image, split_nodes_link
from src.split_nodes_delimiter import split_nodes_delimiter

def md_to_textnodes(md: str) -> list[TextNode]:
    node = TextNode(md, TextType.PLAIN)
    nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes