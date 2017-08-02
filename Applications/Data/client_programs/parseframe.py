import argparse
import sys

# Get arguments
#parser = argparse.ArgumentParser()
#parser.add_argument("data", help="Data string to be transmitted.")
#args = parser.parse_args()

# Parse arguments
#data = args.data
data = sys.stdin
datalist = []
for line in data:
    datalist.append(line)

for item in datalist:
    sys.stdout.write(item)
