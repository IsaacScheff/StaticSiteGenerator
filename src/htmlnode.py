class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
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

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode has no tag")
        if self.children == None:
            raise ValueError("ParentNode has no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
        case "image":
            return LeafNode("img", "", {"src": f"{text_node.url}", "alt": text_node.text})
        case _:
            raise Exception("Text node of unsupported type")
