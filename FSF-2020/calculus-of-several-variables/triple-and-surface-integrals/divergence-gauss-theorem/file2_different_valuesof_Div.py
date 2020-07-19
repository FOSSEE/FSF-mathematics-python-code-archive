from manimlib.imports import *
class Div(Scene):
	def construct(self):
		one=TextMobject(r"Div$ \vec{F} < 0$ ").set_color(RED)
		two=TextMobject(r"Div$ \vec{F} = 0$ ").set_color(BLUE)
		three=TextMobject(r"Div$ \vec{F} > 0$ ").set_color(YELLOW)

		one.shift(2.3*DOWN)
		two.shift(2.3*DOWN)
		three.shift(2.3*DOWN)


		a=Dot(color=RED)
		a.shift(0.1*LEFT)
		b=Dot(color=BLUE)
		b.shift(0.1*LEFT)
		c=Dot(color=YELLOW)
		c.shift(0.1*LEFT)

		rot=[0*DEGREES,45*DEGREES,90*DEGREES,135*DEGREES,180*DEGREES,225*DEGREES,270*DEGREES,315*DEGREES]
		rot2=[180*DEGREES,180*DEGREES,180*DEGREES,180*DEGREES,180*DEGREES,180*DEGREES,180*DEGREES,180*DEGREES]
		shift=[RIGHT,0.7*RIGHT+0.7*UP,UP,0.7*LEFT+0.7*UP,LEFT,0.7*LEFT+0.7*DOWN,DOWN,0.7*RIGHT+0.7*DOWN]   
		shift2=[RIGHT,RIGHT+UP,RIGHT+DOWN,UP,DOWN,LEFT,LEFT+UP,LEFT+DOWN]


		
		u=[Vector(color=RED),Vector(color=RED),Vector(color=RED),Vector(color=RED),
		   Vector(color=RED),Vector(color=RED),Vector(color=RED),Vector(color=RED)]


		[u[i].rotate(rot[i]) for i in range(8) ]
		[u[i].rotate(rot2[i]) for i in range(8) ]
		[u[i].shift(shift[i]) for i in range(8) ]


		divone=VGroup(*u)
		divone.shift(0.6*LEFT)


		v=[Vector(color=BLUE),Vector(color=BLUE),Vector(color=BLUE),Vector(color=BLUE),
		   Vector(color=BLUE),Vector(color=BLUE),Vector(color=BLUE),Vector(color=BLUE)]


		[v[i].rotate(45*DEGREES) for i in range(8)]
		[v[i].shift(shift2[i]) for i in range(8) ]

		divtwo=VGroup(*v)
		divtwo.shift(0.6*LEFT)


		w=[Vector(color=YELLOW),Vector(color=YELLOW),Vector(color=YELLOW),Vector(color=YELLOW),
		   Vector(color=YELLOW),Vector(color=YELLOW),Vector(color=YELLOW),Vector(color=YELLOW)]


		[w[i].rotate(rot[i]) for i in range(8)]
		[w[i].shift(shift[i]) for i in range(8) ]   


		divthree=VGroup(*w)
		divthree.shift(0.6*LEFT)




		self.play(ShowCreation(a),ShowCreation(divone))
		self.play(ShowCreation(one))
		self.wait(1)
		self.play(FadeOut(a),FadeOut(divone),FadeOut(one))

		self.play(ShowCreation(b),ShowCreation(divtwo))
		self.play(ShowCreation(two))
		self.wait(1)
		self.play(FadeOut(b),FadeOut(divtwo),FadeOut(two))


		self.play(ShowCreation(c),ShowCreation(divthree))
		self.play(ShowCreation(three))
		self.wait(1)
		self.play(FadeOut(c),FadeOut(divthree),FadeOut(three))
		self.wait(0.5)











