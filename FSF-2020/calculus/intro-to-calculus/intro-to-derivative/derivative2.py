from manimlib.imports import *
class derivative2(GraphScene, MovingCameraScene):
	def setup(self):
		GraphScene.setup(self)
		MovingCameraScene.setup(self)
	CONFIG = {
		"y_max" : 100,
        "y_min" : 0,
        "x_max" : 10,
        "x_min" : 0,
        "y_tick_frequency" : 100, 
        "x_tick_frequency" : 10, 
        "axes_color" : WHITE, 
        "num_graph_anchor_points": 3000, #this is the number of points that graph manim
        "graph_origin" : ORIGIN,
        "x_labeled_nums": None,#list(range(0,11)),
        "y_labeled_nums": None,#list(range(0,101))[::10],
        "x_axis_label":"$x$",
        "y_axis_label":"$f(x)$",
        "x_axis_width": 5,
        "y_axis_height": 5,
        "start_x" : 2,
        "start_dx" : 6,
        "df_color" : YELLOW,
        "dx_color" : GREEN,
        "secant_line_color" : MAROON_B,
        "zoomed_camera_frame_starting_position": ORIGIN+2*DOWN+6*LEFT,
	}
	def construct(self):
		self.setup()
		self.camera_frame.save_state()
		self.graph_origin = ORIGIN+2*DOWN+6*LEFT
		self.setup_axes()
		graph23 = self.get_graph(lambda x : x**2+7, color = GREEN_SCREEN, x_min = 0, x_max = 10)
		graph24 = self.get_graph(lambda x : x**2+7, color = GREEN_SCREEN, x_min = 8, x_max = 2.01)
		line_1 = DashedVMobject(Line(np.array([-5,-2,0]), np.array([-5,-1.42,0])))
		textdef = TextMobject("")
		text1 = TexMobject("{ x }_{ 0 }").move_to(np.array([-5,-2.2,0]))
		text2 = TextMobject("The line becomes tangential to the curve").move_to(self.graph_origin+RIGHT+0.5*UP).scale(0.01)
		text3 = TexMobject(r"\frac { df }{ dx } =\frac { f({ x }_{ 0 }+h)-f({ x }_{ 0 }) }{ h-0 }").move_to(2*RIGHT)
		text4 = TexMobject(r"\frac { df }{ dx } =\lim _{ h\rightarrow 0 }{ \frac { f({ x }_{ 0 }+h)-f({ x }_{ 0 }) }{ h }  }").move_to(2*RIGHT)  
		squareobj = Square(side_length = 15).move_to(self.graph_origin+RIGHT+0.53*UP)
		ss_group = self.get_secant_slope_group(
            self.start_x, graph23,
            dx = self.start_dx,
            dx_label = "h",
            df_label = "df",
            df_line_color = self.df_color,
            dx_line_color = self.dx_color,
            secant_line_color = self.secant_line_color,
            dot_df_top = True,
            dot_dx_start = True,
            dot_df_top_label = "Q",
            dot_dx_start_label = "P",
            secant_line_length = 8
        )
		self.play(ShowCreation(graph23))
		self.wait()
		self.play(ShowCreation(ss_group.secant_line))
		self.add(text1)
		self.play(ShowCreation(line_1))
		self.wait(3)
		self.play(ShowCreation(ss_group.dx_line))
		self.play(ShowCreation(ss_group.dx_label))
		self.play(ShowCreation(ss_group.df_line))
		self.play(Write(ss_group.df_label))
		self.play(ShowCreation(ss_group.dot_df_top), ShowCreation(ss_group.dot_dx_start))
		self.play(ShowCreation(ss_group.dot_df_top_label), ShowCreation(ss_group.dot_dx_start_label))
		self.wait()
		self.play(ShowCreation(text3))
		self.wait(2)
		self.play(ReplacementTransform(text3, text4))
		self.animate_secant_slope_group_change(ss_group, target_dx = 0.01, run_time = 5)
		self.wait(2)
		self.play(self.camera_frame.set_width,0.2,self.camera_frame.move_to,squareobj,run_time = 2)
		self.wait()
		self.play(ShowCreation(text2))
		self.wait(3)
