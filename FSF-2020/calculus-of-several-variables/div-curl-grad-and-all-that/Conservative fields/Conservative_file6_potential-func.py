from manimlib.imports import *

def field_func(coordinate):
	x,y = coordinate[:2]
	return np.array([
					np.cos(x), 
					np.cos(y),
					0
				])

class Potential(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		self.add(axes)
		self.set_camera_orientation(phi=0*DEGREES,theta=0*DEGREES,distance=40)
		vec_field = VectorField(field_func, x_min =-3, x_max = 3, y_min =-3, y_max =3)
		surf = ParametricSurface(lambda u,v: np.array([u,v,
														np.sin(u) + np.sin(v)]),
														u_min = -3, u_max = 3, v_min = -3, v_max = 3, stroke_color = PURPLE_E, checkerboard_colors = [PURPLE_E, PURPLE_E]).fade(0.5)

		#text 
		vec = TexMobject(r"\vec F = \cos x \hat i + \cos y \hat j ").set_color(YELLOW_C).shift(3.8*UP+3.6*RIGHT).scale(0.7)
		func = TexMobject(r"\textit{has a potential function }", r"f(x,y) = \sin x + \sin y").scale(0.7).next_to(vec, DOWN, buff = 0.2)
		func[1].set_color(PURPLE_E)	

		self.play(ShowCreation(vec_field))
		self.add_fixed_in_frame_mobjects(vec)
		self.wait()
		self.play(FadeIn(surf))
		self.begin_ambient_camera_rotation()
		self.move_camera(phi=45*DEGREES,theta=60*DEGREES)
		self.add_fixed_in_frame_mobjects(func)
		self.wait(2)
