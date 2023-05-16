book_to_find = input()
book_checked = input()

num_books_checked = 0

while book_checked != "No More Books":
    if book_checked == book_to_find:
        print(f"You checked {num_books_checked} books and found it.")
        break
    book_checked = input()
    num_books_checked += 1

if book_checked == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {num_books_checked} books.")
