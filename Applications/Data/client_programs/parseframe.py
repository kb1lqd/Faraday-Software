import argparse
import sys
import bytestuff

# Get arguments
#parser = argparse.ArgumentParser()
#parser.add_argument("data", help="Data string to be transmitted.")
#args = parser.parse_args()

rxframeparser = bytestuff.rxparse()

# Parse arguments
#data = args.data
data = sys.stdin
datalist = []
datastr = ''
for line in data:
    datalist.append(line)
    datastr = datastr + line

#for item in datalist:
#    sys.stdout.write(item)

#sys.stdout.write("Parsing")

for i in range(0,len(datastr)):
    #sys.stdout.write(datastr[i])
    test = rxframeparser.parseframe(datastr[i], bytestuff.framing_startbyte, bytestuff.framing_stopbyte, bytestuff.framing_escapebyte)
    try:
        sys.stdout.write(test)
    except TypeError as e:
        #print "ERROR:", e
        pass

#sys.stdout.write("Parsed")