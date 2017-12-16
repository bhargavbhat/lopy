## Steps to Bringup LoPy

### Hardware
- Connect LoPy to expansion board as per official [docs](https://docs.pycom.io/chapter/gettingstarted/unboxing.html)
- The Heartbeat LED (big white square) comes right on top of the Micro-USB port
- The LoRa Antenna connector is right next to heartbeat LED & Reset button see [here](https://github.com/ttn-liv/devices/wiki/Getting-started-with-the-PyCom-LoPy)

### Update Firmware
- Follow official docs [here](https://docs.pycom.io/chapter/gettingstarted/installation/firmwaretool.html)
- For linux, dependency resolution required
    
### PyMakr Plugin
- Plugin for developing using LoPy, available for VS Code and Atom Editors, details [here](https://docs.pycom.io/chapter/pymakr/)
- VS Code version Setup : HowTo
    - Before installing this plugin, ensure [NodeJS](https://nodejs.org/en/) is installed and working correctly (type `node -v` in terminal and the output should be similar to `v8.9.3`)
    - Then follow official [doc](https://docs.pycom.io/chapter/pymakr/installation/vscode.html)
    - *Note* : VS Code displays all the commands such as "Run", "Sync" and "All Commands" in the status bar (bottom of application) not within Main Menus or toolbars
    - To load and example code:
        - Ensure connected to LoPy via serial
        - In VS Code click File -> Open Folder -> Select folder with code (*.py files)
        - Once files loaded, click "Sync" at bottom of the editor
        - Code will be flashed and run, observe output in the terminal
