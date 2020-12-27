# 连接 Redis
import redis

client = redis.Redis(host='81.68.90.212',password='qwer!@#$1')

# 插入数据
client.lpush('list_demo','18217517890')
client.rpush('list_demo','18217517891')

# 查看长度
print(client.llen('list_demo'))

# 弹出数据
data = client.lpop('list_demo')  # 左侧弹出
print(data)
data2 = client.rpop('list_demo')  # 右侧弹出
print(data2)

# 查看一定范围内的 list 数据
data3 = client.lrange('list_demo',0,5)
print(data3)

# 循环取数 d
for i in data3:
    print(i.decode())

