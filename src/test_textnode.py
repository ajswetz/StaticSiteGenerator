import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_empty_url(self):
        node = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", "bold", "https://me.com/")
        node2 = TextNode("This is a text node", "bold", "https://me.com/")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This node is different", "bold")
        self.assertNotEqual(node, node2)

    def test_not_eq_texttype(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
