from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        message = """
        <html>
            <body>
                <h1>Hello from Jenkins + Docker!</h1>
                <p>My DevOps CI/CD pipeline is working.</p>
            </body>
        </html>
        """

        self.wfile.write(message.encode())


server = HTTPServer(("0.0.0.0", 8000), MyHandler)

print("Server running on port 8000...")

server.serve_forever()