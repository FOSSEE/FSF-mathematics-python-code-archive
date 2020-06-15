from manimlib.imports import *

class Surface(ThreeDScene):

	def construct(self):
		axes=ThreeDAxes()
		x=TextMobject("X")
		y=TextMobject("Y")
		z=TextMobject("Z")

		x.rotate(PI/2, axis=RIGHT)
		x.rotate(PI/4,axis=OUT)
		x.shift(5.8*DOWN)

		y.rotate(PI/2, axis=RIGHT)
		y.rotate(PI/8,axis=OUT)
		y.shift(5.8*RIGHT)

		z.rotate(PI/2, axis=RIGHT)
		z.rotate(PI/5,axis=OUT)
		z.shift(3.2*OUT+0.4*LEFT)
		axis_label=VGroup(x,y,z)





		para_hyp = ParametricSurface(
			lambda u, v: np.array([
				u,
				v,
				2+u/4+np.sin(v)
			]),v_min=-3,v_max=-0.4,u_min=-1,u_max=1,
			resolution=(15, 32)).scale(1)
		para_hyp.scale(0.3)
		para_hyp.shift(1.2*RIGHT + 0.2*OUT + 0.4*DOWN)
		para_hyp.rotate(PI,axis=RIGHT)
		para_hyp.scale(2.5)
		# para_hyp.rotate(PI/3.2,axis=OUT)
		para_hyp2= ParametricSurface(
			lambda u, v: np.array([
				u,
				v,
				2+u/4+np.sin(v)
			]),v_min=-3,v_max=-0.4,u_min=-1,u_max=1,
			resolution=(15, 32)).scale(1)
		para_hyp2.scale(0.3)
		para_hyp2.shift(1.2*RIGHT + 0.2*OUT + 0.4*DOWN)
		para_hyp2.rotate(PI,axis=RIGHT)
		para_hyp2.scale(2.5)

		rec=Rectangle(height=2.11, width=1.58, color=RED, fill_opacity=0.66)
		rec.shift(1.3*RIGHT +  2.295*DOWN)
		# rec.scale(2.5)


		l1=DashedLine(start=0.5*RIGHT+1.1*DOWN+1.55*OUT,end=0.5*RIGHT+1.1*DOWN)
		l2=DashedLine(start=2.1*RIGHT+1.1*DOWN+1.25*OUT,end=2.1*RIGHT+1.1*DOWN)
		l3=DashedLine(start=2.1*RIGHT+3.4*DOWN+1.6*OUT,end=2.1*RIGHT+3.4*DOWN)
		l4=DashedLine(start=0.5*RIGHT+3.4*DOWN+2*OUT,end=0.5*RIGHT+3.4*DOWN)
		l=VGroup(l1,l2,l3,l4)

		
		
		s=TextMobject("S",tex_to_color_map={"S": YELLOW})
		s.rotate(PI/4,axis=RIGHT)
		s.rotate(PI/15,axis=OUT)
		s.shift(RIGHT + 2*OUT + 1.5*DOWN)
		d=TextMobject("D",tex_to_color_map={"D": YELLOW})
		d.scale(0.85)
		d.shift(1.26*RIGHT +  2.45*DOWN)




		self.set_camera_orientation(phi=75 * DEGREES,theta=-60*DEGREES)
		# self.set_camera_orientation(phi=90 * DEGREES,theta=-82.7*DEGREES)
		self.begin_ambient_camera_rotation(rate=-0.02)
		self.play(ShowCreation(axes),ShowCreation(axis_label))
		self.wait(1.3)
		self.play(ShowCreation(para_hyp))
		self.play(ShowCreation(s))
		self.add(para_hyp2)
		# self.play(ShowCreation(l))
		self.play(Transform(para_hyp,rec),run_time=2)
		# self.play(ShowCreation(rec))
		# self.wait(0.7)
		
		# # self.stop_ambient_camera_rotation() 
		# self.wait(1.2)
		self.play(ShowCreation(d))
		
		self.wait(3)


