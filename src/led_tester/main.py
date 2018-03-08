import urllib.request
import os
import re


def readFile(filename):
	# use readlines to read a line a time
	if filename.startswith('http'):
		req = urllib.request.urlopen(filename)
		buffer = req.read().decode('utf-8').split('\n')
		N,instructions = regexTest(buffer)
		return N,instructions
	else:
		if os.path.exists(filename):
			buffer = open(filename).read().split('\n')
			N,instructions = regexTest(buffer)
			return N,instructions
		else:
			print("Not found")

def  regexTest(buffer):
	N=int(buffer[0])
	instructions=[]
	for i in range(1,len(buffer)):
		regex = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
		newI=regex.match(buffer[i])
		instructions.append(newI)
	return N,instructions