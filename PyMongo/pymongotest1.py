import pymongo
from pymongo import MongoClient

my_client = MongoClient()
db = my_client.mydb

users = db.users

# single user
user1 = {"username": "joão", "password": "mypass",
         "favourite_num": 445, "hobbies": ["python", "games", "pizza"]}
# insert single user in db
user_id1 = users.insert_one(user1).inserted_id

# single user
user2 = {"username": "joana", "password": "pass01",
         "favourite_num": 777, "hobbies": ["maquilhagem", "instagram", "sushi"]}
# insert single user in db
user_id2 = users.insert_one(user2).inserted_id

# bulk insert

bulk_users = [{"username": "Manuel", "password": "123456"},
              {"username": "Maria", "password": "654321"}]

user_id3 = users.insert_many(bulk_users).inserted_ids

print("Number of files:", users.find().count())
print("Number of files with favourite number equal 777 :",
      users.find({"favourite_num": 777}).count())
print("Number of files with favourite number equal 777 and username is Joana :",
      users.find({"favourite_num": 777, "username": "joana"}).count())
    
    
