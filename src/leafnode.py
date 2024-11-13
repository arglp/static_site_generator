from htmlnode import HTMLNode
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=[], props=props)
    
    def to_html(self):
        if self.value == "" or self.value is None:
            raise ValueError("LeafNode needs a value")
        if self.tag == None:
            return self.value
        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

