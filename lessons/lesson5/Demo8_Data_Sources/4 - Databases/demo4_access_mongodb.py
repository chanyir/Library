from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(port=27017)
db = client["KivunDB"]
users_collection = db["users"]

# Get all documents (a list of results)
users = users_collection.find( {} )
for user in users:
    print(user["name"])

# Get a document by its ID (find_one will return only 1 result)
user = users_collection.find_one({"_id": ObjectId("6776bca51a83361909580f7e")})
# print(user)

# Add a new document
new_user = {"name": "Avi", "age": 40}

users_collection.insert_one(new_user)
users_collection.insert_many([new_user, new_user2, new_user3])

# Update documents
new_data = {"city": "Haifa"}
# update one document
users_collection.update_one({"_id": ObjectId("6776bc9b1a83361909580f7d")},  {"$set": new_data}    )

# update more than 1 document
users_collection.update_many({"name": "Avi"}, {"$set": new_data})

# Delete a document
users_collection.delete_one({"_id": ObjectId("6776bca51a83361909580f7e")})
# Delete Many document
# users_collection.delete_many({"name": "Aviva"})
print("DELETED!")


