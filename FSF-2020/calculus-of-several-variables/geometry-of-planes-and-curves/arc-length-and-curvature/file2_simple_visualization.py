from manimlib.imports import *

class a(GraphScene):
    CONFIG = {
    "x_min": -3,
    "x_max": 6,
    "y_min": -6,
    "y_max": 10,
    "graph_origin": ORIGIN
    }
    def construct(self):
        intro = TextMobject('Consider the following curve.')
        mid = TextMobject(r'Notice how the direction of the unit tangent vector\\changes with respect to the arc length.')
        outro = TextMobject(r'The rate of change of unit tangent with \\ respect to the arc length $ds$ is called curvature.\\Mathematically, curvature $ = k = \left|{\frac{dT}{ds}}\right|$')

        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)

        circle = Circle(radius = 0.95, color = GRAY, fill_opacity = 0.2, fill_color = RED)
        circle.set_stroke(width = 0.1)

        tgt1 = Arrow((-2.2*XTD,-0.5*YTD,0),(-1*XTD,1,0))
        tgt2 = Arrow((-1.2*XTD, 1.93*YTD,0),(0*XTD,1.6,0)).scale(1.2)
        tgt3 = Arrow((-0.3*XTD,3*YTD, 0), (1.5*XTD, 3*YTD,0))
        tgt4 = Arrow((1.4*XTD, 2*YTD,0),(2.4*XTD, 1*YTD,0)).scale(2.8)
        tgt5 = Arrow((2.4*XTD, 0, 0), (3.8*XTD,-2*YTD, 0)).scale(1.2).shift(0.26*RIGHT)
        tgt6 = Arrow((3.8*XTD,-1*YTD, 0), (4.8*XTD, -1*YTD, 0)).scale(2.8).shift(0.26*RIGHT)
        tgt7 = Arrow((5.3*XTD, 0, 0),(6.3*XTD,1,0)).shift(0.35*LEFT+0.1*DOWN).scale(1.3)

        dot1 = Dot(tgt1.get_start(), color = RED)
        dot2 = Dot(tgt2.get_start(), color = RED)
        dot3 = Dot(tgt3.get_start(), color = RED)
        dot4 = Dot(tgt4.get_start(), color = RED)
        dot5 = Dot(tgt5.get_start(), color = RED)
        dot6 = Dot(tgt6.get_start(), color = RED)
        dot7 = Dot(tgt7.get_start(), color = RED)

        arc = ArcBetweenPoints(dot1.get_center(), dot2.get_center(), color = GREEN_SCREEN, angle = 10*DEGREES).rotate(180*DEGREES)

        dots = VGroup(*[dot1, dot2, dot3, dot4, dot5, dot6, dot7])

        ds = CurvedArrow((-4, 2, 0), (tgt1.get_start() + tgt2.get_start()) / 2, color = YELLOW)
        ds_text = TextMobject(r'$ds$').next_to(ds, UP, buff = 0.1).shift(1.3*LEFT)

        self.setup_axes(hideaxes=True)

        def curve(x):
            return 3 - (3653*x**2)/5292 + (2477*x**3)/31752 + (13*x**4)/784 - (17*x**5)/5292 + (17*x**6)/63504

        # parabola_x_out = FunctionGraph(curve, x_min=-2, x_max=6, stroke_width = 2, color = BLUE)
        parabola_x_out = self.get_graph(curve)

        dot_x = Dot().rotate(PI/2).set_color(YELLOW_E)
        alpha_x = ValueTracker(-2)
        vector_x = self.get_tangent_vector(alpha_x.get_value(),parabola_x_out,scale=1.5)
        dot_x.add_updater(lambda m: m.move_to(vector_x.get_center()))
        vector_x.add_updater(
            lambda m: m.become(
                    self.get_tangent_vector(alpha_x.get_value()%1,parabola_x_out,scale=1.5)
                )
            )

        self.play(FadeIn(intro))
        self.wait(2)
        self.play(FadeOut(intro))
        self.setup_axes(hideaxes=False)
        self.play(ShowCreation(parabola_x_out), FadeIn(dots), FadeIn(ds), FadeIn(ds_text), FadeIn(arc))
        self.wait(2)
        self.play(FadeOut(self.axes), FadeOut(arc), FadeOut(parabola_x_out),FadeIn(mid), FadeOut(dots), FadeOut(ds), FadeOut(ds_text))
        self.wait(3)
        self.play(FadeOut(mid))
        self.play(FadeIn(self.axes), FadeIn(parabola_x_out), FadeIn(dots))
        self.add(vector_x)
        self.play(alpha_x.increment_value, 1, run_time=8, rate_func=linear)
        self.remove(vector_x)
        self.play(FadeOut(VGroup(*[self.axes, dots, parabola_x_out])))
        self.play(FadeIn(outro))
        self.wait(3)
        self.play(FadeOut(outro))
        self.wait(1)




    def get_tangent_vector(self, proportion, curve, dx=0.001, scale=1):
        coord_i = curve.point_from_proportion(proportion)
        coord_f = curve.point_from_proportion(proportion + dx)
        reference_line = Line(coord_i,coord_f)
        unit_vector = reference_line.get_unit_vector() * scale
        vector = Arrow(coord_i , coord_i + unit_vector, color = YELLOW, buff=0)
        return vector
