import re

from enum import StrEnum

class BlockType(StrEnum):
    PARA = 'p'
    HEAD = 'h'
    CODE = 'code'
    QUOTE = 'blockquote'
    UNORD = 'ul'
    ORD  = 'ol'

def block_to_block_type(block: str) -> BlockType:
    if block.startswith('#'):
        h_level = len(re.match(r'#+', block).group())
        if h_level > 6:
            h_level = 6
        return f'{BlockType.HEAD}{h_level}'
    elif block.startswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith('-'):
        return BlockType.UNORD
    elif re.match(r'\d+\. ', block):
        return BlockType.ORD
    return BlockType.PARA

