# 连接 Redis
import redis

client = redis.Redis(host='81.68.90.212',password='qwer!@#$1')

client.set('key', 'value', nx=True)
client.set('key2', 'value2')
client.set('key3', '100')


# 根据key查询value
result = client.get('key')
print(result.decode())

# 追加String
client.append('key2','100')
print('====> key2: ',client.get('key2').decode())
result = client.get('key2')

# 逻辑运算
result2 = client.incr('key3')  # +1
print(result2)
result3 = client.decr('key3')  # +1
print(result3)

# 不要贸然使用key * 指令，如果数据达到百万级，会造成短暂无响应

# print(client.keys())
# for key in client.keys():
#     print(key.decode())