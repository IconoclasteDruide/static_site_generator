from src.textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    newNodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            newNodes.append(node)
            continue
        if delimiter in node.text:
            delimiter_count = node.text.count(delimiter)
            nodeText = node.text
            if delimiter_count % 2 == 0:
                while delimiter_count != 0:
                    delimiter_count -= 2
                    pre, newTypeText, post = nodeText.split(delimiter, 2)
                    if pre:
                        newNodes.append(TextNode(pre, TextType.PLAIN))
                    newNodes.append(TextNode(newTypeText, text_type))
                    nodeText = post
                if post:
                    newNodes.append(TextNode(post, TextType.PLAIN))
            else:
                raise ValueError(f"Invalid Markdown passed into split_nodes_delimiter. The node text '{node.text}' contains an uneven number of the delimiter '{delimiter}'.")
        else:
            newNodes.append(node)
    return newNodes