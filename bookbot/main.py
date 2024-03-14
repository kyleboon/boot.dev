def initialize_letter_count() -> dict:
    """ initializes a dict that has all lower case letters mapped to the int 0 """
    return { chr(i): 0 for i in range(ord('a'), ord('z')+1) }

def print_report(path, word_count, letters) -> None:
    """ prints the book report to stdout """
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for char, count in letters.items():
        print(f"The '{char}' charecter was found {count} times")

def read_book(path) -> str:
    """ reads a file into a string """
    with open(path) as f:
        return f.read()

def count_letters_in_words(words) -> dict:
    """ takes a list of words and returns a dict of lower case letters and number of occurences of each """
    letters = initialize_letter_count() 
    for word in words:
        for letter in word:
            if letter.isalpha():
                lower = letter.lower()
                letters[lower] += 1
    return letters


def main() -> int:
    """ main method for bookbot """ 
    path = "books/frankenstein.txt"
    book_text = read_book(path)
    words = book_text.split()
    letters = count_letters_in_words(words)
    print_report(path, len(words), dict(sorted(letters.items(), reverse=True, key=lambda item: item[1])))

    return 0

if __name__ == "__main__":
    main()

