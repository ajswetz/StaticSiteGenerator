import re

def extract_title(markdown):
    
    h1_header_pattern = r"^#{1}\s.*"
    regex = re.compile(h1_header_pattern, re.MULTILINE)

    h1_header_match = regex.search(markdown)



    if not h1_header_match:

        raise Exception("No h1 header found in input Markdown document.")
    
    #else
    h1_header = h1_header_match.group()
    title = h1_header.lstrip("# ")
    return title


test1 = "# This is my valid markdown heading 1"

title = extract_title(test1)
print("printing test1:")
print(title)
print("================")
test2 = "## I made a mistake and only put an h2 header"

title2 = extract_title(test2)