import re

def extract_md_image(text):
    first_match = re.search(r"!\[(.*?)\]\((.*?)\)", text)
    if first_match:
        return first_match.groups()
    else:
        return None