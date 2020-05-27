from manimlib.imports import *
import numpy as np

class vectorspace(GraphScene):
	CONFIG={
	"x_min": -7,
	"x_max": 7,
	"y_min": -7,
	"y_max": 7,
	"graph_origin": ORIGIN,
	"x_axis_label":"$X$",
	"y_axis_label":"$Y$",
	"x_labeled_nums": list(np.arange(-7, 8,1)),
	"y_labeled_nums": list(np.arange(-7, 8,1)),
	"x_axis_width": 8,
	"y_axis_height": 7,
	"x_tick_frequency":1,
	"axes_color": GREY,
	"area_opacity": 3,
    "num_rects": 10,
	}	
	def construct(self):
		XD = self.x_axis_width/(self.x_max- self.x_min)
		YD = self.y_axis_height/(self.y_max- self.y_min)	
		a1=1*XD*RIGHT+2*YD*UP
		a2=1*XD*RIGHT+1*YD*UP	
		vec1=Vector(direction=a1).set_color(RED_E)
		vec1.shift(self.graph_origin)
		vec2=Vector(direction=a2).set_color(YELLOW_E)
		vec2.shift(self.graph_origin)
		vec1_text=TextMobject(r"$\vec{a}$")
		vec2_text=TextMobject(r"$\vec{b}$")
		vec1_text=(vec1_text.shift(self.graph_origin+a1+0.2)).scale(.7)
		vec2_text=(vec2_text.shift(self.graph_origin+a2+0.2)).scale(.7)
		self.setup_axes(animate=True)
		self.wait(2)
		self.play(ShowCreation(vec1))
		self.play(ShowCreation(vec1_text))
		self.wait(.7)
		self.play(ShowCreation(vec2))
		self.play(ShowCreation(vec2_text))
		self.wait(.7)
		a=TextMobject(r"$\vec{a} = (1,2)$",color=RED_B).scale(.6)
		a.shift(3*LEFT+2.7*UP)
		b=TextMobject(r"$\vec{b} = (1,1)$",color=YELLOW_E).scale(.6)
		b.shift(3*LEFT+2*UP)
		self.play(ShowCreation(a))
		self.play(ShowCreation(b))
		self.wait(.5)
		c=TextMobject(r"$2\cdot\vec{a} = 2\cdot(1,2) = (2,4)$",color=RED_B)
		c.shift(3*LEFT+2.7*UP)
		c.scale(.6)
		self.play(Transform(a,c))
		scaling1=TextMobject(r"Scaling vector $\vec{a}$ by 2 units",color=GOLD).scale(.5)
		scaling1.shift(3.4*RIGHT+2.4*UP)
		self.play(ShowCreation(scaling1))
		a1=2*XD*RIGHT+4*YD*UP
		self.play(FadeOut(vec1_text))
		vec1_scaled=Vector(direction=a1).set_color(RED_E)
		vec1_scaled.shift(self.graph_origin)
		self.play(ShowCreation(vec1_scaled))
		self.play(FadeOut(vec1))
		vec1_scaled_text=TextMobject(r"$2\vec{a}$").scale(.7)		
		vec1_scaled_text.shift(self.graph_origin+a1+0.2)
		self.play(ShowCreation(vec1_scaled_text))
		self.play(FadeOut(scaling1))
		d=TextMobject(r"$3\cdot\vec{b} = 3\cdot(1,1) = (3,3)$",color=YELLOW_E).scale(.6)
		d.shift(3*LEFT+2*UP)
		self.play(Transform(b,d))
		scaling2=TextMobject(r"Scaling vector $\vec{b}$ by 3 units",color=GOLD).scale(.5)
		scaling2.shift(3.4*RIGHT+2.4*UP)
		self.play(ShowCreation(scaling2))
		a2=3*XD*RIGHT+3*YD*UP
		self.play(FadeOut(vec2_text))
		vec2_2=Vector
		vec2_scaled=Vector(direction=a2).set_color(YELLOW_E)
		vec2_scaled.shift(self.graph_origin)
		self.play(ShowCreation(vec2_scaled))
		self.play(FadeOut(vec2))
		vec2_scaled_text=TextMobject(r"$3\vec{b}$").scale(.7)
		vec2_scaled_text.shift(self.graph_origin+a2+0.2)
		self.play(ShowCreation(vec2_scaled_text))
		self.wait(.7)
		self.play(FadeOut(scaling2))
		add = TextMobject("+").scale(.7)
		add.shift(4.8*LEFT+2*UP)
		self.play(ShowCreation(add))
		self.wait(.5)
		line = Line()
		line.shift(3*LEFT+1.6*UP)
		line.scale(1.8)
		self.play(ShowCreation(line))
		self.wait(1)
		e = TextMobject(r"$\vec{c} = 2\cdot\vec{a} + 3\cdot\vec{b} = (5,7)$",color=GREEN_D).scale(.6)
		e.shift(3*LEFT+1.3*UP)
		self.play(ShowCreation(e))
		self.wait(.5)
		add1=TextMobject("Addition of the scaled vectors",color=GOLD).scale(.5)
		add1.shift(4.1*RIGHT+2.4*UP)
		self.play(ShowCreation(add1))
		self.wait(.5)
		self.play(FadeOut(vec1_scaled_text))
		self.play(FadeOut(vec2_scaled_text))
		self.play(FadeOut(vec1_scaled))
		vec1_scaled2=Vector(direction=a1).set_color(RED_E)
		vec1_scaled2.shift(self.graph_origin+3*RIGHT*XD+3*UP*YD)
		self.play(ShowCreation(vec1_scaled2))
		a3=5*XD*RIGHT+7*YD*UP	
		vec3=Vector(direction=a3).set_color(GREEN_C)
		vec3.shift(self.graph_origin)
		vec3_text=TextMobject(r"$\vec{c}$").scale(.7)
		vec3_text.shift(self.graph_origin+a3+0.2)
		self.play(ShowCreation(vec3))
		self.wait(.5)
		self.play(ShowCreation(vec3_text))
		self.wait(1)




		











		
		
	

	
