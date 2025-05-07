from functools import reduce
#ex 6.2.1
def my_func(str="Hello"):
    length = len(str)
    return (length)


# print(my_func("dovi"))

#6.2.1b

def my_func2(str_arr):
    total = 0 
    for str in str_arr:
        total += my_func(str)
    return total

#print(my_func(["dovi","adi","idan"]))

#6.2.2
names = ["Yoav", "Ron","Aviva","Ronen","Dan","Galit"]

filtered = filter(lambda name: len(name)>4 ,names)
mapped = map(lambda x : len(x), filtered)
reduced  = reduce(lambda x,y: x+y,mapped)
print(reduced)

#6.2.3
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub(a,b):
    return a-b
arr = [add,mul,sub]
def pub_sub(num1, num2,arr):
    new_arr = []
    for f in arr:
        new_arr.append(f(num1,num2))
    return new_arr    

print(pub_sub(5,3,arr))

#6.2.4
arr = [6,2,8,12,4]

results = reduce (lambda x,y: x if x<y else y , arr)
print(results)


