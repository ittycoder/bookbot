import os
import sys

from stats import get_num_words, sort_chars


def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


def get_book_path():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    if not os.path.exists(book_path):
        print("Book not found")
        sys.exit(1)
    return book_path


def main():
    book_path = get_book_path()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    file_contents = get_book_text(book_path)
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_contents)} total words")
    print("--------- Character Count -------")
    for entry in sort_chars(file_contents):
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
