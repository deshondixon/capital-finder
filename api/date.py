# http.server from standard library for handling HTTP requests
from http.server import BaseHTTPRequestHandler
# datetime from standard library for handling dates
from datetime import datetime


# new subclass called handler that extends BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
        return
