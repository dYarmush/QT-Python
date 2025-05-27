
class Reader():
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