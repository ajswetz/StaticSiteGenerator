from markdown_to_html_node import *
from extract_title import *
import os
import shutil

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    # Crawl every entry in the content directory

    content_dir_contents = []
    for root, dirs, files in os.walk(dir_path_content):
        content_dir_contents.append((root, dirs, files))

    files_to_convert = []
    for item in content_dir_contents:

        root_dir = item[0] #This will be a string
        child_dirs = item[1] #This will be a list of strings
        child_files = item[2] #This will be a list of strings

        for file in child_files:
            if file.endswith(".md"):
                source_file_path = os.path.join(root_dir, file)
                dest_file_path = source_file_path.replace(dir_path_content, dest_dir_path, 1)
                dest_file_path_html = dest_file_path.replace(".md", ".html")
                both_files = (source_file_path, dest_file_path_html)
                files_to_convert.append(both_files)

    # For each markdown file found, generate a new .html file using the same template.html.
    # The generated pages should be written to the public directory in the same directory structure.
    for files in files_to_convert:
        source_file = files[0]
        dest_file = files[1]
        # Print a message like "Generating page from from_path to dest_path using template_path".
        print(f"Generating page from {source_file} to {dest_file} using {template_path}")

        # Read the markdown file at source_file and store the contents in a variable.
        with open(source_file) as file:
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
        parent_dir = os.path.dirname(dest_file)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        dest_file = open(dest_file, "w")
        dest_file.write(content_added)
        dest_file.close()

generate_pages_recursive("content", "template.html", "public")
