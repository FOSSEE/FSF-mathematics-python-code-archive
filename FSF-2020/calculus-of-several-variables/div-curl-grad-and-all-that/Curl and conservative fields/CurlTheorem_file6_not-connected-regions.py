from manimlib.imports import *

class Connected(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		self.add(axes)

		connected2D = Circle(radius = 2, fill_color = BLUE_E, fill_opacity = 0.8).set_color(BLUE_E)
		connected2D_label = TextMobject("Two dimensional, simply connected").move_to(np.array([0, -3, 0])).set_color(YELLOW_E)

		connected3D = Sphere(radius = 2, checkerboard_colors = [BLUE_E, BLUE_E], stroke_color = BLUE_E).fade(0.5)
		connected3D_label = TextMobject("Three dimensional, simply connected").move_to(np.array([0, -3, 0])).set_color(YELLOW_E)

		self.set_camera_orientation(phi = 0, theta = 0, distance = 40)

		self.add(connected2D)
		self.add_fixed_in_frame_mobjects(connected2D_label)
		self.wait(2)
		self.play(FadeOut(connected2D), FadeIn(connected3D))
		self.play(FadeOut(connected2D_label))
		self.add_fixed_in_frame_mobjects(connected3D_label)
		self.move_camera(phi = 45*DEGREES, theta = 45*DEGREES)
		self.begin_ambient_camera_rotation(rate=.2)
		self.wait(2)



class NotConnected(ThreeDScene):
	def construct(self):
		axes = ThreeDAxes()
		self.add(axes)

		Nconnected2D = Annulus(fill_color = BLUE_E, fill_opacity = 0.8).set_color(BLUE_E)
		Nconnected2D_label = TextMobject("Two dimensional, not simply connected").move_to(np.array([0, -3, 0])).set_color(YELLOW_E)

		Nconnected3D = ParametricSurface(lambda u, v: np.array([(2.5 + np.cos(v))*np.cos(u),
																(2.5 + np.cos(v))*np.sin(u),
																np.sin(v)]),
		u_min = 0, u_max = 2*np.pi, v_min = 0, v_max = 2*np.pi, 
		checkerboard_colors = [BLUE_E, BLUE_E], stroke_color = BLUE_E).fade(0.5)
		Nconnected3D_label = TextMobject("Three dimensional, not simply connected").move_to(np.array([0, -3, 0])).set_color(YELLOW_E)

		self.set_camera_orientation(phi = 0, theta = 0, distance = 40)

		self.play(ShowCreation(Nconnected2D))
		self.add_fixed_in_frame_mobjects(Nconnected2D_label)
		self.wait(2)
		self.play(FadeOut(Nconnected2D), FadeIn(Nconnected3D))
		self.play(FadeOut(Nconnected2D_label))
		self.add_fixed_in_frame_mobjects(Nconnected3D_label)
		self.move_camera(phi = 45*DEGREES, theta = 45*DEGREES)
		self.begin_ambient_camera_rotation(rate=.2)
		self.wait(2)

