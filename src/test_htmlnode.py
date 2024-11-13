import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_initialization(self):
        node = HTMLNode("p", "text", [], {"class": "highlight"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "text")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "highlight"})

    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://wizard-bear.com", "target": "_blank"})
        expected = ' href="https://wizard-bear.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html(self):
        node = HTMLNode(None)
        expected = ""
        self.assertEqual(node.props_to_html(), expected)

    def test_repr(self):
        node = HTMLNode("div", "content")
        expected_repr = "THTMLNode(tag: div, value: content, children: None, props: None)"
        self.assertEqual(repr(node), expected_repr)