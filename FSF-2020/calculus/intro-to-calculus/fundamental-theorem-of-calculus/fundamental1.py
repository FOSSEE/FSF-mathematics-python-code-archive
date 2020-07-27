from manimlib.imports import *

class funda1(GraphScene, MovingCameraScene):
	def setup(self):
		MovingCameraScene.setup(self)
		GraphScene.setup(self)
	CONFIG = {
        "y_max": 5,
        "x_max": 8,
        "x_min": 0,
        "y_min": 0,
        "x_axis_width": 10,
        "y_axis_height": 5,
        "init_dx":0.5,
        "x_axis_label":"$t$",
        "y_axis_label":"$F(x)$",
        "graph_origin": ORIGIN+2*DOWN+6*LEFT,
    }
	def construct(self):
		self.setup_axes()
		def func(x):
			return 0.1*(x)*(x-3)*(x-7)+3

		graph1 = self.get_graph(func, x_min = 0, x_max = 7)
		graph2 = self.get_graph(func, x_min = 5, x_max = 6)
		sqr = Square(side_length = 15.0).move_to(np.array([0.5,-1.5,0]))
		line1 = self.get_vertical_line_to_graph(1,graph1,DashedLine, color = PINK)
		line2 = self.get_vertical_line_to_graph(5,graph1,DashedLine, color = PINK)
		line3 = self.get_vertical_line_to_graph(6,graph1,DashedLine, color = PINK)
		line4 = self.get_vertical_line_to_graph(5.01,graph1,DashedLine, color = PINK)
		t1 = TextMobject("a").next_to(line1, DOWN)
		t2 = TextMobject("x").next_to(line2, DOWN)
		t3 = TextMobject("x+h").next_to(line3, DOWN)
		text1 = TexMobject(r"\int _{ a }^{ x+h }{ f(t)dt }").move_to(np.array([3,2,0])).scale(0.7)
		text2 = TexMobject(r"\int _{ a }^{ x }{ f(t)dt }").move_to(np.array([1,2,0])).scale(0.7)
		text3 = TexMobject(r"= \int _{ x }^{ x+h }{ f(t)dt }").move_to(np.array([3,2,0])).scale(0.7)
		text4 = TexMobject(r"h \rightarrow 0").move_to(np.array([1,-1.5,0])).scale(0.8)
		text5 = TexMobject(r"F^{ ' }\left( x \right)=\lim _{ h\rightarrow 0 }{ \frac { f(x).h }{ h } }").move_to(np.array([1,-1.5,0])).scale(0.2)
		text6 = TexMobject(r"F^{ ' }\left( x \right)=f(x)").move_to(np.array([1,-1.5,0])).scale(0.2)
		minus = TextMobject("-").move_to(np.array([0.2,2,0]))
		group = VGroup(line1, line2, line3, t1, t2, t3)
		brace1 = Brace(line2, LEFT).scale(0.35)
		br1text = brace1.get_text(r"$f(x)$").next_to(brace1, 1.001*LEFT+1*RIGHT).scale(0.1)
		brgrp = VGroup(brace1, br1text)
		flat_rectangles1 = self.get_riemann_rectangles(self.get_graph(lambda x : 0),dx=self.init_dx,start_color=invert_color(PURPLE),end_color=invert_color(ORANGE))
		riemann_rectangles_list3 = self.get_riemann_rectangles_list(graph1, 8, max_dx=self.init_dx, power_base=2, start_color = GREEN, end_color=GREEN, x_min =1, x_max = 6)
		riemann_rectangles_list1 = self.get_riemann_rectangles_list(graph1,8,max_dx=self.init_dx,power_base=2,start_color=PURPLE,end_color=BLUE_A,x_min = 1, x_max = 5)
		riemann_rectangles_list2 = self.get_riemann_rectangles_list(graph1,8,max_dx=self.init_dx,power_base=2,start_color=RED,end_color=RED,x_min = 5, x_max = 6)
		riemann_rectangles_list4 = self.get_riemann_rectangles_list(graph1,8,max_dx=self.init_dx,power_base=2,start_color=RED,end_color=RED,x_min = 5, x_max = 5.01)
		
		self.add(graph1)
		self.play(ReplacementTransform(flat_rectangles1,riemann_rectangles_list3[7]), ShowCreation(text1))
		self.wait(3)
		self.play(ShowCreation(group))
		self.wait(1)
		self.play(ReplacementTransform(flat_rectangles1,riemann_rectangles_list2[7]), ReplacementTransform(flat_rectangles1,riemann_rectangles_list1[7]))
		self.play(FadeOut(riemann_rectangles_list3[7]))
		self.wait(2)
		self.play(ApplyMethod(text1.shift, 4*LEFT), ShowCreation(minus), ShowCreation(text2), ShowCreation(text3))
		self.play(FadeOut(riemann_rectangles_list1[7]))
		self.wait(3)
		self.camera_frame.save_state()
		self.play(self.camera_frame.set_width,2.25,self.camera_frame.move_to,sqr,run_time = 2)
		self.wait(2)
		self.play(ReplacementTransform(riemann_rectangles_list2[7], riemann_rectangles_list4[7]), FadeOut(riemann_rectangles_list2[7]), ReplacementTransform(line3, line4), FadeOut(line3), ShowCreation(text4))	
		self.wait(2)
		self.play(ShowCreation(brgrp))
		self.wait(2)
		self.play(ReplacementTransform(text4, text5))
		self.wait(2)
		self.play(ReplacementTransform(text5, text6))
		self.wait(5)