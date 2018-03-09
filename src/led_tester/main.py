import urllib.request
import numpy as np
import os
import re
import pytest
import sys
import argparse
sys.path.append(".")

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--input', help='input help')
	args = parser.parse_args()
	filename = args.input
	N,instructions = readFile(filename)
	lights = LightTester(N)

	for line in instructions:
		if line != None:
			cmd = line[1]		
			x1,y1,x2,y2 = int(line[2]),int(line[3]),int(line[4]),int(line[5])
			x1,x2 = lights.setValidValue(x1,x2)
			y1,y2 = lights.setValidValue(y1,y2)
			lights.applyLights(cmd,x1,y1,x2,y2)

	count= lights.countLights()
	print(count)

if __name__ == '__solve_led_project__':
    main()



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

def regexTest(buffer):
	N=int(buffer[0])
	instructions=[]
	for i in range(1,len(buffer)):
		regex = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
		newI = regex.match(buffer[i])
		instructions.append(newI)
	return N,instructions



class LightTester(object):
	"""main program for LightTester"""
	def __init__(self, N):
		self.lights = np.zeros((N,N))
		self.size = N

	def setValidValue(self,p1,p2):
	
		if p1 < 0:
			if p2 > 0:
				p1 = 0
			else:
				p1 = p2 = 0
		if p2 > self.size:
			if p1 < self.size:
				p2 = self.size
			else:
				p1 = p2 = 0
		return p1,p2

	def applyLights(self,cmd,x1,x2,y1,y2):
			
		if cmd == "turn on":
			self.lights[x1:x2+1,y1:y2+1] = 1
		elif cmd == "turn off":
			self.lights[x1:x2+1,y1:y2+1] = 0
		elif cmd == "switch":
			self.lights[x1:x2+1,y1:y2+1] = self.lights[x1:x2+1,y1:y2+1] * -1 + 1
	
	def countLights(self):	
		count = np.count_nonzero(self.lights)
		return count


