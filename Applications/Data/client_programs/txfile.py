# RX File is used to read in and prepare a file for being transmitted over a bytestream.
import argparse
import sys

# Get arguments
parser = argparse.ArgumentParser()
parser.add_argument("--filepath", help="Path to file that will be prepared for transmission")
args = parser.parse_args()

# Parse arguments
filepath = args.filepath


with open(filepath, 'r') as f:
    read_data = f.read()
    
sys.stdout.write(read_data)