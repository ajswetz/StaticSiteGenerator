from text_to_textnodes import *
from remove_markdown_tags import *
from textnodetohtmlnode import *
from htmlnode import *

def block_to_html_children(block, block_type):
    
    block_no_tags = remove_markdown_tags(block, block_type)

    if block_type == "unordered_list" or block_type == "ordered_list":
        #Each list item needs to be surrounded by parent tag <li>
        #This code splits the block into lines so each line can be handled separately
        block_lines = block_no_tags.splitlines()
        children = []
        for line in block_lines:
            text_nodes = text_to_textnodes(line)
            
            html_child_nodes = []
            for text_node in text_nodes:
                html_node = text_node_to_html_node(text_node)
                html_child_nodes.append(html_node)
            line_parent_node = ParentNode(tag="li", children=html_child_nodes)
            children.append(line_parent_node)

        return children
    
    #Else
    text_nodes = text_to_textnodes(block_no_tags)

    html_child_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_child_nodes.append(html_node)

    if block_type == "code":
        #Reduce entire code block into single HTML ParentNode with tag "code"
        #The rest of the code text will be held as children in this parent node
        #The outer function calling this one will add this ParentNode as a child
        #Of an outer ParentNode with tag "pre"
        code_parent_node = ParentNode(tag="code", children=html_child_nodes)
        code_parent_node_list = [code_parent_node]
        return code_parent_node_list

    #Else
    return html_child_nodes