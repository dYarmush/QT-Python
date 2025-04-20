# like JSON key:value pair
# key can be any data tyoe but strings are the most common as they are readable
#  values can be any data type even another dictionary
# can not change key names

person = {
    "name":"Dovi",
    "age":42
}

print(person["name"])

#changing key value if key does not exist this will create the key:value
person["name"] = "dovi2"

#delete key value
person.pop("name")

#view all keys
person.keys()

# view all values
person.values() 
