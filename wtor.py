"""
wtor
by Cth103, 2017
Usage:
wtor.py http://www.google.com
"""

import os
import shutil
import urllib
from stem.control import Controller
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
  hitmebabyonemoretime = urllib.request.urlopen(sys.argv[1])
  endhtml = hitmebabyonemoretime.read()
  return endhtml
  
print('wtor')
print('By cth103')
print('Connecting to Tor...')

with Controller.from_port() as controller:
  controller.authenticate()
  
  response = controller.create_ephemeral_hidden_service({80: 5000}, await_publication = True)
  print("Service online at %s.onion, " % response.service_id)

  try:
    app.run()
  finally:
    print("Shutting down the hidden service")
