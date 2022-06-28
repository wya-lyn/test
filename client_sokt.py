# encoding=utf-8
import socket
client_sokt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_sokt.connect(("192.168.0.23",8888))
data="今天是个好日子".encode("utf-8")
client_sokt.send(data)
rdata = client_sokt.recv(1024)
rdata = rdata.decode("utf-8")
print(rdata)
# s_data=client_sokt.recv(1024).decode()
# print(s_data)