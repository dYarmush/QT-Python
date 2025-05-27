import requests

# get request
r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json() # converts obj to json format

# post - Create (method takes the api address and data in json / dict format)
r = requests.post("https://jsonplaceholder.typicode.com/users", {"name":"Dovi"})
data = r.json()
print(data)

#put updates an entire object  PATCH does just a certain field
r = requests.put("https://jsonplaceholder.typicode.com/users/1", {"name": "Dovi"})
print(f"put response {r.json()}")

