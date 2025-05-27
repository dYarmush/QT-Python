from reader import Reader      
from Shelves import Shelf
from book import Book
class Library():
    def __init__(self):
        self.shelves = []
        self.readers = []

    def is_there_place_for_new_book(self,shelf):
            if shelf.is_shelf_full == False:
                return True
            else:
                return False
            
    def add_new_book(self, book):
        for shelf in self.shelves:
            if self.is_there_place_for_new_book(shelf):
                shelf.add_book(book)
                print("book added to shelf ")
                
                return # breaks the loop if the shelf has room 
        print ("No room for more books on shelf")

    def delete_book(self, title):
        for shelf in self.shelves:
            for book in shelf.books:
                if book.title == title:
                    shelf.books.pop(shelf.books.index(book))
    
    def register_reader(self, name):
        reader = Reader(name)
        reader.set_Id()
        self.readers.append(reader)
                

    def remove_reader(self, reader_name):
        for reader in self.readers:
            if reader.name == reader_name:
                self.readers.pop( self.readers.index(reader))

    def search_by_author(self, author):
        books = []
        for shelf in self.shelves:
            for book in shelf.books:
                if book.author == author:
                    books.append(book.title)
        if books:        
            return books            
        else:
            return "No results found"  
              
b1 = Book("Batman","Dovi",50)    
b2 = Book("BatGirl","Adi",62)    
b3 = Book("Thor","Idan",98)    
b4 = Book("Hulk","Omri",42)    
b5 = Book("Iron-Man","Eran",47)    
b6 = Book("Green Lantern","Dovi",685)  

s1 = Shelf()
s1.add_book(b1)
s1.add_book(b2)

s2 = Shelf()
s2.add_book(b3)
s2.add_book(b4)

s3 = Shelf()
s3.add_book(b5)
s3.add_book(b6)

lib = Library()
lib.shelves.extend([s1,s2,s3])


while True:
    try:
        choice = int(input("\
To ADD a book - Press 1. \n\
To DELETE a book - Press 2.\n\
To REGISTER a new reader - Press 3.\n\
TO REMOVE a reader - Press 4.\n\
To SEARCH books by author - Press 5.\n\
To exit  Press 6. \n" ))
    except ValueError:
        print("Invalid Choice! Try Again\n\n")
        continue 
    
    if choice < 7 and choice > 0:
        match choice:
            case 1: # Add a book
                print("\nADD A NEW BOOK")
                book_name = input("Please enter the book name: ")
                author =  input("Please enter the book author: ")
                num_of_pages =  int(input("Please enter the number of pages: "))
                new_book = Book(book_name,author,num_of_pages)
                lib.add_new_book(new_book)
            case 2: # Delete a  book
                print("\nDELETE A BOOK")
                book_name = input("Please enter the book name: ")
                lib.delete_book(book_name)
            case 3: # Rgister new reader
                print("\nREGISTER NEW READER")
                name = input("Please enter reader's name: ")
                lib.register_reader(name)
            case 4: # Delete Reader
                print("\nREMOVE A READER")
                name = input("Please enter reader's name: ")
                lib.remove_reader(name)
            case 5: # Search by author
                print("\nSEARCH BY AUTHOR")
                author = input("Please enter author's name: ")
                print(f"The author {author} wrote the book(s): {lib.search_by_author(author)} ")
            case 6: # Exit
                print("GoodBye!")
                break
            case _:
                print("Invalid Choice! Try Again\n\n")

                