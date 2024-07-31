class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props != None:
            html_props_string = ""
            for key, value in self.props.items():
                html_props_string += f' {key}="{value}"'
            return html_props_string
        else:
            raise Exception("This object's 'props' attribute is blank.")

    def __repr__(self) -> str:
        return f'''Printing HTMLNode Object:
            tag: {self.tag}
            value: {self.value}
            children: {self.children}
            props: {self.props}
            '''


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, children=None, props=None):
        if children != None:
            raise ValueError("Objects of class LeafNode must not have any children.")
        
        if value == None:
            raise ValueError("Objects of class LeafNode must have a 'value' defined.")
        
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        
        if not self.tag:
            return self.value
        
        if self.props:
            html_prop_str = self.props_to_html()
            return f"<{self.tag}{html_prop_str}>{self.value}</{self.tag}>"
        
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"