import re

def block_to_block_type(markdown_block):

    md_block_lines = markdown_block.splitlines()

    #HEADINGS - Start with 1-6x '#' characters, plus space plus text, all on one line
    if len(md_block_lines) == 1:
        heading_match = re.search(r"^#{1,6}\s.", markdown_block)
        if heading_match:
            block_type = "heading"
            return block_type

    #CODE BLOCKS - Start and end with '```'
    if markdown_block.startswith("```") and markdown_block.endswith("```"):
        block_type = "code"
        return block_type

    #QUOTE BLOCKS - Each line must start with '>'
    is_quote = True
    for line in md_block_lines:
        if line[0] != ">":
            is_quote = False
            break
    if is_quote == True:
        block_type = "quote"
        return block_type

    #UNORDERED LIST - Every line must start with a * or - character, followed by a space.
    is_unordered_list = True
    for line in md_block_lines:
        if (line[0:2] == "* ") or (line[0:2] == "- "):
            is_unordered_list = True
        else:
            is_unordered_list = False
            break
    if is_unordered_list == True:
        block_type = "unordered_list"
        return block_type

    #ORDERED LIST - Every line in an ordered list block must start with a number
    #               followed by a . character and a space.
    #               The number must start at 1 and increment by 1 for each line.
    is_ordered_list = True
    for i in range(len(md_block_lines)):
        line = md_block_lines[i]
        line_num = i + 1
        ol_syntax = f"{line_num}. "
        if line[0:3] != ol_syntax:
            is_ordered_list = False
            break
    if is_ordered_list == True:
        block_type = "ordered_list"
        return block_type

    #NORMAL PARAGRAPH - anything that doesn't match one of the above cases
    block_type = "paragraph"
    return block_type
