# encoding = utf-8

import socket
import threading
lock = threading.Lock()


def severer():
    s_ckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_ckt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s_ckt.bind(("", 8899))
    s_ckt.listen()
    c_ckt_info = s_ckt.accept()
    c_ckt, ip_port = c_ckt_info
    c_data = s_ckt.recv(1024)
    message = c_data.decode()
    print(message)
    send_data = "测试信息".encode()
    c_ckt.send(send_data)
    s_ckt.close()


if __name__ == '__main__':
    severer()
