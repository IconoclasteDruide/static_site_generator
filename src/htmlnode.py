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
        if self.children:
            numChildren = len(self.children)
        else:
            numChildren = 0
        return f"HTMLNode: tag='{self.tag}';\nvalue='{self.value}';\nnumber of children={numChildren};\nprops='{self.props_to_html()}'"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, children=None, props=props)
    
    def to_html(self):
        if not self.tag:
            return self.value
        html_props = self.props_to_html()
        if not html_props:
            html_props = ""

        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            return ValueError('ParentNode is missing a tag.')
        if not self.children:
            return ValueError('Parent node does not have any children.')
        html_children = []
        for child in self.children:
            html_children.append(child.to_html())
        html_children = "".join(html_children)
        html_props = self.props_to_html()
        if not html_props:
            html_props = ""
        html_tag = f'{self.tag}'
        return f"<{html_tag}{html_props}>{html_children}</{html_tag}>"
        