import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_initialization(self):
        node = LeafNode("p", "text", {"class": "highlight"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "text")
        self.assertEqual(node.props, {"class": "highlight"})

    def test_to_html1(self):
        node = LeafNode("p", "this is a paragraph")
        expected = "<p>this is a paragraph</p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html(self):
        node = LeafNode("a", "click this link", {"href": "https://wizard-bear.com", "target": "_blank"})
        expected = '<a href="https://wizard-bear.com" target="_blank">click this link</a>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html(self):
        with self.assertRaises(ValueError):
            node = LeafNode("a", None)
            node.to_html()

    def test_repr(self):
        node = LeafNode("p", "text")
        self.assertEqual(node.__repr__(), "LeafNode(p, text, None)")
