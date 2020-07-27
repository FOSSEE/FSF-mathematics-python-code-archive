from manimlib.imports import *
import numpy as np

def curl(coordinate):
	x,y = coordinate[:2]
	return np.array([
			-y,
			x,
			0
	])


class Subtle(Scene):
	def construct(self):
		vf1 = VectorField(curl)
		pinwheel = SVGMobject("geo").move_to(np.array([2, 0, 0])).scale(0.3).set_stroke(width = 0.3).set_color_by_gradient(["#adf802",  YELLOW_C]).move_to(np.array([2.3, 0, 0]))
		self.add(pinwheel)

		label1 = TexMobject(r"\textit{Microscopic curl}").shift(3*DOWN).add_background_rectangle()
		label2 = TexMobject(r"\textit{Macroscopic curl}").shift(3*DOWN)

		ball1 = Dot(checkerboard_colors = [BLUE_E, PURPLE_E], resolution = [2,2], radius = 0.4).move_to(np.array([-1, -1, 0]))
		ball2 = Sphere(checkerboard_colors = [BLUE_E, TEAL], resolution = [16, 16], radius = 0.3).move_to(np.array([2, 0, 0]))
		circ = Circle(radius = 2)


		self.add(vf1)
		self.wait()
		self.play(ShowCreation(pinwheel))
		self.bring_to_front(pinwheel)
		self.play(Rotating(pinwheel), ShowCreation(label1))
		self.wait(2)
		#self.add(ball1)
		move_submobjects_along_vector_field(pinwheel, curl)
		self.play(FadeOut(label1), ShowCreation(label2))
		self.play(Indicate(label2))

		self.wait(5)




