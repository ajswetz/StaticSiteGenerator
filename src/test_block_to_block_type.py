import unittest
from block_to_block_type import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        test_heading = "# This is my heading"
        block_type = block_to_block_type(test_heading)
        self.assertEqual(block_type, "heading1")

        test_heading = "## This is my heading"
        block_type = block_to_block_type(test_heading)
        self.assertEqual(block_type, "heading2")

        test_heading = "### This is my heading"
        block_type = block_to_block_type(test_heading)
        self.assertEqual(block_type, "heading3")

        test_heading = "#### This is my heading"
        block_type = block_to_block_type(test_heading)
        self.assertEqual(block_type, "heading4")

        test_heading = "##### This is my heading"
        block_type = block_to_block_type(test_heading)
        self.assertEqual(block_type, "heading5")

        test_heading = "###### This is my heading"
        block_type = block_to_block_type(test_heading)
        self.assertEqual(block_type, "heading6")

        #This example uses 7 '#' characters, which is invalid.
        #Should be block_type "paragraph"
        test_heading = "####### This is my invalid heading"
        block_type = block_to_block_type(test_heading)
        self.assertEqual(block_type, "paragraph")

        #This one is missing the ' ' after the opening '#'.
        #Should be block_type "paragraph"
        test_heading = "#This is my invalid heading"
        block_type = block_to_block_type(test_heading)
        self.assertEqual(block_type, "paragraph")

    def test_code(self):
        test_code = '''```
my_text = "Hello World"
print(my_text)
```'''
        block_type = block_to_block_type(test_code)
        self.assertEqual(block_type, "code")

    def test_quote(self):
        test_quote = '''>It was the best of times
>It was the worst of times
>And I'm tired
>So I'm going to bed'''
        block_type = block_to_block_type(test_quote)
        self.assertEqual(block_type, "quote")

    def test_unordered_list(self):
        test_unordered_list = '''* Item One
- Item Two
* Item Three
* Item Four'''

        block_type = block_to_block_type(test_unordered_list)
        self.assertEqual(block_type, "unordered_list")

    def test_ordered_list(self):
        test_ordered_list = '''1. Item Num 1
2. Item Num 2
3. Item Num 3
4. Item Num 4'''

        block_type = block_to_block_type(test_ordered_list)
        self.assertEqual(block_type, "ordered_list")

    def test_paragraph(self):
        test_paragraph = '''One plain paragraph.
Nothing Special.
No unique block type.'''

        block_type = block_to_block_type(test_paragraph)
        self.assertEqual(block_type, "paragraph")

if __name__ == "__main__":
    unittest.main()
