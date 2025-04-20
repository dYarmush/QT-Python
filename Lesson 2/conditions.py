# conditiional operators

# > < =
num = int(input("enter num: "))

#if statements    if, if-else, el-if
if num > 10:
    print(f"{num} is greater than 10")
elif num > 5 :
    print(f"{num} is betwenn 5 and 10")
else:
    print(f"{num} is less than 5")



#Multiple Conditions
#And operator "and"
if num > 5 and num < 10:
    print("between 5 and 10")

# Or operator "or"
# once the frist condition is met, python does not look a the rest, 
# only continues to chekc when the condition is not met                                                                        is not met

print (10 > 7)

#can combine AND and OR in same if statement
#more readable if the conditiions are in parenthesis

#if (num1 > 5 or num2 < 13) and (num3 ==17) 


#can write an if sttement in one line wit