import pymongo
from bson.objectid import ObjectId
 
uri = 'mongodb://duyvukhanh:123456a@ds059125.mlab.com:59125/vukhanhduy'
 
client = pymongo.MongoClient(uri)
db = client.vukhanhduy
collection = db.vkduy

def update_food_by_id(food_id,name,price): 
    collection.update_one({"_id":ObjectId(food_id)},
    {"$set":{"name":name,"price":price}})

def get_food_by_id(food_id): 
    return collection.find_one({"_id":  ObjectId(food_id)})

def get_all(): 
    return list(collection.find())


def insert_food(name:str, price:int):
    collection.insert_one({"name": name, "price": price})

def delete_food_by_id(food_id):
    collection.delete_one({"_id":  ObjectId(food_id)})
