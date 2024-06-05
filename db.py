from pymongo.mongo_client import MongoClient


uri = "mongodb+srv://test:test@url-shortner.feghp9s.mongodb.net/?retryWrites=true&w=majority&appName=url-shortner"
client = MongoClient(uri)

db = client.get_database("trending_x")
trends_collection = db.get_collection("trend")



for x in d:
    print(x)
