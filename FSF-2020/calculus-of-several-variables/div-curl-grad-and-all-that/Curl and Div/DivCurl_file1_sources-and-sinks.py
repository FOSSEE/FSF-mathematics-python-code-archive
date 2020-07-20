from manimlib.imports import *
import numpy as np

def divergence(coordinate):
	x,y = coordinate[:2]
	return np.array([
			np.sin(x),
			np.cos(y),
			0
		])

def curl(coordinate):
    x,y = coordinate[:2]
    return np.array([
            np.sin(y),
            np.cos(x),
            0
        ])

class fluid_flow(Scene):
	def construct(self):



		ball_a = Dot().set_color_by_gradient(["#F87666", "#F53A23", PURPLE_E]).move_to(np.array([-6,-1,0])).fade(0.2).scale(1.2)
		ball_b = Dot().set_color_by_gradient(["#F87666", "#F53A23", PURPLE_E]).move_to(np.array([0.1,3,0])).fade(0.2).scale(1.2)
		ball_c = Dot().set_color_by_gradient(["#F87666", "#F53A23", PURPLE_E]).move_to(np.array([-0.5,-1, 0])).fade(0.2).scale(1.2)
		ball_d = Dot().set_color_by_gradient(["#F87666", "#F53A23", PURPLE_E]).move_to(np.array([4.5,-1.2,0])).fade(0.2).scale(1.2)
		ball2 = Dot().set_color_by_gradient(["#F87666", "#F53A23", PURPLE_E]).move_to(np.array([-0.5,0,0])).fade(0.2).scale(1.2)
		ball3 = Dot().set_color_by_gradient(["#F87666", "#F53A23", PURPLE_E]).move_to(np.array([-1.5,1.2,0])).fade(0.2).scale(1.2)
		ball4 = Dot().set_color_by_gradient(["#F87666", "#F53A23", PURPLE_E]).move_to(np.array([-1.5,-1.2,0])).fade(0.2).scale(1.2)
		ball5 = Sphere(radius = 0.2, chekerboard_colors =["#F87666", "#F53A23", PURPLE_E]).set_color_by_gradient(["#F87666", "#F53A23", PURPLE_E]).fade(0.2).move_to(np.array([-4.7,0,0]))

		flow_one = StreamLines(
			divergence,
			virtual_time=3,
			min_magnitude=0,
			max_magnitude=1,
		).set_color_by_gradient(["#003853", "#0478A1","#04AED9", WHITE])
		flow_div =(AnimatedStreamLines(
			flow_one,
			line_anim_class=ShowPassingFlashWithThinningStrokeWidth
		))

		flow_two = StreamLines(
			curl,
			
			virtual_time=3,
			min_magnitude=0,
			max_magnitude=1,
		).set_color_by_gradient(["#003853", "#0478A1","#04AED9", WHITE])
		flow_curl =(AnimatedStreamLines(
			flow_two,
			line_anim_class=ShowPassingFlashWithThinningStrokeWidth
		))

		label_div = TexMobject(r"\textit{Fluid flows out from }", r"\textit{sources }", r"\textit{and into }", r"\textit{sinks}" ).move_to(np.array([0,3.5, 0])).set_stroke(width = 1.5).scale(0.7)
		label_div[1].set_color("#F87666")
		label_div[3].set_color("#F87666")
		title_div = TexMobject(r"Divergence").set_stroke(width = 1.5).move_to(3*DOWN).set_color("#F87666").scale(1.2)
		label_curl = TexMobject(r"\textit{Fluid also rotates }", r"\textit{clockwise }", r"\textit{and }", r"\textit{counter-clockwise}" ).move_to(np.array([0,3.5, 0])).set_stroke(width = 1.5).scale(0.7)
		label_curl[1].set_color("#F87666")
		label_curl[3].set_color("#F87666")
		title_curl = TexMobject(r"Curl").set_stroke(width = 1.5).move_to(3*DOWN).set_color("#F87666").scale(1.2)




		self.add(flow_div, label_div)
		self.play(Write(title_div))
		self.wait(5)
		self.remove(flow_div)
		self.wait()
		self.add(flow_curl)
		self.play(ReplacementTransform(label_div, label_curl), ReplacementTransform(title_div, title_curl))
		self.wait(6)
