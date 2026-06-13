from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) % 2 != 0:
            raise Exception("invalid markdown syntax; missing matching delimiter")
        split_text = node.text.split(delimiter)
        temp = []
        for i in range(0, len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                temp.append(TextNode(split_text[i], TextType.TEXT))
            else:
                temp.append(TextNode(split_text[i], text_type))
        new_nodes.extend(temp)
    return new_nodes