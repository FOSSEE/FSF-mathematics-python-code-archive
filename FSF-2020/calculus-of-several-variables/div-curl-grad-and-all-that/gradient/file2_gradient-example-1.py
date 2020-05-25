from manimlib.imports import *
import numpy as np


def function(coordinate):
	x,y = coordinate[:2]
	return np.array([
		0.4*x,
		0.4*y,
		0.4*np.cos(np.sqrt((x**2)+(y**2))
	)])

class ThreeDVector(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=45*DEGREES,theta=60*DEGREES,distance=40)
		self.begin_ambient_camera_rotation(rate=0.5)

		surface = ParametricSurface(
			lambda u, v: np.array([
				0.4*u,
				0.4*v,
				0.4*np.cos(np.sqrt((u**2)+(v**2)))
			]),u_min=-20,u_max=20, v_min=-10,v_max=10).set_color(BLUE_E).fade(0.7)

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
		self.wait()



