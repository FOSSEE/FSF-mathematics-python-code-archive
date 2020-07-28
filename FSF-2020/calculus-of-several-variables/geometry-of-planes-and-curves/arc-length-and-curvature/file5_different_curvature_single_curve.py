from manimlib.imports import *

class GR(GraphScene):
    CONFIG = {
        "x_axis_label": "",
        "y_axis_label": "",
        "x_min": -4,
        "x_max": 6,
        "y_min": -6,
        "y_max": 10,
        "graph_origin": ORIGIN,
        'x_tick_frequency': 20,
        'y_tick_frequency': 20
    }

    def construct(self):

        self.setup_axes()
        def curve(x):
            return 3 - (3653*x**2)/5292 + (277*x**3)/31752 + (13*x**4)/784 - (17*x**5)/5292 + (170*x**6)/63504

        graph = FunctionGraph(curve, x_min=-2, x_max=6, stroke_width = 2, color = BLUE)

        tracker = ValueTracker(-2)

        text = TextMobject(r'$\because R_{1} > R_{2}$, the curvature at \\ point $P_{1}$ is less than that \\ at point $P_{2}$ as $\kappa = \frac{1}{R}$').shift(3.2*LEFT+3*UP).scale(0.6)

        dot1 = Dot((0,3,0), color = YELLOW)
        dot1label = TextMobject(r'$P_{1}$').next_to(dot1, UP+RIGHT, buff = 0.1)
        dot2 = Dot((2.9,-0.47, 0), color = YELLOW)
        dot2label = TextMobject(r'$P_{2}$').next_to(dot2, DOWN, buff = 0.1)
        dots = VGroup(*[dot1, dot2, dot1label, dot2label])

        def get_tangent_line():
            line = Line(
                ORIGIN, 2 * RIGHT,
                color=RED,
                stroke_width=4,
            )
            dx = 0.0001

            x = tracker.get_value()
            p0 = np.array([x-dx,curve(x-dx),0])
            p1 = np.array([x, curve(x), 0])
            p2 = np.array([x + dx, curve(x + dx), 0])

            angle = angle_of_vector(p2 - p1)
            line.rotate(angle)
            line.move_to(p0)
            return line

        circle1 = Circle(radius = 0.8, color = GREY, opacity = 0.2).shift(2.2*UP)
        tgt1 = Line((-2,3,0), (2,3,0), color = GREY, opacity = 0.2).scale(0.4)

        r1 = Line(circle1.get_center(), circle1.get_center() + np.array([0,0.8,0]), color=GREEN_SCREEN)
        r1label = TextMobject(r'$R_{1}$',color=WHITE).next_to(r1, RIGHT, buff = 0.1).scale(0.6)

        curvature1 = VGroup(*[circle1, tgt1, r1, r1label])

        circle2 = Circle(radius = 0.2, color = GREY, opacity = 0.2).shift(0.3*DOWN + 2.9*RIGHT)
        tgt2 = Line((4,-2,0), (6, -2, 0), color = GREY, opacity = 0.2).scale(0.5).shift(2.1*LEFT + 1.5*UP)

        r2 = Line(circle2.get_center(), circle2.get_center() - np.array([0,0.2,0]), color=GREEN_SCREEN)
        r2label = TextMobject(r'$R_{2}$', color=WHITE).next_to(r2.get_start(), np.array([0,0,0]), buff = 0).scale(0.4)

        curvature2 = VGroup(*[circle2, tgt2, r2, r2label])

        line = always_redraw(get_tangent_line)

        self.add(graph, line, dots, text)
        self.wait(1.2)
        self.play(tracker.set_value, 4, rate_func=smooth, run_time=10)
        self.play(FadeIn(curvature1), FadeIn(curvature2))
        self.wait(2)
        self.play(FadeOut(VGroup(*[curvature1, curvature2, graph, self.axes, line, dots, text])))
        self.wait()
