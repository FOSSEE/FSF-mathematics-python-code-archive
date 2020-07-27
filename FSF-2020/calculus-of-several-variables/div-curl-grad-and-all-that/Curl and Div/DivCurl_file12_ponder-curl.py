from manimlib.imports import *
import numpy as np

def curl(coordinate):
	x,y = coordinate[:2]
	return np.array([
			y,
			0,
			0
	])

class Ponder_curl(Scene):
	def construct(self):
		vf = VectorField(curl)
		self.add(vf)
		self.wait()

