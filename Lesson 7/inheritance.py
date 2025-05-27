class Product:
    def __init__(self,price):
        self.price = price

    def print_data(self):
        print(self.price)


class Tablet(Product): # Tablet inherits product
    def __init__(self, price,storage):
        # Inititate the inheritance and send to specific function
        super().__init__(price)
        
        # variable unique to child 
        self.storage = storage    
    def print_data(self):
        super().print_data()
        print(self.storage)

t1 = Tablet(100,"1GB")



t1.print_data()