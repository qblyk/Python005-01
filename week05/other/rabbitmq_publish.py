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

