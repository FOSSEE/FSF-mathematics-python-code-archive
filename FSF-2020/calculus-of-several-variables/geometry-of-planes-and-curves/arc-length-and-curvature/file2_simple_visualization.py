from manimlib.imports import *

class randomcurve(GraphScene):
    CONFIG = {
    "x_min": -4,
    "x_max": 6,
    "y_min": -6,
    "y_max": 10,
    "graph_origin": ORIGIN
    }
    def construct(self):
        intro = TextMobject('Consider the following curve.')
        mid = TextMobject(r'Notice how the direction of the unit tangent vectors\\changes with respect to the arc length.')
        outro = TextMobject(r'The rate of change of unit tangents with \\ respect to the arc length $ds$ is called curvature.\\Mathematically, curvature $ = k = \left|{\frac{dT}{ds}}\right|$')

        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)

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
        graphobj = self.get_graph(self.curve)
        self.play(FadeIn(intro))
        self.wait(2)
        self.play(FadeOut(intro))
        self.setup_axes(hideaxes=False)
        self.play(ShowCreation(graphobj), FadeIn(dots), FadeIn(ds), FadeIn(ds_text), FadeIn(arc))
        self.wait(1)
        self.play(FadeOut(self.axes), FadeOut(arc), FadeOut(graphobj),FadeIn(mid), FadeOut(dots), FadeOut(ds), FadeOut(ds_text))
        self.wait(3)
        self.play(FadeOut(mid))
        self.play(FadeIn(self.axes), FadeIn(graphobj), FadeIn(dots))

        tangents = [tgt1, tgt2, tgt3, tgt4, tgt5, tgt6, tgt7]
        for tangent in tangents:
            self.play(ShowCreation(tangent), run_time = 0.2)
            self.wait(1)
        tangents = VGroup(*tangents)
        self.play(FadeOut(self.axes), FadeOut(graphobj), FadeOut(tangents), FadeOut(dots))
        self.wait(1)
        self.play(FadeIn(outro))
        self.wait(3)
        self.play(FadeOut(outro))
        self.wait(1)


    def curve(self, x):
        return 3 - (3653*x**2)/5292 + (2477*x**3)/31752 + (13*x**4)/784 - (17*x**5)/5292 + (17*x**6)/63504
