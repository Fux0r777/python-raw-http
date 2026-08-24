import socket

# Server address and porttt
target_host = "127.0.0.1"
port = 9997

# udp socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send a test message to the server
client.sendto(b"test", (target_host, port))

#response
data, addr = client.recvfrom(4096)

# Display the response
print(data.decode())

# Close the socket
client.close()
