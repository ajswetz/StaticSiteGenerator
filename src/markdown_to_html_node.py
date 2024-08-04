from htmlnode import *
from textnode import *
from textnodetohtmlnode import *
from block_to_block_type import *
from markdown_to_blocks import *
from text_to_textnodes import *

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

    # 1. Split the markdown into blocks (you already have a function for this)
    markdown_blocks = markdown_to_blocks(markdown)

    # 2. Loop over each block:
    all_parent_nodes = []

    for block in markdown_blocks:
        # a. Determine the type of block (you already have a function for this)
        block_type = block_to_block_type(block)

        # b. Based on the type of block, create a new HTMLNode with the proper data

        # I think each block should turn into one Parent HTML Node with children
        # Each block type will get a certain variety of Parent
        # Probably then need to strip the Markdown formatting tags
        # Then, turn the remainder of the block into Leaf HTML nodes





    #     c. Assign the proper child HTMLNode objects to the block node. I created
    #         a shared text_to_children(text) function that works for all block types.
    #         It takes a string of text and returns a list of HTMLNodes that represent
    #         the inline markdown using previously created functions (think TextNode -> HTMLNode).
    # 3. Make all the block nodes children under a single parent HTML node
    #     (which should just be a div) and return it.
