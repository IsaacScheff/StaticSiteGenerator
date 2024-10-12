from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have value")
        
        if self.tag == None: 
            return self.value
        elif self.props == None: #tag without props
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else: #tag with props
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
