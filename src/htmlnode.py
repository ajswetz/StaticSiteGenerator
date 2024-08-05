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
        raise NotImplementedError


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, children=None, props=None):
        if children:
            raise ValueError("Objects of class LeafNode must not have any children.")

        if (not value) and (tag != "img"):
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

    def __repr__(self) -> str:
        return f'''Leaf Node:
            tag: {self.tag}
            value: {self.value}
            children: {self.children}
            props: {self.props}
            '''

class ParentNode(HTMLNode):
    def __init__(self, tag, children, value=None, props=None):
        if not children:
            raise ValueError("Objects of class ParentNode must have children.")

        if value:
            raise ValueError("Objects of class ParentNode cannot take a 'value' argument.")

        if not tag:
            raise ValueError("Objects of class ParentNode must have a tag.")

        super().__init__(tag=tag, value=None, children=children, props=props)


    def to_html(self):
        child_obj_string = ""
        for obj in self.children:
            child_obj_string += obj.to_html()

        if self.props:
            html_prop_str = self.props_to_html()
            return f"<{self.tag}{html_prop_str}>{child_obj_string}</{self.tag}>"

        else:
            return f"<{self.tag}>{child_obj_string}</{self.tag}>"
        
    def __repr__(self) -> str:
        return f'''Parent Node:
            tag: {self.tag}
            value: {self.value}
            children: {self.children}
            props: {self.props}
            '''
