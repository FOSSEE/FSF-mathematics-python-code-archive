from manimlib.imports import *
import numpy as np


def function(coordinate):
	x,y = coordinate[:2]
	return np.array([
		x,
		y,
		1/np.cos(x*y),
	])

class ThreeDVector(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=45*DEGREES,theta=45*DEGREES,distance=40)
		self.begin_ambient_camera_rotation(rate=0.5)

		surface = ParametricSurface(
			lambda x, y: np.array([
			x,
			y,
			1/np.cos(x*y),
		]),u_min=-1.15,u_max=1.15, v_min=-1.15,v_max=1.15).set_color(BLUE_E).fade(0.7).scale(1.4)

		text_func = TexMobject(r"\textbf{Input: Function}").shift(4.4*LEFT+3.3*UP).scale(0.3)
		text_field = TexMobject(r"\textbf{Output: Vector Field}").shift(4.4*LEFT+3.3*UP).scale(0.7)
		
		self.add_fixed_in_frame_mobjects(text_func)
		self.play(ShowCreation(surface))
		self.wait(2)

		field = VectorField(function).scale(0.7)
		self.play(FadeIn(field), FadeOut(text_func))
		self.add_fixed_in_frame_mobjects(text_field)
		self.wait()

		self.play(FadeOut(surface))
		self.wait(2)
