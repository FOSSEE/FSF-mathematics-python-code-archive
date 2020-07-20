class mimi(GraphScene):
	CONFIG = {
		"y_max": 5,
        "x_max": 6,
        "x_min": 0,
        "y_min": 0,
        "x_axis_width": 5,
        "y_axis_height": 5,
        "init_dx":0.5,
        "graph_origin": ORIGIN+2*DOWN+6*LEFT,
	}
	def construct(self):
		self.setup_axes()
		def func(x):
			return  0.1*(x)*(x-3)*(x-7)+3

		graph=self.get_graph(func,x_min=0,x_max=6)
		kwargs = {
			"x_min" : 1.5,
			"x_max" : 5.5,
			"fill_opacity" : 0.5,
			"stroke_width" : 0.25,
		}
		flat_rectangles = self.get_riemann_rectangles(self.get_graph(lambda x : 0),dx=self.init_dx,**kwargs)
		riemann_rectangles_list = self.get_riemann_rectangles_list(graph,8,max_dx=self.init_dx,power_base=2,start_color=PURPLE,end_color=ORANGE,**kwargs, input_sample_type = "right")
		riemann_rectangles_list1 = self.get_riemann_rectangles_list(graph,8,max_dx=self.init_dx,power_base=2,start_color=PURPLE,end_color=ORANGE,**kwargs, input_sample_type = "left")
		self.add(graph)
		self.play(ReplacementTransform(flat_rectangles,riemann_rectangles_list[0]), ReplacementTransform(flat_rectangles,riemann_rectangles_list1[0]))
		#self.play(ReplacementTransform(flat_rectangles,riemann_rectangles_list1[0]))
		self.wait(2)
		kwargs = {
			"x_min" : 3,
			"x_max" : 3.5,
			"fill_opacity" : 0.5,
			"stroke_width" : 0.25,
		}
		riemann_rectangles_list2 = self.get_riemann_rectangles_list(graph,8,max_dx=self.init_dx,power_base=2,start_color=PURPLE,end_color=ORANGE,**kwargs, input_sample_type = "right")
		riemann_rectangles_list3 = self.get_riemann_rectangles_list(graph,8,max_dx=self.init_dx,power_base=2,start_color=PURPLE,end_color=ORANGE,**kwargs, input_sample_type = "left")
		#self.play(FadeOut(riemann_rectangles_list[0]), FadeOut(riemann_rectangles_list1[0]))
		self.play(ReplacementTransform(flat_rectangles,riemann_rectangles_list2[0]), ReplacementTransform(flat_rectangles,riemann_rectangles_list3[0]), FadeOut(riemann_rectangles_list[0]), FadeOut(riemann_rectangles_list1[0]))
		minlim = self.get_vertical_line_to_graph(3,graph,DashedLine)
		maxlim = self.get_vertical_line_to_graph(3.5,graph,DashedLine)
		line2 = Line(self.graph_origin+2.5*RIGHT, self.graph_origin+2.9*RIGHT)
		brace1 = Brace(minlim, LEFT)
		brace2 = Brace(line2, DOWN)
		brace3 = Brace(maxlim, RIGHT)
		br1text = brace1.get_text(r"${M}_{i}$").next_to(brace1, LEFT)
		br2text = brace2.get_text(r"$\Delta x$").next_to(brace2, DOWN)
		br3text = brace3.get_text(r"${m}_{i}$").next_to(brace3, RIGHT)
		text1 = TexMobject(r"\Delta x=(b-a)/n").shift(2*RIGHT)
		grp3 = VGroup(br1text, br2text, br3text, brace1, brace2, brace3, text1)
		self.play(ShowCreation(grp3))
		self.wait(5)
