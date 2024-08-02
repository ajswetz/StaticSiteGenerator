import unittest

from extract_md_image import extract_md_image
from extract_md_link import extract_md_link


class TestExtractMdImage(unittest.TestCase):
    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted = extract_md_image(text)
        self.assertEqual(extracted[0], "rick roll")
        self.assertEqual(extracted[1], "https://i.imgur.com/aKaOqIh.gif")

    def test_extract_nothing(self):
        text = "This text has no links or images."
        extracted = extract_md_image(text)
        self.assertIsNone(extracted)
        

class TestExtractMdLink(unittest.TestCase):
    def test_extract_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted = extract_md_link(text)
        self.assertEqual(extracted[0], "to boot dev")
        self.assertEqual(extracted[1], "https://www.boot.dev")

    def test_extract_nothing(self):
        text = "This text has no links or images."
        extracted = extract_md_link(text)
        self.assertIsNone(extracted)

if __name__ == "__main__":
    unittest.main()
