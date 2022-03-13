import pymongo
import json
from pymongo import MongoClient, InsertOne
#from django.conf import settings


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://<group1>:<seng3011>@cluster0.jhta3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['search_results']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    collection_name = dbname["test1"]

    with open("data.json") as f:
        myList = json.load(f)
        print(type(myList))

    result = collection_name.insert_many(myList)
    #count = collection_name.count()
    #print(count)
    #dbname.close()
    