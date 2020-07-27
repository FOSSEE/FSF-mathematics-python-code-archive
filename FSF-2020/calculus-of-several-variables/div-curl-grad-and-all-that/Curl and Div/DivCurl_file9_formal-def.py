from manimlib.imports import *
import numpy as np



def func(coordinate):
	x,y = coordinate[:2]
	return np.array([
			1.9*np.cos(x+2*y),
			1.5*np.sin(x-2*y),
			0
	])

def coord(x,y,z=0):
	return np.array([x,y,z])

class Instrument(Scene):
	CONFIG = {
		"x_coords": ([1, 2.2, 3.9, 3, -0, -0.2, 1]),
		"y_coords": ([1.5, 1, -0.5, -2.0, -1.4, 0.5, 1.5]),
	}

	def setup(self):
		self.tuples = list(zip(self.x_coords,self.y_coords))
		dots = self.get_all_mobs()

	def get_dots(self, coords):
		dots = VGroup(*[Dot(coord(x,y)) for x,y in coords])
		return dots
	
	def get_all_mobs(self):
		dots = self.get_dots(self.tuples)
		return dots


class Curl_one(MovingCameraScene, Instrument):
	def setup(self):
		MovingCameraScene.setup(self)
		Instrument.setup(self)


	def construct(self):
		vec = VectorField(func)


		frame_one = Circle(radius = 0.5).move_to(np.array([4, 2, 0]))
		dot = Dot(frame_one.get_center()).scale(0.5)
		surface = VMobject()
		surface.set_points_smoothly([*[coord(x,y) for x,y in self.tuples]])
		surface.move_to(dot.get_center()).set_stroke(width = 0.5)
		
		label = TexMobject(r"A").scale(0.5).next_to(dot, LEFT+UP, buff = SMALL_BUFF)
		#self.add(frame_one)
		self.camera_frame.save_state()
		self.play(
			self.camera_frame.set_width,frame_one.get_width()*7.0,
			self.camera_frame.move_to,frame_one)


	

		self.add(vec, dot, label)
		lines = StreamLines(
			func,
			virtual_time=7,
			min_magnitude=0,
			max_magnitude=8,
		)
		lines1 = AnimatedStreamLines(
			lines,
			line_anim_class=ShowPassingFlashWithThinningStrokeWidth
		)

		self.add(lines1)
		self.wait(3)
		self.play(Restore(self.camera_frame))
		self.wait(2)
		self.add(surface)
		self.wait(3)
		self.play(ApplyMethod(surface.scale, 0.01), run_time = 2)
		self.remove(surface)
		self.wait(2)
