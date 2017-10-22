
from network import LoRa
from network import WLAN
import socket
import binascii
import struct
import time
import pycom

# Configuration for India
LORA_FREQUENCY = 866000000
LORA_NODE_DR = 5

# Turn off WiFi see also https://forum.pycom.io/topic/156/disable-wifi-for-low-power-operation
wlan = WLAN()
wlan.deinit()
print('WiFi OFF')

# Initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)
print('Device ID: ' + binascii.hexlify(lora.mac()).lower().decode('utf-8'))

# create an OTA authentication params
# these settings can be found from TTN
dev_eui = binascii.unhexlify(' '.replace(' ',''))
app_eui = binascii.unhexlify(' '.replace(' ',''))
app_key = binascii.unhexlify(' '.replace(' ',''))

# remove all the non-default channels
for i in range(3, 16):
    lora.remove_channel(i)

# set the 3 default channels to the same frequency
lora.add_channel(0, frequency=LORA_FREQUENCY, dr_min=0, dr_max=LORA_NODE_DR)
lora.add_channel(1, frequency=LORA_FREQUENCY, dr_min=0, dr_max=LORA_NODE_DR)
lora.add_channel(2, frequency=LORA_FREQUENCY, dr_min=0, dr_max=LORA_NODE_DR)

# join a network using OTAA
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0, dr=LORA_NODE_DR)
print('Sent Join...')

while not lora.has_joined():
    print('Not Joined...')
    time.sleep(5)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, LORA_NODE_DR)

# make the socket blocking
s.setblocking(False)

while True:
    for i in range (10):
        s.send(b'Tx #' + bytes([i]))
        print('Tx #' + str(i))
        rx, port = s.recvfrom(256)
        if rx:
            print('Rx: {}, on port: {}'.format(rx, port))
        time.sleep(30)