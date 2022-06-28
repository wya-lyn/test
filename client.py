# encoding = utf-8

import socket
import tkinter
import tkinter.messagebox
import threading
import json
import tkinter.filedialog
from tkinter.scrolledtext import ScrolledText

ip = ''
port = ''
# user = ''
listbox1 = ''  # 用于显示在线用户的列表框
show = 1  # 用于判断是开还是关闭列表框
users = []  # 在线用户列表
chat = '------group chat-------'  # 聊天对象

# 登陆窗口
# tkinter.Tk
root0 = tkinter.Tk()
root0.geometry("300x150")
root0.title('用户登陆窗口')
root0.resizable(0, 0)
one = tkinter.Label(root0, width=300, height=150, bg="lightblue")
one.pack()

ip0 = tkinter.StringVar()
ip0.set('')
user = tkinter.StringVar()
user.set('')

labelip = tkinter.Label(root0, text='ip地址', bg="lightblue")
labelip.place(x=20, y=20, width=100, height=40)
entryip = tkinter.Entry(root0, width=60, textvariable=ip0)
print(entryip.get())
entryip.place(x=120, y=25, width=100, height=30)

labeluser = tkinter.Label(root0, text='用户名', bg="lightblue")
labeluser.place(x=20, y=70, width=100, height=40)
entryuser = tkinter.Entry(root0, width=60, textvariable=user)
entryuser.place(x=120, y=75, width=100, height=30)


def login(*args):
    global ip, port, user
    ip, port = entryip.get().split(':')
    user = entryuser.get()
    if not user:
        tkinter.messagebox.showwarning('warning', message='用户名为空!')
    else:
        root0.destroy()


login_button = tkinter.Button(root0, text="登录", command=login, bg="yellow")
login_button.place(x=135, y=110, width=40, height=25)
root0.bind('return', login)

root0.mainloop()

# 建立连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
s.connect((ip, int(port)))
if user:
    s.send(user.encode())  # 发送用户名
else:
    s.send('用户名不存在'.encode())
    user = ip + ':' + port

# 聊天窗口
root1 = tkinter.Tk()
root1.geometry("640x480")
root1.title('群聊')
root1.resizable(0, 0)

# 消息界面
listbox = ScrolledText(root1)
listbox.place(x=5, y=0, width=640, height=320)
listbox.tag_config('tag1', foreground='green', backgroun="yellow")
listbox.insert(tkinter.END, '欢迎进入群聊，大家开始聊天吧!', 'tag1')

input = tkinter.StringVar()
input.set('')
entryiuput = tkinter.Entry(root1, width=120, textvariable=input)
entryiuput.place(x=5, y=320, width=580, height=170)

# 在线用户列表
listbox1 = tkinter.Listbox(root1)
listbox1.place(x=510, y=0, width=130, height=320)


def send(*args):
    message = entryiuput.get() + '~' + user + '~' + chat
    s.send(message.encode())
    input.set('')


sendbutton = tkinter.Button(root1, text="\n发\n送", anchor='n', command=send, font=('helvetica', 12), bg='white')
sendbutton.place(x=585, y=320, width=60, height=160)
root1.bind('return', send)


def receive():
    global users
    while True:
        data = s.recv(1024)
        data = data.decode()
        print(data)
        try:
            uses = json.loads(data)
            listbox1.delete(0, tkinter.END)
            listbox1.insert(tkinter.END, "当前在线用户")
            listbox1.insert(tkinter.END, "群聊：")
            for x in range(len(uses)):
                listbox1.insert(tkinter.END, uses[x])
            users.append('群聊：')
        except:
            data = data.split('~')
            message = data[0]
            username = data[1]
            chatwith = data[2]
            message = '\n' + message
            if chatwith == '群聊：':  # 群聊
                if username == user:
                    listbox.insert(tkinter.END, message)
                else:
                    listbox.insert(tkinter.END, message)
            elif username == user or chatwith == user:  # 私聊
                if username == user:
                    listbox.tag_config('tag2', foreground='red')
                    listbox.insert(tkinter.END, message, 'tag2')
                else:
                    listbox.tag_config('tag3', foreground='green')
                    listbox.insert(tkinter.END, message, 'tag3')

            listbox.see(tkinter.END)


r = threading.Thread(target=receive)
r.start()  # 开始线程接收信息

root1.mainloop()
s.close()
