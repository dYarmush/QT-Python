class Person:
    def __init__(self, name):
        self.__name = name
    
    # allows us to use the function name as a variable and change private variables as if they are 
    # public variables
    @property
    def name(self):
        return self.__name

#access the property and can add funtionality ontop of setting the name
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name
# create the Person
p1 = Person("Dovi")

# Set private attribute using functions
p1.set_name("dovi2")
print(p1.get_name())

#set and get using gdecorators to allow as if it is the private attribute
p1.name = "Dovi 3"
print(p1.name)
