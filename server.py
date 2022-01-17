from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from logic import processInput

HOST = ''
PORT = 8080

class JuanHTTP(BaseHTTPRequestHandler):
    
    def do_GET(self):
        content_size = int(self.headers['Content-Length'])
        #print(content_size)

        input = self.rfile.read(content_size)
        res = dict()
        ans = processInput(input, res)
        #a = a.decode("utf-8")
        #a = a.split("\n")
        #print(a)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        self.wfile.write(bytes(json.dumps(res), "utf-8"))
    
server = HTTPServer((HOST, PORT), JuanHTTP)
print("Runnin server in port: {}".format(PORT))

server.serve_forever()

