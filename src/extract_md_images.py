import re

def extract_md_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches