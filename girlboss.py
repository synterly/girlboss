from http.server import BaseHTTPRequestHandler
import urllib.parse
import math
import random

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
