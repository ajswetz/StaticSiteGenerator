from htmlnode import LeafNode
from textnode import TextNode

def text_node_to_html_node(text_node):

    
    match text_node.text_type:
        case "text":
            return LeafNode(value=text_node.text)

        case "bold":
            return LeafNode(value=text_node.text, tag="b")

        case "italic":
            return LeafNode(value=text_node.text, tag="i")

        case "code":
            return LeafNode(value=text_node.text, tag="code")

        case "link":
            props = {"href": text_node.url}
            return LeafNode(value=text_node.text, tag="a", props=props)

        case "image":
            props = {"src": text_node.url, "alt": text_node.text}
            return LeafNode(value="", tag="img", props=props)
        case _:
            raise ValueError(f"'{text_node.text_type}' is not an allowed text type.")