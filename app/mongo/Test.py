from app.entity.Person import Person
from app.mongo.Operation import Mongo

if __name__ == '__main__':
    mongoOper = Mongo()

    colName = 'User'

    colUser = mongoOper.getCollection(colName)

    # insert data
    # jack = Person('jack', 22, 2000)
    # tom = Person('tom', 21, 1000)

    # mongoOper.insertOne(colUser, tom.__dict__)

    one = colUser.find_one()

    ones = colUser.find({'name': 'tom'}, {'_id': 0})

    coms = colUser.find({'age': {"$gt": 21}}, {'_id': 0})


    print([one for one in ones])

    print([com for com in coms])

    query = {'age': 21}
    newValue = {'$set':{'age':30}}

    colUser.update_one(query,newValue)

    # 传入参数为空，清空整个collection
    colUser.delete_many()

