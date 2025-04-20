# 3.1
# num1 = 3
# num2 = 4
# num3 = 5
# print(num1+num2+num3)

# 3.2
# str1 = "Hi there "

# if len(str1) > num3:
#     print(f"the string {str1} is longer")
# else:
#     print(f" the number {num3} *2 is {num3 *2}")


# 3.3
# str1 = " Dovi"
# str2 = "Yarmush" 

# num = 17

# if len(str1) + len(str2) > num:
#     num2 = 6
#     num3 = 10
#     if num2 > num3
        # print(num2)
    #   else: 
    #     print (num3)

# # 3.4
# str1 = "thi"

# if len(str1) == 3:
#     print("Three")
# elif len(str1) == 5:
#     print("Five")
# elif len(str1) == 7:
#     print("Seven")
# else:
#     print("Other")


# #3.5
# num1 = 8

# for i in range(num1):
#     print("Hello", i)


 # 3.6
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# sum = num1 + num2

# if sum > 10 :
#      print(sum)
# else:
#     i=0
#     multiplier = int(input("Enter multiplier: "))
#     while i < multiplier:
#         print(num1 * num2)
#         i+=1

# 3.7

total= 0
while total < 20 :
    if total==10:
        break
    num1 = int(input("enter number: "))
    total += num1
    if num1 < 3:
        print("number less than 3, bye")
        break                                          
    else:
        for i in range(num1):
            print(f"{num1} is greater than 3")
            print("Hello", i+1)
    total += num1

print(total)    