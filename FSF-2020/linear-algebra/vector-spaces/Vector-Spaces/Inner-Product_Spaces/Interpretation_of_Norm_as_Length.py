from manimlib.imports import *
import numpy as np
class Interpretation_of_norm_as_length(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 5,
        "y_min" : 0,
        "y_max" : 5,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color":LIGHT_GRAY,
        "x_axis_width": 5,
        "y_axis_height":5,
        "graph_origin" : ORIGIN + 2*DOWN + 2*LEFT,
        "enclude_zero_label": False
        
    }   
    def construct(self):
        self.setup_axes(animate=False)
        dot = Dot().scale(0.5)
        self.play(ShowCreation(dot))
        origin = TextMobject(r"(0, 0)").scale(0.5).shift(2.5*LEFT+2.2*DOWN)
        line1 = self.get_graph(lambda x : x, x_min=0,x_max=2,color=WHITE)
        line2 = Line().rotate(np.pi/2).shift(1*DOWN)
        text1 = TextMobject(r"$(v_1, 0)$").scale(0.5).shift(2.2*DOWN+0.2*RIGHT)
        text2 = TextMobject(r"$(0, v_2)$").scale(0.5).shift(2.5*LEFT)
        text3 = TextMobject(r"$(v_1, v_2)$").scale(0.5).shift(0.5*RIGHT)
        text4 = TextMobject(r"$| v_1 |$",color=RED_B).scale(0.5).shift(1*LEFT+2.3*DOWN)
        text5 = TextMobject(r"$| v_2 |$",color=RED_B).scale(0.5).shift(0.3*RIGHT+1*DOWN)
        text6 = TextMobject(r"$\sqrt{{v_1}^2 + {v_2}^2}$",color=RED_B).scale(0.5).rotate(np.pi/4).shift(1.3*LEFT+1*DOWN)
        line3 = Line(color=YELLOW).shift(1*LEFT+2*DOWN)
        self.play(ShowCreation(line1),ShowCreation(line2),ShowCreation(text1),ShowCreation(text2),ShowCreation(text3),ShowCreation(origin))
        self.wait(1.5)
        self.play(ShowCreation(line3),ShowCreation(text4))
        self.wait(1.5)
        line2 = Line(color=YELLOW).rotate(np.pi/2).shift(1*DOWN)
        self.play(ShowCreation(line2),ShowCreation(text5))
        self.wait(1.5)
        line1 = self.get_graph(lambda x : x, x_min=0,x_max=2,color=YELLOW)
        self.play(ShowCreation(text6),ShowCreation(line1))
        self.wait(4)
       