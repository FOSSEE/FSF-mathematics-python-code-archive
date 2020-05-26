from manimlib.imports import *
import numpy as np

class Rules(ThreeDScene):

	def setup(self):
		ThreeDScene.setup(self)

	def construct(self):
		axes = ThreeDAxes()#.scale(0.8)#.shift(2*RIGHT, 2*DOWN)
		self.set_camera_orientation(phi=PI/3 + 10*DEGREES,theta=-PI/4 + 25*DEGREES,distance=60)

		plane = Polygon(np.array([4,4,0]), np.array([4, -4, 0]), np.array([-4, -4, 0]), np.array([-4, 4, 0]), color = BLACK, fill_color = YELLOW_E, fill_opacity = 0.3)

		path_one = Line(start = ORIGIN, end = np.array([3, 0, 0])).set_color(BLUE_E)
		path_one_text = TexMobject(r"\textrm{3 steps in the x direction}").shift(2*DOWN+3.5*LEFT).scale(0.5).set_color(BLUE_E)
		path_two_text = TexMobject(r"\textrm{2 steps in the y direction}").next_to(path_one_text, DOWN, buff = SMALL_BUFF).scale(0.5).set_color(GREEN_C)
		path_three_text = TexMobject(r"\textrm{2 steps in the z direction}").next_to(path_two_text, DOWN, buff = SMALL_BUFF).scale(0.5).set_color(PURPLE_E)
		obj = TextMobject("Objective: ", "Maximise points for a set number of steps").scale(0.8).to_edge(UP+LEFT)

		steps = TexMobject(r"\textrm{Total steps = 7}").to_edge(RIGHT, buff = LARGE_BUFF).set_color(YELLOW_E).scale(0.7).shift(1*UP)
		points_one = TexMobject(r"\textrm{Total points = 13}").next_to(steps, DOWN, buff = SMALL_BUFF).scale(0.7).set_color(YELLOW_E)
		question = TexMobject(r"\textrm{Change direction to score more points?}").shift(2*DOWN+2.5*RIGHT).scale(0.9)

		path_two = Line(start = np.array([3, 0, 0]), end = np.array([3, 2, 0])).set_color(GREEN_C)
		path_three = Line(start = np.array([3, 2, 0]), end = np.array([3, 2, 2])).set_color(PURPLE_E)
		total = Line(start = np.array([0, 0, 0]), end = np.array([3, 2, 2])).set_color(YELLOW_E)
		projection_total = Line(start = np.array([0, 0, 0]), end = np.array([3, 2, 0]))
		paths = VGroup(path_one, path_two, path_three, path_one_text, path_two_text, path_three_text)

		total_one = VGroup(total, projection_total)

		total_two = Line(start = np.array([0, 0, 0]), end = np.array([4, 1, 2])).set_color(YELLOW_E)
		projection_total_two = Line(start = np.array([0, 0, 0]), end = np.array([4, 1, 0])) 
		points_two = TexMobject(r"\textrm{Total points = 12}").next_to(steps, DOWN, buff = SMALL_BUFF).scale(0.7).set_color(YELLOW_E)

		total_three = Line(start = np.array([0, 0, 0]), end = np.array([1, 4, 2])).set_color(YELLOW_E)
		projection_total_three = Line(start = np.array([0, 0, 0]), end = np.array([1, 4, 0]))
		points_three = TexMobject(r"\textrm{Total points = 15}").next_to(steps, DOWN, buff = SMALL_BUFF).scale(0.7).set_color(YELLOW_E)

		everything = VGroup(axes, plane, path_one, path_two, path_three, total, projection_total, total_two, projection_total_two, total_three, projection_total_three)
		everything.scale(0.7).shift(2*LEFT+1*DOWN)
		self.add_fixed_in_frame_mobjects(obj)
		self.add(axes, plane)
		self.wait()
		self.add_fixed_in_frame_mobjects(path_one_text)
		self.play(ShowCreation(path_one))
		self.wait()
		self.add_fixed_in_frame_mobjects(path_two_text)
		self.play(ShowCreation(path_two))
		self.wait()
		self.add_fixed_in_frame_mobjects(path_three_text)
		self.play(ShowCreation(path_three))
		self.add_fixed_in_frame_mobjects(steps, points_one)
		self.wait()
		self.play(ShowCreation(total))
		self.play(ReplacementTransform(total.copy(), projection_total))
		self.wait()
		self.play(FadeOut(paths))
		self.add_fixed_in_frame_mobjects(question)
		self.wait()
		self.play(ReplacementTransform(total, total_two), ReplacementTransform(projection_total, projection_total_two))
		self.play(FadeOut(points_one))
		self.add_fixed_in_frame_mobjects(points_two)
		self.wait()
		self.play(ReplacementTransform(total_two, total_three), ReplacementTransform(projection_total_two, projection_total_three))
		self.play(FadeOut(points_two))
		self.add_fixed_in_frame_mobjects(points_three)
		self.wait()


