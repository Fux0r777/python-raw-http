import socket


target_host = "sqlinjectionstudios.com"
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, port))

request = b"GET / HTTP/1.1\r\nHost: sqlinjectionstudios.com\r\n\r\n"

client.send(request)

response = client.recv(4096)
print(response.decode())
