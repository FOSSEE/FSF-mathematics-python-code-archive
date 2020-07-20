from manimlib.imports import *

def field_func(coordinate):
	x,y = coordinate[:2]
	return np.array([
					-x, 
					-y,
					0
				])

def curl(coordinate):
	x,y = coordinate[:2]
	U = (x**2 + y**2)	
	return np.array([
			-y/(x**2 + y**2),
			x/(x**2 + y**2),
			0
	])


class LineIntegral(ZoomedScene, Scene):
	def setup(self):
		ZoomedScene.setup(self)
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
		CONFIG = {
			"zoom_factor": 0.3,
			"zoomed_display_height": 1,
			"zoomed_display_width": 6,
			"image_frame_stroke_width": 20,
			"zoomed_camera_config": {
				"default_frame_stroke_width": 3,
			},
		}


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
		surface_a = ParametricSurface(
			self.surface,
			u_min=-3,
			u_max=3,
			v_min=-3,
			v_max=3,
			fill_color=BLACK,
			checkerboard_colors=[BLACK, BLACK],
			stroke_color=BLUE_E,
			stroke_width = 1.5,
			resolution = [64,64]
		).set_fill(opacity=0.2).scale(1.5).set_stroke(width = 1.5)
		vector_field = VectorField(field_func)

		dot = Dot().scale(0.5).shift(0.49*LEFT+0.039*UP)
		dot_show = Dot().scale(0.05).move_to(dot.get_center())

		zoomed_camera = self.zoomed_camera
		zoomed_display = self.zoomed_display
		frame = zoomed_camera.frame
		zoomed_display_frame = zoomed_display.display_frame

		frame.move_to(dot)
		frame.scale(0.75)

		box = Square(fill_color= BLUE_E, fill_opacity = 0.8).scale(0.07).move_to(dot.get_center()).flip()

		label_box = TexMobject(r"D_i").scale(0.05).next_to(box, DOWN, buff = 0.05)

		label = TexMobject(r"x_i, y_i").scale(0.06).next_to(dot_show, DOWN, buff = 0.05)

		start_angle = self.get_pending(box, 0)

		pointer = Triangle(fill_opacity = 1).set_height(0.03).set_color(YELLOW_E)
		pointer.set_fill(YELLOW_E)
		pointer.move_to(box.get_start())
		pointer.rotate(- PI / 2)
		pointer.save_state()
		pointer.rotate(start_angle, about_point=pointer.get_center())


		flow = StreamLines(
		curl,
		virtual_time=2,
		min_magnitude=0,
		max_magnitude=1,
		dt = 0.1,
		x_min = -0.5, x_max = 0.5, y_min = -0.5, y_max = 0.5,
		    ).scale(0.05).move_to(dot.get_center())
		flow_1 = AnimatedStreamLines(
		flow,
		line_anim_class=ShowPassingFlashWithThinningStrokeWidth
		)


		# all the text
		text_zoomed = TexMobject(r"\oint_{C_{i}} \vec F \cdot \vec dr = (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}).", r" \mid D_{i} \mid").add_background_rectangle()
		text_gen_1 = TexMobject(r"\sum_{i = 1}^{n}\oint_{C_{i}} \vec F \cdot \vec dr = \sum_{i = 1}^{n} (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}). \mid D_{i} \mid").add_background_rectangle()
		text_gen_2 = TexMobject(r"\oint_{C} \vec F \cdot \vec dr = \sum_{i = 1}^{n} (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}. \mid D_{i} \mid")
		text_conclusion = TexMobject(r"\oint \vec F \cdot \vec dr = \int \int_D (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}) dA").add_background_rectangle()
		text_intuition = TexMobject(r"\oint_{C} \textit{Macroscopic curl } = \int \int_{D} \textit{Sum of microscopic curls }").add_background_rectangle()

		texts = VGroup(text_zoomed, text_gen_1, text_gen_2, text_conclusion, text_intuition).shift(2.8*DOWN).scale(0.8)

		self.add(vector_field, surface_a, dot_show, label)
		self.wait()
		self.activate_zooming(animate=True)
		self.wait(2)
		self.add(pointer)
		def update_rotate_move(mob,alpha):
			pointer.restore()

			angle = self.get_pending(box,alpha)

			pointer.move_to(box.point_from_proportion(alpha))
			pointer.rotate(angle, about_point=pointer.get_center())
		self.add(flow_1)
		self.play(ShowCreation(text_zoomed))
		#self.play(ReplacementTransform(box, text_zoomed[1]))
		#self.wait(2)
		self.play(
			UpdateFromAlphaFunc(pointer,update_rotate_move),
			run_time=3,
			)
		self.wait(3)
		#self.play(ReplacementTransform(text_zoomed, text_gen_1))
		#self.wait(2)
		#self.play(ReplacementTransform(text_gen_1, text_gen_2))

		self.play(
			self.get_zoomed_display_pop_out_animation(),
		# -------> Inverse
			rate_func=lambda t: smooth(1-t),
		)
		self.play(
			Uncreate(zoomed_display_frame),
			FadeOut(frame),
		)
		self.wait()
		self.remove(pointer, flow_1, label, dot_show, label_box)
		self.play(ReplacementTransform(text_zoomed, text_gen_1))
		self.wait(2)
		self.play(FadeIn(text_conclusion), FadeOut(text_gen_1))
		self.wait(2)
		self.play(FadeOut(text_conclusion), FadeIn(text_intuition))
		self.wait(2)








	@staticmethod
	def surface(t, v):
		return np.array([
		v*np.sin(t),
		np.cos(t),
		0
	])