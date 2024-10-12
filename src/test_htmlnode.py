import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):    
    def test_htmlnode_no_values(self):
        node = HTMLNode()
        print(node)
        self.assertEqual(node.__repr__(), "HTML Node: Tag-None Value-None\nChildren-None\nProps-None")
    
    def test_htmlnode_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props = props)
        html_output = node.props_to_html()
        self.assertEqual(html_output, " href=\"https://www.google.com\" target=\"_blank\"")
    
    def test_htmlnode_with_tag(self):
        node = HTMLNode(tag = "h1")
        self.assertEqual(node.__repr__(), "HTML Node: Tag-h1 Value-None\nChildren-None\nProps-None")

if __name__ == "__main__":
    print("test")
    unittest.main()