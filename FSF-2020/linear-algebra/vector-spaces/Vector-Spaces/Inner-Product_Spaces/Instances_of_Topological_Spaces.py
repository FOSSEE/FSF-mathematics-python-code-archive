from manimlib.imports import *
class InnerProduct(Scene):
	def construct(self):
		
		circle1 = Circle(color=DARK_GREY).scale(3.7)
		circle1.set_fill(color=GOLD,opacity=350)
		square1 = Square(color=DARK_GREY).scale(2.5)
		square1.set_fill(color=DARK_BLUE,opacity=350)
		square2=Square(color=DARK_GREY).scale(1.6).shift(0.2*DOWN)
		square2.rotate(np.pi/4).set_fill(color=YELLOW,opacity=350)
		square3 = Square(color=DARK_GREY).scale(1).shift(0.3*DOWN)
		square3.set_fill(color=BLACK,opacity=350)
		circle2 = Circle(color=DARK_GREY).scale(0.5).shift(0.45*DOWN)
		circle2.set_fill(color=MAROON_A,opacity=350)
		text1 = TextMobject("Topological Spaces",color=BLACK).scale(0.5).shift(3*UP)
		text2 = TextMobject("Metric Spaces",color=BLACK).scale(0.5).shift(2.2*UP)
		text3 = TextMobject("Normed",color=BLACK).scale(0.44).shift(1.4*UP)
		text4 = TextMobject("Vector Spaces",color=BLACK).scale(0.44).shift(1.17*UP)
		text5 = TextMobject("Inner Product",color=WHITE).scale(0.37).shift(0.5*UP)		
		text6 = TextMobject("Spaces",color=WHITE).scale(0.37).shift(0.27*UP)
		text7 = TextMobject("Dot",color=BLACK).scale(0.37).shift(0.3*DOWN)
		text8 = TextMobject("Product",color=BLACK).scale(0.32).shift(0.5*DOWN)


	

		self.play(ShowCreation(circle1),ShowCreation(text1))
		self.wait(1.5)
		self.play(ShowCreation(square1),ShowCreation(text2))
		self.wait(1.5)
		self.play(ShowCreation(square2),ShowCreation(text3),ShowCreation(text4))
		self.wait(1.5)
		self.play(ShowCreation(square3),ShowCreation(text5),ShowCreation(text6))
		self.wait(1.5)
		self.play(ShowCreation(circle2),ShowCreation(text7),ShowCreation(text8))
		self.wait(4)
