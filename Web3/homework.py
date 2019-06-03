import pymongo
uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = pymongo.MongoClient(uri)
db = client.c4e
collection = db.posts

collection.insert_one({"title":"Hello", "author":"Khánh Duy","content":"From the other side"})