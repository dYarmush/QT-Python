from functools import reduce
# 1. Create a function that receives 2 numbers and print their sum.
def print_Sum(num1, num2):
    print (num1+num2)
# 2. Create a function that receives 2 strings and print the longer of them.
def print_longer(str1, str2):
    if len(str1)>len(str2):
        print (str1)
    else:
        print(str2)

        
# 3. Create a function that receives an array of Booleans and print that amount of true
# occurrences .
def total_true(bool_array):
    counter = 0
    for bool in bool_array:
        if bool == True:
            counter +=1

    print (f"Total True occurences{counter}")

# 4.Create a function that get an array of numbers and print their multiply
def get_multiply(num_array):
    print( reduce(lambda x,y: x*y, num_array))
# 5 . Create a function that receive 3 numbers and returns their multiply;
def return_three(num1, num2, num3):
    return num1*num2*num3
# 6. Create a function that receives 2 strings and returns the length of the shorter one.
def shorter(str1 ,str2):
    if len(str1)>len(str2):
        return len(str2)
    else:
        return len(str1)
    
# 7.Create a function that receives 2 numbers and Boolean. If the sum of the numbers is
# greater than 10 – returns the Boolean value. Other wise – returns the opposite value.
def rerun_bool(num1, num2, bool):
    if num1+num2 >10:
        return bool
    else:
        return not bool


# 8.Create a function that get a number(N) and return an array of numbers containing the
# numbers : 1,2,3... N
def return_num_array(num):
    new_Array = []
    for i in range(num):
        new_Array.append(i+1)
    print(new_Array)
#return_num_array(5)

# 9. Create a function that Receives 2 numbers and send their multiply to anTHER
# function that print it
def multiply_2(num1, num2):
    return num1 * num2
def print_Multiply_2(numX):
    print(f"print multiply {numX}")

#print(print_Multiply_2(multiply_2(5,2)))

# 10. Create a function that receives an array of int and returns the number of values that
# greater than 5
def greater_than_5(arr):
    new_arr = []
    for num in arr:
        if num > 5:
            new_arr.append(num)
    print (new_arr)
arr=[5,4,3,6,7,8,9]
#greater_than_5(arr)  

# 11. Create a function that receives an array of string and returns a string that build from
# the strings that their length is smaller than 5
def concat_Strings(arr):
    new_str_from_arr=""
    for str in arr:
        if len(str) >5:
            new_str_from_arr += str
    print(new_str_from_arr)
#concat_Strings(arr=["family","is","the","best", "Yarmush"])  

# 12. Create a function that receives a number from the user and returns an array of
# Booleans with that size. The Boolean values will be given from the user.
def bool_values():
    num = input("enter a num: ")
    bool_val = input("enter True or false")
    bool_arr = []
    if bool_val[0] == "t" or bool_val[0] == "T":
        bool_val = True
    else:
        bool_val = False
    for i in range(int(num)):
        bool_arr.append(bool_val)
    return bool_arr    
#print(bool_values()) 

# 12*. Create a function that requests from the user a number, create an array of int with
# that size, get the numbers from the user, and returns their sum
def get_user_int_arr():
    num = input("input a number ")
    arr=[]
    for i in range(int(num)):
        num2 = input(" input a number ")
        arr.append(int(num2))
    return(reduce(lambda x,y: x+y, arr))
#print(get_user_int_arr())    

# 13*. Create a function that receives a string and returns it’s length.
# Create a function that receives an array of strings and returns it’s total lengths, using
# the first function

def return_length(str):

    return len(str)

def return_arr_length(arr):
    len_sum = 0
    for str in arr:
        len_sum += return_length(str)
        print(len(str))      
    return len_sum
arr = ["yes","deluge","menagerie","pineapple"]
#print(return_arr_length(arr))

# 14.Create a function that called “Add” that gets 2 numbers and returns their Sum
# Create anoth7er function called “Mul” that gets 2 numbers and returns their multiply
# but WITHOUT the “*” operator but only by calls to “Add” function

def add(num1, num2):
    return (num1+num2)

def mul(num1, num2):
    prod = num1
    for i in range(int(num2)-1):
        prod = add(prod,num1)
    return prod 
#print(mul(5,6))


# 15*. Create a function that receives 2 arrays of int with the same size, and returns an
# array of int with the bigger numbers among the arrays
def get_avg(arr):
    total = 0
    for num in arr:
        total += int(num)
    return total / len(arr)
    
def two_arr(arr1, arr2):
    new_arr = arr1 + arr2
    bigger_arr=[]
    for num in new_arr:
        if int(num) > get_avg(new_arr):
            bigger_arr.append(num)
    return bigger_arr
arr1 =[1,2,3,4,5,]
arr2 = [7,6,5,4,3,2,2,2,2,2,]
#print(two_arr(arr1,arr2))

# 16* Create a function that receives 4 numbers and returns the sum of the biggest 2
# numbers among them
def biggest2(num1,num2,num3,num4):
    num_arr = [num1,num2,num3,num4]
    num_arr.sort()
    
    biggest=num_arr[2] + num_arr[3]
    return biggest
#print(biggest2(5,6,7,1))        
