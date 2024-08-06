import unittest
from extract_title import *

class TestExtractTitle(unittest.TestCase):

    def test_title(self):
        test_heading = "# This is my heading"
        title = extract_title(test_heading)
        self.assertEqual(title, "This is my heading")

        test_wrong_heading = "## This is my (incorrect) heading"
        self.assertRaises(Exception, lambda extract_title:(test_wrong_heading))

        test_trailing_whitespace = "# This is my heading.     "
        title = extract_title(test_trailing_whitespace)
        self.assertEqual(title, "This is my heading.")

        test_heading_on_line_3 = '''This first line isn't a heading for some reason.
Someone put the heading too far down. I guess we'll grab it anyways.
# My heading is on line 3 because I'm nuts.'''
        title = extract_title(test_heading_on_line_3)
        self.assertEqual(title, "My heading is on line 3 because I'm nuts.")

if __name__ == "__main__":
    unittest.main()
