import unittest
from markdown_to_blocks import markdown_to_blocks

class MarkdownToBlocks(unittest.TestCase):
    def test_sample_markdown(self):

        markdown = '''
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item





        Making sure there's lots of empty space above.
        '''

        blocks = markdown_to_blocks(markdown)
        self.assertEqual(4, len(blocks))

    def test_markdown_again(self):
        markdown = '''
        Only one line
        '''
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(1, len(blocks))

    def test_blank_md_string(self):
        markdown = ""
        self.assertRaises(ValueError, lambda: markdown_to_blocks(markdown))

if __name__ == "__main__":
    unittest.main()
