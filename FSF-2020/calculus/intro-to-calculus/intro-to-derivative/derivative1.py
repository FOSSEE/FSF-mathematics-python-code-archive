from manimlib.imports import *
class derivative1(GraphScene, Scene):
	def setup(self):
		GraphScene.setup(self)
	CONFIG = {
        "y_max" : 4,
        "y_min" : -2,
        "x_max" : 4,
        "x_min" : -2,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : WHITE, 
        "num_graph_anchor_points": 3000, #this is the number of points that graph manim
        "graph_origin" : ORIGIN+2*DOWN+4*LEFT,
        "x_labeled_nums": list(range(-2,5)),
        "y_labeled_nums": list(range(-2,5)),
        "x_axis_label":"$x$",
        "y_axis_label":r"$f(x)=y= 3-\frac { 3 }{ 2 } x$",
        "x_axis_width": 5,
        "y_axis_height": 5,
    }
	def construct(self):
		#XTD = self.x_axis_width/(self.x_max - self.x_min)
		#YTD = self.y_axis_height/(self.y_max - self.y_min)

		text1 = TextMobject("")
		text2 = TexMobject("{y}_{2}-{y}_{1}")
		text2 = TexMobject("{x}_{2}-{x}_{1}")
		text3 = TexMobject(r"m\quad =\frac { { y }_{ 2 }-{ y }_{ 1 } }{ { x }_{ 2 }-{ x }_{ 1 } }").move_to(np.array([3,0,0]))
		text4 = TexMobject(r"m\quad =\frac { 3 }{ -2 }").move_to(np.array([3,0,0]))
		text5 = TexMobject(r"m\quad =\quad -1.5").move_to(np.array([3,0,0]))
		self.setup_axes()
		graph_1 = self.get_graph(lambda x : 3-1.5*x, color = GREEN_SCREEN, x_min = -1, x_max = 3)
		graph_2 = self.get_graph(lambda x : 3.1-1.5*x, color = ORANGE, x_min = 0, x_max = 2)
		dot1 = Dot()
		dot2 = SmallDot(self.graph_origin+1.7*RIGHT, color = PINK)
		dot3 = SmallDot(self.graph_origin+2.5*UP, color = RED_B)
		vec1 = Vector(2.5*DOWN, color = PINK).shift(self.graph_origin+2.5*UP)
		vec2 = Vector(1.7*RIGHT, color = RED_B).shift(self.graph_origin)
		brace1 = Brace(vec1, LEFT)
		brace2 = Brace(vec2, DOWN)
		br1text = brace1.get_text(r"${y}_{2}-{y}_{1}$").next_to(brace1, LEFT)
		br2text = brace2.get_text(r"${x}_{2}-{x}_{1}$").next_to(brace2, DOWN) 
		self.play(ShowCreation(graph_1), ShowCreation(dot2), ShowCreation(dot3))
		self.play(MoveAlongPath(dot1, graph_2), ShowCreation(vec1), ShowCreation(vec2), run_time = 3)
		self.wait(1)
		self.play(ShowCreation(brace1), ShowCreation(brace2))
		self.play(ShowCreation(br1text), ShowCreation(br2text))
		self.wait(2)
		self.play(GrowFromCenter(text3))
		self.wait(2.5)
		self.play(ReplacementTransform(text3, text4))
		self.wait(2)
		self.play(ReplacementTransform(text4, text5))
		self.wait(2)
