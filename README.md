# Library-Management-System



Python command line Book Library application with the use of which it is possible to find information about the desired book via the Open Library API and manage the book collection using Object Oriented Programming.



## Features



- Search for books using the Open Library API

- Display book title and author

- Create and manage Book objects

- Borrow available books

- Return borrowed books

- Handle API/request errors

- Input validation

- Missing author information handling



## Technologies



- Python

- Requests

- Open Library API

- JSON

- Object Oriented Programming



## How it works



1. The user enters the book title.

2. The application finds the books with the help of the Open Library API.

3. The book data is returned in JSON format and converted into Book objects.

4. The user can see the books and also borrow or return them using the offered menu.



## Project Structure



```text

Book-Library-API/

├── main.py

├── books.py

├── README.md

└── .gitignore

```



## How to Run



First, you need to install the required library:



```bash

pip install requests

```



Then, you can run the application:



```bash

python main.py

```

## Learning Outcomes



This project demonstrates practical use of Python APIs, JSON data handling, OOP, exception handling, loops, lists, and user input validation.