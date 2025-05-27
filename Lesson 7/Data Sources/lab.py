# Create a JSON file represents Person with the following structure :

# Name : "",Address :
# {
# City : "",Street :
# {
# Name : "",
# Number : ""
# }
# }
# Fill the file with 2 Person data.

# Write a function in module called files_utils that receive a street name and returns theperson's
# name, city & street who lives there (if any) and return it.
import json

def files_utils(street_name):
    f = open("person.json","r")
    people = json.load(f)
    for person in people:
        if person["Address"]["Street"]["Name"] == street_name:
            return f"{person["Name"]},{person["Address"]["City"]},{person["Address"]["Street"]["Name"]}"
        
print(files_utils("spigelman"))        