# work with external sources is done on a CRUD basis

import json

# # open file since in same folder can use just name or ./<name>
# # r = read, w= write
# f = open("data.json","r")
# # load file to json 
# data = json.load(f)

# # close file
# f.close()


#write file
obj = {"name":"Adi","age":42}

f = open("users.json","r")
users = json.load(f)
users.append(obj)
f.close()

f = open("users.json","w")
json.dump(users, f)
f.close()