# to create a class
# write class <class name>:

class Person:
    #construcor - function to create the instance
    def __init__(self, name, id, birthyear, phone):
        self.name = name
        self.id = id
        self.birthyear = birthyear
        self.phone = []
        self.phone.append(f"0{phone}")

    def set_name(self,name): self.name = name
    def get_name(self): print(self.name)

    def print_data(self):
        print(f"name {self.name}, ID: {self.id}, Birth Year: {self.birthyear}, Phone: {self.phone}")

# create instance of class calls to the construcor
dovi = Person("Dovi", 1 , 1983, 538926418)
dovi.get_name()
dovi.print_data()