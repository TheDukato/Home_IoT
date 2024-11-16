# IoT System for a Home

## Project Description

This project aims to create an IoT system for a home. The project is built on bash, python and Node.js technology, using the Node-RED platform.

### Main Features:
- Real-time monitoring of electricity consumption.
- Control of lighting, blinds, systems.
- Notifications about device statuses, faults, or anomalies.
- Integration with IoT devices using MQTT, HTTP, or WebSocket protocols.
- Expandable system for adding more devices.

## Used hardware and software

Before using the system, ensure that you meet the following requirements:

- **Python** version 3.9.2
- **Node.js** version 14.x
- **Node-RED** https://nodered.org/
- **IoT Devices** 
    - Foto resistors
    - iNode energy meter
    - RPI zero
    - outer ADC


## Installation

### Step 1: Install Node.js

Download and install Node.js from https://nodejs.org/. You can also install it using a package manager like `apt` on Linux systems:

```bash
sudo apt update
sudo apt install nodejs
sudo apt install npm
```