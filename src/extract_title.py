import regex as re

def extract_title(markdown):
    try:
        h1_header = re.search(r'(?<=^|\n)[^\S\n]*# (.+)', markdown).group(1)
    except AttributeError:
        print(f'No h1 header was found in the markdown file to extract into a title.')
        return
    return h1_header.rstrip()