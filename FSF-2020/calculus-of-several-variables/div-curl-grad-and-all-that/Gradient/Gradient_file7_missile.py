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

		toggle = Rectangle(width = 7, height = 0.5, fill_color = [BLUE_E, '#BCD2FF', '#FFD5B3', '#FF9225', '#FF6C00'], fill_opacity = 1).rotate(90*DEGREES).shift(6*RIGHT).set_stroke(width = 0.2)
		guide = Triangle(color = WHITE, fill_color = WHITE, fill_opacity = 1).scale(0.3).rotate(90*DEGREES).move_to(toggle.get_center(), RIGHT+DOWN).shift(0.6*RIGHT + 3*DOWN)
		#self.add(toggle, guide)
		path_guide_one = Line(np.array([6.4, -3, 0]), np.array([6.4, 1, 0]))
		path_guide_two = Line(np.array([6.4, 1, 0]), np.array([6.4, 3, 0]))
		label = TexMobject(r"\textit{temperature in }",r"\textrm{ K}").next_to(toggle, DOWN).scale(0.5).shift(0.2*UP)

		self.play(FadeIn(field))
		self.wait()
		self.bring_to_front(toggle, guide, label)
		self.play(FadeIn(dot))
		self.wait()
		self.play(MoveAlongPath(dot, path), MoveAlongPath(guide, path_guide_one))
		self.play(ApplyMethod(dot.rotate, PI/4),rate = 0.1)
		self.play(ApplyMethod(dot.move_to, 3.5*UP), MoveAlongPath(guide, path_guide_two), rate = 0.3)
		#self.play(ApplyMethod(dot.move_to, 3.5*UP))
		#self.add_fixed_in_frame_mobjects(text_field)
		self.wait()