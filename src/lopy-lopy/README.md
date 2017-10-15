### Lopy-Lopy Example
- Test code for raw LoRa (i.e no LoRaWAN) between two LoRa devices
- For Device A
    - Sync code from "src/lopy-lopy/lopy-A" to the device, observe serial logs
- For Device B
    - Sync code from "src/lopy-lopy/lopy-B" to the device, observe serial logs
- Expected exchange is something similar to following:
    - For Device A
        ```
        entry 0x4009fc9c
        Booting LoPy Device A
        .
        Got Ping... Sending Pong
        .
        Got Ping... Sending Pong
        .
        Got Ping... Sending Pong
        .
        ```
    - For Device B
        ```
        entry 0x4009fc9c
        Booting LoPy Device B
        *
        Got Pong...
        *
        Got Pong...
        *
        Got Pong...
        *
        ```
- Original Source Code obtained from PyCom Examples available in [GitHub](https://github.com/pycom/pycom-libraries/tree/master/examples/lopy-lopy)
- Modified Frequncy for India and set Spreading Factor to 7
- Minor changes to logging and messages
