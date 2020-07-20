from manimlib.imports import *
import numpy as np

def div(coordinate):
	x,y = coordinate[:2]
	return np.array([
			x,
			y,
			0
	])


class Loop(Scene):
	def get_pending(self,path,proportion,dx=0.01):
		if proportion < 1:
			coord_i = path.point_from_proportion(proportion)
			coord_f = path.point_from_proportion(proportion+dx)
		else:
			coord_i = path.point_from_proportion(proportion-dx)
			coord_f = path.point_from_proportion(proportion)
		line = Line(coord_i,coord_f)
		angle = line.get_angle()
		return angle
	def construct(self):



		boundary = VMobject(stroke_color = "#F4EDED")
		boundary.set_points_smoothly([np.array([-2, 1.8,0]),np.array([-1.6, 0.5,0]),np.array([-3.2, -1.2,0]),np.array([2.6, -1.5,0]),np.array([1, 0,0]),np.array([3.5,2.3, 0]), np.array([-2,1.8, 0])])
		#c = TexMobject(r"C").next_to(surf,RIGHT+UP).set_color("#F4EDED")


		text = TexMobject(r"\oint \vec F \cdot \vec dr", r" = 0").shift(3*DOWN).set_stroke(width = 1.5)
		vec_field = VectorField(div)

		start_angle = self.get_pending(boundary, 0)

		pointer = Triangle(fill_opacity = 1).set_height(0.25).set_color(WHITE)
		pointer.set_fill(WHITE)
		pointer.move_to(boundary.get_start())
		pointer.rotate(- PI / 2)
		pointer.save_state()
		pointer.rotate(start_angle, about_point=pointer.get_center())
		

		self.play(ShowCreation(boundary), ShowCreation(vec_field))
		self.wait()
		self.play(Write(text[0]))
		def update_rotate_move(mob,alpha):
			pointer.restore()

			angle = self.get_pending(boundary,alpha)

			pointer.move_to(boundary.point_from_proportion(alpha))
			pointer.rotate(angle, about_point=pointer.get_center())
		self.play(
			#self.camera_frame.scale,.25,
			UpdateFromAlphaFunc(pointer,update_rotate_move),
			run_time=3,
			)
		self.play(ShowCreation(text[1]))
		self.play(Indicate(text))
		self.wait()
