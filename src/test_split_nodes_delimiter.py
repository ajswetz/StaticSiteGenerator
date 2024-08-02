import unittest

from textnode import TextNode
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_no_closing_delimiter(self):
        text_item = TextNode("I really want to *go to the store with you.", "text")
        self.assertRaises(Exception, lambda: split_nodes_delimiter(text_item))
        
    def test_text_no_delimiter(self):
        plain_text_node = TextNode("This is a plain text node", "text")
        old_nodes = [plain_text_node]
        new_nodes = split_nodes_delimiter(old_nodes, "*", "italic")
        self.assertEqual(old_nodes, new_nodes)

    def test_text_with_bold(self):
        bold_text_node = TextNode("This node has some **bold text** in it.", "text")
        old_nodes = [bold_text_node]
        new_nodes = split_nodes_delimiter(old_nodes, "**", "bold")
        self.assertEqual(3, len(new_nodes))
        self.assertEqual("bold text", new_nodes[1].text)

    def test_text_with_italic(self):
        italic_text_node = TextNode("This node has some *italic text* in it.", "text")
        old_nodes = [italic_text_node]
        new_nodes = split_nodes_delimiter(old_nodes, "*", "italic")
        self.assertEqual(3, len(new_nodes))
        self.assertEqual("italic text", new_nodes[1].text)

    def test_text_with_code(self):
        code_text_node = TextNode("Everyone should learn `print('Hello World')` in Python.", "text")
        old_nodes = [code_text_node]
        new_nodes = split_nodes_delimiter(old_nodes, "`", "code")
        self.assertEqual(3, len(new_nodes))
        self.assertEqual("print('Hello World')", new_nodes[1].text)

    def test_link_text(self):
        link_node = TextNode("Link Display Text", "link", "https://me.com/")
        old_nodes = [link_node]
        new_nodes = split_nodes_delimiter(old_nodes, "*", "italic")
        self.assertEqual(old_nodes, new_nodes)

    def test_image_text(self):
        image_node = TextNode("alt text for my image", "image", "content/images/img.jpeg")
        old_nodes = [image_node]
        new_nodes = split_nodes_delimiter(old_nodes, "*", "italic")
        self.assertEqual(old_nodes, new_nodes)
    

if __name__ == "__main__":
    unittest.main()
