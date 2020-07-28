from manimlib.imports import *
import numpy as np

def func(coordinate):
	x,y = coordinate[:2]
	return np.array([
		-2*x,
		-2*y,
		0
	])




class many_paths(GraphScene):
	CONFIG = {
			"x_min" : 0,
			"x_max" : 8.5,
			"x_axis_height": 8.5,
			"y_min" : 0,
			"y_max" : 8.5,
			"y_axis_height": 8.5,
			"graph_origin" : ORIGIN, 
			"function_color" : RED,
 
		} 
	def construct(self):
		self.setup_axes(animate=False)
		self.remove(self.x_axis, self.y_axis)
		background = VectorField(func,
			x_min = 0, x_max = 8.5, y_min = 0, y_max = 8.5, colors = ["#DBD8AE"]
			)
		
		pointer = Dot(np.array([0, 1.5, 0])).scale(0.7).set_color_by_gradient(["#84732B", YELLOW_E])
		start = np.array([0, 1.5, 0])
		end = np.array([7.53, 5.043, 0])
		path_one= self.get_graph(self.one, x_min = 0, x_max = 7.53)
		path_two= self.get_graph(self.two, x_min = 0, x_max = 7.53)
		path_three = self.get_graph(self.three, x_min = 0, x_max = 7.53)

		group = VGroup(path_one, path_two, background, path_three).move_to(np.array([-3,0, 0])).scale(0.75)


		
		path_one.set_color("#F6523C")
		path_two.set_color("#80475E")
		path_three.set_color("#0F7173")

		# all the text
		#function = TexMobject(r"f(x,y) = -(x^2 + y^2)").scale(0.6).set_color("#DBD8AE").shift(3.6*UP + 3*LEFT)
		field = TexMobject(r"\vec F = -2x\hat i - 2y\hat j").set_color("#DBD8AE").shift(3.6*DOWN + 3*LEFT)
		c1 = TexMobject(r"C_{1}: y = 6sin(\frac{x}{3} + 1.5)").scale(0.7).set_color("#0F7173").shift(3*UP + 4*RIGHT)
		#c3 = TexMobject(r"C_{3}: y = 6sin(\frac{x}{3} + 1.5)").scale(0.7).set_color("#0F7173").next_to(li_path2, DOWN, buff = LARGE_BUFF)
		li_path1 = TexMobject(r"\int_{C_{1}} \vec F \cdot \vec dr = ").set_color("#0F7173").next_to(c1, DOWN, buff = 0.2)
		c2 = TexMobject(r"C_{2}: y = 0.47x + 1.5").scale(0.7).set_color("#80475E").next_to(li_path1, DOWN, buff = 0.4)
		li_path2 = TexMobject(r"\int_{C_{2}} \vec F \cdot \vec dr = ").set_color("#80475E").next_to(c2, DOWN, buff = 0.2)
		c3 = TexMobject(r"C_{3}: y = \frac{x^{16}}{2}+ 1.5").scale(0.7).set_color("#F6523C").next_to(li_path2, DOWN, buff = 0.4)
		li_path3 = TexMobject(r"\int_{C_{3}} \vec F \cdot \vec dr = ").set_color("#F6523C").next_to(c3, DOWN, buff = 0.2)

		cs = VGroup(c1, c2, c3)


		c_1 = lambda x: c1_value.get_value()
		c_2 = lambda x: c2_value.get_value()
		c_3 = lambda x: c3_value.get_value()

		c1_value = ValueTracker(0)
		c2_value = ValueTracker(0)
		c3_value = ValueTracker(0)

		c1_tex = DecimalNumber(c1_value.get_value()).add_updater(lambda v: v.set_value(c1_value.get_value())).next_to(li_path1, RIGHT, buff = SMALL_BUFF).set_color("#0F7173")
		c2_tex = DecimalNumber(c2_value.get_value()).add_updater(lambda v: v.set_value(c2_value.get_value())).next_to(li_path2, RIGHT, buff = SMALL_BUFF).set_color("#80475E")
		c3_tex = DecimalNumber(c3_value.get_value()).add_updater(lambda v: v.set_value(c3_value.get_value())).next_to(li_path3, RIGHT, buff = SMALL_BUFF).set_color("#F6523C")


		paths = VGroup(li_path1, li_path2, li_path3, c1_tex, c2_tex, c3_tex)














		


		self.play(ShowCreation(field), ShowCreation(background))
		self.wait()
		self.play(ShowCreation(path_one), ShowCreation(path_two), ShowCreation(path_three), ShowCreation(cs))
		self.wait(2)
		self.add(c1_tex)
		self.play(ShowCreation(li_path1))
		self.play(MoveAlongPath(pointer, path_three), c1_value.set_value,-78.9,
			rate_func=linear,
			run_time=3
			)
		self.wait(2)
		self.play(ShowCreation(li_path2))
		self.add(c2_tex)
		self.play(MoveAlongPath(pointer, path_two), c2_value.set_value,-78.9,
			rate_func=linear,
			run_time=3
			)
		self.play(ShowCreation(li_path3))
		self.add(c3_tex)
		self.play(MoveAlongPath(pointer, path_one), c3_value.set_value,-78.9,
			rate_func=linear,
			run_time=3
			)
		self.wait()
		self.play(Indicate(paths))
		self.wait()
		#self.play(MoveAlongPath(pointer, path_three))
		#self.wait(2)

	def one(self,x):
		return x**2/16 + 1.5

	def three(self,x):
		return 6*np.sin(x/3) + 1.5

	def two(self,x):
		return 0.4705*x + 1.5

