import os

from src.markdown_to_html_node import markdown_to_html_node
from src.extract_title import extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as file:
        md_text = file.read()
    with open(template_path) as file:
        template_text = file.read()

    html_content = markdown_to_html_node(md_text).to_html()
    title = extract_title(md_text)

    full_html = template_text.replace('{{ Title }}', title).replace('{{ Content }}', html_content).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir, 0o755)


    with open(dest_path, "w") as file:
        file.write(full_html)