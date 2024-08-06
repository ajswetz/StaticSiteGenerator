from copy_static_to_public_recursively import *
from generate_page import *

def main():

    # Delete public dir, recreate public dir, and fill with copy of content in 'static'
    copy_static_to_public()

    # Generate a page from content/index.md using template.html and write it to public/index.html.
    generate_page(from_path="content/index.md", template_path="template.html", dest_path="public/index.html")

main()
