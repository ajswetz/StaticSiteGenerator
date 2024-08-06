from copy_static_to_public_recursively import *
from generate_page import *
from generate_pages_recursive import *

def main():

    # Delete public dir, recreate public dir, and fill with copy of content in 'static'
    copy_static_to_public()

    # Generate HTML pages recursively from "content", saved to "public"
    generate_pages_recursive(dir_path_content="content", template_path="template.html", dest_dir_path="public")

main()
