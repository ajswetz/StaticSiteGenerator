import unittest

from extract_md_images import extract_md_images
from extract_md_links import extract_md_links


class TestExtractMdImages(unittest.TestCase):
    def test_extract_2_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        extracted = extract_md_images(text)
        self.assertEqual(2, len(extracted))

    def test_extract_nothing(self):
        text = "This text has no links or images."
        extracted = extract_md_images(text)
        self.assertEqual(0, len(extracted))
        

class TestExtractMdLinks(unittest.TestCase):
    def test_extract_2_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        extracted = extract_md_links(text)
        self.assertEqual(2, len(extracted))

    def test_extract_nothing(self):
        text = "This text has no links or images."
        extracted = extract_md_links(text)
        self.assertEqual(0, len(extracted))

if __name__ == "__main__":
    unittest.main()
