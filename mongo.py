import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://admin:admin@cluster0-hz7um.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["StudentDeyails"]
collection = db["students"]
post = [
{"name":"balu","age":22},
{"name":"babu","age":52},
{"name":"naidu","age":87}
]

results = collection.insert_many(post)

# for result in results:
#     print(result["name"])
