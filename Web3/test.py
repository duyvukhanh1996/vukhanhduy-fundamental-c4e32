import pymongo
from bson.objectid import ObjectId
 
uri = 'mongodb://duyvukhanh:123456a@ds059125.mlab.com:59125/vukhanhduy'
 
client = pymongo.MongoClient(uri)
db = client.vukhanhduy
collection = db.vkduy

print(list(collection.find())
