import pymongo
import json
from pymongo import MongoClient, InsertOne
from django.conf import settings
'''
def get_db_handle(db_name, host, port, username, password):
    
 client = MongoClient(host=host,
                      port=int(port),
                      username=username,
                      password=password
                     )
 db_handle = client['db_name']
 return db_handle, client
'''
CONNECTION_STRING = "mongodb+srv://<group1>:<seng3011>@cluster0.jhta3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client['search_results']

collection_name = db["test1"]
requesting = []

with open(r"data.json") as f:
    for jsonObj in f:
        myDict = json.loads(jsonObj)
        requesting.append(InsertOne(myDict))

result = collection_name.bulk_write(requesting)
count = collection_name.count()
print(count)
client.close()

#collection_name.insert_many()
