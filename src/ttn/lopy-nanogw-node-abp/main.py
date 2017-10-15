from network import LoRa
import socket
import binascii
import struct
import time

# Configuration for India
LORA_FREQUENCY = 866000000
LORA_NODE_DR = 5

# initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an ABP authentication params
dev_addr = struct.unpack(">l", binascii.unhexlify('DEV_ID'.replace(' ','')))[0]
nwk_swkey = binascii.unhexlify('NwkKey'.replace(' ',''))
app_swkey = binascii.unhexlify('AppKey'.replace(' ',''))

# remove all the non-default channels
for i in range(3, 16):
    lora.remove_channel(i)

# set the 3 default channels to the same frequency
lora.add_channel(0, frequency=LORA_FREQUENCY, dr_min=0, dr_max=LORA_NODE_DR)
lora.add_channel(1, frequency=LORA_FREQUENCY, dr_min=0, dr_max=LORA_NODE_DR)
lora.add_channel(2, frequency=LORA_FREQUENCY, dr_min=0, dr_max=LORA_NODE_DR)

# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

print('Sent Join...')

while not lora.has_joined():
    print('Not Joined...')
    sleep(5)

print('Joined!!')

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, LORA_NODE_DR)

# make the socket blocking
s.setblocking(False)

# remember to turn off frame counters in TTN
# device -> Settings -> Frame Counter Checks (should be unticked)
while True:
    for i in range (10):
        s.send(b'Tx #' + bytes([i]))
        print('Tx #' + str(i))
        rx, port = s.recvfrom(256)
        if rx:
            print('Rx: {}, on port: {}'.format(rx, port))
        time.sleep(30)