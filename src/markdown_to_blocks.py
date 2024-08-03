import pprint

def markdown_to_blocks(markdown):

    blocks = [p.strip() for p in markdown.split('\n\n') if p.strip()]

    return blocks

with open("src/markdown_sample.md") as file:
    markdown_sample = file.read()

print(markdown_sample)

blocks = markdown_to_blocks(markdown_sample)

pprint.pprint(blocks)
