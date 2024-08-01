class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_TextNode) -> bool:
        if self.text != other_TextNode.text:
            return False
        if self.text_type != other_TextNode.text_type:
            return False
        if self.url != other_TextNode.url:
            return False

        return True

    def __repr__(self) -> str:
        if self.url:
            return f"TextNode({self.text}, {self.text_type}, {self.url})"
        if not self.url:
            return f"TextNode({self.text}, {self.text_type}"
