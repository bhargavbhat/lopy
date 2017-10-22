### HTTP Integration ###
- Forwards data received from end-node to HTTP endpoint
- Provides a URL for posting data back to end-node (will be queued as a scheduled downlink)

### Steps ###
- Detailed tutorial [here](https://www.youtube.com/watch?v=Uebcq7xmI1M)
- Documentation [here](https://www.thethingsnetwork.org/docs/applications/http/)

### Received Data ###
- Will be in JSON format, example:
```
{"app_id":"aa00bb","dev_id":"XXXX","hardware_serial":"XXXX","port":2,"counter":9,"payload_raw":"BASE64-PAYLOADDATA","metadata":{"time":"2017-10-22T06:59:22.718123654Z","frequency":866,"modulation":"LORA","data_rate":"SF7BW125","coding_rate":"4/5","gateways":[{"gtw_id":"eui-XXX","timestamp":4220672586,"time":"2017-10-22T06:59:22.419521Z","channel":0,"rssi":-57,"snr":5}],"latitude":0.00,"longitude":1.11},"downlink_url":"https://integrations.thethingsnetwork.org/ttn-eu/api/v2/down/XXX/YYY?key=aabbcc00"}
```
### CURL Command ###
- Schedules `01 01` to be sent to end-node, example:
```
curl -X POST --data '{"dev_id":"XXX","payload_raw":"AQE="}' https://integrations.thethingsnetwork.org/ttn-eu/api/v2/down/XXX/YYY?key=aabbcc00
```
