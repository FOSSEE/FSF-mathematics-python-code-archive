from manimlib.imports import *

def field_func(coordinate):
	x,y = coordinate[:2]
	return np.array([
					-y, 
					x,
					0
				])


class LineIntegral(MovingCameraScene, Scene):
	def setup(self):
		MovingCameraScene.setup(self)
		Scene.setup(self)

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

		vector_field = VectorField(field_func)
		vec_field_for_flow = VectorField(field_func, x_min = -1.5, x_max = 1.5, y_min = -1.5, y_max = 1.5)
		flow_rep = StreamLines(
        	field_func,
			virtual_time=4,
			min_magnitude=0,
			max_magnitude=2,
			dt = 0.1,
			x_min = -1, x_max = 1, y_min = -1, y_max = 1,
			).set_color_by_gradient([BLUE_E, TEAL, WHITE])
		flow = AnimatedStreamLines(
			flow_rep,
			line_anim_class=ShowPassingFlashWithThinningStrokeWidth
			)
		boundary = Circle(radius = 2).set_color("#7FFF00")
		
		start_angle = self.get_pending(boundary, 0)

		pointer = Triangle(fill_opacity = 1).set_height(0.25).set_color("#ffff00")
		pointer.set_fill("#ffff00")
		pointer.move_to(boundary.get_start())
		pointer.rotate(- PI / 2)
		pointer.save_state()
		pointer.rotate(start_angle, about_point=pointer.get_center())
		sym_1 = TexMobject(r"\oint \vec F \cdot \vec dr").next_to(pointer, RIGHT, buff = SMALL_BUFF).scale(0.7).set_color("#ffff00").add_background_rectangle()
		sym_2 = TexMobject(r"\nabla \times \vec F").scale(0.7).set_color(TEAL).add_background_rectangle()

		self.play(ShowCreation(vector_field))
		self.wait()
		self.add(flow)
		self.play(Write(boundary), Write(sym_2))
		self.wait(2)
		self.play(Write(pointer))
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
		self.play(Write(sym_1))
		self.wait()



