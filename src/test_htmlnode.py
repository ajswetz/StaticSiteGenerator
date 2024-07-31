import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="my link", props={"href": "https://me.com"})
        props_to_html = node.props_to_html()
        self.assertIsInstance(props_to_html, str)
        self.assertEqual(props_to_html[0], " ")
        self.assertIn(' href="https://me.com"', props_to_html)

class TestLeafNode(unittest.TestCase):
    def test_no_children(self):
        self.assertRaises(ValueError, LeafNode, value="test", children=["child1", "child2"])

    def test_value_required(self):
        self.assertRaises(ValueError, LeafNode, value=None)

    def test_no_tag(self):
        leaf = LeafNode(value="This should return as raw text.")
        test_to_html = leaf.to_html()
        self.assertEquals(leaf.value, test_to_html)

    def test_props(self):
        leaf = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        test_to_html = leaf.to_html()
        props_to_html = leaf.props_to_html()
        self.assertIn(leaf.tag, test_to_html)
        self.assertIn(props_to_html, test_to_html)

if __name__ == "__main__":
    unittest.main()
