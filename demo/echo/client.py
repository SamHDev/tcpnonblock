import tcpnonblock

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

client.connect("localhost", 8080)
