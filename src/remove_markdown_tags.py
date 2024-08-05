def remove_markdown_tags(markdown_block, block_type):

    md_block_lines = markdown_block.splitlines()

    match block_type:

        case "heading1":
            return markdown_block.lstrip("# ")

        case "heading2":
            return markdown_block.lstrip("# ")

        case "heading3":
            return markdown_block.lstrip("# ")

        case "heading4":
            return markdown_block.lstrip("# ")

        case "heading5":
            return markdown_block.lstrip("# ")

        case "heading6":
            return markdown_block.lstrip("# ")

        case "code":
            return markdown_block.strip("`")

        case "quote":
            stripped_lines = list(map(lambda line: line.lstrip(">"), md_block_lines))
            stripped_block = "\n".join(stripped_lines)
            return stripped_block

        case "unordered_list":
            stripped_lines = list(map(lambda line: line[2:], md_block_lines))
            stripped_block = "\n".join(stripped_lines)
            return stripped_block

        case "ordered_list":
            stripped_lines = list(map(lambda line: line[3:], md_block_lines))
            stripped_block = "\n".join(stripped_lines)
            return stripped_block

        case _:
            return markdown_block
