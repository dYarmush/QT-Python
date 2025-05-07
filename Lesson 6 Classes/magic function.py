class Person:
    #construcor - function to create the instance
    def __init__(self, name, age):
        self.name = name
        self.age = age

        
# define a shortcut for evaluating 2 objects of the same type        

    def __gt__(self,other):
        if self.age > other.age:
            print("hello gt")
            return True    
        else:
            return False
    def __lt__(self,other):
        print("hello lt")
        return True 
    
#can edit what is printed when printing the object
    def __str__(self):
        return f"name {self.name}, age: {self.age}" 
    
p1 = Person("Dovi", 42)
p2 = Person("Adi", 43)

if p2 > p1:
    print ("hi")

if p2 < p1:
    print("bye")    

print(p1,p2)