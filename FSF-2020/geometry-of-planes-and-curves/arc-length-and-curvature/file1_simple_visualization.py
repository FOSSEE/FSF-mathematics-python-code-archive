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
        outro = TextMobject(r'This is called curvature.\\Mathematically, curvature $ = k = \left|{\frac{dT}{ds}}\right|$')

        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)
          
        self.setup_axes(hideaxes=True)
        graphobj = self.get_graph(self.curve)
        self.play(FadeIn(intro))
        self.wait(2)
        self.play(FadeOut(intro))
        self.setup_axes(hideaxes=False)
        self.play(ShowCreation(graphobj))
        self.wait(1)
        self.play(FadeOut(self.axes), FadeOut(graphobj),FadeIn(mid))
        self.wait(2)
        self.play(FadeOut(mid))
        self.play(FadeIn(self.axes), FadeIn(graphobj))

        tgt1 = Arrow((-2.2*XTD,-0.5*YTD,0),(-1*XTD,1,0))
        tgt2 = Arrow((-1.2*XTD, 1.93*YTD,0),(0*XTD,1.6,0)).scale(1.2)
        tgt3 = Arrow((-0.3*XTD,3*YTD, 0), (1.5*XTD, 3*YTD,0))
        tgt4 = Arrow((1.4*XTD, 2*YTD,0),(2.4*XTD, 1*YTD,0)).scale(2.8)

        tangents = [tgt1, tgt2, tgt3, tgt4]
        for tangent in tangents:
            self.play(ShowCreation(tangent))
            self.wait(1)
        tangents = VGroup(*tangents)
        self.play(FadeOut(self.axes), FadeOut(graphobj), FadeOut(tangents))
        self.wait(1)
        self.play(FadeIn(outro))
        self.wait(2)
        self.play(FadeOut(outro))
        self.wait(1)
        

    def curve(self, x):
        return 3 - (3653*x**2)/5292 + (2477*x**3)/31752 + (13*x**4)/784 - (17*x**5)/5292 + (17*x**6)/63504