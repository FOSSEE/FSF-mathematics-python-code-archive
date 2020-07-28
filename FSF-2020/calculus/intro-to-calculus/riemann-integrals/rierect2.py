from manimlib.imports import *
class rierect2(GraphScene):
	CONFIG = {
		"y_max" : 6,
        "y_min" : 0,
        "x_max" : 4,
        "x_min" : 0,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : WHITE, 
        "num_graph_anchor_points": 3000, #this is the number of points that graph manim
        "graph_origin" : ORIGIN+2*DOWN+4*LEFT,
        "x_labeled_nums": None,#list(range(-1,2)),
        "y_labeled_nums": None,#list(range(0,2)),
        "x_axis_label":"$x$",
        "y_axis_label":"$f(x)$",
        "x_axis_width": 10,
        "y_axis_height": 5,
	}
	def construct(self):
		self.setup_axes()
		graph1 = self.get_graph(lambda x : (0.1*(1.5*x+1)**2 +0.5), x_min = 0, x_max = 4)
		minlim = self.get_vertical_line_to_graph(1,graph1,DashedLine, color = PINK)
		maxlim = self.get_vertical_line_to_graph(3,graph1,DashedLine,color = PINK)
		x1 = TexMobject(r"{x}_{1}").next_to(minlim, DOWN)
		x2 = TexMobject(r"{x}_{2}").next_to(maxlim, DOWN)
		rie1 = self.get_riemann_rectangles(graph1, x_min = 1, x_max = 3, dx = 0.1, input_sample_type = "left", fill_opacity = 1, start_color = YELLOW, end_color = YELLOW)
		#rie2 = self.get_riemann_rectangles(graph1, x_min = 1, x_max = 3, dx = 0.01, input_sample_type = "right", fill_opacity = 0.5, start_color = PINK, end_color = LIGHT_PINK)
		group = VGroup(graph1, minlim, maxlim, x1, x2, rie1)
		self.play(ShowCreation(group))
		self.wait(1.5)
