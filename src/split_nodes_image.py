from textnode import TextNode
from extract_md_image import extract_md_image
import pprint

def split_nodes_image(old_nodes):

    new_nodes = []

    for node in old_nodes:
        if node.text_type != "text":
            #This function is only meant to parse "text" type nodes.
            new_nodes.append(node)

        if node.text_type == "text":

            raw_text = node.text
            if extract_md_image(raw_text) == None:
                #No matches for MD image syntax found. Just add node to new_nodes.
                new_nodes.append(node)

            else:
                #At least one instance of MD image syntax was found. Need to split.

                keep_going = True
                while keep_going:
                    image_match = extract_md_image(raw_text)
                    full_img_string = f"![{image_match[0]}]({image_match[1]})"
                    split_text = raw_text.split(full_img_string)
                    
                    #If the matched string was at the beginning of 'raw_text', then split_text[0] will equal ""
                    #In that case, we can skip over that piece, add the match text as a new node, and keep going
                    #Otherwise, first chunk of split_text can be appended to new_nodes
                    if split_text[0] != "":
                        new_nodes.append(TextNode(text=split_text[0], text_type="text"))

                    #Second node will be the regex match
                    new_nodes.append(TextNode(text=image_match[0], text_type="image", url=image_match[1]))

                    #Now need to check whether there are any more images in rest of text
                    raw_text = split_text[1]
                    if not raw_text:
                        #raw_text is now blank, we can stop.
                        keep_going = False
                        break
                    if extract_md_image(raw_text) == None:
                        #No more images in text. We can stop now.
                        new_nodes.append(TextNode(text=raw_text, text_type="text"))
                        keep_going = False


    return new_nodes