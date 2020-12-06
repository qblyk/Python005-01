import pretty_errors
import socket

HOST = 'localhost'
PORT = 10002

file = 'book.json'
fileResponse = 'response.txt'
def echo_client(filepath):
    ''' Echo Server 的 Client 端 '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    while True:
        # 接收用户输入数据并发送服务器
        # data = input('input > ')
        with open(filepath,'rb') as f:
            message = f.read()
        # # 设定退出条件
        # if data == 'exit':
        #     break

        # 发送数据到服务器
        s.sendall(message)

        # 接收服务端数据
        data  = s.recv(1024)
        if not data:
            break
        else:
            with open(fileResponse,'a+') as rsf:
                rsf.write(data)
            print(data.decode('utf-8'))
    s.close()

if __name__ == "__main__":
    echo_client(file)


