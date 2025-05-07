
class Person:
    #construcor - function to create the instance
    def __init__(self, name):
        self.name = name
        #to make private add __ before the variable
        self.__phone = []

    def add_phone(self, phone):
        if len(phone) == 7:
            self.__phone.append(phone)
        else: 
            print("invalid phone")
    def get_phone(self):
        return self.__phone    
