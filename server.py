import socket
import select
import sys
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ip_address = '127.0.0.1'
port = 8081
server.bind((ip_address, port))
server.listen(100)
list_of_clients = []
index = 0

def clientthread(conn, addr):
    while True:
        try:
            message = conn.recv(2048).decode()
            if message:
                if list_of_clients[0]:
                    player = 1
                elif list_of_clients[1]:
                    player = 2
                message_to_send = '<Player {}>\n{}'.format(player, message)
                print(message_to_send)
                broadcast(message_to_send, conn)
            else:
                remove(conn)

        except:
            continue

def broadcast(message, connection):
    for clients in list_of_clients:
        if (clients != connection):
            try:
                print(message.encode())
                clients.send(message.encode())
                # for i in range(14):
                #     print("Ball {}: x={}, y={}", format(i, message.split(',')[0], message.split(',')[1]))
                
            except:
                clients.close()
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while(True):
    conn, addr = server.accept()
    list_of_clients.append(conn)
    index += 1
    if index == 1:
        player_1 = list_of_clients[0]
        print('Player 1 connected')
    elif index == 2:
        player_2 = list_of_clients[1]
        print('Player 2 connected')
        
    threading.Thread(target=clientthread, args=(conn, addr)).start()

conn.close()