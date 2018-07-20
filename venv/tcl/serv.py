from http.server import HTTPServer, BaseHTTPRequestHandler

class serv(BaseHTTPRequestHandler):

    def do_Get(self):
            if self.path == '/':
                self.path = '/index.html'

            try:
                file_to_open = open(self.path[1]).read()
            except:
                file_to_open = 'File not found'
                self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes(file_to_open, 'utf-8'))


httpd = HTTPServer(('localhost', 8088), serv)
httpd.serve_forever()