from manimlib.imports import *
class ThreeDSpace(ThreeDScene):
	
	def construct(self):		
		axes = ThreeDAxes()
		axes.set_stroke(width=1,color=GOLD)	
		self.add(axes)
		self.set_camera_orientation(phi = 70*DEGREES,theta =110*DEGREES)
		line1 = Line(color = YELLOW,opacity=350,start = ORIGIN,end = [0.5,2,2])
		self.play(ShowCreation(line1))
		self.wait(1)
		line2 = Line(color = BLUE,opacity=350,start = ORIGIN,end = [2,2,-1])
		self.play(ShowCreation(line2))
		self.wait(1)	
		line3 = Line(opacity=350,start=axes.c2p(0.5,2,2) ,end=axes.c2p(0.5,1.14,-0.17))	
		self.play(ShowCreation(line3))
		self.wait(1)
		line4 = Line(color=RED,opacity=350,start = ORIGIN,end=[0.5,1.14,-0.145])
		self.play(ShowCreation(line4))
		self.wait(2)
		text1 = TextMobject(r"\text{Projection on }",r"\text{$\vec{v}$}",r"\text{ onto }",r"\text{$\vec{u}$}",r"\text{ = }",r"\text{$ |\vec{v}|cos\theta$,}").scale(0.6).shift(4*LEFT+3.5*UP)
		text1[1].set_color(YELLOW)
		text1[3].set_color(BLUE)
		text1[5].set_color(RED)
		text2 = TextMobject(r"\text{where $\theta$ is the angle between the vectors.}").scale(0.6).shift(4*LEFT+3*UP)
		self.add_fixed_in_frame_mobjects(text1)
		self.add_fixed_in_frame_mobjects(text2)
		self.play(ShowCreation(text1),ShowCreation(text2))
		self.wait(3)
		

