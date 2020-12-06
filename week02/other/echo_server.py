import pretty_errors
import socket

HOST = 'localhost'
PORT = 10000

def echo_server():
    ''' Echo Server 的 Server 端 '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))   #对象S绑定到指定的主机和端口上
    s.listen(1)  #只接收1个链接

    while True:
        # accept表示接受用户端的连接
        conn, addr = s.accept()

        # 输出客户端地址
        print(f'Connected by {addr}')

        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
        conn.close()
    s.close()

if __name__ == "__main__":
    echo_server()
