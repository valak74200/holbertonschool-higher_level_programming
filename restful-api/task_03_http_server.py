import http.server
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def send_json_response(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_json_response(data)
        elif self.path == '/status':
            self.send_json_response({"status": "OK"})
        elif self.path == '/info':
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_json_response(info)
        else:
            self.send_json_response({"error": "Endpoint not found"}, 404)

if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()
