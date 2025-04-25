import socket
import time

def create_post_request(pin):
    return f """POST /HTTP/1.1
Host: 127.0.0.1:8888
Content-Type: application/x-www-form-urlencoded
Content-Length: {length(f"pin={pin}")}


pin={pin}"""

