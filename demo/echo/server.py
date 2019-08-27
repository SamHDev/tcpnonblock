import tcpnonblock

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
