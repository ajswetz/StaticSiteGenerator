import unittest
from remove_markdown_tags import *

class TestRemoveMarkdownTags(unittest.TestCase):

    def test_heading(self):
        test_heading = "# This is my heading"
        tags_removed = remove_markdown_tags(test_heading, "heading1")
        self.assertEqual(tags_removed, "This is my heading")

        test_heading = "## This is my heading"
        tags_removed = remove_markdown_tags(test_heading, "heading2")
        self.assertEqual(tags_removed, "This is my heading")

        test_heading = "### This is my heading"
        tags_removed = remove_markdown_tags(test_heading, "heading3")
        self.assertEqual(tags_removed, "This is my heading")

        test_heading = "#### This is my heading"
        tags_removed = remove_markdown_tags(test_heading, "heading4")
        self.assertEqual(tags_removed, "This is my heading")

        test_heading = "##### This is my heading"
        tags_removed = remove_markdown_tags(test_heading, "heading5")
        self.assertEqual(tags_removed, "This is my heading")

        test_heading = "###### This is my heading"
        tags_removed = remove_markdown_tags(test_heading, "heading6")
        self.assertEqual(tags_removed, "This is my heading")

    def test_code(self):
        test_code = '''```
my_text = "Hello World"
print(my_text)
```'''
        result_code = '''
my_text = "Hello World"
print(my_text)
'''
        tags_removed = remove_markdown_tags(test_code, "code")
        self.assertEqual(tags_removed, result_code)

    def test_quote(self):
        test_quote = '''>It was the best of times
>It was the worst of times
>And I'm tired
>So I'm going to bed'''

        result_quote = '''It was the best of times
It was the worst of times
And I'm tired
So I'm going to bed'''

        tags_removed = remove_markdown_tags(test_quote, "quote")
        self.assertEqual(tags_removed, result_quote)

    def test_unordered_list(self):
        test_unordered_list = '''* Item One
- Item Two
* Item Three
* Item Four'''

        result_unordered_list = '''Item One
Item Two
Item Three
Item Four'''

        tags_removed = remove_markdown_tags(test_unordered_list, "unordered_list")
        self.assertEqual(tags_removed, result_unordered_list)

    def test_ordered_list(self):
        test_ordered_list = '''1. Item Num 1
2. Item Num 2
3. Item Num 3
4. Item Num 4'''

        result_ordered_list = '''Item Num 1
Item Num 2
Item Num 3
Item Num 4'''


        tags_removed = remove_markdown_tags(test_ordered_list, "ordered_list")
        self.assertEqual(tags_removed, result_ordered_list)

    def test_paragraph(self):
        test_paragraph = '''One plain paragraph.
Nothing Special.
No unique block type.'''

        tags_removed = remove_markdown_tags(test_paragraph, "paragraph")
        self.assertEqual(tags_removed, test_paragraph)

if __name__ == "__main__":
    unittest.main()
