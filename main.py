from books import Book
import requests
title = input("Enter title of book : ")
try:
    r = requests.get(f'https://openlibrary.org/search.json' , params={"q": title, "fields": "title,author_name"})
except requests.exceptions.RequestException as e:
    print("Request failed!!" , e)
    exit()
if r.status_code == 200:
    response = r.json()
else:
    print("Error!!")
    exit()
books = []
try:
    n = int(input("Enter number of books you want to see :"))
except ValueError:
    print("Please enter a valid number!")
    exit()
if n <= 0:
    print("Please enter a number greater than 0!")
    exit()
if response["docs"]:
    for i in range(min(n, len(response["docs"]))):
        name = response["docs"][i]["title"]
        author_name = response["docs"][i].get("author_name" , "Unknown")
        b = Book(name , author_name , True)
        books.append(b)
else:
     print("Book not found")
while True:
    print('''
    1. Display Book
    2. Borrow Book
    3. Return Book
    4. Exit''')
    choice = input("Enter your choice: ")
    if choice == "1":
        for book in books:
            book.display()
    elif choice == "2":
        book_name =input("Enter the name of book you want borrow : ")
        for book in books:
            if book.name == book_name: 
                book.borrow_book()
                break
        else:
            print("Invalid book name!!")
    elif choice == "3":
        book_name =input("Enter the name of book you want to return : ")
        for book in books:
            if book.name == book_name: 
                book.return_book()
                break
        else:
            print("Invalid book name!!")
    elif choice == "4":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice!!")
                