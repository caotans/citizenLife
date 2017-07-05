#! usr/bin/python
# cording:utf-8
import redis
#获得连接
def getRedisConn():
 r=redis.Redis(host="127.0.0.1",port="6379",password="123456",db=0)
 return r
#关闭连接
def closeRedisConn():
    try:
        redis.shutdown()
    except:
        print("redis关闭异常!")
#重新连接
def reRedisConn():
    try:
        return getRedisConn()
    except:
        print("redis重新连接失败!")