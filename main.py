from src.static_to_public import static_to_public
from src.generate_pages_recursive import generate_pages_recursive

def main():
    static_to_public('static', 'public')
    generate_pages_recursive('content', 'template.html', 'public')

if __name__ == "__main__":
    main()
