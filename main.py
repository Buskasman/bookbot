def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_number = word_count(text)
    letters_count = get_num_letters(text)
    letters_sorted = sort_dict(letters_count)
    print(f"----- Begin of bookreport on {book_path} -----")
    print(f"{word_number} number of word were found in this document")
    for i in letters_sorted:
        print(f"The letter {i} appears {letters_sorted.get(i)} times in the document")
    print("--- End of report ---")

      
        
        

def sort_dict(dict):
    sorted_list = sorted(dict.items(), key = lambda x: x[1], reverse=True)       
    sorted_dict ={}
    for i in sorted_list:
        x = str(i).replace("(", "").replace(")", "").replace(",", "")
        y = x.split()
        sorted_dict[y[0]] = y[1]
    return sorted_dict



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
