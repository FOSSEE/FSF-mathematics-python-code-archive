from manimlib.imports import *

class circleC(GraphScene):
    CONFIG = {
    "x_min": -6,
    "x_max": 6,
    "y_min": -6,
    "y_max": 6,
    "graph_origin": ORIGIN,
    "x_axis_width": 12,
    "y_axis_height": 12
    }
    def construct(self):
        epiphany = TextMobject(r'Driving a vehicle on which of \\ the two paths would be easier?').scale(0.6).shift(3.5*LEFT + 3*UP)
        outro = TextMobject(r'The larger path, due to its \\ smaller curvature, since $k = \frac{1}{R}$.').scale(0.6).shift(3.7*LEFT + 3*UP)
        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)

        circle = Circle(radius = 2, color = BLUE)
        circle2 = Circle(radius = 3, color = GREEN_E)

        self.setup_axes(hideaxes=True)
        self.play(FadeIn(self.axes), Write(circle, run_time = 2), FadeIn(epiphany))
        self.play(Write(circle2, run_time = 3))
        self.play(ReplacementTransform(epiphany, outro))
        self.wait(2)
        self.play(FadeOut(VGroup(*[self.axes, circle, circle2, epiphany, outro])))
