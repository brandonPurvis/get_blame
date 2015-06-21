from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from main import run as run_blame
from search import INDEX


def on_post(data):
    run_blame(data)

class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(INDEX)

    def do_POST(self):
        self._set_headers()
        length = int(self.headers.getheader('content-length'))
        data = self.rfile.read(length)
        on_post(data)
        self.wfile.write('ack')


def run(server_class=HTTPServer, handler_class=Handler, port=9500):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting server')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv
    if len(argv) > 1:
        run(port=int(argv[1]))
    else:
        run()
