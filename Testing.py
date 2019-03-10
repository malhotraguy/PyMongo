import pymongo
import datetime
import pprint
#This tutorial also assumes that a MongoDB instance is running on the default host and port.
# Assuming you have downloaded and installed MongoDB, you can start it like so: $ mongod
from pymongo import MongoClient
#The first step when working with PyMongo is to create a MongoClient to the running mongod instance. Doing so is easy:

#client = MongoClient()

#The above code will connect on the default host and port. We can also specify the host and port explicitly, as follows:

client = MongoClient('localhost',27017)
# Or use the MongoDB URI format:

#client = MongoClient('mongodb://localhost:27017')
db= client["test_database"]
# Or db = client.test_database
collection = db["test_collection"]
# Or collection = db.test_collection
post={ "author":"Rahul",
       "text":"My first play with PyMongo",
       "tags":["mongodb","python","pymongo"],
       "date":datetime.datetime.utcnow()
     }
# Making new collection posts
posts = db.posts

#x= posts.insert_one(post)
#print(x)
#print(x.inserted_id)
print(db.collection_names(include_system_collections=False))
pprint.pprint(posts.find_one())
for post in posts.find():
    pprint.pprint(post)
print(posts.count_documents({}))
posts.update_one({"author":"Rahul"},{"$set":{"author":"Nikunj"}})
for post in posts.find():
    pprint.pprint(post)