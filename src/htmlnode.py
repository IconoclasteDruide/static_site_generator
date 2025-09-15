class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag #HTML tag name; without one, tag will just render as raw text
        self.value = value #text inside of tag; without one, will be assumed to have children
        self.children = children #other nodes that are the children of this node; without one, will be assumed to have a value
        self.props = props #key-value pairs representing attributes of the HTML tag
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        to_html_attribute = ""
        if not self.props:
            return None
        for key, value in self.props.items():
            to_html_attribute += f' {key}="{value}"'
        return to_html_attribute
    
    def __repr__(self):
        numChildren = len(self.children)
        return f"HTMLNode: tag='{self.tag}';\nvalue='{self.value}';\nnumber of children={numChildren};\nprops='{self.props_to_html()}'"