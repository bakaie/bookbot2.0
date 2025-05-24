from stats import get_num_words
from stats import get_num_chars
from stats import sort_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    words = get_num_words(path_to_book)
    sorted = sort_dict(get_num_chars(path_to_book))

    print("============ BOOKBOT ============")
    print("Analyzng book found at books/frankenstein.txt...")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for dict in sorted:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")
    
main()