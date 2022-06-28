# encoding=utf-8

import socket


sever_sokt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_sokt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
sever_sokt.bind(("", 8888))
sever_sokt.listen(5)
client_sokt, ip_port = sever_sokt.accept()
print("客户端的IP地址是：", ip_port)
r_data = client_sokt.recv(1024)
r_data = r_data.decode("utf-8")
print(r_data)
data = "大号是士别三日要两位".encode("utf-8")
client_sokt.send(data)
sever_sokt.close()