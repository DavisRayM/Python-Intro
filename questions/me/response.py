


class Response:

    def __init__(self,response_status,content,content_type):
        self.response_status =response_status
        self.content = content
        self.content_type = content_type


    def make_response(self):
        response = f"HTTP/1.1 {self.response_status}\r\nContent-Type: text/html\r\nContent-Length: {len(self.content)}\r\n\r\n{self.content}"