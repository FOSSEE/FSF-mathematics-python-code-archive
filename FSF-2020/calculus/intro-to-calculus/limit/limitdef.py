from manimlib.imports import *
class limitdef(GraphScene, Scene):
	CONFIG = {
		"y_max" : 5,
        "y_min" : 0,
        "x_max" : 5,
        "x_min" : -5,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : WHITE, 
        "num_graph_anchor_points": 3000, #this is the number of points that graph manim
        "graph_origin" : ORIGIN+2*DOWN,
        "x_labeled_nums": None,#list(range(-1,2)),
        "y_labeled_nums": None,#list(range(0,2)),
        "x_axis_label":"$x$",
        "y_axis_label":"$f(x)$",
        "x_axis_width": 10,
        "y_axis_height": 5,
	}
	def construct(self):
		Ldot = MediumDot(self.graph_origin+2.1*UP).set_color(GREEN_SCREEN)
		adot = MediumDot(self.graph_origin+3*RIGHT).set_color(PINK)
		epline1 = DashedVMobject(Line(self.graph_origin+1*LEFT+2.5*UP, self.graph_origin+4*RIGHT+2.5*UP))
		epline2 = DashedVMobject(Line(self.graph_origin+1*LEFT+1.7*UP, self.graph_origin+4*RIGHT+1.7*UP))
		epline3 = DashedVMobject(Line(self.graph_origin+3.5*RIGHT+0.5*DOWN, self.graph_origin+3.5*RIGHT+2.5*UP))
		epline4 = DashedVMobject(Line(self.graph_origin+2.5*RIGHT+0.5*DOWN, self.graph_origin+2.5*RIGHT+2.5*UP))
		Lline = Line(self.graph_origin+2.1*UP, self.graph_origin+3*RIGHT+2.1*UP).set_color(GREEN_SCREEN)
		aline = Line(self.graph_origin+3*RIGHT, self.graph_origin+3*RIGHT+2.1*UP).set_color(PINK)
		vertical_rectangle = Rectangle(width = 1, height = 0.8, color = PINK, fill_opacity = 0.5, fill_color = LIGHT_PINK).move_to(self.graph_origin+3*RIGHT+2.1*UP)
		horizontal_rectangle = Rectangle(width = 1, height = 0.8, color = GREEN_SCREEN, fill_opacity = 0.5, fill_color = GREEN).move_to(self.graph_origin+3*RIGHT+2.1*UP)
		vec1 = Line(self.graph_origin+2.5*UP, self.graph_origin+2.1*UP)
		vec2 = Line(self.graph_origin+2.1*UP, self.graph_origin+1.7*UP)
		vec3 = Line(self.graph_origin+2.5*RIGHT, self.graph_origin+3*RIGHT)
		vec4 = Line(self.graph_origin+3*RIGHT, self.graph_origin+3.5*RIGHT)
		brace1 = Brace(vec1, LEFT)
		brace2 = Brace(vec2, LEFT)
		brace3 = Brace(vec3, DOWN)
		brace4 = Brace(vec4, DOWN)
		br1text = brace1.get_text(r"$\epsilon$").next_to(brace1, LEFT)
		br2text = brace2.get_text(r"$\epsilon$").next_to(brace2, LEFT)
		br3text = brace3.get_text(r"$\delta$").next_to(brace3, DOWN)
		br4text = brace4.get_text(r"$\delta$").next_to(brace4, DOWN)
		epgrp = VGroup(epline1, epline2, Ldot, adot, Lline, aline, epline4, epline3)
		recgrp = VGroup(vertical_rectangle, horizontal_rectangle)
		epbrgrp = VGroup(brace1, brace2, br1text, br2text)
		delbrgrp = VGroup(brace3, brace4, br3text, br4text)
		self.setup_axes()
		graph_1 = self.get_graph(lambda x :0.1*(x+1)**2 +0.5, x_min = -5, x_max = 5)
		graph_2 = self.get_graph(lambda x : 0.1*(x+1)**2 +0.5, x_min = 2.5, x_max = 3.5, color = YELLOW_A)
		graph_2.shift(2.5*LEFT)
		self.play(ShowCreation(graph_1))
		self.wait(2)
		self.play(ShowCreation(epgrp), ShowCreation(horizontal_rectangle), ShowCreation(vertical_rectangle))
		self.wait(2)
		self.play(ShowCreation(epbrgrp))
		self.play(ShowCreation(delbrgrp))
		self.wait(2)
		self.play(FadeOut(recgrp))
		self.wait(2)
		for i in range(0,1):
			self.play(ApplyMethod(graph_2.shift, 2.5*RIGHT))
			self.wait(1)
			self.play(ApplyMethod(graph_2.shift, 1.7*DOWN))
			self.play(ApplyMethod(graph_2.shift, 1.7*UP))
			self.wait(1)
			self.play(ApplyMethod(graph_2.shift, 2.5*LEFT))
			self.play(ApplyMethod(graph_2.shift, 2.5*RIGHT))
			self.wait(1)
			self.play(ApplyMethod(graph_2.shift, 1.7*DOWN))
			self.play(ApplyMethod(graph_2.shift, 1.7*UP))
			self.wait(1)
			self.play(ApplyMethod(graph_2.shift, 2.5*LEFT))
		self.wait()
