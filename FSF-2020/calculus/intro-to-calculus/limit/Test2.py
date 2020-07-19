from manimlib.imports import *
class Test2(GraphScene):
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
        graph_1 = self.get_graph(lambda x : x+2, 
                                    color = GREEN,
                                    x_min = -5, # Domain 1
                                    x_max = +5
                                    )
        self.play(ShowCreation(graph_1))
        self.wait()
