from manimlib.imports import *

def field_func(coordinate):
	x,y = coordinate[:2]
	return np.array([
					-x, 
					-y,
					0
				])


class LineIntegral(MovingCameraScene, Scene):
	def setup(self):
		MovingCameraScene.setup(self)
		Scene.setup(self)

	def get_pending(self,path,proportion,dx=0.01):
		if proportion < 1:
			coord_i = path.point_from_proportion(proportion)
			coord_f = path.point_from_proportion(proportion+dx)
		else:
			coord_i = path.point_from_proportion(proportion-dx)
			coord_f = path.point_from_proportion(proportion)
		line = Line(coord_i,coord_f)
		angle = line.get_angle()
		return angle

	def construct(self):
		axes_config = {"x_min": -6,
					"x_max": 6,
					"y_min": -6,
					"y_max": 6,
					"z_axis_config": {},
					"z_min": -1,
					"z_max": 1,
					"z_normal": DOWN,
					"light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
					"number_line_config": {
						"include_tip": False,
						},
					}

		axes = Axes(**axes_config)
		c_sym = TexMobject(r"C").move_to(4.8*RIGHT+1.3*UP)


		final_eq = TexMobject(r"\oint_{C} \vec F \cdot \vec dr", r" = \sum_{i = 1}^{n} \oint_{C_{i}} \vec F \cdot \vec dr ").shift(3*DOWN).set_color("#EDF2EF").scale(1.5)
		final_eq[0].set_color("#D1D646")
		
		text = TexMobject(r"\oint_{C} \vec F . dr",r" = \oint_{C_{1}} \vec F . dr ",r"+ \oint_{C_{2}} \vec F . dr",r" + \oint_{C_{3}} \vec F . dr + \oint_{C_{4}} \vec F . dr + ...", r" + \oint_{C_n} \vec F \cdot \vec dr ").shift(3*DOWN).set_color("#EDF2EF").scale(0.7)
		text[0].set_color("#D1D646")

		vector_field = VectorField(field_func, x_min = -15, x_max = 15, y_min = -15, y_max = 15).fade(0.5)
		boundary = Ellipse(width = 9, height = 3).set_color("#32908F")
		start_angle = self.get_pending(boundary, 0)

		pointer = Triangle(fill_opacity = 1).set_height(0.25).set_color(YELLOW_E)
		pointer.set_fill(YELLOW_E)
		pointer.move_to(boundary.get_start())
		pointer.rotate(- PI / 2)
		pointer.save_state()
		pointer.rotate(start_angle, about_point=pointer.get_center())

		split_1 = Line(boundary.get_center()+1.5*UP, boundary.get_center()+1.5*DOWN).set_color("#32908F")
		split_2 = Line(boundary.get_center()+4.5*LEFT, boundary.get_center()+4.5*RIGHT).set_color("#32908F")

		surface_3 = ParametricSurface(
			self.surface,
			u_min=-3,
			u_max=3,
			v_min=-3,
			v_max=3,
			fill_color=BLACK,
			checkerboard_colors=[BLACK, BLACK],
			stroke_color="#32908F",
			stroke_width = 1.5,
			resolution = [4,4]
		).set_fill(opacity=0.2).scale(1.5).set_stroke(width = 1.5)

		surface_4 = ParametricSurface(
			self.surface,
			u_min=-3,
			u_max=3,
			v_min=-3,
			v_max=3,
			fill_color=BLACK,
			checkerboard_colors=[BLACK, BLACK],
			stroke_color="#32908F",
			stroke_width = 1.5,
			resolution = [16,16]
		).set_fill(opacity=0.2).scale(1.5).set_stroke(width = 1.5)

		surface_5 = ParametricSurface(
			self.surface,
			u_min=-3,
			u_max=3,
			v_min=-3,
			v_max=3,
			fill_color=BLACK,
			checkerboard_colors=[BLACK, BLACK],
			stroke_color="#32908F",
			stroke_width = 1.5,
			resolution = [32,32]
		).set_fill(opacity=0.2).scale(1.5).set_stroke(width = 1.5)
		surface_6 = ParametricSurface(
			self.surface,
			u_min=-3,
			u_max=3,
			v_min=-3,
			v_max=3,
			fill_color=BLACK,
			checkerboard_colors=[BLACK, BLACK],
			stroke_color="#32908F",
			stroke_width = 1.5,
			resolution = [64,64]
		).set_fill(opacity=0.2).scale(1.5).set_stroke(width = 1.5)

		dot = Dot()
		dot_1 = Dot()
		dot_2 = Dot()


		pointer = Triangle(fill_opacity = 1).set_height(0.25).set_color("#75485E")
		pointer.set_fill("#75485E")
		pointer.move_to(boundary.get_start())
		pointer.rotate(- PI / 2)
		pointer.save_state()
		pointer.rotate(start_angle, about_point=pointer.get_center())

		pointer_b2 = Triangle(fill_opacity = 1).set_height(0.25).set_color(YELLOW_E)
		pointer_b2.set_fill(YELLOW_E)
		pointer_b2.move_to(boundary.get_start())
		pointer_b2.rotate(- PI / 2)
		pointer_b2.save_state()
		pointer_b2.rotate(start_angle, about_point=pointer_b2.get_center())


		# labels
		labels_1 = VGroup( TexMobject(r"C_{1}").move_to(np.array([0, 3, 0])),
							TexMobject(r"C_{2}").move_to(np.array([0, -3, 0]))).scale(0.7)
		labels_2 = VGroup( TexMobject(r"C_{1}").move_to(np.array([-2.25, 2.5, 0])),
							TexMobject(r"C_{2}").move_to(np.array([-2.25, -2.5, 0])),
							TexMobject(r"C_{3}").move_to(np.array([2.25, -2.5, 0])),
							TexMobject(r"C_{4}").move_to(np.array([2.25, 2.5, 0]))).scale(0.7)

		og = VGroup(boundary, split_1, split_2, labels_1, labels_2)


		self.add(vector_field, boundary, pointer, text[0], c_sym)
		def update_rotate_move(mob,alpha):
			pointer.restore()

			angle = self.get_pending(boundary,alpha)

			pointer.move_to(boundary.point_from_proportion(alpha))
			pointer.rotate(angle, about_point=pointer.get_center())

		self.play(
			UpdateFromAlphaFunc(pointer,update_rotate_move),
			run_time=3,
			)
		self.wait()
		self.play(Indicate(text[0]))
		self.wait(2)
		self.play(ShowCreation(text[1]), FadeIn(split_2), ShowCreation(text[2]), ShowCreation(labels_1), FadeOut(pointer), FadeOut(c_sym))
		self.play(Indicate(text[1]), Indicate(text[2]))
		self.wait(2)
		self.play(FadeIn(split_1), ShowCreation(text[3]), ReplacementTransform(labels_1, labels_2))
		self.play(Indicate(text[1]), Indicate(text[2]), Indicate(text[3]))
		self.wait(2)
		self.play(FadeOut(og), ShowCreation(surface_3))
		self.play(FadeOut(surface_3), ShowCreation(surface_4))
		self.play(FadeOut(surface_4), ShowCreation(surface_5))
		self.play(FadeOut(surface_5), ShowCreation(surface_6), ShowCreation(text[4]))
		self.wait(2)
		self.play(ReplacementTransform(text, final_eq))
		self.wait()
		self.play(Indicate(final_eq))
		self.wait()























	@staticmethod
	def surface(t, v):
		return np.array([
		v*np.sin(t),
		np.cos(t),
		0
	])


