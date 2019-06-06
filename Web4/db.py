import pymongo
from bson.objectid import ObjectId
 
uri = 'mongodb://duyvukhanh:123456a@ds059125.mlab.com:59125/vukhanhduy'
 
client = pymongo.MongoClient(uri)
db = client.vukhanhduy
collection = db.bike_list

def insert_bike(name:str, price:int, image:str, year:int):
    collection.insert_one({"name": name, "price": price,"image":image,"year":year})

def get_all(): 
    return list(collection.find())