# can create default/optional paramaters to allow for missing parameter
def add(a=1,b=2,c=3):
    print(a+b+c)

#allows to input 1,2, or 3 paramaters (can keep paramaters at 0 in this case)
add(4)
add(4,5)
add(4,5,6)

#named arguments do not need to be given left to right and can rely on the default or not
#must
def add(a=1,b=2,c=3):
    print(a+b+c)

add(10, b=20)

#functions can return value
#Reurns exit the function and returns the value
def add_return(a,b):
    return a+b
#can use retrun *** if **** > 5 else 10
# if (num>5):return num


print("this is this is the return", add_return(3,10))