from textnode import TextNode
import pprint

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    type_text = "text"
    type_bold = "bold"
    type_italic = "italic"
    type_code = "code"

    new_nodes = []

    for node in old_nodes:
        if node.text_type != type_text:
            #This project isn't parsing deeper than one level of nesting.
            #This function is only meant to parse "text" type nodes.
            new_nodes.append(node)
        if node.text_type == type_text:
            chunks = node.text.split(delimiter)

            if len(chunks) == 1:
                #No delimiter was found in the string. Just add node to new_nodes
                new_nodes.append(node)
            if len(chunks) == 2:
                #Only one delimiter was found. Invalid markdown syntax.
                raise Exception(f"Only one '{delimiter}' was found in this string. Invalid markdown syntax.")
            if len(chunks) == 3:
                #Correct markdown syntax. Splitting string.

                #chunks[0] will be plain text
                node1 = TextNode(text=chunks[0], text_type="text")

                #chunks[1] will be type {text_type}
                node2 = TextNode(text=chunks[1], text_type=text_type)

                #chunks[2] will be plain text
                node3 = TextNode(text=chunks[2], text_type="text")

                new_nodes.append(node1)
                new_nodes.append(node2)
                new_nodes.append(node3)


    return new_nodes

plain_text_node = TextNode("This is a plain text node", "text")
bold_text_node = TextNode("This is a bold text node", "bold")
italic_text_node = TextNode("This is an italic node", "italic")
code_text_node = TextNode("print('Hello World')", "code")

nested_node_bold = TextNode("This is a very **bold** text node.", "text")
nested_node_italic = TextNode("That man was *probably* under the influence.", "text")
nested_node_code = TextNode("My favorite python code always uses the `class` feature.", "text")

old_nodes = [
    plain_text_node,
    bold_text_node,
    italic_text_node,
    code_text_node,
    nested_node_bold,
    nested_node_italic,
    nested_node_code
]

print("=====================")
print("old nodes:")
pprint.pprint(old_nodes)
print("=====================")

new_nodes = split_nodes_delimiter(old_nodes, "**", "bold")
new_nodes = split_nodes_delimiter(new_nodes, "*", "italic")
new_nodes = split_nodes_delimiter(new_nodes, "`", "code")

print("=====================")
print("new nodes:")
pprint.pprint(new_nodes)
print("=====================")
