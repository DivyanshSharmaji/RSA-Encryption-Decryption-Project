import socket
import Receiver_Key
import time

c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # By default it will use IPV4 and TCP for connection

c_sock.connect(('192.168.43.134',9999))
# c_sock.connect(('10.1.3.250',9999))

e,d,n = Receiver_Key.get_keys()
print("Generated e and n (Public key) as follows: ")
print("e = ",e," n = ",n)
print("Sent values of e and n from receiver end")
time.sleep(5)
c_sock.send(bytes(str(e),'utf-8'))
time.sleep(0.1)
c_sock.send(bytes(str(n),'utf-8'))


time.sleep(5)
received_bytes = c_sock.recv(409600)
ciphertext = []
size_enc=0
for i in range(0, len(received_bytes), 4):  # 4 bytes per int
    chunk = received_bytes[i:i+4]
    if len(chunk) == 4:
        size_enc+=4
        num = int.from_bytes(chunk, byteorder='big')
        ciphertext.append(num)
print("File data(Encrypted integer list): ",ciphertext)
time.sleep(5)


encrypted_msg = b''
for c in ciphertext:
    encrypted_msg += c.to_bytes(4, byteorder='big')
with open('Encrypted_d.jpg','wb') as file:
    file.write(encrypted_msg)
file.close()

decoded_msg = [pow(int(c), d, n) for c in ciphertext]
size_dec=len(decoded_msg)
print("File data(integer): ",decoded_msg)
time.sleep(5)

message = bytes(decoded_msg)
print("File data(Binary): ",message)
time.sleep(5)
with open('Decrypted_d.jpg','wb') as file:
    file.write(message)
print("File successfully decrypted")
print("Encrypted file size: ", size_enc/1024,"Kb")
print("Decrypted file size: ", size_dec/1024,"Kb")

file.close()

c_sock.close()