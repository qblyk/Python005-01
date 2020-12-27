# 连接 Redis
import redis

client = redis.Redis(host='81.68.90.212',password='qwer!@#$1')

# 设置集合数据
times = client.sadd('redis_set','123')
times = client.sadd('redis_set','1234')

times = client.sadd('redis_set1','123')
times = client.sadd('redis_set1','1235')

print(times)

# 弹出集合数据
# spop1 = client.spop('redis_set')
# print(spop1)

# 查询集合数据
smembers1 = client.smembers('redis_set')
print('smembers1: ',smembers1)

# 交集
sinter1 = client.sinter('redis_set','redis_set1')
print('sinter1: ',sinter1)

# 并集
sunion1 = client.sunion('redis_set','redis_set1')
print('sunion1: ',sunion1)

# 差集
sdiff1 = client.sdiff('redis_set','redis_set1')
print('sdiff1: ',sdiff1)
