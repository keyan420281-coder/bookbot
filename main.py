from stats import get_num_words, get_chars_dict,sort_chars
import sys

def get_book_text(filepath) :
    with open(filepath) as f:
        content = f.read()
    return content

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars = sort_chars(chars_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
