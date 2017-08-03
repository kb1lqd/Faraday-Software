import socket
import time
import struct
import bytestuff
import argparse
import sys
import json

# Get arguments
#parser = argparse.ArgumentParser()
#parser.add_argument("--json", help="Interpret stdin data as JSON encoded data", action="store_true")
#args = parser.parse_args()

# Get stdin data

rxdata_list = []
rxdata = sys.stdin
for line in rxdata:
    #rxdata_list.append(line)
    print json.loads(line)