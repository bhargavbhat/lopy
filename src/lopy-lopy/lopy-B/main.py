from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA, frequency=866000000, sf=7)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

print('Booting LoPy Device B')
while True:
    s.send('Ping')
    if s.recv(64) == b'Pong':
        print('Got Pong...')
    time.sleep(5)
    print('*')
