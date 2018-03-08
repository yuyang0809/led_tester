import urllib.request
import os
import re


def readFile(filename):
	# use readlines to read a line a time
	if filename.startswith('http'):
		req = urllib.request.urlopen(uri)
		buffer = req.read().decode('utf-8').split('\n')
		N=int(buffer[0])
		instructions=[]
		for i in range(1,len(buffer)):
			regex = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
			newI=regex.match(buffer[i])
			instructions.append(newI)
		return N,instructions
	else:
		if os.path.exists(filename):
			buffer = open(filename).read().split('\n')
			N=int(buffer[0])
			instructions=[]
			for i in range(1,len(buffer)):
				regex = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
				newI=regex.match(buffer[i])
				instructions.append(newI)
			return N,instructions
		else:
			print("Not found")
