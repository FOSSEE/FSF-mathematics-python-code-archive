from manimlib.imports import *
from scipy import sin 
class Integral_Properties(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 5,
        "y_min" : 0,
        "y_max" : 6,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color":LIGHT_GRAY,
        "x_labeled_nums" : list(range(6)),
        "y_labeled_nums" : list(range(6))
    }   
    def construct(self):
        self.setup_axes(animate=False)
        curve1 = self.get_graph(lambda x : sin(x), x_min=0,x_max=2.5,color=RED)
        curve2 = self.get_graph(lambda x : x, x_min=0,x_max=2.5,color=DARK_BLUE)
        curve3 = self.get_graph(lambda x : sin(x) + x, x_min=0,x_max=2.5,color=GREEN)
        fx = TextMobject(r"$f(x)$").scale(0.5).shift(1*RIGHT+1.8*DOWN)
        gx = TextMobject(r"$g(x)$").scale(0.5).shift(1*RIGHT)
        sum = TextMobject(r"$f(x) + g(x)$").scale(0.5).shift(1.3*RIGHT+0.6*UP)
        area1 = self.get_area(curve1,0,2.5)
        area2 = self.get_area(curve2,0,2.5)
        area3 = self.get_area(curve3,0,2.5)        
        area2.set_fill(color=PURPLE)
        area3.set_fill(color=ORANGE)
        text1=TextMobject(r"$\int_{0}^{2.5}$ f(x) dx = Area under the curve f(x)",color=BLUE_C).scale(0.7).shift(2.7*RIGHT+3*UP)
        text2=TextMobject(r"$\int_{0}^{2.5}$ g(x) dx = Area under the curve g(x)",color=PURPLE_B).scale(0.7).shift(2.7*RIGHT+2.4*UP)
        text3=TextMobject(r"Area under the curve f(x) + g(x) = $\int_{0}^{2.5} (f(x) + g(x)) dx$",color=ORANGE).scale(0.7).shift(2.7*RIGHT+1.8*UP)
        text4=TextMobject(r"\text{$\int_{0}^{2.5}$ (f(x) + g(x)) dx}",r"\text{ = }",r"\text{ $\int_{0}^{2.5}$ f(x) dx }",r"\text{+}",r"\text{$\int_{0}^{2.5}$ g(x) dx}").scale(0.62).shift(2.7*RIGHT+2.7*UP)
        text4[0].set_color(ORANGE)
        text4[2].set_color(BLUE_C)
        text4[4].set_color(PURPLE_B)
        self.play(ShowCreation(curve1), ShowCreation(fx))
        self.wait(1.2)
        self.play(ShowCreation(curve2),ShowCreation(gx))
        self.wait(1.2)
        self.play(ShowCreation(area1))
        self.play(ShowCreation(text1))
        self.wait(1.5)
        self.play(ShowCreation(area2))
        self.play(ShowCreation(text2))
        self.wait(1.5)
        self.play(ShowCreation(curve3),ShowCreation(sum))
        self.play(ShowCreation(area3))
        self.play(ShowCreation(text3))
        self.wait(2)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3))
        self.wait(1)
        self.play(ShowCreation(text4))
        self.wait(3)
        self.play(FadeOut(curve1),FadeOut(curve2),FadeOut(area1),FadeOut(area2))
        self.wait(1.5)
        self.play(FadeOut(text4),FadeOut(area2),FadeOut(curve2),FadeOut(gx),FadeOut(curve3),FadeOut(sum),FadeOut(area3),ShowCreation(curve1),ShowCreation(fx))
        self.wait(1.5)
        self.play(ShowCreation(area1),ShowCreation(text1))
        self.wait(1.5)
        curve4 = self.get_graph(lambda x : 2*sin(x), x_min=0,x_max=2.5,color=RED)
        area4 = self.get_area(curve4,0,2.5)
        area4.set_fill(color=YELLOW)
        fx2 = TextMobject(r"$2f(x)$").scale(0.7).shift(1*RIGHT+1.2*DOWN)
        scalar_mul=TextMobject(r"$\int_{0}^{2.5} ( 2f(x) ) dx$ = 2 $\times$ Area under the curve f(x)",color=YELLOW).scale(0.7).shift(2.7*RIGHT+2.4*UP)
        self.play(ShowCreation(curve4),ShowCreation(fx2))
        self.wait(1)
        self.play(ShowCreation(area4))
        self.wait(2)
        self.play(ShowCreation(scalar_mul))
        self.wait(2)
        text5=TextMobject(r"\text{$\int_{0}^{2.5}$ (2 f(x)) dx}",r"\text{ = }",r"\text{2 $\int_{0}^{2.5}$ f(x) dx }").scale(0.67).shift(2.7*RIGHT+2.7*UP)
        text5[0].set_color(YELLOW)
        text5[2].set_color(BLUE_C)
        self.play(FadeOut(text1),FadeOut(scalar_mul))
        self.wait(1)
        self.play(ShowCreation(text5))
        self.wait(3)
 
