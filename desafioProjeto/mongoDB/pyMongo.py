import datetime
import pprint
import pymongo as pyM

client = pyM.MongoClient(
    "mongodb+srv://pymongo:<password>@pymongo.ehbb9ge.mongodb.net/?retryWrites=true&w=majority")

db = client.test
collection = db.test_collection

print(db.list_collection_names())

post = {
    "author": "Mike",
    "text": "MY first mongoDB application based on python",
    "tags": ["mongodb", "pthon", "pymongo"],
    "data": datetime.datetime.utcnow()
}


posts = db.posts
post_id = posts.insert_one(post).inserted_id
# print(post_id)
# print(db.posts.find_one())

print("\n Documentos presentes na coleção posts: \n")
for post in posts.find():
    pprint.pprint(post)
