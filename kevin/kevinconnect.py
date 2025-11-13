"""
import discord
import globals

import threading

import json

from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus

PORT = 53640

server:HTTPServer = None
thread:threading.Thread = None

class KevinHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("got")

        print(self.headers)

        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        
        if "kcactionqueue" in globals.kevin_globals.keys():
            self.wfile.write(json.dumps(globals.kevin_globals["kcactionqueue"]).encode('utf-8'))
            globals.kevin_globals["kcactionqueue"].clear()
        else:
            self.wfile.write(b"{\"error\": \"action queue does not exist yet\"}")

    def do_POST(self):
        print("post")

        self.send_response(HTTPStatus.IM_A_TEAPOT) #
        self.send_header("Content-type", "text/html")
        self.end_headers()


async def on_ready(client:discord.Client):
    global thread

    def do():
        global server

        server_address = ('', PORT)
        server = HTTPServer(server_address, KevinHandler)
        print(f"starting server on {PORT}")
        server.serve_forever()

    thread = threading.Thread(target=do)
    thread.start()

async def on_exit(client:discord.Client):
    print("shutting down server")
    server.shutdown()
    thread.join()
"""