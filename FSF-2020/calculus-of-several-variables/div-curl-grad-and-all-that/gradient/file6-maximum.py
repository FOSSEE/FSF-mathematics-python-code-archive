from manimlib.imports import *
import numpy as np


def function(coordinate):
	x,y = coordinate[:2]
	return np.array([
		x,
		y,
		2 - x**2 - y**2
	])

class ThreeDVector_one(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=75*DEGREES,theta=45*DEGREES,distance=40)
		self.begin_ambient_camera_rotation(rate=0.5)

		surface = ParametricSurface(
			lambda x, y: np.array([
			x,
			y,
			2 - x**2 - y**2
		]),u_min=-2,u_max=2, v_min=-2,v_max=2).set_color(RED_E).fade(0.7)

		probe = Sphere(radius = 0.2).set_color(PURPLE_E)
		probe_one = Sphere(radius = 0.1).set_color(PURPLE_E).move_to(np.array([0,0,2.1]))
		text_one_b = TexMobject(r" \textrm{ reads 0 at local maximum }").next_to(probe, RIGHT, buff = SMALL_BUFF)
		name = TextMobject("PROBE2.0 ").next_to(probe, DOWN, buff = SMALL_BUFF).scale(0.5)
		text = VGroup(probe, text_one_b, name).to_edge(1.5*UP+0.5*LEFT).scale(0.5) 
		

		self.play(ShowCreation(surface))
		self.add(probe_one)
		field = VectorField(function).scale(0.8)
		self.play(FadeIn(field))
		self.add_fixed_in_frame_mobjects(text)
		self.wait(3)
