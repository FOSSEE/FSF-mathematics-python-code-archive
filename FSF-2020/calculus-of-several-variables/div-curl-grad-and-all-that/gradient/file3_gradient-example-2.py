from manimlib.imports import *
import numpy as np


def function(coordinate):
	x,y = coordinate[:2]
	return np.array([
		x,
		y,
		x**2  - y**2
	])

class ThreeDVector_three(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=45*DEGREES,theta=85*DEGREES,distance=40)
		self.begin_ambient_camera_rotation(rate=0.5)

		surface = ParametricSurface(
			lambda x, y: np.array([
			x,
			y,
			x**2  - y**2
		]),u_min=-2,u_max=2, v_min=-1.5,v_max=1.5).set_color(BLUE_E).fade(0.7).scale(1.7)

		text_func = TexMobject(r"\textbf{Input: Function}").shift(4.4*LEFT+3.3*UP).scale(0.7)
		text_field = TexMobject(r"\textbf{Output: Vector Field}").shift(4.4*LEFT+3.3*UP).scale(0.7)
		
		self.add_fixed_in_frame_mobjects(text_func)
		self.play(ShowCreation(surface))
		self.wait(3)

		field = VectorField(function)
		self.play(FadeIn(field), FadeOut(text_func))
		self.add_fixed_in_frame_mobjects(text_field)
		self.wait()
		self.play(FadeOut(surface))
		self.wait(2)