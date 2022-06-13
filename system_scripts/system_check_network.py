#!/usr/bin/env python3
import requests
import socket

# check_network.py file checks validation of localhost
def check_localhost():
  """ Checks and validates that localhost is present """
        localhost = socket.gethostbyname('localhost')
        return localhost=="127.0.0.1"

def check_connectivity():
  """ Checks the connection to outside website is code 200 """
        request = requests.get("http://www.google.com")
        return request.status_code== int(200)
