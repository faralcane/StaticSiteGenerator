from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "air"
    BOLD_TEXT = "water"
    ITALIC_TEXT = "earth"
    CODE_TEXT = "fire"
    LINK = "[anchor text](url)" 
    IMAGE = "![alt text](url)"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    #def __str__(self):
    #    return f"{self.text_type.value}: {self.text}" 
    
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"