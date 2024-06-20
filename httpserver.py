#!/usr/bin/env python3

# by Honghe
# Ported to Python 3 by Telmo "Trooper" (telmo.trooper@gmail.com)
#
# Original code from:
# http://www.piware.de/2011/01/creating-an-https-server-in-python/
# https://gist.github.com/dergachev/7028596
#
# To generate a certificate use:
# openssl req -newkey rsa:4096 -nodes -keyout key.pem -x509 -days 365 -out cert.pem

# from http.server import HTTPServer, SimpleHTTPRequestHandler
# import ssl


# httpd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
# httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile="cert.pem", server_side=True)

# print("Server running on https://0.0.0.0:" + str(port))

# httpd.serve_forever()

from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
port = 4443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
context.check_hostname = False

with HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()
print('server running')

