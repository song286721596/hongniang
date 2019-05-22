# -*-coding:utf-8-*-
# @Author: Songzq
#@Time: 2019年05月22日09时
#说明:
#总结:
#将hn的reids库中的数据存入到mongodb中，使用条件，本机安装了mongodb数据库

import json
import redis
import MySQLdb

def process_item():
    # 创建redis数据库连接
    rediscli = redis.Redis(host = "127.0.0.1", port = 6379, db = 0)

    # 创建mysql数据库连接
    mysqlcli = MySQLdb.connect(host = "127.0.0.1", port = 3306, \
                               user = "root", passwd = '123456', db='hongniang', charset='utf8')
    offset = 0

    while True:
        # 将数据从redis里pop出来u
        source, data = rediscli.blpop("hn:items")
        item = json.loads(data)
        #创建mysql操作游标对象，可以执行mysql语句
        cursor = mysqlcli.cursor()
        #插入数据前需要自己现在数据库中创建一个表Femal_VIP
        cursor.execute("insert into Femal_VIP (username, age, header_url, images_url, content, workplace, education, income, source_url, source, spidername) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                           ,[item['username'],item['age'],item['header_url'], item['images_url'], item['content'], item['workplace'], item['education'], item['income'], item['source_url'], item['source'], item['spidername']])
        # 提交事务
        mysqlcli.commit()
        # 关闭游标
        cursor.close()
        offset += 1
        print(offset)




if __name__ == '__main__':
    process_item()
