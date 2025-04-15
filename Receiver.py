import socket
import Receiver_Key

c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # By default it will use IPV4 and TCP for connection

c_sock.connect(('10.1.3.250',9999))

e,d,n = Receiver_Key.get_keys()
c_sock.send(bytes(str(e),'utf-8'))
c_sock.send(bytes(str(n),'utf-8'))

ciphertext=[]
while True:
    ch = c_sock.recv(1024).decode()
    if ch:
        ciphertext.append(int(ch))
    else:
        break

# encrypted_msg = b""
# for ch in ciphertext:
#     encrypted_msg += bytes(str(ch),'utf-8')

# with open('Encrypted_d.jpg','wb') as file:
#     file.write(encrypted_msg)
# file.close()

decoded_msg = [pow(int(c), d, n) for c in ciphertext]

# message = b""
# for ch in decoded_msg:
#     message += bytes(str(ch),'utf-8')

with open('Decrypted_d.jpg','wb') as file:
    # file.write(message)
    

file.close()

c_sock.close()