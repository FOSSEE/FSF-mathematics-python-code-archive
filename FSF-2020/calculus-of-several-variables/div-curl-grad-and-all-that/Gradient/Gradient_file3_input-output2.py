from manimlib.imports import *
import numpy as np


def function(coordinate):
	x,y = coordinate[:2]
	return np.array([
		0.4*(-x*np.sin((x**2+y**2)))/1*(x**2 + y**2),
		0.4*(-y*np.sin((x**2+y**2)))/1*(x**2 + y**2),
		0,
	])


def function_two(coordinate):
	x,y = coordinate[:2]
	return np.array([
		6*x*y/(x**2+y**2+1)**2,
		-3*(x**2 -y**2 +1)/(x**2+y**2+1)**2,
		0,
	])

def function_three(coordinate):
	x,y = coordinate[:2]
	return np.array([
		np.exp(x)*np.cos(y),
		-np.exp(x)*np.sin(y),
		0,
	])


class Second(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=45*DEGREES,theta=60*DEGREES,distance=40)
		self.begin_ambient_camera_rotation(rate=0.05)

		surface = ParametricSurface(
			lambda u, v: np.array([
				0.4*u,
				0.4*v,
				0.4*np.cos(np.sqrt((u**2)+(v**2)))
			]),u_min=-10,u_max=10, v_min=-10,v_max=10, checkerboard_colors = (["#1C6E8C", "#1C6E8C"]), stroke_color = "#1C6E8C").fade(0.7)

		text_func = TexMobject(r"\textbf{Input: Function}").shift(4.4*LEFT+3.3*UP).scale(0.7).set_stroke(width = 1.2)
		text_field = TexMobject(r"\textbf{Output: Vector Field}").shift(4.4*LEFT+3.3*UP).scale(0.7).set_stroke(width = 1.2)
		field = VectorField(function, x_min = -4, x_max = 4, y_min = -4, y_max = 4, colors = (["#CC2936", "#4D8B31","#FFAD05"]))
		
		
		self.add_fixed_in_frame_mobjects(text_func)
		self.play(ShowCreation(surface))
		self.wait(3)
		self.stop_ambient_camera_rotation()
		self.move_camera(phi=0*DEGREES, theta=0*DEGREES)

		self.play(FadeIn(field),FadeOut(text_func))
		self.add_fixed_in_frame_mobjects(text_field)
		self.wait()
		self.play(FadeOut(surface), FadeOut(axes))
		self.wait()


class Third(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=45*DEGREES,theta=60*DEGREES,distance=40)
		self.begin_ambient_camera_rotation(rate=0.2)




		surface_two = ParametricSurface(
			lambda x, y: np.array([
			x,
			y,
			-3*y/(x**2+y**2+1)
		]),u_min=-2,u_max=2, v_min=-2,v_max=2).set_color(BLUE_E).fade(0.7).scale(1.7)

		text_func = TexMobject(r"f = \frac{-3y}{x^{2} + y^{2} +1}").shift(4.8*LEFT+3*UP).scale(0.7)
		text_field = TexMobject(r"\nabla", r"f = \begin{bmatrix}\frac{\partial f}{\partial x}\\\frac{\partial f}{\partial y}\end{bmatrix}").shift(4.8*LEFT+3*UP).scale(0.7)
		text_field_a = TexMobject(r"\nabla", r" f = \begin{bmatrix} \frac{6xy}{(x^{2} + y^{2} + 1)^{2}}\\-3\frac{x^{2} - y^{2} + 1}{(x^{2} + y^{2} + 1)^{2}}\end{bmatrix}").shift(4.8*LEFT+3*UP).scale(0.7)

		field_two = VectorField(function_two, x_min = -3, x_max = 3, y_min = -3, y_max = 3, colors = (["#CC2936", "#4D8B31","#FFAD05"]))
		text_field[0].set_color("#CC2936")
		text_field_a[0].set_color("#CC2936")



		self.add_fixed_in_frame_mobjects(text_func)
		self.play(ShowCreation(surface_two))
		self.wait(3)
		self.stop_ambient_camera_rotation()
		self.move_camera(phi=0*DEGREES, theta=0*DEGREES)

		self.play(FadeIn(field_two),FadeOut(text_func))
		self.add_fixed_in_frame_mobjects(text_field)
		self.wait()
		self.play(FadeOut(surface_two))
		self.wait()



class Fourth(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=45*DEGREES,theta=60*DEGREES,distance=100)
		self.begin_ambient_camera_rotation(rate=0.2)

		surface = ParametricSurface(
			lambda u, v: np.array([
				u,
				v,
				np.exp(u)*np.cos(v)
			]),u_min=-3,u_max=3, v_min=-3,v_max=3).set_color(BLUE_E).fade(0.7)

		text_func = TexMobject(r"\textbf{Input: Function}").shift(4.4*LEFT+3.3*UP).scale(0.7)
		text_field = TexMobject(r"\textbf{Output: Vector Field}").shift(4.4*LEFT+3.3*UP).scale(0.7)
		field = VectorField(function_three, x_min = -3, x_max = 3, y_min = -3, y_max = 3)
		
		
		self.add_fixed_in_frame_mobjects(text_func)
		self.play(ShowCreation(surface))
		self.wait(3)

		self.stop_ambient_camera_rotation()
		self.move_camera(phi=0*DEGREES, theta=0*DEGREES)

		self.play(FadeIn(field),FadeOut(text_func))
		self.add_fixed_in_frame_mobjects(text_field)
		self.wait()
		self.add_fixed_in_frame_mobjects(text_field_a)
		self.play(ReplacementTransform(text_field, text_field_a))
		self.play(FadeOut(surface))
		self.wait()