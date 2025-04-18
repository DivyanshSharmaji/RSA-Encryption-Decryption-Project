# RSA-Encryption-Decryption-Project
This is a simple project which illustrates how RSA encryption and decryption works over the internet

## Steps to follow:
1. Save the Receiver.py and Receiver_Key.py on receiver's machine.
2. Save the Sender.py on Sender's machine.
3. Write the IP address of sender's machine in the code at the line "sock.bind(('192.168.43.134',9999))" in place of "192.168.43.134" and also change the file path from the line "with open('d.jpg','rb') as file:"
4. Run the Sender.py file
5. Write the IP address of sender's machine in the code at the line "c_sock.bind(('192.168.43.134',9999))" in place of "192.168.43.134"
6. Run the Receiver.py

Now the files from sender will gets encrypted and than send to receiver and than receiver decrypts the file. Hence the file get transferred securely.
