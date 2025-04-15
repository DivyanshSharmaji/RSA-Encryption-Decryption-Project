import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # By default it will use IPV4 and TCP for connection

sock.bind(('10.1.3.250',9999)) # Binds the socket with a port number(0-65535), localhost is the IP address of current machine, so we passed a tuple of IP address and port number in bind() method
# Type ipconfig on cmd to check your machine's ip address

sock.listen(5)
print('Waiting for connection...')
c_sock, addr = sock.accept() # Accepts the connection from the client and returns client socket and address of the client
print("Connection established with ",addr)
e = c_sock.recv(1024).decode() # Public key of receiver
n = c_sock.recv(1024).decode()

msg = b""
with open('d.jpg','rb') as file:
    msg = file.read()

integer_list = list(msg)
ciphertext = [pow(ch, int(e), int(n)) for ch in integer_list]
# pow(ch,e,n) = (ch^e)%n

for ch in ciphertext:
    c_sock.send(bytes(str(ch),'utf-8'))
    time.sleep(0.000001)
print("Successfully sent the encrypted file")

c_sock.close()
sock.close()