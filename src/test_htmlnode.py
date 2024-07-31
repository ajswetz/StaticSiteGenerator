import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag="a", value="my link", props={"href": "https://me.com"})
        props_to_html = node.props_to_html()
        self.assertIsInstance(props_to_html, str)
        self.assertEqual(props_to_html[0], " ")
        self.assertIn(' href="https://me.com"', props_to_html)

if __name__ == "__main__":
    unittest.main()
