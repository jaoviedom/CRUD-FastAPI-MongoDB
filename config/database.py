from pymongo import MongoClient

# client = MongoClient("mongodb+srv://Cluster97946:e1t0Smhdb198@cluster97946.4g0gtcj.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient("mongodb://root:secret@localhost:27017")

db = client.test

collection_name = db["users"]