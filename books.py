class Book:
    def __init__(self , name ,author_name , availability ):
        self.name = name
        self.author_name = author_name
        self.availability  = availability 
    def display(self):
        print("==============Book Details===============")
        print(f"The name of book is {self.name}")
        print(f"The name of author is {self.author_name}")
        print(f"The avalibity status is {self.availability }")
    def borrow_book(self):
        if(self.availability ):
            print("Book borrowed successfully!")
            self.availability  = False
        else:
            print("Book is not available!")
    def return_book(self):
        if not self.availability :
            print("Book returned successfully!")
            self.availability  = True
        else:
            print("Book is already available!")
