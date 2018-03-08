import urllib.request
import os
import re
from led_tester import class_lights
import pytest
import sys
sys.path.append(".")

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

def mainFunction(filename,N):
	lights = class_lights.LightTester(N)
	N,instructions = readFile(filename)
	for i in instructions:
		cmd = i[1]
		x1 = int(i[2])
		y1 = int(i[3])
		x2 = int(i[4])
		y2 = int(i[5])
		lights.applyLights(cmd,x1,x2,y1,y2)
	return (lights.countLights())






