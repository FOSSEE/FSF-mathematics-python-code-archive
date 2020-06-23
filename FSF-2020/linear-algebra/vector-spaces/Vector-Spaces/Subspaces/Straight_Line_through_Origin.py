from manimlib.imports import *
from scipy import exp, sin, log,tan,cos
class Straight_Line(GraphScene):
    CONFIG = {
        "x_min" : -4,
        "x_max" : 4,
        "y_min" : -4,
        "y_max" : 4,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "x_labeled_nums" : list(np.arange(-4,5,1)),
        "y_labeled_nums" : list(np.arange(-4,5,1)),
        "graph_origin" : ORIGIN+0.7*DOWN,
        "axes_color" : GREY,
        "x_axis_width": 6,
        "y_axis_height":6,
    }   
    def construct(self):
        self.setup_axes(animate=True)
        line_1 = self.get_graph(lambda x : x, x_min=-3,x_max=3,color=YELLOW)
        self.play(ShowCreation(line_1))
        text1 = TextMobject("ax + by = 0",color=BLUE_B)
        text1.shift(3*RIGHT+2*UP)
        text1.scale(0.65)
        dot = Dot(color=BLUE_B).shift(0.7*DOWN)
        dot.scale(1.3)
        self.play(ShowCreation(dot))
        text2 = TextMobject("Line passing through the origin")
        text2.scale(0.7)
        text2.shift(3.5*UP)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(1)
        self.play(FadeOut(line_1),FadeOut(text2),FadeOut(text1))
        text4=TextMobject("Line not passing through the origin")
        text4.scale(0.7)
        text4.shift(3.5*UP)
        self.play(ShowCreation(text4))
        
        line_2 = self.get_graph(lambda x : 2.5*x +1, x_min = -2, x_max=1, color = RED)
        text3 = TextMobject(r"ax + by $\neq 0$",color=BLUE_B)
        text3.scale(0.65)
        self.play(ShowCreation(line_2))
        text3.shift(1.5*RIGHT+2.2*UP)
        self.play(ShowCreation(text3))
        self.wait(1)
        
    
        