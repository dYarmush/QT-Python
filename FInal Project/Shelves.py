from book import Book
class Shelf():
    def __init__(self):
        self.books =[]
        self.is_shelf_full = False
    
    
    
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
