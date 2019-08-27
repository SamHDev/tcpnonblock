# TCP Non-Block
A Simple Implementation of Non-Blocking TCP Socket Server. 

## Key Features

 * Simple to Use
 * Threading Built In
 * Expandable
 * Stress Tested

## Installation
You can install via python's `pip` module:

Install with Offical Python Package Index:
```bash
python3 -m pip install tcpnonblock
```
or with this Git Respiratory
```bash
python3 -m pip install git+https://github.com/SamHDev/tcpnonblock.git
```
*Note for Noobies: If `python3` work then use `python`*

----
## Usage

You can import the libary with the following statement:
```py
import tcpnonblock
```

Here is a quick Example of a TCPSocket Server. This is an [Echo Server](/demos/echo/server.py) that replies the message from a client.
```py
server = tcpnonblock.TCPSocketServer() # Create a Server Object

# Create a Client Instance for the Server
@server.client_instance
class ClientInstance(tcpnonblock.TCPSocketServerInstance):
    # On Client Connect
    def connect(self):
        print("Client Connected")
    
    # On Client Disconnect
    def disconnect(self):
        print("Client Disconnected")
    
    # On Client Message
    def message(self, msg):
        self.send("Client Message: ",msg)
        self.reply(msg) # Echo the Message

# On Server Start Event
@server.on_start
def start(host, port):
    print("Server Start")

# On Server Stop Event
@server.on_stop
def stop():
    print("Server Stop")

# Start the Server
server.listen("0.0.0.0", 8080) # Host,Port
server.start()
```
