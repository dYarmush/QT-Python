from pymongo import MongoClient

#chhose server
client = MongoClient(port = 27017)# connection string if not localhost, port

#choose DB
db = client["Test"]

# choose collection
collection = db["users"]
#returns ODM - usable by python

#read
# collection.find({}) # inside the {} would be k:v for search criteria returns array
# collection.find_one({"name":"Avi"}) # should be a uniques value

#Create
collection.insert_one({"name":"Dovi"})#inserts one
# collection.insert_many("insert array of dict") # inserts many

#update
# collection.update_one()# 2 parameters k:v of which field, what to update ("name":"Dovi",
#{"$set":{"name":"Dovi2"})

# collection.update_many

#delete
# collection.delete_one()# {k:v} of what to delete
# collection.delete_many()

