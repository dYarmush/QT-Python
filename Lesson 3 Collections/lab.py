#4.1
# my_list = [5,6,2,9,12,4]

# total = int(my_list[0]+my_list[len(my_list)-1])
# print(total)


#4.2 In the following array , [5, 6, 2, 9, 12, 4], set the third value to be the multiply of the first 2
#values ( 2 will become 11 )

# arr = [5, 6, 2, 9, 12, 4]
# arr[2] = arr[0] + arr[1]

# print(arr[2])

#4.3 Create an array of numbers and print their sum
# arr =[1,2,3,4,5,6,7,8,9,10]
# total = 0

# for num in arr:
#     total += num

# print(total)


# #4.4
# my_list = ["Dovi","Adi","Eran","Peanut butter"]

# for name in my_list:
#     if len(name) >= 4:
#         print(name)

#4.5
# bool_list = [True,False,False,True,False,True,True]

# for v in bool_list:
#     if v == True:
#         print(v)

#4.6

# array = [[1,6,7],[8,3],[2,9,5,4]]
# for a in array:
#     for num in a:
#         print(num)
# for a in array:
#     print("length", len(a))
# for a in array:
#     for num in a:
#         if num >=4 and num <=8:
#             print("number between 4 and 8 ", num)

# total_sum = 0
# for a in array:
# #     for num in a:
#         total_sum+= num
#     print(total_sum)


#5.2
# dictionary = {
#     "nums1": [4, 1, 2, 5],
#     "nums2": [6, 1, 8, 3],
#     "Student": {"Name": "Avi",
#                  "ID": 111111, 
#                  "Grades": {
#                      "nums3": [4, 1, 9, 3]}}}
# num1_avg = 0
# for num in dictionary["nums1"]:
#     num1_avg += num

# num3_avg = 0
# for num in dictionary["Student"]["Grades"]["nums3"]:
#     num3_avg += num

# num1_avg = num1_avg/len(dictionary["nums1"])
# num3_avg = num3_avg/len(dictionary["Student"]["Grades"]["nums3"])

# if num1_avg > num3_avg:
#     print(num1_avg)
# else:
#     print(num3_avg)


# #avg of numbers
# 5.1

# my_list  = [ 4, "Hello" , [ True, "Avi" , [5,1,9,3] ] ]
# total = 0
# arr_len = 0
# for item in my_list:
#     if isinstance(item, list):
#         for inner_item in item:
#             if isinstance(inner_item, list):
#                 arr_len = len(inner_item)
#                 for num in inner_item:
#                     total += num

# print (total/arr_len)
