import socket
import time
import struct
import bytestuff
import argparse
import sys
import json
import base64

# Get arguments
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Name of file to save completed assembly as")
parser.add_argument("--json", help="Interpret stdin data as JSON encoded data", action="store_true")
args = parser.parse_args()

# Get stdin data

rxdata_list = []
rxdata = sys.stdin

if args.json:
    for line in rxdata:
        temp = json.loads(line)
        for item in temp:
            rxdata_list.append(base64.b64decode(item))  # Decode BASE64 due to stdin and stdout binary issues
else:
    for line in rxdata:
        rxdata_list.append(line)


data = ''.join(rxdata_list)

file = open(args.filename, 'wb')
for item in data:
    file.write(item)

file.close()