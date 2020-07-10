from manimlib.imports import *
class limit3(GraphScene, MovingCameraScene):
	def setup(self):
		GraphScene.setup(self)
		MovingCameraScene.setup(self)
	CONFIG = {
        "y_max" : 10,
        "y_min" : 0,
        "x_max" : 100,
        "x_min" : 0,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 10, 
        "axes_color" : WHITE, 
        "num_graph_anchor_points": 3000, #this is the number of points that graph manim
        "graph_origin" : ORIGIN+3*DOWN+4*LEFT,
        "x_labeled_nums": list(range(0,101))[::10],
        "y_labeled_nums": list(range(0,11)),
        "x_axis_label":"$x$",
        "y_axis_label":"$f(x)$",
        "x_axis_width": 10,
        "y_axis_height": 5,
    }
	def construct(self):
		XTD = self.x_axis_width/(self.x_max - self.x_min)
		YTD = self.y_axis_height/(self.y_max - self.y_min)
		sqr1 = Square(side_length = 15).move_to(np.array([1,0.5,0]))
		sqr2 = Square(side_length = 15).move_to(np.array([-4,-3,0]))
		
		textdef = TextMobject("")
		text20 = TextMobject("f(x) is not defined at x=50").move_to(np.array([1,0.3,0])).scale(0.2)
		text21 = TexMobject(r"\text {f(x) is not defined in interval }",r" (-\infty ,\quad 1]").move_to(np.array([-4,-3.2,0])).scale(0.18)
		text22 = TextMobject("1").move_to(np.array([-3.9,-3.05,0])).scale(0.2)
		text1 = TexMobject(r"\text {Let }" ,r"f\left( x \right) =\begin{cases} \sqrt { x-1 } ,x\in \quad (1,\infty )-50 \end{cases}")
		text2 = TextMobject("Graph of f(x) is ")
		text3 = TextMobject("Right hand neighbour of 50 will approximately be 50.000001").move_to(np.array([1,0.3,0])).scale(0.15)
		text4 = TextMobject("Left hand neighbour of 50 will approximately be 49.999999").move_to(np.array([1,0.3,0])).scale(0.15)
		text5 = TexMobject(r"\text {Hence R.H.L }", r"=\lim _{ x\rightarrow { 50 }^{ + } }{ \sqrt { 50.000001 - 1 }  }  \approx  7.000000071").move_to(np.array([1,0.3,0])).scale(0.13)
		text6 = TexMobject(r"\text{Hence L.H.L }", r" = \lim _{ x\rightarrow { 50 }^{ - } }{ \sqrt { 49.999999-1 }  }\approx 6.999999929").move_to(np.array([1,0.3,0])).scale(0.13)
		text7 = TextMobject("7.000000071").move_to(np.array([1.9,0.25,0])).scale(0.1)
		text8 = TextMobject("6.999999929").move_to(np.array([0.1,0.25,0])).scale(0.1)
		text9 = TexMobject(r"6.999999929\quad \approx \quad 7.000000071 \quad \approx 7").move_to(np.array([1,0.25,0])).scale(0.2)
		text10 = TexMobject(r"\text{Because LHL }" ,r"\approx" ,r"\text{ RHL, Limit exists at x=50 and equals 7").move_to(np.array([1,0.25,0])).scale(0.13)
		text11 = TextMobject("There is no Left hand neighbour of x=1").move_to(np.array([-4,-3.2,0])).scale(0.22)
		text12 = TexMobject(r"\therefore\quad \lim _{ x\rightarrow 0 }{ f(x) } \quad =\quad \lim _{ x\rightarrow { 0 }^{ + } }{ f(x) } ").move_to(np.array([-4,-3.2,0])).scale(0.25)
		text13 = TexMobject(r"\text {R.H.L =}",r" \lim _{ x\rightarrow { 0 }^{ + } }{ \sqrt { 1.000000000001-1 }  } \quad \approx 0").move_to(np.array([-4,-3.2,0])).scale(0.13)
		text14 = TexMobject(r"\therefore \quad \lim _{ x\rightarrow 0 }{ f(x)\quad =\quad 0 }").move_to(np.array([-4,-3.2,0])).scale(0.13)
		self.camera_frame.save_state()
		self.play(ShowCreation(text1))
		self.wait(3)
		self.play(ReplacementTransform(text1, text2))
		self.wait()
		self.play(ReplacementTransform(text2, textdef))
		self.setup_axes()
		self.setup()
		graph_1 = self.get_graph(lambda x : (x-1)**(1/2),color = PINK, x_min = 1, x_max = 49.9)
		graph_2 = self.get_graph(lambda x : (x-1)**(1/2),color = PINK, x_min = 50.1, x_max = 100)
		graph_3 = self.get_graph(lambda x : (x-1)**(1/2),color = PINK, x_min = 1.05, x_max = 1.001)
		dot1 = SmallDot(color = PURPLE_A)
		cir = Circle(radius = 0.01, color = GREEN_SCREEN).move_to(np.array([1,0.5,0]))
		grp1 = VGroup(graph_1, graph_2, cir)
		grp2 = VGroup(text7, text8)
		self.play(ShowCreation(grp1))
		self.wait(2)
		self.play(self.camera_frame.set_width,2.25,self.camera_frame.move_to,sqr1,run_time = 2)
		self.wait(1)
		self.play(ShowCreation(text20))
		self.wait(2)
		self.play(ReplacementTransform(text20, text3))
		self.wait(3)
		self.play(ReplacementTransform(text3, text5))
		self.wait(3)
		self.play(ReplacementTransform(text5, text7), ShowCreation(text4))
		self.wait(4)
		self.play(ReplacementTransform(text4, text6))
		self.wait(3)
		self.play(ReplacementTransform(text6, text8))
		self.wait(1.5)
		self.play(ReplacementTransform(grp2, text9))
		self.wait(1.5)
		self.play(ReplacementTransform(text9, text10))
		self.wait(3)
		self.play(self.camera_frame.set_width,2.25,self.camera_frame.move_to,sqr2,run_time = 2)
		self.play(ShowCreation(text21), ShowCreation(text22))
		self.play(MoveAlongPath(dot1, graph_3), run_time = 3)
		self.wait(3)
		self.play(ReplacementTransform(text21, text11))
		self.wait(3)
		self.play(ReplacementTransform(text11, text12))
		self.wait(3)
		self.play(ReplacementTransform(text12, text13))
		self.wait(2)
		self.play(ReplacementTransform(text13, text14))
		self.wait(3)
		self.play(ReplacementTransform(text14, textdef))
		self.wait(2)
