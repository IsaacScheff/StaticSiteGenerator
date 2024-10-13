import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):    
    def test_htmlnode_no_values(self):
        node = HTMLNode()
        self.assertEqual(node.__repr__(), "HTML Node: Tag-None Value-None\nChildren-None\nProps-None")
    
    def test_htmlnode_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props = props)
        html_output = node.props_to_html()
        self.assertEqual(html_output, " href=\"https://www.google.com\" target=\"_blank\"")
    
    def test_htmlnode_with_tag(self):
        node = HTMLNode(tag = "h1")
        self.assertEqual(node.__repr__(), "HTML Node: Tag-h1 Value-None\nChildren-None\nProps-None")
      
    def test_leafnode_only_value(self):
        node = LeafNode(None, "example text")
        self.assertEqual(node.__repr__(), "HTML Node: Tag-None Value-example text\nChildren-None\nProps-None")

    def test_leafnode_no_value(self):
        with self.assertRaises(TypeError):
            LeafNode()

    def test_leafnode_tag_no_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")


    def test_leafnode_tag_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    print("test")
    unittest.main()