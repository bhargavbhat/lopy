# Required to add device to TTN
# Taken from: https://www.thethingsnetwork.org/forum/t/lopy-otaa-example/4471/6

from network import LoRa
import binascii
lora = LoRa(mode=LoRa.LORAWAN)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))