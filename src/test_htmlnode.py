import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_init(self):
        node = HTMLNode("div", "This is a div", [], {"class": "container"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "This is a div")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "container"})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=This is a div, children=[], props={'class': 'container'})")

    def test_htmlnode_add_child(self):
        parent_node = HTMLNode("div", "This is a div", [], {"class": "container"})
        child_node = HTMLNode("p", "This is a paragraph", [], {})
        parent_node.add_child(child_node)
        self.assertEqual(parent_node.children, [child_node])