class Book:
    def __init__(self, title,author,num_of_pages):
        if isinstance(author, str):
            self.author = author
        if isinstance(title, str):
            self.title = title
        if isinstance(num_of_pages, int):
            self.num_of_pages= num_of_pages
    def __str__(self):
        return self.title        

class Shelf(Book):
    def __init__(self):
        self.books = []
        self.is_shelf_full = False
    def get_books(self):
        for book in self.books:
            print(book) 
    def add_book(self, book):
        if isinstance(book, Book):
            if len(self.books)<5:
                self.books.append(book)
            if len(self.books)==5:
                self.is_shelf_full = True
                print("The shelf is full")

    def replace_books(self,pos1, pos2):
        if pos1 > 0 and pos1 <=5:
            book1 = self.books[pos1]
        if pos2 > 0 and pos2 <=5:    
            book2 = self.books[pos2]
        self.books.pop(pos2)
        self.books.insert(pos2,book1)
        self.books.pop(pos1)
        self.books.insert(pos1,book2)

class Reader(Shelf):
    def __init__(self,name):
        self.id = 0
        if isinstance(name, str):
            self.name = name
        self.books_read = []

    def set_Id(self):
        self.id = self.id + 1 
    
    def read_book(self, title):
        if isinstance(title, str):
            self.books_read.append(title)            

class Library(Reader):
    def __init__(self):
        self.shelves = []
        self.readers = []

    def is_there_place_for_new_book(self,shelf):
            if shelf.is_shelf_full == False:
                return True
            else:
                return False
            
    def add_new_book(self, book):
        for  shelf in self.shelves:
            
            if self.is_there_place_for_new_book(shelf):
                shelf.add_book(book)
                print("book added to shelf")
               
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
            return "No Results Found"        
        
b1 = Book("Batman","Dovi",50)    
b2 = Book("Batgirl","Adi",62)    
b3 = Book("Thor","Idan",98)    
b4 = Book("Hulk","Omri",42)    
b5 = Book("Iron-man","Eran",47)    
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
        choice = int(input(" \
        For adding a book - Press 1. \n \
        For deleting a book - Press 2.\n \
        For registering a new reader - Press 3.\n \
        For removing a reader - Press 4.\n \
        For searching books by author  Press 5.\n \
        For exit  Press 6. \n" ))
    except ValueError:
        print("Invalid Choice! Try Again\n\n")
        continue 
    
    if choice < 7 and choice > 0:
        match choice:
            case 1: # Add a book
                title = input(" Please enter the book title: ")
                author =  input(" Please enter the book author: ")
                num_of_pages =  int(input(" Please enter the number of pages: "))
                new_book = Book(title, author, num_of_pages)
                lib.add_new_book(new_book)
                s1.get_books()
            case 2: # Delete a  book
                tiele = input(" Please enter the book title: ")
                lib.delete_book(title)
            case 3: # Rgister new reader
                name = input("Please enter reader's name: ")
                lib.register_reader(name)
            case 4: # Delete Reader
                name = input("Please enter reader's name: ")
                lib.remove_reader(name)
            case 5: # Search by author
                author = input("Please enter author's name: ")
                print(f"The author {author} wrote the book(s): {lib.search_by_author(author)} ")
            case 6: # Exit
                print("GoodBye!")
                break
            case _:
                print("Invalid Choice! Try Again\n\n")

                       
    
                