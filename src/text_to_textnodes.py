from split_nodes_link import *
from split_nodes_image import *
from split_nodes_delimiter import *
from textnode import TextNode

def text_to_textnodes(text):
    #Need to cycle through all the split_nodes functions
    #Start by initializing input 'text' as a TextNode
    text_node = TextNode(text=text, text_type="text")
    #Then, create a new list of "old_nodes" containing "text_node"
    old_nodes = [text_node]

    #bold
    new_nodes = split_nodes_delimiter(old_nodes=old_nodes, delimiter="**", text_type="bold")

    #italic
    new_nodes = split_nodes_delimiter(old_nodes=new_nodes, delimiter="*", text_type="italic")

    #code
    new_nodes = split_nodes_delimiter(old_nodes=new_nodes, delimiter="`", text_type="code")

    #image
    #NOTE: With the code as is, image needs to run before link.
    #Otherwise, the split_nodes_link function will grab items that should be images instead.
    new_nodes = split_nodes_image(old_nodes=new_nodes)

    #link
    new_nodes = split_nodes_link(old_nodes=new_nodes)

    return new_nodes
