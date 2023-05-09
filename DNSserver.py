# SIT202 Computer Networking
# Task 6.2 Developing a DNS Server
# Andrew Belcher - 222 390 295
# DNS Server will reply to the DNS Client with dummy information stored in if statements
# Resource records are:
# 1. Decoded when received from the DNS Client
# 2. Converted to a dictionary / object
# 3. Updated based on dummy database / information
# 4. Converted to a json string
# 5. Encoded for transmission to the DNS Client

# Import socket module & json package
from socket import *
import json

# Set the parameters of the DNS server
serverPort = 53

# Set the server socket for the DNS client to communicate to
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

# Print server start message
print('The server is listening')

# Run until DNS Server stopped
while True:
    # Receive message from the DNS client
    message, clientAddress = serverSocket.recvfrom(2048)

    # Decode message
    messageStr = message.decode()

    # Convert message to dictionary / object
    messageObj = json.loads(messageStr)

    # Update resource record based on dummy information & print result
    if messageObj['type'] == 'A':
        print('Hostname to IP address translation')
        if messageObj['name'] == 'Google':
            messageObj['value'] = '8.8.8.8'
            print('Successful')
        else:
            print('Hostname not found')
    elif messageObj['type'] == 'CNAME':
        print('Host aliasing')
        if messageObj['name'] == 'www.my.com':
            messageObj['value'] = 'example.host.aliasing.com'
            print('Successful')
        else:
            print('Host alias not found')

    # Convert resource record to json
    messageToReturn = json.dumps(messageObj)

    # Encode message
    messageToReturnEncoded = messageToReturn.encode()

    # Send encoded message to DNS Client
    serverSocket.sendto(messageToReturnEncoded, clientAddress)
