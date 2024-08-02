from textnode import TextNode

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