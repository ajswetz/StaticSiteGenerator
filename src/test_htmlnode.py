import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        self.assertEqual(leaf.value, test_to_html)

    def test_props(self):
        leaf = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        test_to_html = leaf.to_html()
        props_to_html = leaf.props_to_html()
        self.assertIn(leaf.tag, test_to_html)
        self.assertIn(props_to_html, test_to_html)

class TestParentNode(unittest.TestCase):
    def test_children_required(self):
        self.assertRaises(ValueError, ParentNode, tag="p", children=[])
        self.assertRaises(ValueError, ParentNode, tag="p", children=None)

    def test_no_value(self):
        self.assertRaises(ValueError, ParentNode, value="test", tag="p", children=["child1"])

    def test_tag_required(self):
        self.assertRaises(ValueError, ParentNode, tag="", children=["child1"])
        self.assertRaises(ValueError, ParentNode, tag=None, children=["child1"])

    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )
        to_html_output = node.to_html()
        self.assertIsInstance(to_html_output, str)

    def test_nested_ParentNode(self):

        node2 = ParentNode(
            tag="p",
            children=[
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ],
        )

        node1 = ParentNode(tag="body", children=[node2])

        full_html_str = node1.to_html()

        self.assertIsInstance(full_html_str, str)
        self.assertIn(node1.tag, full_html_str)
        self.assertIn(node2.tag, full_html_str)

if __name__ == "__main__":
    unittest.main()
