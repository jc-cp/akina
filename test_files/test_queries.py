import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://jayqwalin:sBizum7HyN2Isvmi@cluster0.hvkyyid.mongodb.net/?retryWrites=true&w=majority")
db = cluster["akina"]
listings = db["listings_AutoScout"]
adac = db["adac_scores"]

print(listings.find({"MAKENAME": "BMW"}))
# results = collection.find({"MAKENAME":"BMW"}).pretty()
results = db.inventory.find({"MAKENAME":"BMW"})

for result in results:
    print(result)


cluster.close()