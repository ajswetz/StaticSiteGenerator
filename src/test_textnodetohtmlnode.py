import unittest

from textnode import TextNode
from htmlnode import LeafNode
from textnodetohtmlnode import text_node_to_html_node


class TestTextToHTMLNode(unittest.TestCase):
    def test_unsupported_type(self):
        list_item = TextNode("This is a list item", "list")
        self.assertRaises(ValueError, lambda: text_node_to_html_node(list_item))
        
    def test_plain_text(self):
        plain_text_node = TextNode("This is a plain text node", "text")
        converted_node = text_node_to_html_node(plain_text_node)
        plain_text_leaf = LeafNode(value="This is a plain text node")
        self.assertEqual(converted_node.value, plain_text_leaf.value)

    def test_bold_text(self):
        bold_text_node = TextNode("This is a bold text node", "bold")
        converted_node = text_node_to_html_node(bold_text_node)
        bold_text_leaf = LeafNode(value="This is a bold text node", tag="b")
        self.assertEqual(converted_node.value, bold_text_leaf.value)
        self.assertEqual(converted_node.tag, bold_text_leaf.tag)

    def test_italic_text(self):
        italic_text_node = TextNode("This is an italic node", "italic")
        converted_node = text_node_to_html_node(italic_text_node)
        italic_text_leaf = LeafNode(value="This is an italic node", tag="i")
        self.assertEqual(converted_node.value, italic_text_leaf.value)
        self.assertEqual(converted_node.tag, italic_text_leaf.tag)

    def test_code_text(self):
        code_text_node = TextNode("print('Hello World')", "code")
        converted_node = text_node_to_html_node(code_text_node)
        code_text_leaf = LeafNode(value="print('Hello World')", tag="code")
        self.assertEqual(converted_node.value, code_text_leaf.value)
        self.assertEqual(converted_node.tag, code_text_leaf.tag)

    def test_link_text(self):
        link_node = TextNode("Link Display Text", "link", "https://me.com/")
        converted_node = text_node_to_html_node(link_node)
        props = {"href": link_node.url}
        link_leaf = LeafNode(value=link_node.text, tag="a", props=props)
        self.assertEqual(converted_node.value, link_leaf.value)
        self.assertEqual(converted_node.tag, link_leaf.tag)
        self.assertEqual(converted_node.props, link_leaf.props)

    def test_image_text(self):
        image_node = TextNode("alt text for my image", "image", "content/images/img.jpeg")
        converted_node = text_node_to_html_node(image_node)
        props = {"src": image_node.url, "alt": image_node.text}
        image_leaf = LeafNode(value="", tag="img", props=props)
        self.assertEqual(converted_node.value, image_leaf.value)
        self.assertEqual(converted_node.tag, image_leaf.tag)
        self.assertEqual(converted_node.props, image_leaf.props)
    

if __name__ == "__main__":
    unittest.main()
