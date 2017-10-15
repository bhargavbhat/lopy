## Steps to Bringup LoPy

### Hardware
    - Connect LoPy to expansion board as per official [docs](https://docs.pycom.io/chapter/gettingstarted/unboxing.html)
    - The Heartbeat LED (big white square) comes right on top of the Micro-USB port
    - The LoRA Antenna connector is right next to heartbeat LED & Reset button see [here](https://github.com/ttn-liv/devices/wiki/Getting-started-with-the-PyCom-LoPy)

### Update Firmware
    - Follow official docs [here](https://docs.pycom.io/chapter/gettingstarted/installation/firmwaretool.html)
    - For linux, dependency resolution required
    
### PyMakr Plugin
- Plugin for developing using LoPy, available for VS Code and Atom Editors, details [here](https://docs.pycom.io/chapter/pymakr/)
- VS Code version Setup : HowTo
    - Before setup, ensure 
    - Then follow official [doc](https://docs.pycom.io/chapter/pymakr/installation/vscode.html)
    - *Note* : VS Code displays all the commands such as "Run", "Sync" and "All Commands" in the status bar (bottom of application) not within Main Menus or toolbars
    - To load and example code:
        - Ensure connected to LoPy via serial
        - In VS Code click File -> Open Folder -> Select folder with code (*.py files)
        - Once files loaded, click "Sync" at bottom of the editor
        - Code will be flashed and run, observe output in the terminal

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

- End Node Flash Steps (OTAA Method)
    - TODO