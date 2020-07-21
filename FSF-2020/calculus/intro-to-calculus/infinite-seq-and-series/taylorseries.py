from manimlib.imports import *
class conv(GraphScene):
	CONFIG = {
		"y_max" : 10,
        "y_min" : 0,
        "x_max" : 5,
        "x_min" : -1,
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 1, 
        "axes_color" : WHITE, 
        "num_graph_anchor_points": 3000,
        "graph_origin" : ORIGIN+2*DOWN+6*LEFT,
        "x_labeled_nums": list(range(0,6)),
        "y_labeled_nums": list(range(0,11))[::1],
        "x_axis_label":"x",
        "y_axis_label":"$f(x)$",
        "x_axis_width": 9,
        "y_axis_height": 5,
	}
	def construct(self):
		XTD = self.x_axis_width/(self.x_max - self.x_min)
		YTD = self.y_axis_height/(self.y_max - self.y_min)
		texta = TexMobject(r"\text{Expressing }", r"{e}^{x}", r"\text{ as its Taylor series}")
		self.play(FadeIn(texta))
		self.wait(3)
		self.play(FadeOut(texta))
		self.setup_axes()
		graph1 = self.get_graph(lambda x : (np.e)**x, x_min = -1, x_max = 5, color = PINK)
		graph2 = self.get_graph(lambda x : 1+x, x_min = -1, x_max = 5, color = GREEN_SCREEN)
		graph3 = self.get_graph(lambda x : 1+(x)+(x**2)/2, x_min = -1, x_max = 5, color = GREEN_SCREEN)
		graph4 = self.get_graph(lambda x : 1+(x)+(x**2)/2+(x**3)/6, x_min = -1, x_max = 5, color = GREEN_SCREEN)
		graph5 = self.get_graph(lambda x : 1+(x)+(x**2)/2+(x**3)/6+(x**4)/24, x_min = -1, x_max = 5, color = GREEN_SCREEN)
		graph6 = self.get_graph(lambda x : 1+(x)+(x**2)/2+(x**3)/6+(x**4)/24+(x**5)/120, x_min = -1, x_max = 5, color = GREEN_SCREEN)
		graph7 = self.get_graph(lambda x : 1+(x)+(x**2)/2+(x**3)/6+(x**4)/24+(x**5)/120+(x**6)/720, x_min = -1, x_max = 5, color = GREEN_SCREEN)
		graph8 = self.get_graph(lambda x : 1+(x)+(x**2)/2+(x**3)/6+(x**4)/24+(x**5)/120+(x**6)/720+(x**7)/5040, x_min = -1, x_max = 5, color = GREEN_SCREEN)
		texta = TexMobject(r"{e}^{x}").move_to(self.graph_origin+ 1*RIGHT+2*UP)
		textb = TexMobject(r"\therefore {e}^{x}=").move_to(3.5*LEFT+0.5*DOWN)
		text1 = TexMobject(r"1+x").move_to(4*RIGHT)
		text2 = TexMobject(r"+\frac{{x}^{2}}{2!}").move_to(4*RIGHT)
		text3 = TexMobject(r"+\frac{{x}^{3}}{3!}").move_to(4*RIGHT)
		text4 = TexMobject(r"+\frac{{x}^{4}}{4!}").move_to(4*RIGHT)
		text5 = TexMobject(r"+\frac{{x}^{5}}{5!}").move_to(4*RIGHT)
		text6 = TexMobject(r"+\frac{{x}^{6}}{6!}").move_to(4*RIGHT)
		text7 = TexMobject(r"+\frac{{x}^{7}}{7!}+...").move_to(4.5*RIGHT)

		self.play(ShowCreation(texta))
		self.play(ShowCreation(graph1))
		self.wait(3)
		self.play(FadeOut(texta))
		self.play(ShowCreation(graph2))
		self.play(ShowCreation(text1))
		self.wait(3)
		self.play(ReplacementTransform(graph2, graph3), ApplyMethod(text1.shift, 1*LEFT), ShowCreation(text2))
		self.wait(3)
		self.play(ReplacementTransform(graph3, graph4), ApplyMethod(text1.shift, 1*LEFT), ApplyMethod(text2.shift, 1*LEFT), ShowCreation(text3))
		self.wait(3)
		self.play(ReplacementTransform(graph4, graph5), ApplyMethod(text1.shift, 1*LEFT), ApplyMethod(text2.shift, 1*LEFT), ApplyMethod(text3.shift, 1*LEFT), ShowCreation(text4))
		self.wait(3)
		self.play(ReplacementTransform(graph5, graph6), ApplyMethod(text1.shift, 1*LEFT), ApplyMethod(text2.shift, 1*LEFT), ApplyMethod(text3.shift, 1*LEFT), ApplyMethod(text4.shift, 1*LEFT), ShowCreation(text5))
		self.wait(3)
		self.play(ReplacementTransform(graph6, graph7), ApplyMethod(text1.shift, 1*LEFT), ApplyMethod(text2.shift, 1*LEFT), ApplyMethod(text3.shift, 1*LEFT), ApplyMethod(text4.shift, 1*LEFT), ApplyMethod(text5.shift, 1*LEFT), ShowCreation(text6))
		self.wait(3)
		self.play(ReplacementTransform(graph7, graph8),ApplyMethod(text1.shift, 1*LEFT), ApplyMethod(text2.shift, 1*LEFT), ApplyMethod(text3.shift, 1*LEFT), ApplyMethod(text4.shift, 1*LEFT), ApplyMethod(text5.shift, 1*LEFT), ApplyMethod(text6.shift, 1*LEFT), ShowCreation(text7))
		self.wait(3)
		grp = VGroup(text1, text2, text3, text4, text5, text6, text7)
		self.play(ApplyMethod(grp.shift, 0.5*DOWN), FadeIn(textb))
		self.wait(5)