from manimlib.imports import *
import numpy as np
import math

class Unit_Circle(GraphScene):
    CONFIG = {
        "x_min" : -3,
        "x_max" : 3,
        "y_min" : -3,
        "y_max" : 3,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "x_labeled_nums" : list(np.arange(-3,4,1)),
        "y_labeled_nums" : list(np.arange(-3,4,1)),
        "graph_origin" : ORIGIN,
        "axes_color" : GREY,
        "x_axis_width": 6,
        "y_axis_height":6,
    }   

    def construct(self):
        self.setup_axes(animate = True)
        circle = Circle(radius=1,color=BLUE)
        self.play(ShowCreation(circle))
        dot1 = Dot(color=RED).scale(0.7)
        dot1.shift(1*UP)
        dot2 = Dot(color=RED).scale(0.7)
        dot2.shift(1*LEFT)
        dot3 = Dot(color=RED).scale(0.7)
        dot3.shift(1*DOWN)
        dot4 = Dot(color=RED).scale(0.7)
        dot4.shift(1*RIGHT)
        dot5= Dot(color=RED).scale(0.7)
        dot6 = Dot(color=RED).scale(0.7)
        dot5.shift(0.5*RIGHT+(math.sqrt(3)/2)*UP)
        dot6.shift(0.5*LEFT+(math.sqrt(3)/2)*DOWN)
        dot7 = Dot(color=RED).scale(0.7)
        dot7.shift(math.sqrt(2)/2*RIGHT+math.sqrt(2)/2*UP)
        dot8 = Dot(color=RED).scale(0.7)
        dot8.shift(math.sqrt(2)/2*LEFT+math.sqrt(2)/2*UP)
        dot9 = Dot(color=RED).scale(0.7)
        dot9.shift(0.5*LEFT+(math.sqrt(3)/2)*UP)
        dot10 = Dot(color=RED).scale(0.7)
        dot10.shift(math.sqrt(3)/2*LEFT+0.5*UP)
        dot11=Dot(color=RED).scale(0.7)
        dot11.shift(math.sqrt(3)/2*RIGHT+0.5*UP)
        dot12= Dot(color=RED).scale(0.7)
        dot12.shift(math.sqrt(3)/2*LEFT+0.5*DOWN)
        dot13=Dot(color=RED).scale(0.7)
        dot13.shift(math.sqrt(2)/2*RIGHT+math.sqrt(2)/2*DOWN)
        dot14=Dot(color=RED).scale(0.7)
        dot14.shift(math.sqrt(2)/2*LEFT+math.sqrt(2)/2*DOWN)
        dot15=Dot(color=RED).scale(0.7)
        dot15.shift(math.sqrt(3)/2*RIGHT+0.5*DOWN)
        dot16=Dot(color=RED).scale(0.7)
        dot16.shift(0.5*RIGHT+(math.sqrt(3)/2)*DOWN)
        self.play(ShowCreation(dot1),ShowCreation(dot2))
        self.play(ShowCreation(dot3),ShowCreation(dot4))
        self.play(ShowCreation(dot5),ShowCreation(dot6))
        self.play(ShowCreation(dot7),ShowCreation(dot8))
        self.play(ShowCreation(dot9),ShowCreation(dot10))
        self.play(ShowCreation(dot11),ShowCreation(dot12))
        self.play(ShowCreation(dot13),ShowCreation(dot14))
        self.play(ShowCreation(dot15),ShowCreation(dot16))
        self.wait(4)
    


