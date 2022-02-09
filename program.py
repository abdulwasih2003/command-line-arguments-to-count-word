import sys
fp =open(sys.argv[1])
data=fp.read()
words=data.split()
print("Total number of words",len(words))