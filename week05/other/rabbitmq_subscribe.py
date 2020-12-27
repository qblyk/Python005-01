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
