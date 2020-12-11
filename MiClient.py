import socket

CHUNK = 65535
port = 3000#from server.py
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#instead of explicitly binding socket let os do it
#ephemaral ports
hostname = '127.0.0.1'#from server.py

while True:
    s.connect((hostname, port))
    msg = input("Type msg: ")
    data = msg.encode('ascii')
    s.send(data)
    #data received
    data = s.recv(CHUNK)
    text = data.decode('ascii')
    print(f"mimi says {text}")