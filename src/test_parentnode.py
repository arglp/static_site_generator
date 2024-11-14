import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_init1(self):
        child_node = LeafNode("b", "text", {"class": "highlight"})
        parent_node = ParentNode("p", child_node)
        self.assertEqual(parent_node.tag, "p")
        self.assertEqual(parent_node.value, None)
        self.assertEqual(parent_node.children, child_node)

    def test_init2(self):
        child_node = LeafNode("b", "text", {"class": "highlight"})
        parent_node = ParentNode("p", child_node, {"href": "google.at"})
        self.assertEqual(parent_node.tag, "p")
        self.assertEqual(parent_node.value, None)
        self.assertEqual(parent_node.children, child_node)
        self.assertEqual(parent_node.props, {"href": "google.at"})
    
    def test_to_html1(self):
        child_node = LeafNode("b", "text", {"class": "highlight"})
        parent_node = ParentNode("p", [child_node], {"href": "google.at"})
        self.assertEqual(parent_node.to_html(), '<p href="google.at"><b class="highlight">text</b></p>')
    
    def test_to_html2(self):
        child_node = LeafNode("b", "text", {"class": "highlight"})
        child_node2 = LeafNode("i", "inverted")
        parent_node = ParentNode("p", [child_node2, child_node], {"href": "google.at"})
        self.assertEqual(parent_node.to_html(), '<p href="google.at"><i>inverted</i><b class="highlight">text</b></p>')

    def test_to_html3(self):
        child_node = LeafNode("b", "text", {"class": "highlight"})
        child_node2 = LeafNode("i", "inverted")
        child_node3 = LeafNode("x", "xxx")
        parent_node2 = ParentNode("a", [child_node3])
        parent_node = ParentNode("p", [child_node2, child_node, parent_node2], {"href": "google.at"})        
        self.assertEqual(parent_node.to_html(), '<p href="google.at"><i>inverted</i><b class="highlight">text</b><a><x>xxx</x></a></p>')

    def test_to_html4(self):
        with self.assertRaises(ValueError):
            child_node = LeafNode("b", "text", {"class": "highlight"})
            child_node2 = LeafNode("i", "inverted")
            child_node3 = LeafNode("x", "xxx")
            parent_node2 = ParentNode("a", [child_node3])
            parent_node = ParentNode("p", [], {"href": "google.at"})        
            parent_node.to_html()

    def test_to_html5(self):
        with self.assertRaises(ValueError):
            child_node = LeafNode("b", "text", {"class": "highlight"})
            child_node2 = LeafNode("i", "inverted")
            child_node3 = LeafNode("x", "xxx")
            parent_node2 = ParentNode("a", [])
            parent_node = ParentNode("p", [child_node, parent_node2], {"href": "google.at"})        
            parent_node.to_html()
    
    def test_to_html6(self):
        child_node = LeafNode("b", "text", {"class": "highlight"})
        child_node2 = LeafNode(None, "inverted")
        child_node3 = LeafNode("x", "xxx")
        parent_node2 = ParentNode("a", [child_node3])
        parent_node = ParentNode("p", [child_node2, child_node, parent_node2], {"href": "google.at"})        
        self.assertEqual(parent_node.to_html(), '<p href="google.at">inverted<b class="highlight">text</b><a><x>xxx</x></a></p>')

    def test_to_html7(self):
        with self.assertRaises(ValueError):
            child_node = LeafNode("b", "text", {"class": "highlight"})
            child_node2 = LeafNode("i", "inverted")
            child_node3 = LeafNode("x", "xxx")
            parent_node2 = ParentNode(None, [child_node3])
            parent_node = ParentNode("p", [child_node, parent_node2], {"href": "google.at"})        
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()
