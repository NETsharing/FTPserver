"""
На стороне клиента: использует сокеты для передачи данных серверу
и выводит ответ сервера на каждую строку сообщения - счетчик get обращений сессии; 'localhost' означает,
что сервер выполняется на одном компьютере с клиентом, что позволяет
тестировать клиента и сервер на одном компьютере;
"""

import sys
from socket import *
import struct
serverHost = 'localhost'
serverPort = 50007

message = [b'Hello network world']
if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((serverHost, serverPort))
for line in message:
    sockobj.send(line)
    data = sockobj.recv(1024)
    nums = struct.unpack('i', data)[0]
    print('Your appeal number:', nums)
sockobj.close()