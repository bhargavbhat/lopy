### TTN Connectivity
- To connect to TTN, register an account first. 
- Gateway Flash Steps
    - Sync one LoPy as Nano-gateway "src/ttn/lopy-nanogw", note the Gateway ID
    - Add Gateway to TTN with displayed Gateway ID. See [here](./ttn_config/00gw.md)
    - Edit "config.py" and add the correct WiFi SSID and Password (WiFi is used for backhaul i.e connecting Gateway to TTN servers)
    - Sync changes. Gateway should connect to TTN after reboot
    - In TTN Console:
        - check Gateways -> Overview -> "Last Seen" it will be "now" or "xx seconds ago"
        - check Gateways -> Traffic -> will show exchange of packets

- End Node Flash Steps (ABP Method)
    - Sync another LoPy with "src/ttn/lopy-dev-eui", note the Dev EUI
    - Add Device with this Dev EUI. See [here](./ttn_config/02dev.md)
    - Load End-node code "src/ttn/lopy-nanogw-node-abp"
    - Edit various parameters in End-node code i.e Dev ID, Nwk Key and App Key to match TTN configuration
    - Sync changes to End-node and reboot. The End-node will connect to TTN via gateway
    - In TTN Console:
        - check Application -> Devices -> Overview -> "Last Seen" it will be "now" or "xx seconds ago"
        - check Application -> Devices -> Data -> will show exchange of packets
        - *Note For ABP Only:* in case packets show up in gateway traffic but not in application, reset the frame counters. See [this](https://www.thethingsnetwork.org/forum/t/reset-frame-counter-issue/5169) for details 

- End Node Flash Steps (OTAA Method)
    - TODO
