from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        sections = old_node.text.split(f"![{images[0][0]}]({images[0][1]})", 1)
        if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
        if sections[0] != "":
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
        new_nodes.append(TextNode(images[0][0], TextType.IMAGE, images[0][1]))
        if sections[1] != "":
            new_nodes.extend(split_nodes_image([TextNode(sections[1], TextType.TEXT)]))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        sections = old_node.text.split(f"[{links[0][0]}]({links[0][1]})", 1)
        if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
        if sections[0] != "":
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
        new_nodes.append(TextNode(links[0][0], TextType.LINK, links[0][1]))
        if sections[1] != "":
            new_nodes.extend(split_nodes_link([TextNode(sections[1], TextType.TEXT)]))
    return new_nodes 



node4 = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png[second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT,)





node = TextNode("This ![alt text for image](url/of/image.jpg) some other text [This is another link](url/of/imagetwotwotwo.jpg) inbetween [Yet another link](url/aaa)", TextType.TEXT)
node2 = TextNode("This is some bold text", TextType.BOLD) 
node3 = TextNode(" some other text ![This is another link](url/of/imagetwotwotwo.jpg) inbetween", TextType.TEXT, None)

print(split_nodes_image([node4]))




