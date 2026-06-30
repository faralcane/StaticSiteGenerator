import os
import shutil
from markdown_blocks import generate_page

from copystatic import copy_files_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"


def main() -> None:
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    #Update main.py: after copying files from static to public, it should generate a page from content/index.md 
    # using template.html and write it to public/index.html.

    generate_page("./content/index.md", "./template.html", "./public/index.html")

main()
