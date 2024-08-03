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


# test_heading = "# This is my heading"
# block_type = block_to_block_type(test_heading)
# print(f"heading block type: {block_type}")

# ##########

# test_code = '''```
# my_text = "Hello World"
# print(my_text)
# ```'''
# block_type = block_to_block_type(test_code)
# print(f"code block type: {block_type}")

# ##########

# test_quote = '''>It was the best of times
# >It was the worst of times
# >And I'm tired
# >So I'm going to bed'''

# block_type = block_to_block_type(test_quote)
# print(f"quote block type: {block_type}")

##########

test_unordered_list = '''* Item One
- Item Two
* Item Three
* Item Four'''

block_type = block_to_block_type(test_unordered_list)
print(f"unordered list block type: {block_type}")

##########

test_ordered_list = '''1. Item Num 1
2. Item Num 2
3. Item Num 3
4. Item Num 4'''

block_type = block_to_block_type(test_ordered_list)
print(f"ordered list block type: {block_type}")

# ##########

# test_paragraph = '''One plain paragraph.
# Nothing Special.
# No unique block type.'''

# block_type = block_to_block_type(test_paragraph)
# print(f"paragraph block type: {block_type}")
