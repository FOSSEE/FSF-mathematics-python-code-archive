from manimlib.imports import *

class Mobius(ThreeDScene):
	def construct(self):
		axes=ThreeDAxes()



		R=2.5


		mobius = ParametricSurface(
			lambda u, v: np.array([
				(R+u*np.cos(v/2))*np.cos(v),
				(R+u*np.cos(v/2))*np.sin( v),
				u*np.sin(v/2)
			]),
			 u_min = -0.5, u_max = 0.5, v_min = 0, v_max = 2*PI, 

			resolution=(6, 32)).fade(0.5) #Resolution of the surfaces
		circle=Circle(radius=2.5, color=BLUE)



		mobius.rotate(PI/2, axis=RIGHT)
		mobius.rotate(PI/2, axis=OUT)
		# # mobius.shift(RIGHT+OUT+DOWN)





		along = ParametricSurface(
			lambda u, v: np.array([
				(R+u*np.cos(v/2))*np.cos(v),
				(R+u*np.cos(v/2))*np.sin(v),
				0
			]),
			 u_min = -0.5, u_max = 0.5, v_min = 0, v_max = 2*PI, 

			resolution=(6, 32)).fade(0.5) #Resolution of the surfaces
		circle=Circle(radius=2.5, color=BLUE)


		

		


















		self.set_camera_orientation(phi=75 * DEGREES,theta=-75*DEGREES)
		
		self.play(Write(mobius))
	
		self.wait(1)
		self.begin_ambient_camera_rotation(rate=0.65)

		self.wait(10)
		self.stop_ambient_camera_rotation() 
		self.wait(1)



		


