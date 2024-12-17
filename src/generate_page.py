from block_markdown import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from pathlib import Path
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line[0:2] == "# ":
            return line[2:].strip()
    raise Exception ("no title")

def generate_page(from_path, template_path, dest_path):
    with open(from_path, encoding="utf-8") as f:
        markdown = f.read()
    with open(template_path, encoding="utf-8") as g:
        template = g.read()
    html = markdown_to_html_node(markdown).to_html()
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    title = extract_title(markdown)
    new_page = title.join(template.split("{{ Title }}"))
    new_page = html.join(new_page.split("{{ Content }}"))
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    new_file = open(dest_path, "w")
    new_file.write(new_page)
    new_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        if Path(file).suffix == ".md":
            src_path = Path(os.path.join(dir_path_content, file))
            dest_path = Path(os.path.join(dest_dir_path, file)).with_suffix(".html")
            print(src_path, dest_path)
            generate_page(src_path, template_path, dest_path)

        if not os.path.isfile(os.path.join(dir_path_content, file)):
            new_dir_path_content = os.path.join(dir_path_content, file)
            new_dest_dir_path = os.path.join(dest_dir_path, file)
            generate_pages_recursive(new_dir_path_content, template_path, new_dest_dir_path)