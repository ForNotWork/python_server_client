from requests import get
import socket
import threading
# Define the host and port
HOST = 'server_ip'
PORT = 5555

nickname = input('Choose a nickname:')
# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('an Error occured!')
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input()}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target= receive)
receive_thread.start()

write_thread = threading.Thread(target= write)
write_thread.start()
