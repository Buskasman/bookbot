def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_number = word_count(text)
    letters_count = get_num_letters(text)
    print(f"Letter count is as follows {letters_count}")
    

def get_num_letters(text):
    low_case = text.lower()
    split_list = list(low_case)
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "z", "y"]
    letter_count = {}
    for letter in alphabet:
        count = split_list.count(letter)
        letter_count.update({letter: count})
    return letter_count
        
    



def word_count(text):
    split_text = text.split()
    return len(split_text)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
