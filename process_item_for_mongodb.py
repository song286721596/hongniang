# -*-coding:utf-8-*-
# @Author: Songzq
#@Time: 2019年05月22日09时
#说明:
#总结:
#将hn的reids库中的数据存入到mongodb中，使用条件，本机安装了mongodb数据库

import json
import redis
import pymongo

def main():
    #指定Redis数据库信息，如果是本机就写127.0.0.1就可以，否则写真实的redis地址
    rediscli = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    #指定Mongodb数据库信息，如果是本机就写127.0.0.1就可以，否则写真实的redis地址
    mongocli = pymongo.MongoClient(host='127.0.0.1', port=27017)

    #创建数据库名
    db = mongocli['hongniang']
    #创建表名
    sheet = db['Female_VIP']
    offset = 0
    while True:
        #FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        # redis 数据表名 和 数据
        source, data = rediscli.blpop(['hn:items'])
        offset += 1
        # 将json对象转换为Python对象
        item = json.loads(data)
        # 将数据插入到sheetname表里
        sheet.insert(item)
        print(offset)



if __name__ == "__main__":
    main()
