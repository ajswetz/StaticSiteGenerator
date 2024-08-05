def block_type_to_parent_tag(block_type):
    match block_type:
        case "heading1":
            return "h1"

        case "heading2":
            return "h2"

        case "heading3":
            return "h3"

        case "heading4":
            return "h4"

        case "heading5":
            return "h5"

        case "heading6":
            return "h6"

        case "quote":
            return "blockquote"

        case "code":
            return "pre"

        case "unordered_list":
            return "ul"

        case "ordered_list":
            return "ol"

        case "paragraph":
            return "p"

        case _:
            raise ValueError("Unsupported block type.")
