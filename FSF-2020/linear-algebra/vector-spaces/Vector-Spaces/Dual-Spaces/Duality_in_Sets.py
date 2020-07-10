from manimlib.imports import *
import numpy as np
class Duality_in_sets(Scene):
	def construct(self):
		circle1 = Circle(radius=0.4,color=BLACK).shift(2.3*LEFT)
		circle1.set_fill(color=RED,opacity=200)
		rect1=Rectangle(height=2,width=2,color=GREY).shift(2*LEFT)
		rect1.set_fill(color=DARK_BLUE,opacity=1)		
		text1 = TextMobject("S").scale(0.7).shift(0.9*UP+0.7*LEFT)
		text2 = TextMobject("X",color=BLACK,stroke_width=0.5).scale(0.5).shift(2.3*LEFT)
		self.play(ShowCreation(rect1),ShowCreation(text1),ShowCreation(circle1),ShowCreation(text2))
		circle2 = Circle(radius=0.4,color=BLACK).shift(1.7*RIGHT)
		circle2.set_fill(color=BLACK,opacity=200)
		rect2=Rectangle(height=2,width=2,color=GREY).shift(2*RIGHT)
		rect2.set_fill(color=DARK_BLUE,opacity=1)	
		text3 = TextMobject("S").scale(0.7).shift(0.9*UP+3.3*RIGHT)
		text4 = TextMobject(r"X$^c$",color=BLACK,stroke_width=0.2).scale(0.5).shift(2.55*RIGHT+0.6*UP)
		text5 = TextMobject(r"\text{The subset}",r"\text{X$^c$}",r"\text{is the dual of subset}",r"\text{X}").scale(0.6).shift(2.7*UP+0.5*LEFT)
		text5[1].set_color(GREY)
		text5[3].set_color(GREY)
		self.play(ShowCreation(rect2),ShowCreation(circle2),ShowCreation(text3),ShowCreation(text4))
		self.wait(2)
		self.play(ShowCreation(text5))
		self.wait(3)
		
