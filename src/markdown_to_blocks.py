def markdown_to_blocks(markdown):

    if not markdown:
        raise ValueError("Input cannot be blank.")

    blocks = [p.strip() for p in markdown.split('\n\n') if p.strip()]

    return blocks
