from manimlib.imports import *
class Test1(GraphScene):
    CONFIG = {
        "y_max" : 5,
        "y_min" : -5,
        "x_max" : 5,
        "x_min" : -5,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color" : BLUE, 
        "num_graph_anchor_points": 3000, #this is the number of points that graph manim
        "graph_origin" : ORIGIN,
        "x_labeled_nums": list(range(-5,6)),
        "y_labeled_nums": list(range(-5,6)),
        "x_axis_label":"$x$",
        "y_axis_label":"${ f }_{ 1 }(x)$"
    }
    def construct(self):
        self.setup_axes()
        cir1 = Circle(radius = 0.1, color = BLUE)
        graph_1 = self.get_graph(lambda x : x+2, 
                                    color = GREEN,
                                    x_min = -5, # Domain 1
                                    x_max = +1.9
                                    )
        graph_2 =self.get_graph(lambda x : x+2,
                                    color = GREEN,
                                    x_min = 2.1, # Domain 2
                                    x_max = 5
                                    )
        cir1.move_to(np.array([1,2,0]))
        self.play(ShowCreation(graph_1))
        self.play(ShowCreation(cir1))
        self.play(ShowCreation(graph_2))
