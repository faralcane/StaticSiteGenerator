
class HTMLNode:
    def __init__(self, tag: str|None =None, value: str|None =None, children=None, props: dict[str, str]|None  =None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def add_child(self, child):
        if self.children is None:
            self.children = []
        self.children.append(child)

    def to_html(self):
        raise NotImplementedError("to_html method is not implemented yet")  
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'        
        return props_html
    
    def __repr__(self):        
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"    

class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None, value: str, props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
