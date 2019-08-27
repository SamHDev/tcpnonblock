# TCP Non-Block
A Simple Implementation of Non-Blocking TCP Socket Server. 

## Key Features

 * Simple to Use
 * Threading Built In
 * Expandable  - Does'nt use a thread per connection
 * Stress Tested - Can handle 100+ connections  (tested on a [OVH VPS SSD 1](https://www.ovh.co.uk/vps/vps-ssd.xml))

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


## Usage

You can import the libary with the following statement:
```py
import tcpnonblock
```

### Server Example
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
        print("Client Message: ",msg)
        self.send("You Said: ", msg) # Echo the Message (Send)

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

### Client Example
Here is a quick Example of a TCPSocket Client to go with our Echo Server. This is an [Echo Client](/demos/echo/client.py) that interacts with our Example.
```py
client = remote.TCPSocketClient() # Create a Client Object

# On Client Connected to Server
@client.on_open
def on_open():
    print("Connected to Server")
    client.send("Hello World!")

# On Client Disconnected from Server
@client.on_close
def on_close():
    print("Disconnected to Server")

# On Server Message Received
@client.on_message
def on_message(msg):
    print("Reply: ", msg) #`Msg` is a `string`

client.connect("localhost", 81)
```

### Threading

What about that threading I mentioned earlier, well its this simple. 
Just declare the `threading` argument in the creation of the object.
It works for both `TCPSocketServer` and `TCPSocketClient`

```py
server = tcpnonblock.TCPSocketServer(threaded=True)
client = rtcpnonblock.TCPSocketClient(threaded=True)
```

The Thread will be created and started on `.start()`

## License and Attributes

Created by Sam Huddart under alias [SamHDev](https://github.com/SamHDev/) for the [Blume Open Source Project](https://www.youtube.com/watch?v=oHg5SJYRHA0). `SamHDev/tcpnonblock` is licensed under the GNU General Public License v3.0 and is Open-Source. Commercial use, Modification and Distribution are permmited. Although credit is not necessary, it is much obliged. If you do wish to credit the author, please link the [respiratory](https://github.com/SamHDev/tcpnonblock/) and the author at [github](https://github.com/SamHDev/) or [website](https://samhdev.com). Thank you for using our work.
