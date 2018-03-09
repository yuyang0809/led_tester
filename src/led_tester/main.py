import urllib.request
import numpy as np
import os
import re
import pytest
import sys
import argparse
sys.path.append(".")


def main():
	# here is the main function to read web or local file in the terminal and count the number of lights
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
			lights.applyLights(cmd,x1,y1,x2,y2)

	count= lights.countLights()
	print("There are ",count," lights on.")


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
	# apply regex to the instructions
	N=int(buffer[0])
	instructions=[]
	for i in range(1,len(buffer)):
		regex = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
		newI = regex.match(buffer[i])
		instructions.append(newI)
	return N,instructions

class LightTester(object):
	"""Class for LightTester"""
	def __init__(self, N):
		self.lights = np.zeros((N,N)) #Preset all lights are off and assign the value = 0.
		self.size = N

	def applyLights(self,cmd,x1,y1,x2,y2):
		# Determine whether the coordinates are within the boundary and determine the valid coordinates.
		x1, x2 = min(x1, x2), max(x1, x2)
		y1, y2 = min(y1, y2), max(y1, y2)
		if x1>self.size or y1>self.size or x2<0 or y2<0:
			pass
		if x1<0:
			x1 = 0
		if x2>self.size:
			x2 = self.size
		if y1<0:
			y1 = 0
		if y2>self.size:
			y2 = self.size

		if cmd == "turn on":
			self.lights[x1:x2+1,y1:y2+1] = 1   # when lights turn on, Set the value equal to 1.
		elif cmd == "turn off":
			self.lights[x1:x2+1,y1:y2+1] = 0   # when lights turn off, Set the value equal to 0.
		elif cmd == "switch":
			self.lights[x1:x2+1,y1:y2+1] = self.lights[x1:x2+1,y1:y2+1] * -1 + 1
	
	def countLights(self):	
		count = np.count_nonzero(self.lights)
		return count


