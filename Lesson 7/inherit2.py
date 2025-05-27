class Person:
    def __init__(self, id , name):
        self.id = id
        self.name = name
    def print_data(self):
        print(self.id,self.name)

class Employee(Person):
    def __init__(self, id, name, dept):
        super().__init__(id, name)
        self.dept = dept

    def print_data(self):
        super().print_data()
        print(self.dept)

class Manager(Employee):
    def __init__(self, id, name, dept,salary):
        super().__init__(id, name, dept)
        self.salary = salary
