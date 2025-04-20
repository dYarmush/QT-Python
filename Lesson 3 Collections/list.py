grades = [80,90,95]
sorted = grades.sort


print(sum(grades))
# prints length of the list  starts from 1
print(len(grades))

# add item to the end of the list
grades.append(75)
print (grades)

#add item to specific index
grades.insert(2,100)
print (grades)

# remove an item from the end of list, also returns the erased value
grades.pop()

#  remove a SPecific index
grades.pop(1)

# List operators - In
if 90 in grades:
    print("90 is in the list")

if 87 not in grades:
    print("87 not in the list")