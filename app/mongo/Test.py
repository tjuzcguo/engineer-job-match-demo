from app.entity.Person import Person
from app.mongo.Operation import Mongo
import json

# 初始化数据库
mongoOper = Mongo()
colName = 'User'
colUser = mongoOper.getCollection(colName)


def insert():
    # insert data
    jack = Person('jack', 22, 2000)
    tom = Person('tom', 21, 1000)
    mongoOper.insertOne(colUser, tom.__dict__)
    mongoOper.insertOne(colUser, jack.__dict__)


def query():
    one = colUser.find_one()
    ones = colUser.find({'name': 'tom'}, {'_id': 0})
    coms = colUser.find({'age': {"$gt": 21}}, {'_id': 0})
    print([one for one in ones])
    print([com for com in coms])


def update():
    query = {'age': 21}
    newValue = {'$set': {'age': 30}}
    colUser.update_one(query, newValue)


if __name__ == '__main__':

    file = open(r'../data/user.json')
    for line in file:
        mongoOper.insertOne(colUser, json.loads(line))
        print(line)

    query()

    # 传入参数为空，清空整个collection
    # colUser.delete_many({'age':{'$gt': 20}})
