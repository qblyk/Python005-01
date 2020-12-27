# 连接 Redis
import redis

client = redis.Redis(host='81.68.90.212',password='qwer!@#$1')

# 设置哈希数据
client.hset('hash_user_vip','1001',1)
client.hset('hash_user_vip','1002',1)

# 删除数据
client.hdel('hash_user_vip','1002')

# 查询数据是否存在
istrue = client.hexists('hash_user_vip','1001')
isfalse = client.hexists('hash_user_vip','1002')

print('存在：',istrue)
print('不存在：',isfalse)

# 添加多个键值对
client.hmset('hash_user_vip',{'1003':1,'1004':1})

# 取所有keys
field = client.hkeys('hash_user_vip')
print(field)

# 取value
value1 = client.hget('hash_user_vip','1001')
print(value1.decode())
valuem = client.hmget('hash_user_vip','1001','1003')  # 取多个
print(valuem)

valueall = client.hgetall('hash_user_vip')   # 取所有
print(valueall)

for i in valueall:   #循环输出
    print(i.decode())
