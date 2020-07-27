from manimlib.imports import *
import numpy as np


def function(coordinate):
	x,y = coordinate[:2]
	return np.array([
		x,
		y,
		0,
	])
def x_dir(coordinate):
	x,y = coordinate[:2]
	return np.array([
		x,
		0,
		0
	])

def y_dir(coordinate):
	x,y = coordinate[:2]
	return np.array([
		0,
		y,
		0,
	])


class PartialDerivatives(MovingCameraScene):
	def setup(self):
		MovingCameraScene.setup(self)
	
	def construct(self):
		dot = Dot().move_to(np.array([2.5,2,0]))

		self.camera_frame.save_state()
		self.play(
			self.camera_frame.set_width,dot.get_width()*35,
			self.camera_frame.move_to,dot)

		dx = TexMobject(r"\frac{\partial f}{\partial x}").move_to(np.array([4,2.5, 0])).set_color(["#00635D", BLUE_E]).scale(0.5)
		x_aros = VectorField(x_dir, x_min = 0.5, x_max = 3, y_min = 0.5, y_max =3).set_color(["#00635D", BLUE_E])

		dy = TexMobject(r"\frac{\partial f}{\partial y}").move_to(np.array([4,1.5, 0])).set_color_by_gradient(["#BAAB68", WHITE]).scale(0.5)
		y_aros = VectorField(y_dir, y_min = 0.5, y_max =3, x_min = 0.5, x_max = 3 ).set_color_by_gradient(["#BAAB68", WHITE])

		partials = VGroup(x_aros, y_aros, dx, dy)

		dxdy = VectorField(function, y_min = 0.5, y_max =3, x_min = 0.5, x_max = 3 ).set_color_by_gradient(["#BAAB68", "#00635D"])
		field = VectorField(function, y_min = -3, y_max =3, x_min = -3, x_max = 3 ).set_color_by_gradient(["#BAAB68", "#00635D"])
		vector = TexMobject(r"\nabla f =").set_color_by_gradient(["#BAAB68", "#00635D"]).move_to(np.array([4,2, 0])).scale(0.5)
		threed = TexMobject(r"\textit{With respect to the function, the gradient is computed by...}").scale(0.3).move_to(dot.get_center())



		self.play(Write(x_aros), Write(dx))
		self.wait()
		self.play(Write(y_aros), Write(dy))
		self.wait()
		self.play(Write(dxdy), Write(vector), ApplyMethod(dx.next_to,vector, RIGHT+0.3*UP), ApplyMethod(dy.next_to, vector, RIGHT+0.3*DOWN))
		self.wait()
		self.play(FadeOut(x_aros), FadeOut(dx), FadeOut(vector), FadeOut(dxdy), FadeOut(y_aros), FadeOut(dy), ShowCreation(threed))
		self.wait(2)
		self.play(Uncreate(threed))


