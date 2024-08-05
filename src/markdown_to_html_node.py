from htmlnode import *
from textnode import *
from textnodetohtmlnode import *
from block_to_block_type import *
from markdown_to_blocks import *
from text_to_textnodes import *
from remove_markdown_tags import *
from block_type_to_parent_tag import *
from block_to_html_children import *


def markdown_to_html_node(markdown):

    #Break raw markdown text into individual blocks
    markdown_blocks = markdown_to_blocks(markdown)

    #Initialize empty list to hold HTML parent nodes each representing a single MD block
    all_parent_nodes = []

    #Loop through each block to convert raw markdown into single HTML ParentNode per block
    #Then add each ParentNode to all_parent_nodes
    for block in markdown_blocks:
        #Get type of MD block
        block_type = block_to_block_type(block)

        #Convert block to HTML child nodes
        children = block_to_html_children(block, block_type)

        #Build Parent Node
        parent_tag = block_type_to_parent_tag(block_type)
        parent_node = ParentNode(tag=parent_tag, children=children)

        all_parent_nodes.append(parent_node)


    #Make all the block nodes children under a single parent HTML node
    #(which should just be a div) and return it.
    top_parent_node = ParentNode(tag="div", children=all_parent_nodes)
    return top_parent_node