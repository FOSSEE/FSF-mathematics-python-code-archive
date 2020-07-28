from manimlib.imports import *
import numpy as np

class routes(ThreeDScene):
	def construct(self):

		axes = ThreeDAxes()
		self.begin_ambient_camera_rotation(rate=0.08)
		self.set_camera_orientation(phi=45 * DEGREES,theta=-65*DEGREES, distance = 45)
		function = ParametricFunction(
            lambda t: np.array([
            1.5*np.cos(t),
            1.5*np.sin(t),
            t/4
            ]), t_min = 0, t_max =3*PI).set_color("#0EB1D2")
	

		line = Line(np.array([1.5, 0, 0]), np.array([-1.5, 0, 2.35619])).set_color("#F8F32B")

		dot1 = Sphere(radius = 0.1).move_to(np.array([1.5,0,0])).set_color("#74226C")
		dot2 = Sphere(radius = 0.1).move_to(np.array([1.5,0,0])).set_color("#74226C")

		label1 = TexMobject(r"A").move_to(np.array([1.5,0,0])).set_color("#FCF7F8")
		label2 = TexMobject(r"B").move_to(np.array([-1.5,0,2.42])).set_color("#FCF7F8")

		title = TexMobject(r"\textit{Work done}",r"\textit{ against gravity is the}", r"\textit{ same for both paths}").set_color("#F1E3F3").move_to(np.array([0,-3,0]))
		title[1].set_color("#F8F32B")

		self.add(axes)
		self.wait()
		self.play(ShowCreation(function), ShowCreation(line), run_time = 2)
		self.wait()
		self.play(MoveAlongPath(dot1, function), run_time = 2)
		self.wait()
		self.play(MoveAlongPath(dot2, line), run_time = 1.2)
		self.wait()
		self.add_fixed_in_frame_mobjects(title)
		self.play(Write(title))
		self.wait()


