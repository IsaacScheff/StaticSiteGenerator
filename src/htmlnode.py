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