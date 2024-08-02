import unittest

from textnode import TextNode
from split_nodes_image import split_nodes_image


class TestSplitNodesImage(unittest.TestCase):
    
    def test_one_image_beginning(self):
        one_image_start = TextNode(
        "![img alt text](image1.jpg) is my favorite",
        "text",
        )

        old_nodes = [one_image_start]
        new_nodes = split_nodes_image(old_nodes)
        self.assertEqual(2, len(new_nodes))
    
    def test_one_image_middle(self):
        one_image_middle = TextNode(
        "This website, ![img alt text](image1.jpg), is my favorite!",
        "text",
        )
        
        old_nodes = [one_image_middle]
        new_nodes = split_nodes_image(old_nodes)
        self.assertEqual(3, len(new_nodes))

    def test_one_image_end(self):
        one_image_end = TextNode(
        "This is my favorite website: ![img alt text](image1.jpg)",
        "text",
        )

        old_nodes = [one_image_end]
        new_nodes = split_nodes_image(old_nodes)
        self.assertEqual(2, len(new_nodes))

    def test_two_images_beginning(self):
        two_images_start = TextNode(
        "![img alt text](image1.jpg) and ![alt img txt 2](image2.jpg) are awesome",
        "text",
        )

        old_nodes = [two_images_start]
        new_nodes = split_nodes_image(old_nodes)
        self.assertEqual(4, len(new_nodes))

    def test_two_images_middle(self):
        two_images_middle = TextNode(
        "This is text with a image ![img alt text](image1.jpg) and ![alt img txt 2](image2.jpg) my favorite places.",
        "text",
        )

        old_nodes = [two_images_middle]
        new_nodes = split_nodes_image(old_nodes)
        self.assertEqual(5, len(new_nodes))

    def test_two_images_end(self):
        two_images_end = TextNode(
        "This is text with a image ![img alt text](image1.jpg) and ![alt img txt 2](image2.jpg)",
        "text",
        )

        old_nodes = [two_images_end]
        new_nodes = split_nodes_image(old_nodes)
        self.assertEqual(4, len(new_nodes))
        

if __name__ == "__main__":
    unittest.main()
