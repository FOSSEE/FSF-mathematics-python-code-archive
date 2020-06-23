from manimlib.imports import *

class SineVectors(GraphScene):
    CONFIG = {
    "x_min": 0,
    "x_max": 10,
    "y_min": -1,
    "y_max": 1,
    "graph_origin": ORIGIN+4*LEFT,
    #"x_labeled_nums": list(range(-5, 6)),
    #"y_labeled_nums": list(range(0, 5)),
    }
    def construct(self):

       
        


        XTD = self.x_axis_width/(self.x_max - self.x_min)
        YTD = self.y_axis_height/(self.y_max - self.y_min)

        self.setup_axes(animate = True)


        sine1 = self.get_graph(lambda x :  np.sin(x), x_min = 0, x_max = 1.575, color = GREEN)

        point1 = Dot().shift(self.graph_origin+1*YTD*UP + 1.575*XTD*RIGHT)
        point1_lab = TextMobject(r"$t = (\frac{\pi}{2})$") 
        point1_lab.scale(0.7)
        point1_lab.next_to(point1, UP)

        vector1 = Arrow(self.graph_origin, self.graph_origin+1*YTD*UP + 1.575*XTD*RIGHT, buff=0.1, color = RED)
        vector1_lab = TextMobject(r"$r(\frac{\pi}{2})$", color = RED) 
        vector1_lab.move_to(self.graph_origin+1.5*XTD*RIGHT+ 0.5*YTD*UP)

        self.play(GrowArrow(vector1),Write(vector1_lab))
        self.play(ShowCreation(point1), Write(point1_lab))
        self.play(ShowCreation(sine1))
        self.wait(1)


        sine2 = self.get_graph(lambda x :  np.sin(x), x_min = 1.575, x_max = 3.15, color = GREEN)

        point2 = Dot().shift(self.graph_origin+3.15*XTD*RIGHT)
        point2_lab = TextMobject(r"$t = (\pi)$") 
        point2_lab.scale(0.7)
        point2_lab.next_to(point2, UP+RIGHT)

        vector2 = Arrow(self.graph_origin, self.graph_origin+3.15*XTD*RIGHT, buff=0.1, color = BLUE)
        vector2_lab = TextMobject(r"$r(\pi)$", color = BLUE) 
        vector2_lab.move_to(self.graph_origin+1.5*XTD*RIGHT+ 0.15*YTD*UP)

        self.play(GrowArrow(vector2),Write(vector2_lab))
        self.play(ShowCreation(point2), Write(point2_lab))
        self.play(ShowCreation(sine2))
        self.wait(1)


        sine3 = self.get_graph(lambda x :  np.sin(x), x_min = 3.15, x_max = 4.725, color = GREEN)

        point3 = Dot().shift(self.graph_origin+1*YTD*DOWN + 4.725*XTD*RIGHT)
        point3_lab = TextMobject(r"$t = (\frac{3\pi}{2})$") 
        point3_lab.scale(0.7)
        point3_lab.next_to(point3, DOWN)

        vector3 = Arrow(self.graph_origin, self.graph_origin+1*YTD*DOWN + 4.725*XTD*RIGHT, buff=0.1, color = YELLOW_C)
        vector3_lab = TextMobject(r"$r(\frac{3\pi}{2})$", color = YELLOW_C) 
        vector3_lab.move_to(self.graph_origin+2*XTD*RIGHT+ 0.7*YTD*DOWN)

        self.play(GrowArrow(vector3),Write(vector3_lab))
        self.play(ShowCreation(point3), Write(point3_lab))
        self.play(ShowCreation(sine3))
        self.wait(1)


        sine4 = self.get_graph(lambda x :  np.sin(x), x_min = 4.725, x_max = 6.3, color = GREEN)

        point4 = Dot().shift(self.graph_origin+6.3*XTD*RIGHT)
        point4_lab = TextMobject(r"$t = (2\pi)$") 
        point4_lab.scale(0.7)
        point4_lab.next_to(point4, UP+RIGHT)

        vector4 = Arrow(self.graph_origin, self.graph_origin+6.3*XTD*RIGHT, buff=0.1, color = PURPLE)
        vector4_lab = TextMobject(r"$r(2\pi)$", color = PURPLE) 
        vector4_lab.move_to(self.graph_origin+4.5*XTD*RIGHT+ 0.15*YTD*DOWN)

        self.play(GrowArrow(vector4),Write(vector4_lab))
        self.play(ShowCreation(point4), Write(point4_lab))
        self.play(ShowCreation(sine4))
        self.wait(3)

