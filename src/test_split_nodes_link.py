import unittest

from textnode import TextNode
from split_nodes_link import split_nodes_link


class TestSplitNodesLink(unittest.TestCase):
    
    def test_one_link_beginning(self):
        one_link_start = TextNode(
        "[bootdev](https://boot.dev/) is my favorite",
        "text",
        )

        old_nodes = [one_link_start]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(2, len(new_nodes))
    
    def test_one_link_middle(self):
        one_link_middle = TextNode(
        "This website, [to boot dev](https://www.boot.dev), is my favorite!",
        "text",
        )
        
        old_nodes = [one_link_middle]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(3, len(new_nodes))

    def test_one_link_end(self):
        one_link_end = TextNode(
        "This is my favorite website: [boot dev](https://www.boot.dev)",
        "text",
        )

        old_nodes = [one_link_end]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(2, len(new_nodes))

    def test_two_links_beginning(self):
        two_links_start = TextNode(
        "[to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) are awesome",
        "text",
        )

        old_nodes = [two_links_start]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(4, len(new_nodes))

    def test_two_links_middle(self):
        two_links_middle = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) my favorite places.",
        "text",
        )

        old_nodes = [two_links_middle]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(5, len(new_nodes))

    def test_two_links_end(self):
        two_links_end = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        "text",
        )

        old_nodes = [two_links_end]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(4, len(new_nodes))
        

if __name__ == "__main__":
    unittest.main()
