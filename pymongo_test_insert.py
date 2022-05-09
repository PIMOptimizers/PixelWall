import pymongo
from pprint import pprint
from pymongo import MongoClient

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = "mongodb+srv://pim:pimpassword@cluster0.5yxrc.mongodb.net/DB-PIM?retryWrites=true&w=majority"

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(CONNECTION_STRING)
# Creation DB
db = client.dbPim

pprint(db.list_collection_names())

user1 = {"name": "fathi", "score": "0"}

# Create collection
users = db.users

# Add new user to collection
result = users.insert_one(user1)

