import numpy as np


class LightTester(object):
	"""main program for LightTester"""
	def __init__(self, N):
		self.lights = np.zeros((N,N))

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