import re

from enum import Enum

class BlockType(Enum):
    PARA = 'p',
    HEAD = 'h',
    CODE = 'code',
    QUOTE = 'blockquote',
    UNORD = 'ul',
    ORD  = 'li'

def block_to_block_type(block: str) -> BlockType:
    if block.startswith('#'):
        h_level = len(re.match(r'#+', block).group())
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

