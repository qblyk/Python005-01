# 连接 Redis
import redis

client = redis.Redis(host='81.68.90.212',password='qwer!@#$1')

# 新增集合 rank
client.zadd('rank',{'a':4,'b':3,'c':1,'d':5,'e':2})

# 修改集合值
client.zincrby('rank',-2,'d')

# 从小到大排序
zrange = client.zrangebyscore('rank',1,5)
print(zrange)
# 从大到小
zrevrange = client.zrevrangebyscore('rank',5,1)
print(zrevrange)

# 基card
zcard = client.zcard('rank')
print(zcard)

# 显示评分
zrange1 = client.zrange('rank',0,-1,withscores=True)  # 0,-1 即所有
zrange2 = client.zrange('rank',0,2,withscores=True)  # 0,2 即0，1，2前三个

print(zrange1)
print(zrange2)

# 倒序显示评分
zrange3 = client.zrevrange('rank',0,2,withscores=True)  # 0,2 即0，1，2前三个
print(zrange3)


