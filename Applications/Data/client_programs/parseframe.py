import argparse
import sys
import bytestuff
import json

# Get arguments
parser = argparse.ArgumentParser()
parser.add_argument("--json", help="Output JSON formatted parsed frames to stdout instead of raw frame contents", action="store_true")
args = parser.parse_args()

rxframeparser = bytestuff.rxparse()

# Parse arguments
#data = args.data
data = sys.stdin

datalist = []
datastr = ''
for line in data:
    datastr = datastr + line

for i in range(0,len(datastr)):
    # Parse frames
    test = rxframeparser.parseframe(datastr[i], bytestuff.framing_startbyte, bytestuff.framing_stopbyte, bytestuff.framing_escapebyte)
    if test != None:
        datalist.append(test)
    else:
        # Ignore
        pass

if args.json:
    sys.stdout.write(json.dumps(datalist))
else:
    for item in datalist:
        try:
            sys.stdout.write(item)
        except TypeError as e:
            # print "ERROR:", e
            pass
