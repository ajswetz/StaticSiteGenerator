import unittest

from textnode import TextNode
from text_to_textnodes import text_to_textnodes


class TestTextToTextNodes(unittest.TestCase):
    def test_all_types(self):
        example = "This is **bold text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(example)
        self.assertEqual(10, len(new_nodes))

    def test_bold_only(self):
        example = "This is **bold text** only."
        new_nodes = text_to_textnodes(example)
        self.assertEqual(3, len(new_nodes))
        self.assertEqual("bold", new_nodes[1].text_type)

    def test_italic_only(self):
        example = "This is *italic text* only."
        new_nodes = text_to_textnodes(example)
        self.assertEqual(3, len(new_nodes))
        self.assertEqual("italic", new_nodes[1].text_type)

    def test_code_only(self):
        example = "This is `code text` only."
        new_nodes = text_to_textnodes(example)
        self.assertEqual(3, len(new_nodes))
        self.assertEqual("code", new_nodes[1].text_type)

    def test_image_only(self):
        example = "![Mr. Freeze](content/mrfreeze.jpg) This is my favorite picture!"
        new_nodes = text_to_textnodes(example)
        self.assertEqual(2, len(new_nodes))
        self.assertEqual("image", new_nodes[0].text_type)

    def test_link_only(self):
        example = "My favorite game is [Old School RuneScape](https://runescape.com)"
        new_nodes = text_to_textnodes(example)
        self.assertEqual(2, len(new_nodes))
        self.assertEqual("link", new_nodes[1].text_type)


if __name__ == "__main__":
    unittest.main()
