from manimlib.imports import *
import numpy as np
# granny smith apple
#misty moss

class Analogue(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes().set_color("#EBF2FA")

		hills_2D = ParametricFunction(
		lambda t: np.array([
		0,
		t,
		-((1/1.02)*t**2)
		]),t_min= -2.5,t_max=2.5).set_color("#679436")

		hills_2D_a = ParametricFunction(
		lambda t: np.array([
		0,
		t,
		-((1/1.02)*t**2)
		]),t_min= 0,t_max=2.5).set_color("#679436")


		hills_3D = ParametricSurface(
		lambda u, v: np.array([
		u,
		v,
		-(u**2 + v**2)
		]),u_min=-2.5,u_max=2.5, v_min=-2.5,v_max=2.5, checkerboard_colors = ["#679436", "#679436"], stroke_color = "#679436").fade(0.7)

		hills_2D_b = ParametricFunction(
		lambda t: np.array([
		t,
		0,
		-((1/1.02)*t**2)
		]),t_min= 0,t_max=2.5).set_color("#FFCAB1")


		hills = VGroup(hills_2D_a, hills_3D, hills_2D_b, hills_2D).move_to(np.array([0,0,-3.8]))
		ball = Sphere(radius = 0.08).set_color("#28666E")


		path_one = DashedVMobject(hills_2D_a).set_stroke(width = 0.9).set_color("#F0C808")
		path_two = DashedVMobject(hills_2D_b).set_stroke(width = 0.9).set_color("#F0C808")

		text_a = TexMobject(r"\textit{In the case of a one dimensional hill, }" ,r"\textit{the ball moves along a single path}").set_color("#EBF2FA").scale(0.5).move_to(np.array([-1.5, 2.7, 0]))
		text_b = TexMobject(r"\textit{In higher dimensions,}", r"\textit{ there is more than one direction}", r"\textit{the ball can roll in}").set_color("#EBF2FA").scale(0.5).move_to(np.array([-1.5, 2.6, 0]))
		text_a[1].next_to(text_a[0], DOWN, buff = SMALL_BUFF)
		text_b[1].next_to(text_b[0], DOWN, buff = SMALL_BUFF)
		text_b[2].next_to(text_b[1], DOWN, buff = SMALL_BUFF)
		text_b[0].set_color("#28666E")











		self.set_camera_orientation(phi=90*DEGREES,theta=180*DEGREES,distance=40)
		self.add(axes)
		self.add_fixed_in_frame_mobjects(text_a)
		self.play(ShowCreation(hills_2D), ShowCreation(text_a))
		self.play(MoveAlongPath(ball,hills_2D_a),run_time = 2.5)
		self.wait()
		self.play(FadeIn(hills_3D), FadeOut(hills_2D), FadeOut(text_a))
		self.move_camera(phi=45*DEGREES,theta=45*DEGREES)
		self.add_fixed_in_frame_mobjects(text_b)
		self.begin_ambient_camera_rotation(rate=0.05)
		self.play(MoveAlongPath(ball, hills_2D_a), ShowCreation(path_one), run_time = 2.5)
		self.wait()
		self.play(FadeOut(path_one), MoveAlongPath(ball, hills_2D_b), ShowCreation(path_two), run_time = 2.5)
		self.wait()