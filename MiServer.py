import socket

CHUNK = 65535# receive at most these bytes of data at once

port = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#create socket object
#socket.socket(family,type)
#AF_NET : family of ipv4 ip address
#SOCK_DRA : UDP, SOCK_STREAM : TCP

#some ip address that the server will listen to when msg comes
hostname = '127.0.0.1'#ip address of local machine ,same for everyone in here

#aka home, there is no place like '127.0.0.1' <---- MEME    hehehehehe (#^.^#)

s.bind((hostname, port))#bind the socket with host machine on port 3000 
print(f"Server is live on {s.getsockname()}")

#run this server infinitely until i want to stop
while True:

    data, clientAdd = s.recvfrom(CHUNK)
    message = data.decode('ascii')# data travels in bytes by default
    print(f"kiki Says: {message} ")
    
    msg_send = input("Reply: ")
    data = msg_send.encode('ascii')
    #send data to ip add that sent me the data
    s.sendto(data,clientAdd)
    
    