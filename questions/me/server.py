import socket

from requests import request

HOST = 'localhost'
PORT = 8000

# The arguments passed to socket() are constants used to specify the address family and socket type. AF_INET is the Internet address family for IPv4.
# SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network.
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    #binds socket to address
    s.bind((HOST,PORT))
    #enables server to connect
    s.listen()
    #tuple unpacking of Host and PORT
    #accepting connection with the client
    conn,addr = s.accept()
    #confirming connection has taken place
    with conn:
        print(f"connected by{addr}")
        while True:
            #accessing and reading data sent by the client which is in bytes of 1024
            data = conn.recv(1024).decode().split('\r\n')
            print(data)
            #Parse HTTP headers
            # headers =data.split('\n')
            path = data[0].split()[1]
            #Get the content of html file
            if path == '/':
                path = 'index.html'
            elif path =='/about':
                path = 'about.html'
            elif path == '/post':
                path = 'post.html'

            try:
                page = open(path)
                content = page.read()
                response_status= 200
                no_response=404

                response = f"HTTP/1.1 {response_status}\r\nContent-Type: text/html\r\nContent-Length: {len(content)}\r\n\r\n{content}"
            except FileNotFoundError:
                response = f"HTTP/1.1 404 NOT FOUND\n\nFile Not Found'"
            #send HTTP response
            conn.sendall(response.encode())