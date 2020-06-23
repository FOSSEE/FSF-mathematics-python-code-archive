from manimlib.imports import *

class Limit(GraphScene):
    CONFIG = {
    "x_min": 0,
    "x_max": 4,
    "y_min": 0,
    "y_max": 4,
    "graph_origin": ORIGIN + 3* DOWN+4*LEFT,
    "x_labeled_nums": list(range(0, 4)),
    "y_labeled_nums": list(range(0, 5)),
    }
    def construct(self):
        topic = TextMobject("Different paths of approach to limit point")
        topic.scale(1.5)
        topic.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        self.play(Write(topic))
        self.wait(1)
        self.play(FadeOut(topic))
        
        

        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)

        self.setup_axes(animate = True)

        y_x = self.get_graph(lambda x :  x, x_min = -1, x_max = 4)
        y_x_lab = self.get_graph_label(y_x, label = r"y = x")

        y_xsquare = self.get_graph(lambda x :  x*x, x_min = -1, x_max = 4)
        y_xsquare_lab = self.get_graph_label(y_xsquare, label = r"y = x^2")

        y_1 = self.get_graph(lambda x :  1, x_min = -1, x_max = 4)
        y_1_lab = self.get_graph_label(y_1, label = r"y = 1")

        y_2minusx = self.get_graph(lambda x :  2 - x, x_min = -1, x_max = 4, color = RED)
        y_2minusx_lab = self.get_graph_label(y_2minusx, label = r"y = 2 - x")

        limit_point = Dot().shift(self.graph_origin+1*XTD*RIGHT+1*YTD*UP)
        limit_point_lab = TextMobject(r"(1,1)") 
        limit_point_lab.next_to(limit_point, DOWN)

        self.play(ShowCreation(limit_point))
        self.play(Write(limit_point_lab))
        self.wait(1)

        self.play(ShowCreation(y_x))
        self.play(Write(y_x_lab))
        self.wait(1)

        self.play(ShowCreation(y_xsquare))
        self.play(Write(y_xsquare_lab))
        self.wait(1)

        self.play(ShowCreation(y_1))
        self.play(Write(y_1_lab))
        self.wait(1)

        self.play(ShowCreation(y_2minusx))
        self.play(Write(y_2minusx_lab))
        self.wait(1)

        

        