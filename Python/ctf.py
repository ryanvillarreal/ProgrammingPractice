#! /usr/bin/env python
import socket
import re

host = ''
port = ''

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        data = b''
        while True:
            chunk = client.recv(1024)
            data += chunk
            if len(chunk) < 1024:
                break

        # check the the logic here. 
        # don't forget to add the newline character to actually send the data back.  
        command = data.split()
        command = command[-1]
        print command
        if command == "data":
          payload = str("data").encode('utf-8') + b'\n'
          client.send(payload)
        elif command == "data":
          payload = str("data").encode('utf-8') + b'\n'
          client.send(payload)
        elif command == "data":
          payload = str("data").encode('utf-8') + b'\n'
          client.send(payload)
        elif command == "data":
          payload = str("data").encode('utf-8') + b'\n'
          client.send(payload)
        else: break
client.close()
