from htmlnode import *
from textnode import *
from textnodetohtmlnode import *
from block_to_block_type import *
from markdown_to_blocks import *
from text_to_textnodes import *
from remove_markdown_tags import *
from block_type_to_parent_tag import *

### Assignment

# Create a new function called def markdown_to_html_node(markdown):
#     that converts a full markdown document into a single HTMLNode.
#     That single HTMLNode should of course contain many child HTMLNode
#     objects representing the nested elements.

# I created an additional 8 helper functions to keep my code neat and
#     easy to understand, because there's a lot of logic necessary for the
#     markdown_to_html_node. I don't want to give you my exact functions
#     because I want you to do this from scratch.
#     However, I'll give you the basic order of operations.

### Tips
#     Quote blocks should be surrounded by a <blockquote> tag.
#     Unordered list blocks should be surrounded by a <ul> tag, and each list item should be surrounded by a <li> tag.
#     Ordered list blocks should be surrounded by a <ol> tag, and each list item should be surrounded by a <li> tag.
#     Code blocks should be surrounded by a <code> tag nested inside a <pre> tag.
#     Headings should be surrounded by a <h1> to <h6> tag, depending on the number of # characters.
#     Paragraphs should be surrounded by a <p> tag.



def markdown_to_html_node(markdown):

    markdown_blocks = markdown_to_blocks(markdown)

    all_parent_nodes = []

    for block in markdown_blocks:
        block_type = block_to_block_type(block)
        block_no_tags = remove_markdown_tags(block, block_type)
        text_nodes = text_to_textnodes(block_no_tags)

        html_child_nodes = []
        for text_node in text_nodes:
            html_node = text_node_to_html_node(text_node)
            html_child_nodes.append(html_node)

        # Need to figure out how to wrap the ordered / unordered lists with the <ol> / <ul> tags
        # Also need to figure out what to do about code block types - they need a <pre> tag too

        #Build Parent Node
        parent_tag = block_type_to_parent_tag(block_type)
        parent_node = ParentNode(tag=parent_tag, children=html_child_nodes)

        if block_type == "code":
            pre_parent_node = ParentNode(tag="pre", children=parent_node)
            all_parent_nodes.append(pre_parent_node)

        all_parent_nodes.append(parent_node)


    # 3. Make all the block nodes children under a single parent HTML node
    #    (which should just be a div) and return it.
    top_parent_node = ParentNode(tag="div", children=all_parent_nodes)
    return top_parent_node
