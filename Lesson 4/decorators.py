#decorator

#instead of all this
# def get_greet():
#     print("how ae you?")

# def print_hello():
#     print("hello")
#     get_greet()


# def print_bye():
#     print("bye")
#     get_greet()

def get_greet(f):
    def inner_func(n1,n2):
        print("aftb4er")
        return f(n1,n2)
        
    return inner_func    

@get_greet
def print_bye():
    print("bye")

@get_greet
def add(n1,n2):
    return n1 + n2

print(add(5,3))