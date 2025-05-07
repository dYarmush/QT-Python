class Toy():
    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color
    
    def print_toy_data(self):
        print(f"toy {self.name} in color {self.color}, costs ${self.price}")
    
    def get_toy_name(self):
        print(self.name)

class Store():
    def __init__(self, store_name):
        self.store_name = store_name
        self.toys = []

    def add_toy(self, new_toy):
        if isinstance(new_toy, Toy):
            self.toys.append(new_toy)

    def get_toys(self):
        for toy in self.toys:
            toy.get_toy_name()

t1 = Toy("ball",100, "blue")


t2 = ("star", 5,"white")

t_store = Store("toy Store")
t_store.add_toy(t1)
t_store.add_toy(t2)

t_store.get_toys()



