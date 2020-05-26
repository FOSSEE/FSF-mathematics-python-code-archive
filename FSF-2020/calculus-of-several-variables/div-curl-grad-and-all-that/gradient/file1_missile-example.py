from manimlib.imports import *
import numpy as np


def function(coordinate):
	x,y = coordinate[:2]
	return np.array([
		np.sin(x-y),
		np.exp(y),
		0
	])
def func(coordinate):
	x,y = coordinate[:2]
	return np.array([
		-2*x,
		y,
		0])

class Missiles(GraphScene):
	def construct(self):

		field = VectorField(function)
		#path = ParametricFunction(lambda x: -2*x)

		dot = SVGMobject("miss").move_to(DL).scale(0.09).set_color(WHITE).rotate(PI/4 + PI)
		path = ArcBetweenPoints(dot.get_center(), UP+0.2*LEFT)

		self.play(FadeIn(field))
		self.wait()
		self.play(FadeIn(dot))
		self.wait()
		self.play(MoveAlongPath(dot, path))
		self.play(ApplyMethod(dot.rotate, PI/4), rate = 0.2)
		self.play(ApplyMethod(dot.move_to, 3.5*UP), rate = 0.3)
		#self.play(ApplyMethod(dot.move_to, 3.5*UP))
		#self.add_fixed_in_frame_mobjects(text_field)
		self.wait()