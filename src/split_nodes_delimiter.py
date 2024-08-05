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

            delimiter_count = node.text.count(delimiter)

            if delimiter_count == 0:
                #No delimiter was found in the string. Just add node to new_nodes
                new_nodes.append(node)
                continue

            if delimiter_count % 2 != 0:
                #Odd number of delimiters found. Invalid markdown syntax.
                raise Exception(f"Only one '{delimiter}' was found in this string. Invalid markdown syntax.")

            if delimiter_count % 2 == 0:
                #Even number of delimiters found. Time to split string.

                chunks = node.text.split(delimiter)

                #If the delimited string was at the beginning of 'node.text', then chunks[0] will equal ""
                #In that case, we can skip over that piece
                #Otherwise, first chunk of split_text can be appended to new_nodes
                if chunks[0] != "":                
                    #chunks[0] will be plain text
                    node1 = TextNode(text=chunks[0], text_type="text")
                    new_nodes.append(node1)

                #chunks[1] will be type {text_type}
                node2 = TextNode(text=chunks[1], text_type=text_type)
                new_nodes.append(node2)

                #chunks[2] will be plain text
                if chunks[2] != "":
                    node3 = TextNode(text=chunks[2], text_type="text")
                    new_nodes.append(node3)


    return new_nodes