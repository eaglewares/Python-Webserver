# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>EagleWares</title></head>", "utf-8"))
        self.wfile.write(bytes("<p style='background-color:#FFFFE0;font-size:50px;text-align:center;'>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body style='background-color:#B0C4DE;'>", "utf-8"))
        self.wfile.write(bytes("<p>Here You are on web server.<br> Please Enter Your Details</p>", "utf-8"))
        self.wfile.write(bytes("""<div style='background-color:#FFFFE0;text-align:center; border: 3px solid #555; width: 60%;
  height: 150px;margin:10%''><div style='margin:3%'><label>UserName:</label><input type="text"><br>
        </div><div style='margin:3%'><label>Password:</label><input type="password"><br><input type="submit" value="Submit"></div></div>""", "utf-8"))

        self.wfile.write(bytes("<p>host name<br> %s</p>" % hostName, "utf-8"))
        self.wfile.write(bytes("<p>server port<br> %s</p>" % serverPort, "utf-8"))
        self.wfile.write(bytes("<footer style='padding:5;size:100%;'><p style='font-size:20px;text-align:center;'>A python webserver<p/></footer>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

