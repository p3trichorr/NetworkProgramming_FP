import socket
import select
import sys
from threading import Thread
from main import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8081
server.connect((ip_address, port))

def send_msg(sock):
    while True:
        data = ''
        for i in range(len(balls)):
            data += balls[i].x + ',' + balls[i].y + '\n'
        
        sock.send(data.encode())
        sys.stdout.write(data)
        sys.stdout.flush()

def recv_msg(sock):
    while True:
        data = sock.recv(2048)
        sys.stdout.write(data.decode())

Thread(target=send_msg, args=(server,)).start()
Thread(target=recv_msg, args=(server,)).start()
Thread(target=Table).start()

while True:
    socket_list = [server]
    read_socket, write_socket, error_socket = select.select(socket_list, [], [])
    for socks in read_socket:
        if socks == server:
            recv_msg(socks)
        else:
            send_msg(socks)

server.close()
