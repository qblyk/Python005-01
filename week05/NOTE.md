学习笔记

#G20200389060116
#姓名：秦朝亮
#作业&总结链接：https://github.com/qblyk/Python005-01/tree/main/week05


#下载
wget http://download.redis.io/releases/redis-6.0.9.tar.gz

#解压
tar -xzvf redis-6.0.9.tar.gz

# 安装
make ; make install
# 查看服务端地址
which redis-server
# 查看客户端地址
which redis-cli

# 配置文件复制到  /etc/
cp redis.conf /etc/

# 修改配置文件
requirepass qwer!@#$1         # 密码
bind 0.0.0.0        # 监听IP地址（修改为监听所有）

# 启动redis
redis-server /etc/redis.conf
# 查看启动进程
ss -ntpl | grep 6379

# 客户端链接redis
redis-cli
# 关闭redis
redis-cli
127.0.0.1:6379> shutdown

## Python链接redis
# 安装依赖包
pip3 install redis

# 连接 Redis
import redis

client = redis.Redis(host='81.68.90.212',password='qwer!@#$1')

# set设置或插入值
client.set('key', 'value', nx=True)  #set时设置nx=ture，可保证参数存在时不进行覆盖
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
result3 = client.decr('key3')  # -1
print(result3)

# 不要贸然使用key * 指令，如果数据达到百万级，会造成短暂无响应

print(client.keys())

for key in client.keys():
    print(key.decode())


gcc 版本升级 4.8.5版本过低会导致无法编译redis安装文件
#!/bin/bash
# yum install centos-release-scl scl-utils-build
# yum list all --enablerepo='centos-sclo-rh'
# yum install -y devtoolset-8-toolchain
scl enable devtoolset-8 bash
# gcc --version




列表list
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

# 循环取数
for i in data3:
    print(i.decode())



集合
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




哈希hash
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



有序集合zset
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


# 安装rabbitmq
yum install rabbitmq-server

# 插件安装
rabbitmq-plugins enable rabbitmq_management

# 启动 端口：5672
systemctl start rabbitmq-server

# http://81.68.90.212:15672/#/

# 默认用户名和密码
guest/guest


# 安装pika包（支持Python连接rabbitmq）
pip3 install pika

消息发送
# pip3 install pika
import pretty_errors
import pika

# 用户名和密码
credentials = pika.PlainCredentials('guest', 'guest')

# 虚拟队列需要制定参数 virtual_host , 如果是默认的可以不填。
parameters = pika.ConnectionParameters(host='81.68.90.212',
                                            port=5672,
                                            virtual_host='/',
                                            credentials=credentials)

# 阻塞方法(建立连接)
connection = pika.BlockingConnection(parameters)

# 建立信道
channel = connection.channel()

# 声明消息队列
# 如不存在自动创建
# durable=True 队列持久化
channel.queue_declare(queue='direct_demo',durable=False)

# exchange 制定交换机
# routing_key 制定队列名并发送消息
channel.basic_publish(exchange='',routing_key='direct_demo',
                        body='send message to rabbitmq!')

connection.sleep(10)

# 关闭与rabbitmq server的连接
connection.close()




消息接收
# pip3 install pika
import pretty_errors
import pika

# 用户名和密码
credentials = pika.PlainCredentials('guest', 'guest')

# 虚拟队列需要制定参数 virtual_host , 如果是默认的可以不填。
parameters = pika.ConnectionParameters(host='81.68.90.212',
                                            port=5672,
                                            virtual_host='/',
                                            credentials=credentials)

# 阻塞方法(建立连接)
connection = pika.BlockingConnection(parameters)

# 建立信道
channel = connection.channel()

# 定义一个回调函数来处理消息队列中的消息


def callback(ch, method, properties, body):
    # 手动发送确认消息
    ch.basic_ack(delivery_tag=method.delivery_tag)
    # 实现如何处理消息
    print(body.decode())


# 消费者使用队列和哪个回调函数处理消息
channel.basic_consume('direct_demo', on_message_callback=callback)

# 开始接收信息，并进入阻塞状态
channel.start_consuming()




# 安装依赖
pip3 install grpcio

# 安装编译工具
pip3 install grpcio-tools

# 升级protobuf
pip3 install --upgrade protobuf -i https://pypi.douban.com/simple