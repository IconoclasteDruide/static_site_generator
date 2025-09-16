from src.extract_markdown import extract_markdown_images, extract_markdown_links

from src.textnode import TextNode, TextType

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    newNodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if not images:
            newNodes.append(node)
            continue
        nodeText = node.text
        for image in images:
            text, imageLink = image
            md_text = f"![{text}]({imageLink})"
            pre, post = nodeText.split(md_text, 1)
            if pre:
                newNodes.append(TextNode(pre, TextType.PLAIN))
            newNodes.append(TextNode(text, TextType.IMAGE, imageLink))
            nodeText = post
        if post:
            newNodes.append(TextNode(post, TextType.PLAIN))
    return newNodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    newNodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        nodeText = node.text
        if not links:
            newNodes.append(node)
            continue
        for link in links:
            text, linkUrl = link
            md_text = f"[{text}]({linkUrl})"
            pre, post = nodeText.split(md_text, 1)
            if pre:
                newNodes.append(TextNode(pre, TextType.PLAIN))
            newNodes.append(TextNode(text, TextType.LINK, linkUrl))
            nodeText = post
        if post:
            newNodes.append(TextNode(post, TextType.PLAIN))
    return newNodes