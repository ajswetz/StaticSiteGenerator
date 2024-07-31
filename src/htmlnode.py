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
