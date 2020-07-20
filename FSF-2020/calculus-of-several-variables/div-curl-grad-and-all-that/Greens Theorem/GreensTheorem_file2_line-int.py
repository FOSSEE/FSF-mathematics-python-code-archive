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


		# all the text
		vec_f = TexMobject(r"\vec F",r" \textit{ is a vector field defined on the plane}").set_color("#EDF2EF")
		c = TexMobject(r"C",r" \textit{ is a curve on the plane, oriented counter-clockwise.}").set_color("#EDF2EF")
		dr = TexMobject(r"\vec dr", r"\textit{ gives the direction as we move along C}").set_color("#EDF2EF")

		intg = TexMobject(r"\oint \vec F \cdot \vec dr", r"\textit{ gives the rotation along the curve}").shift(2.5*DOWN).scale(0.7).set_color("#EDF2EF")
		text = VGroup(vec_f, c, dr).scale(0.6).set_stroke(width = 1.5)
		text.arrange(DOWN, buff = 0.2)
		text.shift(3.2*DOWN)

		vec_f[0].set_color("#D1D646")
		dr[0].set_color("#D1D646")
		intg[0].set_color("#D1D646")




		self.camera_frame.save_state()
		vec_f_sym = TexMobject(r"\vec F")
		c_sym = TexMobject(r"C").move_to(4.8*RIGHT+1.3*UP)
		dr_sym = TexMobject(r"\vec dr").next_to(vec_f_sym, DOWN, buff = SMALL_BUFF)
		dp_sym = TexMobject(r"\vec F \cdot \vec dr")
		intg_sym = TexMobject(r"\oint \vec F \cdot \vec dr")

		symbols = VGroup(vec_f_sym, dr_sym, dp_sym, intg_sym).shift(3*UP).set_color("#D1D646")




		vector_field = VectorField(field_func, x_min = -15, x_max = 15, y_min = -15, y_max = 15).fade(0.5)
		boundary = Ellipse(width = 9, height = 3).set_color("#32908F")
		b2 = Ellipse(width = 9, height = 3).set_color(WHITE)

		start_angle = self.get_pending(boundary, 0)

		pointer = Triangle(fill_opacity = 1).set_height(0.25).set_color(WHITE)
		pointer.set_fill(WHITE)
		pointer.move_to(boundary.get_start())
		pointer.rotate(- PI / 2)
		pointer.save_state()
		pointer.rotate(start_angle, about_point=pointer.get_center())
		dp_sym_1 = TexMobject(r"\vec F \cdot \vec dr").next_to(pointer, RIGHT, buff = SMALL_BUFF).scale(0.5).set_color("#D1D646").add_background_rectangle()
		intg_sym_1 = TexMobject(r"\oint \vec F \cdot \vec dr").next_to(pointer, RIGHT, buff = SMALL_BUFF).scale(0.5).set_color("#75485E").add_background_rectangle()
		dp = TexMobject(r"\vec F \cdot \vec dr \textit{ measures whether } \vec F \textit{ and } \vec dr", r" \textit{ are oriented the same way }").next_to(dp_sym_1, DOWN, buff = SMALL_BUFF).scale(0.3).set_color("#EDF2EF")
		dp[1].next_to(dp[0], DOWN, buff = SMALL_BUFF)


		# groups according to animation
		#one = VGroup( vec_f, vec_f_sym)
		#two = VGroup(boundary, c_sym)
		#three = VGroup(dr_sym, pointer)
		#four = VGroup(dp, dp_sym) #this is when to zoom in
		#five = VGroup(intg, intg_sym)

		delete = VGroup(vec_f, vec_f_sym, c, dr, dr_sym)


		self.play(ShowCreation(vec_f), ShowCreation(vec_f_sym))
		self.wait()
		self.play(ShowCreation(vector_field), Indicate(vec_f_sym))
		self.wait(2)
		self.play(ShowCreation(c))
		self.wait()
		self.play(ShowCreation(boundary), ShowCreation(c_sym), Indicate(c))
		self.wait(2)
		self.play(ShowCreation(dr))
		self.wait(2)
		self.play(ShowCreation(dr_sym), Indicate(dr), ShowCreation(pointer))

		self.play(FadeOut(delete))
		self.play(
			self.camera_frame.scale,.25,
			self.camera_frame.move_to,pointer
			)
		self.play(ShowCreation(dp_sym_1), ShowCreation(dp[0]), ShowCreation(dp[1]))
		self.add(dp_sym)
		self.wait(3)
		self.play(Restore(self.camera_frame))
		self.remove(dp[0], dp[1], dp_sym_1)
		self.wait()
		self.add(boundary, pointer, self.camera_frame)
		def update_rotate_move(mob,alpha):
			pointer.restore()

			angle = self.get_pending(boundary,alpha)

			pointer.move_to(boundary.point_from_proportion(alpha))
			pointer.rotate(angle, about_point=pointer.get_center())



		self.play(
			#self.camera_frame.scale,.25,
			UpdateFromAlphaFunc(pointer,update_rotate_move),
			run_time=3,
			)
		self.play(Write(b2))
		self.play(ReplacementTransform(dp_sym, intg_sym), ShowCreation(intg))
		self.play(ReplacementTransform(b2, intg_sym))
		self.play(Indicate(intg_sym))
		self.wait(2)

