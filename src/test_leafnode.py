import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):    
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

if __name__ == "__main__":
    print("test")
    unittest.main()