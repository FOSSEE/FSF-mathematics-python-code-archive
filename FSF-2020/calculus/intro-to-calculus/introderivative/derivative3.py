from manimlib.imports import *
class derivative3(GraphScene, Scene):
	def setup(self):
		Scene.setup(self)
		#ZoomedScene.setup(self)
	CONFIG = {
		"y_max" : 8,
        "y_min" : 0,
        "x_max" : 11,
        "x_min" : 0,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : WHITE, 
        "num_graph_anchor_points": 3000, #this is the number of points that graph manim
        "graph_origin" : ORIGIN+3*DOWN+6.5*LEFT,
        "x_labeled_nums": list(range(0,12))[::1],
        "y_labeled_nums": list(range(0,9))[::1],
        "x_axis_label":"$t$",
        "y_axis_label":"$s$",
        "x_axis_width": 5,
        "y_axis_height": 5,
	}
	def construct(self):
		XTD = self.x_axis_width/(self.x_max - self.x_min)
		YTD = self.y_axis_height/(self.y_max - self.y_min)

		self.setup_axes()
		graph_1 = self.get_graph(lambda x : -(x-2)**2+4, color = GOLD_A, x_min = 0, x_max = 1.5)
		graph_2 = self.get_graph(lambda x : 1*x+2.25, color = GOLD_A, x_min = 1.5, x_max = 5)
		graph_3 = self.get_graph(lambda x : 7.25, color = GOLD_A, x_min = 5, x_max = 8)
		graph_4 = self.get_graph(lambda x : -3.625*x + 36.25, color = GOLD_A, x_min = 8, x_max = 10)

		self.y_max = 5
		self.x_max = 10
		self.x_min = 0
		self.y_min = -5
		self.x_labeled_nums = list(range(0,11))
		self.y_labeled_nums = list(range(-5,6))[::1]
		self.x_axis_label = r"$t$"
		self.y_axis_label = r"$v$"
		self.y_tick_frequency = 1
		self.x_tick_frequency = 1
		self.graph_origin = ORIGIN+1*RIGHT
		self.setup_axes()
		graph_5 = self.get_graph(lambda x : 2*(x-2)+4, color = GREEN_SCREEN, x_min = 0, x_max = 1.5)
		graph_6 = self.get_graph(lambda x : 3, color = GREEN_SCREEN, x_min = 1.5, x_max = 5)
		graph_7 = self.get_graph(lambda x : 0, color = GREEN_SCREEN, x_min = 5, x_max = 8)
		graph_8 = self.get_graph(lambda x : -3.625, color = GREEN_SCREEN, x_min = 8, x_max = 10)
		line1 = DashedVMobject(Line(self.graph_origin+2.5*RIGHT, self.graph_origin+2.5*RIGHT+1.5*UP))
		line2 = DashedVMobject(Line(self.graph_origin+4*RIGHT, self.graph_origin+4*RIGHT+1.835*DOWN))
		self.play(ShowCreation(graph_1), ShowCreation(graph_5), run_time = 3)
		self.play(ShowCreation(graph_2), ShowCreation(graph_6), run_time = 3)
		self.add(line1)
		self.play(ShowCreation(graph_3), ShowCreation(graph_7), run_time = 3)
		self.add(line2)
		self.play(ShowCreation(graph_4), ShowCreation(graph_8), run_time = 3)
		self.wait(3)
