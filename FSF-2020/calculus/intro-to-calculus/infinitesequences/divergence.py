from manimlib.imports import *
class divergence(GraphScene):
	CONFIG = {
		    "y_max" : 2,
        "y_min" : -2,
        "x_max" : 20,
        "x_min" : 0,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : WHITE, 
        "num_graph_anchor_points": 3000,
        "graph_origin" : ORIGIN+6*LEFT,
        "x_labeled_nums": None,
        "y_labeled_nums": [-2,-1,1,2],
        "x_axis_label":r"${(-1)}^{n}$",
        "y_axis_label":"$Sum$",
        "x_axis_width": 10,
        "y_axis_height": 4,
	}
	def construct(self):
		XTD = self.x_axis_width/(self.x_max - self.x_min)
		YTD = self.y_axis_height/(self.y_max - self.y_min)
		text1 = TextMobject("Consider the series 1-1+1-1+1-1+1-......")
		self.add(text1)
		self.wait(3)
		self.play(FadeOut(text1))
		self.setup_axes()
		rangeo = (20)//self.x_axis_width
		for i in range(0,2):
			texta = TextMobject(str((-1)**i)).move_to(self.graph_origin+0.2*(rangeo*i)*RIGHT+0.5*DOWN+0.5*RIGHT)
			self.add(texta)
		for i in range(2,4):
			texta = TextMobject(str((-1)**i)).move_to(self.graph_origin+0.2*(rangeo*i)*RIGHT+0.5*DOWN+0.65*RIGHT)
			self.add(texta)
		for i in range(4,6):
			texta = TextMobject(str((-1)**i)).move_to(self.graph_origin+0.2*(rangeo*i)*RIGHT+0.5*DOWN+0.8*RIGHT)
			self.add(texta)
		for i in range(6,8):
			texta = TextMobject(str((-1)**i)).move_to(self.graph_origin+0.2*(rangeo*i)*RIGHT+0.5*DOWN+0.95*RIGHT)
			self.add(texta)
		for i in range(8,10):
			texta = TextMobject(str((-1)**i)).move_to(self.graph_origin+0.2*(rangeo*i)*RIGHT+0.5*DOWN+1.1*RIGHT)
			self.add(texta)
		for i in range(10,12):
			texta = TextMobject(str((-1)**i)).move_to(self.graph_origin+0.2*(rangeo*i)*RIGHT+0.5*DOWN+1.35*RIGHT)
			self.add(texta)
		for i in range(12,14):
			texta = TextMobject(str((-1)**i)).move_to(self.graph_origin+0.2*(rangeo*i)*RIGHT+0.5*DOWN+1.5*RIGHT)
			self.add(texta)
		for i in range(14,16):
			texta = TextMobject(str((-1)**i)).move_to(self.graph_origin+0.2*(rangeo*i)*RIGHT+0.5*DOWN+1.65*RIGHT)
			self.add(texta)
		for i in range(16,18):
			texta = TextMobject(str((-1)**i)).move_to(self.graph_origin+0.2*(rangeo*i)*RIGHT+0.5*DOWN+1.8*RIGHT)
			self.add(texta)
		for i in range(18,20):
			texta = TextMobject(str((-1)**i)).move_to(self.graph_origin+0.2*(rangeo*i)*RIGHT+0.5*DOWN+1.95*RIGHT)
			self.add(texta)

		text2 = TextMobject("Number of purple lines denotes the number of terms added").move_to(1*UP).scale(0.8)
		self.play(ShowCreation(text2))
		self.wait(4)
		self.play(FadeOut(text2))
		for i in range(0,2):
			horline = Line(np.array([-5.5+i,1,0]), np.array([-5+i,1,0]), color = PINK)
			verline = DashedVMobject(Line(np.array([-5+i,1,0]), np.array([-5+i,0,0])))
			botline = Line(np.array([-6+i,0,0]), np.array([-5.5+i,0,0]), color = PINK)
			upline = DashedVMobject(Line(np.array([-5.5+i,0,0]), np.array([-5.5+i,1,0])))
			self.play(ShowCreation(botline), run_time = 0.2)
			self.play(ShowCreation(upline), run_time = 0.2)
			self.play(ShowCreation(horline), run_time = 0.2)
			self.play(ShowCreation(verline), run_time = 0.2)
			
		text3 = TextMobject("For even number of terms, sum is 0").move_to(1*UP).scale(0.8)
		self.play(FadeIn(text3))
		self.wait(4)
		self.play(FadeOut(text3))
		for i in range(2,4):
			horline = Line(np.array([-5.5+i,1,0]), np.array([-5+i,1,0]), color = PINK)
			verline = DashedVMobject(Line(np.array([-5+i,1,0]), np.array([-5+i,0,0])))
			botline = Line(np.array([-6+i,0,0]), np.array([-5.5+i,0,0]), color = PINK)
			upline = DashedVMobject(Line(np.array([-5.5+i,0,0]), np.array([-5.5+i,1,0])))
			self.play(ShowCreation(botline), run_time = 0.2)
			self.play(ShowCreation(upline), run_time = 0.2)
			self.play(ShowCreation(horline), run_time = 0.2)
			self.play(ShowCreation(verline), run_time = 0.2)
		botline = Line(np.array([-6+4,0,0]), np.array([-5.5+4,0,0]), color = PINK)
		upline = DashedVMobject(Line(np.array([-5.5+4,0,0]), np.array([-5.5+4,1,0])))
		self.play(ShowCreation(botline))
		self.play(ShowCreation(upline))
		text4 = TextMobject("For odd number of terms, sum is 1").move_to(1.5*UP).scale(0.8)
		self.play(FadeIn(text4))
		self.wait(3)
		for i in range(4,10):
			horline = Line(np.array([-5.5+i,1,0]), np.array([-5+i,1,0]), color = PINK)
			verline = DashedVMobject(Line(np.array([-5+i,1,0]), np.array([-5+i,0,0])))
			botline = Line(np.array([-6+i,0,0]), np.array([-5.5+i,0,0]), color = PINK)
			upline = DashedVMobject(Line(np.array([-5.5+i,0,0]), np.array([-5.5+i,1,0])))
			self.play(ShowCreation(botline), run_time = 0.2)
			self.play(ShowCreation(upline), run_time = 0.2)
			self.play(ShowCreation(horline), run_time = 0.2)
			self.play(ShowCreation(verline), run_time = 0.2)
		text5 = TextMobject("The sum is oscillating between 1 and 0").move_to(1.5*UP).scale(0.8)
		self.play(ReplacementTransform(text4, text5))
		self.wait(4)
		text6 = TextMobject("It does not coerce to a particular finite value").move_to(1.5*UP).scale(0.8)
		self.play(ReplacementTransform(text5, text6))
		self.wait(4)
		text7 = TextMobject("Hence it diverges").move_to(1.5*UP).scale(0.8)
		self.play(ReplacementTransform(text6, text7))
		self.wait(3)
