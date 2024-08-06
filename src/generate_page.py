from markdown_to_html_node import *
from extract_title import *
import os
import shutil

def generate_page(from_path, template_path, dest_path):

    # Print a message like "Generating page from from_path to dest_path using template_path".
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file at from_path and store the contents in a variable.
    with open(from_path) as file:
        markdown = file.read()

    # Read the template file at template_path and store the contents in a variable.
    with open(template_path) as file:
        template = file.read()

    # Use your markdown_to_html_node function and .to_html() method to convert the markdown file to an HTML string.
    html_node = markdown_to_html_node(markdown)
    raw_html = html_node.to_html()

    # Use the extract_title function to grab the title of the page.
    title = extract_title(markdown)

    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    title_added = template.replace("{{ Title }}", title)
    content_added = title_added.replace("{{ Content }}", raw_html)

    # Write the new full HTML page to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    parent_dir = os.path.dirname(dest_path)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    dest_file = open(dest_path, "w")
    dest_file.write(content_added)
    dest_file.close()
