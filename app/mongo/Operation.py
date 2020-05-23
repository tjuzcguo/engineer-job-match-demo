import pymongo as pm

# client = pm.MongoClient("mongodb://martin:admin@cluster0-shard-00-00-a8t1m.mongodb.net:27017,cluster0-shard-00-01-a8t1m.mongodb.net:27017,cluster0-shard-00-02-a8t1m.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
from app.entity.Person import Person


class Mongo:

    def __init__(self, url='mongodb://localhost:27017/', dbName='demo'):
        self.client = pm.MongoClient(url)
        self.demoDB = self.client[dbName]

    def getCollection(self, col):
        if col not in self.demoDB.list_collection_names():
            return -1
        return self.demoDB[col]

    def createCollection(self, colName):
         self.demoDB[colName]

    def insertOne(self, col, data):
        if col != -1:
            col.insert_one(data)

    def insertMany(self, col, data):
        if col != -1:
            col.insert_many(data)
