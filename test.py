from http.server import HTTPServer, BaseHTTPRequestHandler
import json
 
 
class Resquest(BaseHTTPRequestHandler):
    def handler(self):
        print("data:", self.rfile.readline().decode())
        self.wfile.write(self.rfile.readline())
 
 
    def do_POST(self):
        print(self.headers)
        print(self.command)
        req_datas = self.rfile.read(int(self.headers['content-length'])) #重点在此步!
        print(req_datas.decode())

 
 
if __name__ == '__main__':
    host = ('', 9002)
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()