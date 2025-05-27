# Create a Python program that receives an id from the user, get his data from
# https://jsonplaceholder.typicode.com/users REST API, and prints his name & email.
# If his name starts with “E” (try with user with id 2..), get his todo’s titles from
# https://jsonplaceholder.typicode.com/todos/userId={userid} REST API and save all his todo’s
# titles to a json file
# 


import requests
import json
from pymongo import MongoClient

client = MongoClient(port = 27017)

db = client["Movies"]

collection = db["movies"]

# userId = input("Input user ID:")

# r = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")
# user = r.json()
# print(user["name"], user["email"])
# username = user["name"]
# if username[0] == "E":
#     todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}/todos")
#     f = open("todo.json","w")
#     titles = []
  
#     for todo in todos.json():
#         toDo_dict ={"id":todo["id"],"title":todo["title"]}
#         titles.append(toDo_dict)
#     json.dump(titles,f)
#     f.close()

# Load the first 10 movies from the https://api.tvmaze.com/shows REST APIand
# insert that data to a proper collection in the MongoDB.
# Each movie Document will stores the following data :
# - _id (Object ID)
# - Name
# - Genres
# - Average rating

# Ask from the user for a current movie name. Ask from the user a new movie name andupdate
# the existing movie with the new name.

r = requests.get("https://api.tvmaze.com/shows")

for item in r.json():
    if item["id"] <=10:
        movie ={"Name":item["name"],"Genre":item["genres"],"Avg Rating":item["rating"]["average"]}
        collection.insert_one(movie)
        print(movie)        

