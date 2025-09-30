import os

from src.markdown_to_html_node import markdown_to_html_node
from src.extract_title import extract_title

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_paths = os.listdir(dir_path_content)
    for path in content_paths:
        full_src_path = os.path.join(dir_path_content, path)
        full_dst_path = os.path.join(dest_dir_path, path.replace(".md", ".html"))
        if os.path.isfile(full_src_path):
            print(f"Generating page from {full_src_path} to {full_dst_path} using {template_path}")

            with open(full_src_path) as file:
                md_text = file.read()
            with open(template_path) as file:
                template_text = file.read()
            html_content = markdown_to_html_node(md_text).to_html()
            title = extract_title(md_text)
            full_html = template_text.replace('{{ Title }}', title).replace('{{ Content }}', html_content)

            if not os.path.isdir(dest_dir_path):
                os.makedirs(dest_dir_path, 0o755)
            
            with open(full_dst_path, "w") as file:
                file.write(full_html)

        elif os.path.isdir(full_src_path):
            generate_pages_recursive(full_src_path, template_path, full_dst_path)
        