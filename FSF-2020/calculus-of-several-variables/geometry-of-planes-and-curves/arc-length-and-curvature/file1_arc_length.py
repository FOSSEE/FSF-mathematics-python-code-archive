from manimlib.imports import *


class arcl(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 10,
        "y_min" : 0,
        "y_max" : 6,
        "graph_origin": ORIGIN,
        "x_axis_width": 10,
        "y_axis_height": 6 ,
        "x_tick_frequency": 2,
        "y_tick_frequency": 2,
        "Func":lambda x :  1+x**1.3*np.exp(-.12*(x-2)**2)*np.sin(x/4),
    }
    def construct(self):
        self.setup_axes(hideaxes = True)
        def curve_(x):
            return 3 - (3653*x**2)/5292 + (2477*x**3)/31752 + (13*x**4)/784 - (17*x**5)/5292 + (17*x**6)/63504

        curve = FunctionGraph(curve_, x_min=-2, x_max=6, stroke_width = 2, color = BLUE).scale(0.1).move_to(ORIGIN)
        lines = [Line(length = 0.05, color = RED) for i in range(10)]
        lines[0].move_to(np.array([curve_(-2),-2, 0]))



        # self.play(FadeIn(curve))
        # self.wait(2)
        self.play(ApplyMethod(curve.scale, 10))
        self.play(FadeIn(VGroup(*lines)))
        self.wait(5)
