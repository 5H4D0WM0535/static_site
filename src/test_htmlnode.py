import unittest

from htmlnode import HTMLNode 


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
    
    def test_repr_method(self):
        node = HTMLNode(tag="p", value="Hello", children=[], props={"class": "text"})
        expected_repr = "HTMLNode(p Hello [] {'class': 'text'})"
        self.assertEqual(repr(node), expected_repr)
    
    def test_to_html_not_implemented(self):
        node = HTMLNode(tag="div")
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()
