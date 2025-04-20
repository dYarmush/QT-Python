from functools import reduce
# unnamed function / annonymous functions
# regular function with no name but has place in memory

# annnymous function that takes a # and returns multiplied by 2
#lambda is run when the code gets to it and then it is deleted from memory
f1 = lambda x : x * 2

f1 (5)

#high order functions
#instead of below
arr = [1,2,3,4]
arr2 =[]

for num in arr:
    arr2.append(num*2)

#print(arr2)

# can do

#print(list(map(lambda num : num *2, arr)))

# map takes a funtion and array 
# and returns an array the same length as the original with the function applied to it

#HOF Filter return must be True/False

arr2 = [ 15,12,1,4,89,63,2,2,24]

filter(lambda num :num >10 , arr)

# REDUCE need to import using from functools import reduce returns compounded value
print(reduce(lambda x,y: x+y,arr))