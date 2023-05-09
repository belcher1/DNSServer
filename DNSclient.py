# SIT202 Computer Networking
# Task 6.2 Developing a DNS Server
# Andrew Belcher - 222 390 295
# DNS Client will send resource records to the DNS Server
# Resource records are:
# 1. Created as dictionaries / objects
# 2. Converted to a json string
# 3. Encoded for transmission to the DNS Server
# 4. Decoded when received from the DNS Server
# 5. Printed

# Import socket module & json package
from socket import *
import json

# Set the parameters of the DNS server we will connect to
serverName = "127.0.0.1"
serverPort = 53

# Set the client socket for the DNS server to communicate to
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Print welcome message
print("Welcome to the client")

# Set variable for while loop condition
varToContinue = True

# Run until user enters no - 'n'
while varToContinue:
    # Prompt user to enter resource record type
    resourceRecordType = input("Enter 'A' for type A or 'CNAME' for type CNAME: ")

    # Initialise variables
    resourceRecordName = ""
    resourceRecordValue = ""

    # Prompt users for resource record name based on record type
    if resourceRecordType == "A":
        resourceRecordName = input("Enter the hostname: ")
    elif resourceRecordType == "CNAME":
        resourceRecordName = input("Enter the alias name: ")

    # Update resource record with user input
    resourceRecord = {
        'name': resourceRecordName,
        'value': resourceRecordValue,
        'type': resourceRecordType,
        'ttl': 'toUpdate'
    }

    # Convert dictionary to json
    messageJson = json.dumps(resourceRecord)

    # Encode json message
    messageEncoded = messageJson.encode()

    # Send message to DNS Server
    clientSocket.sendto(messageEncoded, (serverName, serverPort))

    # Receive server reply & decode
    ServerReply, serverAddress = clientSocket.recvfrom(2048)
    replyDecoded = ServerReply.decode()

    # Print server reply
    print('Response: ' + replyDecoded)

    # Prompt user to check if they want to continue
    checkContinue = input('Do you have another DNS query (y or n): ')

    # If no, set while condition to false
    if checkContinue == 'n':
        varToContinue = False

# Close the client socket
clientSocket.close()
