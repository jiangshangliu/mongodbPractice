import pymongo
from pymongo import MongoClient
#创建连接
conn = MongoClient('localhost',27017)
#创建数据库
db = conn.red
#创建集合
myset:pymongo.collection.Collection = db.hunter
# print(type(myset))
#增
# myset.insert_one({'name':'zs','age':14})
# myset.insert_one({'name':'ls','age':16})
# myset.insert_one({'name':'ww','age':12})
'''
添加多个，必须是一个列表
'''
# myset.insert_many([{'name':'wolf','age':27},{'name':'ray','age':16}])
#改
# myset.update_one({'name':'ww'},{'$set':{'name':'wangwu'}})
#查
# for obj in myset.find():
#     print(obj)
#删
# myset.delete_one({'name':'ls'})
myset.delete_many({})

#关闭连接
conn.close()



