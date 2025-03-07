from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        if props is None:
            props = {}
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.tag is None:
            return self.value

        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
       
        html = f"<{self.tag}"
    
        if self.props:
            html += " " + self.props_to_html()

        html += f">{self.value}</{self.tag}>"
        return html

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
