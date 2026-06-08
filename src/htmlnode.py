
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
        props_str = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return f" {props_str}" if props_str else ""
    
    def __repr__(self):        
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"