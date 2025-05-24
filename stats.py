def get_book_text(book):
    with open(book) as book_file:
        book_text = book_file.read()
    return book_text

def get_num_words(book):
    book_text = get_book_text(book)
    book_text2 = book_text.split()
    count = 0
    for word in book_text2:
        count += 1
    # print(f"{count} words found in the document")
    return count

def get_num_chars(book):
    book_text = get_book_text(book).lower()
    count_dict = {}

    for char in book_text:
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict


def sort_on_key(dict):
    return dict["num"]

def sort_dict(dict):
    for each in dict:
        dict[each] = {"char": each, "num": dict[each]}
    sorted_dict = sorted(dict.values(), key=sort_on_key, reverse=True)
    return sorted_dict