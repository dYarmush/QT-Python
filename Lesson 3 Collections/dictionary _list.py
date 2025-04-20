

people = [
        {"name":"Dovi", "age":420},
        {"name":"Adi", "age":421},
        {"name":"Eran", "age":422}
]
#PRINT ALL AGES
#using for loop
for i in range(len(people)):
    print(people[i]["age"])
# using for each  Syntax  "for x in list"

for person in people:
    print(person["name"])