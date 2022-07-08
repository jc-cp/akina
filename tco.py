import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://jayqwalin:sBizum7HyN2Isvmi@cluster0.hvkyyid.mongodb.net/?retryWrites=true&w=majority")
db = cluster["AkinaDB"]
collection = db["listings_AutoScout"]


