class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        string = ""
        for prop in self.props:
            string += f' {prop}="{self.props[prop]}"'
        return string

    def __repr__(self):
        return f"THTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"