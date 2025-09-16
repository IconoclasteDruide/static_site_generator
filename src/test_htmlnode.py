import unittest

from src.htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="p", value="Hello world!")
        node2 = HTMLNode(tag="p", value="Hello world!")
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)

    def test_props_to_html(self):
        node = HTMLNode(tag="p", value="Hello world!", props={"status": "awesome"})
        self.assertEqual(node.props_to_html(), f' status="awesome"')

    def test_repr(self):
        childNode = HTMLNode(tag="p", value="not really")
        node = HTMLNode(tag="h1", value="Best title", props={"color": "red"}, children=[childNode])
        node_print = node.__repr__()
        self.assertEqual("""HTMLNode: tag='h1';\nvalue='Best title';\nnumber of children=1;\nprops=' color="red"'""", node_print)

if __name__ == "__main__":
    unittest.main()
