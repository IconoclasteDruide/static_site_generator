import sys

from src.static_to_public import static_to_public
from src.generate_pages_recursive import generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = '/'

    static_to_public('static', 'public')
    generate_pages_recursive('content', 'template.html', 'public')

if __name__ == "__main__":
    main()
