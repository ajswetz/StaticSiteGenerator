import re

def extract_title(markdown):

    h1_header_pattern = r"^#{1}\s.*"
    regex = re.compile(h1_header_pattern, re.MULTILINE)

    h1_header_match = regex.search(markdown)

    if not h1_header_match:

        raise Exception("No h1 header found in input Markdown document.")

    #else
    h1_header = h1_header_match.group()
    title = h1_header.lstrip("# ").rstrip()
    return title
