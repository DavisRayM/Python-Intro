import socket


class Response:

    def __init__(self,response_status,content,content_type):
        self.response_status =response_status
        self.content = content
        self.content_type = content_type


    def make_response(self):
        response = f"HTTP/1.1 {self.response_status}\r\nContent-Type: text/html\r\nContent-Length: {len(self.content)}\r\n\r\n{self.content}"

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

        page = open(path)
        content = page.read()
        response_status= 200

        #send HTTP response
        conn.sendall(Response().make_response(response_status,content).encode())