import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.HTML)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.at")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.at")
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = TextNode(None, TextType.BOLD, None)
        node2 = TextNode(None, TextType.BOLD)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()