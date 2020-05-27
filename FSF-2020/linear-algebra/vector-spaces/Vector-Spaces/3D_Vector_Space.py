from manimlib.imports import *
class ThreeDSpace(ThreeDScene):
	def construct(self):
		curve = ParametricFunction(
			lambda x:  np.array([
		    0, -x , x]), color = YELLOW, t_min = -2, t_max = 2)
		axes = ThreeDAxes()
		axes.set_stroke(width=1,color=GOLD)		
		self.add(axes)
		self.set_camera_orientation(phi = 70*DEGREES,theta =60*DEGREES)
		self.begin_ambient_camera_rotation(rate=0.3)
		self.play(ShowCreation(curve))
		self.wait(6)			
		
