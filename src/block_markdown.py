from htmlnode import LeafNode, ParentNode, HTMLNode
from textnode import TextNode, TextType, text_node_to_html_node
from inline_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []
    for block in blocks:
        if block.strip() != "":
            cleaned_blocks.append(block.strip())   
    return cleaned_blocks

def block_to_block_type(block):
    block_lines = block.split("\n")
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if all(line.startswith(">") for line in block_lines) is True:
        return block_type_quote
    if all(line.startswith("* ") for line in block_lines) or all(line.startswith("- ") for line in block_lines) is True:
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in block_lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        if block_to_block_type(block) == block_type_heading:
            html_nodes.append(heading_to_html_node(block))
        if block_to_block_type(block) == block_type_paragraph:
            html_nodes.append(paragraph_to_html_node(block))
        if block_to_block_type(block) == block_type_code:
            html_nodes.append(code_to_html_node(block))
        if block_to_block_type(block) == block_type_olist:
            html_nodes.append(olist_to_html_node(block))
        if block_to_block_type(block) == block_type_ulist:
            html_nodes.append(ulist_to_html_node(block))
        if block_to_block_type(block) == block_type_quote:
            html_nodes.append(quote_to_html_node(block))
    return ParentNode("div", html_nodes)

def paragraph_to_html_node(block):
    children = text_to_children(block.replace("\n", " "))
    return ParentNode("p", children)

def heading_to_html_node(block):
    if block[0:7] == "###### ":
        children = text_to_children(block[7:])
        return ParentNode("h6", children)
    if block[0:6] == "##### ":
        children = text_to_children(block[6:])
        return ParentNode("h5", children)
    if block[0:5] == "#### ":
        children = text_to_children(block[5:])
        return ParentNode("h4", children)
    if block[0:4] == "### ":
        children = text_to_children(block[4:])
        return ParentNode("h3", children)
    if block[0:3] == "## ":
        children = text_to_children(block[3:])
        return ParentNode("h2", children)
    if block[0:2] == "# ":
        children = text_to_children(block[2:])
        return ParentNode("h1", children)
    raise ValueError("Not a correct heading")

def code_to_html_node(block):
    children = text_to_children(block[3:-3])
    return ParentNode("pre", ParentNode("code", children))

def olist_to_html_node(block):
    items = block.split("\n")
    children_block = []
    for item in items:
        children_item = text_to_children(item.split(" ", 1)[1])
        children_block.append(ParentNode("li", children_item))
    return ParentNode("ol", children_block)

def ulist_to_html_node(block):
    items = block.split("\n")
    children_block = []
    for item in items:
        children_item = text_to_children(item.split(" ", 1)[1])
        children_block.append(ParentNode("li", children_item))
    return ParentNode("ul", children_block)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line[2:])
    children = text_to_children(" ".join(new_lines))
    return ParentNode("blockquote", children)        

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    htmlnodes = []
    for textnode in textnodes:
        htmlnodes.append(text_node_to_html_node(textnode))
    return htmlnodes

test2 = """# Welcome to My Website

## About Me

Hi, I'm **John Doe**, a web developer with a passion for creating interactive and user-friendly websites.

### My Skills

- HTML & CSS
- JavaScript
- React
- Node.js

### Portfolio

Here are some of my projects:

1. [Portfolio Website](https://example.com/portfolio)
2. [E-commerce Store](https://example.com/store)
3. [Blog Platform](https://example.com/blog)

### Sample Code

Here’s an example of a simple HTML structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a simple HTML example.</p>
</body>
</html>```

### Contact Me

You can reach me at:

- Email: [john.doe@example.com](mailto:john.doe@example.com)
- LinkedIn: [John Doe](https://linkedin.com/in/johndoe)
- Twitter: [@johndoe](https://twitter.com/johndoe)

*Thank you for visiting my page!*

> "The only way to do great work is to love what you do."  
> – Steve Jobs
"""

test3 = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
print(markdown_to_html_node(test3))


