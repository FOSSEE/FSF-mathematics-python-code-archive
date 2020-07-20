from manimlib.imports import *
import numpy as np

def pos_div(coordinate):
	x,y = coordinate[:2]
	return np.array([
			x,
			y,
			0
	])

def neg_div(coordinate):
	x,y = coordinate[:2]
	return np.array([
			-x,
			-y,
			0
	])

def zero_div(coordinate):
	x,y = coordinate[:2]
	y = 1.0
	return np.array([
			y,
			0,
			0
	])

def curl_c(coordinate):
	x,y = coordinate[:2]
	return np.array([
			y,
			-x,
			0
	])

def curl_ac(coordinate):
	x,y = coordinate[:2]
	return np.array([
			-y,
			x,
			0
	])




class Examples(Scene):
	def construct(self):

		vf1 = VectorField(pos_div, x_min = -1.5, x_max = 1.5, y_min = -1.5, y_max = 1.5).shift(2.5*UP, 4*LEFT)
		vf3 = VectorField(neg_div, x_min = -1.5, x_max = 1.5, y_min = -1.5, y_max = 1.5).shift(2.5*UP, 4*RIGHT)
		vf2 = VectorField(zero_div, x_min = -1.5, x_max = 1.5, y_min = -1.5, y_max = 1.5).move_to(np.array([0, 0.5, 0]))
		vf4 = VectorField(curl_c, x_min = -1.5, x_max = 1.5, y_min = -1.5, y_max = 1.5).shift(2*DOWN, 4*RIGHT)
		vf5 = VectorField(curl_ac, x_min = -1.5, x_max = 1.5, y_min = -1.5, y_max = 1.5).shift(2*DOWN, 4*LEFT)
		dot = Dot().move_to(vf1.get_center())
		label3 = TexMobject(r"\textit{Sink}", r"\textrm{div} F < 0").set_color(BLUE_E).scale(0.6).shift(3*DOWN + 0.7*RIGHT)
		label1 = TexMobject(r"\textit{Source}", r"\textrm{div} F > 0").set_color(YELLOW_E).scale(0.6).shift(2.8*DOWN + 0.7*RIGHT)
		label2 = TexMobject(r"\textrm{div} F =0", r"\textrm{ curl} F = 0").scale(0.6).shift(3*DOWN + 0.7*RIGHT)
		label4 = TexMobject(r"\textit{Clockwise rotation}", r"\textrm{curl} F < 0").set_color(BLUE_E).scale(0.6).shift(3*DOWN + 0.7*RIGHT)
		label5 = TexMobject(r"\textit{Counter-clockwise rotation}", r"\textrm{curl} F > 0").set_color(YELLOW_E).scale(0.6).shift(3*DOWN + 0.7*RIGHT)

		label1[1].next_to(label1[0], DOWN, buff = SMALL_BUFF).set_color(WHITE)
		label2[1].next_to(label2[0], DOWN, buff = SMALL_BUFF).set_color(WHITE)
		label3[1].next_to(label3[0], DOWN, buff = SMALL_BUFF).set_color(WHITE)

		label4[1].next_to(label4[0], DOWN, buff = SMALL_BUFF).set_color(WHITE)
		label5[1].next_to(label5[0], DOWN, buff = SMALL_BUFF).set_color(WHITE)

		lines_a = StreamLines(
			pos_div,
			virtual_time=1.5,
			min_magnitude=0,
			max_magnitude=1.5,
			x_min = -1, x_max = 1, y_min = -1, y_max = 1
		).shift(2.5*UP, 4*LEFT)
		lines1 = AnimatedStreamLines(
			lines_a,
			line_anim_class=ShowPassingFlashWithThinningStrokeWidth
		)

		lines_b = StreamLines(
			zero_div,
			virtual_time=1.5,
			min_magnitude=0,
			max_magnitude=1.5,
			x_min = -0.5, x_max = 0.5, y_min = -0.5, y_max = 0.5
		).move_to(np.array([-0.2, 0.5, 0]))
		lines2 = AnimatedStreamLines(
			lines_b,
			line_anim_class=ShowPassingFlashWithThinningStrokeWidth
		)

		lines_c = StreamLines(
			neg_div,
			virtual_time=1.5,
			min_magnitude=0,
			max_magnitude=1.5,
			x_min = -1, x_max = 1, y_min = -1, y_max = 1
		).shift(2.5*UP, 4*RIGHT)
		lines3 =(AnimatedStreamLines(
			lines_c,
			line_anim_class=ShowPassingFlashWithThinningStrokeWidth
		))

		lines_d = StreamLines(
			curl_c,
			virtual_time=1.5,
			min_magnitude=0,
			max_magnitude=1.5,
			x_min = -1, x_max = 1, y_min = -1, y_max = 1
		).shift(2*DOWN, 4*RIGHT)
		lines4 =(AnimatedStreamLines(
			lines_d,
			line_anim_class=ShowPassingFlashWithThinningStrokeWidth
		))

		lines_e = StreamLines(
			curl_ac,
			virtual_time=1.5,
			min_magnitude=0,
			max_magnitude=1.5,
			x_min = -1, x_max = 1, y_min = -1, y_max = 1
		).shift(2*DOWN, 4*LEFT)
		lines5 =(AnimatedStreamLines(
			lines_e,
			line_anim_class=ShowPassingFlashWithThinningStrokeWidth
		))
		self.play(Write(vf1))
		self.wait()
		self.add(lines1)
		self.play(ShowCreation(label1[0]), ShowCreation(label1[1]))
		self.wait(4)
		self.remove(lines1)
		self.play(Write(vf2))
		self.add(lines2)
		self.play(ReplacementTransform(label1, label2))
		self.play(Indicate(label2))
		self.wait(4)
		self.remove(lines2)
		self.play(Write(vf3))
		self.add(lines3)
		self.play(ReplacementTransform(label2, label3))
		self.play(Indicate(label3))
		self.wait(4)
		self.remove(lines3)
		self.play(Write(vf4))
		self.add(lines4)
		self.play(ReplacementTransform(label3, label4))
		self.play(Indicate(label4))
		self.wait(4)
		self.remove(lines4)
		self.play(Write(vf5))
		self.add(lines5)
		self.play(ReplacementTransform(label4, label5))
		self.play(Indicate(label5))
		self.wait(4)
		self.remove(lines5)
		self.wait()



