# RX File is used to read in and prepare a file for being transmitted over a bytestream.
import argparse
import sys
import base64

# Get arguments
parser = argparse.ArgumentParser()
parser.add_argument("--filepath", help="Path to file that will be prepared for transmission")
args = parser.parse_args()

# Parse arguments
filepath = args.filepath


with open(filepath, 'rb') as f:
    read_data = f.read()

read_data = base64.b64encode(read_data)  # Encode with BASE64 due to STDOUT and STDIN having trouble with binary...

sys.stdout.write(read_data)
