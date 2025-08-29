from stats import *
from output import generate_output
import sys

def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    #book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    sorted_num_char = get_sorted_num_char(get_num_char(text))


    generate_output(book_path, num_words, sorted_num_char)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
