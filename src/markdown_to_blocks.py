import regex as re

def markdown_to_blocks(markdown: str) -> list[str]:
    markdown = re.sub(r'\n\n\n+', r'\n\n', markdown)
    markdown = re.sub(r'(?<!\n)\n(#+.+)', r'\n\n\1', markdown)
    markdown = re.sub(r'(?<=\n|^)(#+.+)\n(?!\n)', r'\1\n\n', markdown)
    markdown = re.sub(r'^\n+', r'', markdown)
    markdown = re.sub(r'\n+$', r'', markdown)
    markdown = re.sub(r'\n[^\n\S]+', r'\n', markdown)
    markdown = re.sub(r'[^\n\S]+\n', r'\n', markdown)
    blocks = markdown.split('\n\n')
    blocks[0] = blocks[0].lstrip()
    blocks[-1] = blocks[-1].rstrip()
    return blocks