import pymongo
from pymongo import MongoClient
import datetime

my_client = MongoClient()
db = my_client.mydb

users = db.users

current_date = datetime.datetime.now()
old_date = datetime.datetime(2017, 8, 19)
input = input("Type Date year-mm-dd: ")
search_date = datetime.datetime.strptime(input, "%Y-%m-%d")


user1 = {"username": "joão", "login_date": current_date}
# insert single user in db
user_id1 = users.insert_one(user1).inserted_id


user2 = {"username": "joão", "login_date": old_date}
# insert single user in db
user_id2 = users.insert_one(user2).inserted_id

# $gte - grater than equal
print(users.find({"login_date": {"$gte": search_date}}).count())

# find a doc based on the existence of a field
print(users.find({"login_date": {"$exists": True}}).count())

# all the documents with the username not equal to "joão"
print(users.find({"username": {"$ne": "joão"}}).count())

# creating index for scalability purposes
# creates a index on the field username
# if the username is unique we need to put the param unique=True after the .ASCENDING),
db.users.create_index([("username", pymongo.ASCENDING)])
