#!/usr/bin/env python3

from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

# get the server start time
start_time = str(datetime.now())

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
    global start_time

    # Send response status code
    self.send_response(200)

    # Send headers
    self.send_header('Content-type','text/html')
    self.end_headers()

    # Send message back to client
    message = "Started at {}".format(start_time)
    # Write content as utf-8 data
    self.wfile.write(bytes(message, "utf8"))
    return

def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('0.0.0.0', 8080)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()
