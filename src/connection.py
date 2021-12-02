from pymongo import MongoClient

client = MongoClient("mongodb://victor:victor@localhost:27017/")

db = client.dio_live

trends_collection = db.trends
