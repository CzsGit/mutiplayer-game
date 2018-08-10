import socket, signal
from multiprocessing import *
import os, sys

# from time import sleep

HOST = '0.0.0.0'
PORT = 8867
shm = Array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 0, 0])
shx = Value('i', 0)


# 处理具体的客户端请求
def handler1(connfd):
    print('进入了handler１')
    while True:
        print('客户端口号:', connfd.getpeername())
        data = connfd.recv(1024).decode()
        if not data:
            print('客户端已退出')
            break
        print('服务器接收值<<<<', data)
        data = data.split('#')
        for i in range(7):
            shm[i] = int(data[i])
        msy = str(shm[7]) + '#' + str(shm[8]) + '#' + str(shm[9]) + '#' + str(shm[10]) + '#' + str(shm[11]) + '#' + str(
            shm[12]) + '#' + str(shm[13]) + '#' + str(shx.value) + '#'
        print('服务器发送值>>>>', msy.encode())
        print('当前的shx的值为', shx.value)
        connfd.send(msy.encode())
    connfd.close()


def handler2(connfd):
    print('进入了handler2')
    while True:
        print('客户端口号:', connfd.getpeername())
        data = connfd.recv(1024).decode()
        if not data:
            print('客户端已退出')
            break
        print('服务器接收值B<<<<', data)
        msy = str(shm[0]) + '#' + str(shm[1]) + '#' + str(shm[2]) + '#' + str(shm[3]) + '#' + str(shm[4]) + '#' + str(
            shm[5]) + '#' + str(shm[6]) + '#'
        print('服务器发送值B>>>>', msy.encode())
        # sleep(10)
        connfd.send(msy.encode())
        data = data.split('#')
        shm[7] = int(data[0])
        shm[8] = int(data[1])
        shm[9] = int(data[2])
        shm[10] = int(data[3])
        shm[11] = int(data[4])
        shm[12] = int(data[5])
        shm[13] = int(data[6])
        connfd.send(msy.encode())
    connfd.close()


# 创建套接字
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.setblocking(0)
s.listen(5)
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# 主线程循环接收客户端连接

while True:
    try:
        c, addr = s.accept()
        shx.value += 1
    except KeyboardInterrupt:
        raise
    except Exception as e:
        # time.sleep(1)
        print(e)
        continue
    while True:
        data = c.recv(1024).decode()
        if data == '###':
            print(data)
            c.send(str(shx.value).encode())
        elif shx.value % 2 == 1:
            print('jihao')
            t = Process(target=handler1, args=(c,))
            t.start()
            break
        else:
            k = Process(target=handler2, args=(c,))
            k.start()
            break

s.close()
