def is_single_plain_html_node(children: list) -> bool:
    if len(children) != 1:
        return False
    if children[0].tag:
        return False
    return True