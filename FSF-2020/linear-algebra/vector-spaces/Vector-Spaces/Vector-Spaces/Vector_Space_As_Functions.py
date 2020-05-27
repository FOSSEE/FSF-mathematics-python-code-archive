from manimlib.imports import *
from scipy import sin,cos
class FunctionalVectorSpace(GraphScene):
    CONFIG = {
    "x_min": -5,
    "x_max": 5,
    "y_min": -5,
    "y_max": 5,
    "graph_origin": ORIGIN,
    }
    def construct(self):
        self.setup_axes(animate = True)        
        curve1 = self.get_graph(lambda x : sin(x), x_min=-5,x_max=5,color=YELLOW_E)
        curve2 = self.get_graph(lambda x : cos(x), x_min=-5,x_max=5,color=RED)
        self.play(ShowCreation(curve1))       
        fx=TextMobject(r"$f(x)$",color=YELLOW_E).scale(0.7)
        fx.shift(5*LEFT+0.7*UP)
        self.play(ShowCreation(fx))
        self.play(ShowCreation(curve2))
        gx=TextMobject(r"$g(x)$",color=RED).scale(0.7)
        gx.shift(5*LEFT+0.2*UP)
        self.play(ShowCreation(gx))
        self.wait(2)
        scaling=TextMobject("Scaling f(x) by 2 units",color=GOLD).scale(0.65)
        scaling.shift(3*LEFT+2.4*UP)
        curve3 = self.get_graph(lambda x : 2*sin(x), x_min=-5,x_max=5,color=BLUE)
        fx2=TextMobject(r"$2f(x)$",color=BLUE).scale(0.7)
        fx2.shift(5*LEFT+1*UP)
        self.play(Transform(curve1,curve3),FadeOut(fx),ShowCreation(fx2),ShowCreation(scaling))
        self.wait(3)
        hx = TextMobject(r"$h(x)$",color=PURPLE).scale(0.7)
        hx.shift(4.9*LEFT+1.5*UP)
        curve4 = self.get_graph(lambda x : 2*sin(x) + cos(x), x_min=-5,x_max=5,color=PURPLE)
        self.play(ShowCreation(curve4),ShowCreation(hx))
        self.play(FadeOut(curve2),FadeOut(curve1),FadeOut(fx2),FadeOut(gx),FadeOut(scaling))
        hxn=TextMobject(r"$h(x)$",color=PURPLE).scale(0.7)
        hxn.shift(3*RIGHT+2.4*UP)
        equal = TextMobject("=").scale(0.7)
        equal.shift(3.5*RIGHT+2.4*UP)
        fx2n=TextMobject(r"$2f(x)$",color=BLUE).scale(0.7)
        fx2n.shift(4.2*RIGHT+2.4*UP)
        add=TextMobject("+").scale(0.7)
        add.shift(4.8*RIGHT+2.4*UP)
        gxn=TextMobject(r"$g(x)$",color=RED).scale(0.7)
        gxn.shift(5.3*RIGHT+2.4*UP)
        vector_add=TextMobject("Vector Addition",color=GOLD).scale(0.65)
        vector_add.shift(3*UP+3*RIGHT)
        self.play(ShowCreation(hxn),ShowCreation(equal),ShowCreation(fx2n),ShowCreation(add),ShowCreation(gxn),ShowCreation(vector_add))
        self.wait(2)

        






     



    