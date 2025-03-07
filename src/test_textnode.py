import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)        
        self.assertEqual(node.url, None)

    def test_url_inot_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.boot.dev")        
        self.assertEqual(node.url, "www.boot.dev")

if __name__ == "__main__":
    unittest.main()
