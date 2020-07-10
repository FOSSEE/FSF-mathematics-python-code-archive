from manimlib.imports import *
class limit1(GraphScene,MovingCameraScene):
	def setup(self):
		GraphScene.setup(self)
		MovingCameraScene.setup(self)
	CONFIG = {
        "y_max" : 1,
        "y_min" : 0,
        "x_max" : 1,
        "x_min" : -1,
        "y_tick_frequency" : 0.2, 
        "x_tick_frequency" : 0.2, 
        "axes_color" : WHITE, 
        "num_graph_anchor_points": 3000, #this is the number of points that graph manim
        "graph_origin" : ORIGIN+3*DOWN,
        "x_labeled_nums": list(range(-1,2)),
        "y_labeled_nums": list(range(0,2)),
        "x_axis_label":"$x$",
        "y_axis_label":"$f(x)$",
        "x_axis_width": 10,
        "y_axis_height": 5,
    }
	def construct(self):
		XTD = self.x_axis_width/(self.x_max - self.x_min)
		YTD = self.y_axis_height/(self.y_max - self.y_min)

		dot1 = SmallDot(np.array([0.025,-2.975,0]))
		dot2 = SmallDot(np.array([-0.025,-2.975,0]))
		sqr = Square(side_length = 15.0).move_to(np.array([0,-3,0]))
		brline1 = DashedVMobject(Line(np.array([0.15,-3,0]), np.array([0.15,-2.85,0])))
		brline2 = DashedVMobject(Line(np.array([0.025,-3,0]), np.array([0.025,-2.975,0])))
		brline3 = DashedVMobject(Line(np.array([-0.15,-3,0]), np.array([-0.15,-2.85,0])))
		brline4 = DashedVMobject(Line(np.array([-0.025,-3,0]), np.array([-0.025,-2.975,0])))
		textdef = TextMobject("")
		text003 = TextMobject("0.03").move_to(np.array([0.15,-3.05,0])).scale(0.1)
		textazero1 = TexMobject(r"\approx 0").move_to(np.array([0.04,-3.05,0])).scale(0.1)
		textazero2 = TexMobject(r"\approx 0").move_to(np.array([-0.04,-3.05,0])).scale(0.1)
		textm003 = TextMobject("-0.03").move_to(np.array([-0.15,-3.05,0])).scale(0.1)
		text2 = TextMobject("Let f(x) = |x|. We'll check neighbourhood of origin") 
		text3 = TextMobject("h has to be a very small number greater than 0").move_to(np.array([0,-3.3,0])).scale(0.2)
		text4 = TextMobject("The point travels through range of neighbourhood").move_to(np.array([0,-3.3,0])).scale(0.19)
		text5 = TextMobject("let h be equal to 0.03").move_to(np.array([0,-3.3,0])).scale(0.25)
		text6 = TextMobject("Notice how the point never touches the origin").move_to(np.array([0,-3.3,0])).scale(0.2)
		text7 = TextMobject("Green line shows the Right hand neighbourhood of origin").move_to(np.array([0,-3.3,0])).scale(0.17)
		text8 = TextMobject("The point is approaching (0,0) for the values of x which are positive").move_to(np.array([0,-3.3,0])).scale(0.1)
		text9 = TextMobject("Values of x are tending to 0 from positive side").move_to(np.array([0,-3.3,0])).scale(0.19)
		text10 = TexMobject(r"\text {Notation for this is }",r"x\rightarrow { 0 }^{ + }").move_to(np.array([0,-3.3,0])).scale(0.25)
		text11 = TextMobject("Similar case can be made for negative values of x").move_to(np.array([0,-3.3,0])).scale(0.19)
		text12 = TextMobject("The point is approaching (0,0) for the values of x which are negative").move_to(np.array([0,-3.3,0])).scale(0.1)
		text13 = TextMobject("Values of x are tending to 0 from negative side").move_to(np.array([0,-3.3,0])).scale(0.19)
		text14 = TexMobject(r"\text {Notation for this is }",r"x\rightarrow { 0 }^{ - }").move_to(np.array([0,-3.3,0])).scale(0.25)


		self.play(FadeIn(text2), run_time = 1.5)
		self.wait(2.5)
		self.setup_axes()
		graph_1 = self.get_graph(lambda x : x, color = RED, x_min = 0, x_max = 1)
		graph_2 = self.get_graph(lambda x : -x, color = RED, x_min = 0, x_max = -1)
		graph_3 = self.get_graph(lambda x : x,color = RED, x_min = 0.005, x_max = 0.03)
		graph_4 = self.get_graph(lambda x : x,color = GREEN_SCREEN, x_min = 0.03, x_max = 0.005)
		graph_5 = self.get_graph(lambda x : -x,color = GREEN_SCREEN, x_min = -0.03, x_max = -0.005)
		grp1 = VGroup(graph_1,graph_2)
		grp2 = VGroup(brline2, textazero1)
		grp3 = VGroup(textazero2, textm003, brline3, brline4)
		self.play(ShowCreation(grp1))
		self.add(sqr)
		self.play(ReplacementTransform(text2, text3))
		self.camera_frame.save_state()
		self.play(self.camera_frame.set_width,2.25,self.camera_frame.move_to,sqr,run_time = 2)
		self.wait(2.5)
		self.play(ReplacementTransform(text3, text4), ShowCreation(dot1))
		self.wait(2.5)
		self.play(ReplacementTransform(text4, text5), ShowCreation(brline1), ShowCreation(text003))
		self.wait(2.5)
		for i in range(0,3):
			self.play(MoveAlongPath(dot1,graph_3), run_time = 0.5)
			self.play(MoveAlongPath(dot1,graph_4), run_time = 0.5)
		self.play(ReplacementTransform(text5, text6), ShowCreation(grp2))
		self.wait(2)
		self.play(FadeOut(dot1))
		self.add(graph_4)
		self.play(ReplacementTransform(text6, text7))
		self.wait(2.5)
		self.play(ReplacementTransform(text7,text8))
		for i in range(0,3):
			self.play(MoveAlongPath(dot1,graph_4), run_time = 0.7)
		self.play(ReplacementTransform(text8, text9))
		self.wait(2.5)
		self.play(ReplacementTransform(text9, text10))
		self.wait(2.5)
		self.play(ShowCreation(grp3), ReplacementTransform(text10, text11), FadeOut(dot1))
		self.add(graph_5)
		for i in range(0,3):
			self.play(MoveAlongPath(dot2, graph_5), run_time = 0.7)
		self.play(ReplacementTransform(text11, text12))
		self.wait(2.5)
		self.play(ReplacementTransform(text12, text13))
		self.wait(2.5)
		self.play(ReplacementTransform(text13, text14))
		self.wait(2)
		self.play(FadeOut(dot2), ReplacementTransform(text14, textdef))
		self.wait(2)
		self.play(Restore(self.camera_frame))

		self.wait(2.5)
