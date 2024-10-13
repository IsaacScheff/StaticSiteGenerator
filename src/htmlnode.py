class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_text = ""
        for prop in self.props:
            html_text += f" {prop}=\"{self.props[prop]}\""
        return html_text

    def __repr__(self):
        return f"HTML Node: Tag-{self.tag} Value-{self.value}\nChildren-{self.children}\nProps-{self.props}"
    
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