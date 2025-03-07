from leafnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, __value: object) -> bool:
        return self.text == __value.text and self.text_type == __value.text_type and self.url == __value.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode("p", text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    elif text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == "image":
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError("Invalid text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == "text":
            new_nodes.extend(split_text_node_delimiter(node, delimiter, text_type))
        else:
            new_nodes.append(node)
    return new_nodes

def split_text_node_delimiter(node, delimiter, text_type):
    new_nodes = node.text.split(delimiter)
    if len(new_nodes) % 2 == 0:
        raise ValueError("No closing delimiter found")

    # the first node is text, the next is text_type and then it repeats
    nodes = []
    for i in range(len(new_nodes)):
        if i % 2 == 0:
            nodes.append(TextNode(new_nodes[i], "text"))
        else:
            nodes.append(TextNode(new_nodes[i], text_type))

    return  filter(lambda x: x.text != "", nodes)
