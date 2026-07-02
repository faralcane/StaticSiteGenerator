from markdown_blocks import markdown_to_html_node, extract_title
from pathlib import Path
import os
import shutil



def generate_page(from_path, template_path, dest_path, basepath)-> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as file:
        markdown_content = file.read()

    with open(template_path, 'r') as file:
        template_content = file.read()

    converted_html = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)

    generated_page = template_content.replace("{{ Title }}", title).replace("{{ Content }}", converted_html)
    generated_page = generated_page.replace('src="/', f'src="{basepath}')
    generated_page = generated_page.replace('src="/', f'src="{basepath}')

    out_path = Path(dest_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(generated_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(source_path):
            if source_path.endswith(".md"):
                dest_path = dest_path[0:-3] + ".html"
                generate_page(source_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(source_path, template_path, dest_path, basepath)