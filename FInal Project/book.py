class Book:
    def __init__(self, title, author,num_of_pages):
        if isinstance(author, str):
            self.author = author
        if isinstance(title, str):
            self.title = title
        if isinstance(num_of_pages, int):
            self.num_of_pages= num_of_pages