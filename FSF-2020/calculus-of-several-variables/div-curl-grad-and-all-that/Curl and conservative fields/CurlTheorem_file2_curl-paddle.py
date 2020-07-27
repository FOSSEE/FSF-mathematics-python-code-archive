from manimlib.imports import *

def field_func(coordinate):
	x,y = coordinate[:2]
	return np.array([
					-y, 
					x,
					0
				])

class Paddlewheel(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		#self.add(axes)
		text = TextMobject("Insert the paddle into the flow of water").shift(3*DOWN).add_background_rectangle()
		text_a = TextMobject("The rotation of the wheel is proportional to the component of curl in the direction of the axle").shift(3*DOWN).scale(0.7)

		vec_field = VectorField(field_func, x_min =-4, x_max = 4, y_min =-4, y_max =4)

		self.set_camera_orientation(phi=0*DEGREES,theta=0*DEGREES,distance=40)
		lines_a = StreamLines(
			field_func,
			virtual_time=3,
			min_magnitude=0,
			max_magnitude=3,
		).set_color_by_gradient([WHITE, BLUE_E])
		flow = AnimatedStreamLines(
			lines_a,
			line_anim_class=ShowPassingFlashWithThinningStrokeWidth
		)

		paddle = VGroup(Line(np.array([3, 0, 0]), np.array([-3, 0, 0])),
						Line(np.array([0, 3, 0]), np.array([0, -3, 0]))).set_stroke(width = 8).set_color(YELLOW_E)
		cylinder = ParametricSurface(
		lambda u, v: np.array([
		0.1*np.cos(u),
		0.1*np.sin(u),
		v,
		]), 
		u_min = 0, u_max = 2*np.pi, v_min = -0.2, v_max = 3.5, checkerboard_colors = [YELLOW_E, YELLOW_E]).fade(0.5)
		plane = ParametricSurface(lambda u, v: np.array([u, v, 0]), checkerboard_colors = [WHITE, WHITE]).fade(0.9)

		self.add(paddle, cylinder, flow)
		self.add_fixed_in_frame_mobjects(text)
		self.play(Rotating(paddle))
		self.wait()
		self.play(FadeIn(vec_field))
		self.remove(flow, text)
		self.bring_to_front(cylinder)
		#self.play(Rotating(paddle))
		self.wait()
		self.add_fixed_in_frame_mobjects(text_a)
		#self.play(ReplacementTransform(text, text_a))
		self.move_camera(phi=60*DEGREES,theta=30*DEGREES)
		self.wait()
