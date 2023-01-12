#!/usr/bin/env python3

# baresip-Roborock
# 2023 elias weingaertner
#
# This script allows one to start a Roborock vacuum cleaner (or anything else supported
# by miio) making a phone call. This works by simply configuring baresip
# to connect to an arbitrary SIP server, for example a Fritzbox.
#
# This script connects to baresip using the ctrl_tcp module and starts
# Roborock using Python-Miio.
#
#

import logging
import socket
import json
import time
from pynetstring import encode,decode
from miio import DeviceFactory
logging.basicConfig(level=logging.INFO)

BARESIP_HOST = "localhost"  # baresip host name, typically localhost
BARESIP_PORT = 4444  # baresip TCP port (enable ctrl_tcp)

ROBOROCK_IP="<ROBOROCK IP>"
ROBOROCK_TOKEN="<YOUR TOKEN>"

logging.info("Connecting to Roborock")
dev = DeviceFactory.create(ROBOROCK_IP, ROBOROCK_TOKEN)
logging.info("Roborock info: {}".format(dev.info()))

def start_roborock():
    logging.info("Starting to clean")
    dev.resume_or_start()
    #dev.find()

hangup_message = '{"command":"hangup"}'

def handle_event(json_event_data):
    event_type = json_event_data.get('type')
    logging.info("Received SIP event from baresip, type={}".format(event_type))
    if event_type=="CALL_INCOMING":
        command_hangup = encode(hangup_message)
        s.sendall(command_hangup)

        start_roborock()

    else:
        logging.debug("Ignoring event of type {}".format(event_type))

def handle_baresip_json(jsonstring):

    json_data = json.loads(jsonstring)
    if json_data.get('event') is True:
        handle_event(json_data)
    else:
        logging.debug("Received non-event baresip json {}".format(json_data))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((BARESIP_HOST, BARESIP_PORT))
    while True:
        data = s.recv(2048)
        jsonstrings = decode(data)
        for jsonstring in jsonstrings:
            handle_baresip_json(jsonstring)
