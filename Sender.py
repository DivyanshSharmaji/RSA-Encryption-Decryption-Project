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
time.sleep(0.01)
n = c_sock.recv(1024).decode()
print("Received public key(e,n) of receiver as follows:")
print("e = ",e," n = ",n)
time.sleep(5)

msg = b""
with open('d.jpg','rb') as file:
    msg = file.read()
print("File data(Binary): ",msg)
time.sleep(5)

integer_list = list(msg)
print("File data(integer): ",integer_list)
time.sleep(5)

ciphertext = [pow(ch, int(e), int(n)) for ch in integer_list]
# pow(ch,e,n) = (ch^e)%n
print("File data(Encrypted integer list): ",ciphertext)
time.sleep(5)

byte_data = b''
for c in ciphertext:
    # Send each integer in 4 bytes (assuming c < 2^32), change if needed
    byte_data += c.to_bytes(4, byteorder='big')
c_sock.sendall(byte_data)
print("Successfully sent the encrypted file")

c_sock.close()
sock.close()