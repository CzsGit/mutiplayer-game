# 导入这个模块并调用仅有的函数，函数需要传一个参数，是一个8个数值的列表
from socket import *

# from time import sleep

s = 0


def func():
    # 创建套接字
    global sockfd
    sockfd = socket(AF_INET, SOCK_STREAM)
    # 发起连接
    sockfd.connect(('10.8.22.110', 8867))


def fooc():
    sockfd.send('###'.encode())
    global s
    s = sockfd.recv(1024).decode()
    s = int(s)
    # sleep(0.01)
    sockfd.send('哈哈'.encode())
    return s


def main(l):
    if s % 2 == 1:
        # print('进入了余为1')
        t = []
        l1 = l[0:7]
        print('565656565656565656565656565656565656565656')
        msg = str(l[0]) + '#' + str(l[1]) + '#' + str(l[2]) + '#' + str(l[3]) + '#' + str(l[4]) + '#' + str(
            l[5]) + '#' + str(l[6])
        print('客户端发送值>>>>', msg)
        sockfd.send(msg.encode())
        # 接受消息
        data = sockfd.recv(2048).decode()
        print('客户端接收值<<<<', data)
        k = []
        data = data.split('#')
        for i in range(8):
            k.append(int(data[i]))
        t = l1 + k
        t = [1] + t
        print('当前t', t)
        return t

    elif s % 2 == 0:
        # print('进入了余为0')
        t = []
        l1 = l[7:14]
        msg = str(l[7]) + '#' + str(l[8]) + '#' + str(l[9]) + '#' + str(l[10]) + '#' + str(l[11]) + '#' + str(
            l[12]) + '#' + str(l[13])
        print('客户端发送值2>>>>', msg)
        sockfd.send(msg.encode())
        # 接受消息
        print('88888888888888888888888888888888888888888888')
        data = sockfd.recv(2048).decode()
        k = []
        print('lellele')
        data = data.split('#')
        data = data[0:7]
        print('客户端接收值2<<<<', data)
        for i in range(7):
            k.append(int(data[i]))
        t = k + l1
        t = [2] + t
        print('当前t', t)
        return t

    # 关闭连接
    sockfd.close()
