from app.entity.Person import Person
from app.mongo.Operation import Mongo




if __name__ == '__main__':

    remoteURL = 'mongodb://martin:admin@cluster0-shard-00-00-a8t1m.mongodb.net:27017,cluster0-shard-00-01-a8t1m.mongodb.net:27017,cluster0-shard-00-02-a8t1m.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'

    mongo = Mongo(url=remoteURL)

    colName = 'User'

    mongo.createCollection(colName)

    colUser = mongo.getCollection(colName)

    # insert data
    jack = Person('jack', 22, 2000)
    tom = Person('tom', 21, 1000)

    mongo.insertOne(colUser, tom.__dict__)

    ones = colUser.find({'name': 'tom'}, {'_id': 0})

    coms = colUser.find({'age': {"$gt": 21}}, {'_id': 0})


    print([one for one in ones])

    print([com for com in coms])
