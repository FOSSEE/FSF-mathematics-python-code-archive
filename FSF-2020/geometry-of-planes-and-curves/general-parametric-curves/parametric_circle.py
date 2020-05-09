from manimlib.imports import *

class sine(GraphScene):
    CONFIG = {
    'x_min': -4,
    'x_max': 4,
    'y_min': -4,
    'y_max': 4,
    'graph_origin': ORIGIN,
    "x_axis_width": 8,
     "y_axis_height": 8,
    }
    def construct(self):
        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)
        self.setup_axes()
        xtext = TextMobject(r'$x = asin(t)\quad y = acos(t)$').shift(2*YTD*UP + 3*XTD*RIGHT)
        func_graph = self.get_graph(self.func_to_graph).rotate(-np.pi/2)
        func_graph2 = self.get_graph(self.func_to_graph2)
        group1 = [xtext,func_graph, func_graph2]
        group1 = VGroup(*group1)
        self.play(FadeIn(group1))
        self.wait(2)
        self.play(FadeOut(group1), FadeOut(self.axes))
        intro = TextMobject(r'What happens when we plot (x,y) for different values of $t$?')
        self.play(FadeIn(intro))
        self.wait(3)
        self.play(FadeOut(intro), FadeIn(group1), FadeIn(self.axes))
        dots = []
        for t in range(19):
            dot = Dot().shift((np.sin(t), np.cos(t), 0))
            dots.append(dot)
            self.play(FadeIn(dot))
        dots = VGroup(*dots)
        self.play(FadeOut(group1), FadeOut(dots), FadeOut(self.axes))
        outro = TextMobject(r'Hence, the locus of these points forms the circle $x^{2} + y^{2} = a^{2}$.')
        self.play(FadeIn(outro))
        self.wait(3)
        self.play(FadeOut(outro))

    def func_to_graph(self,x):
        return np.cos(x)
 
    def func_to_graph2(self,x):
        return np.sin(x)