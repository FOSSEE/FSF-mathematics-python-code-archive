from manimlib.imports import *
from scipy import sin,cos
class Inner_Product_Space_Example(GraphScene):
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
        self.setup_axes(animate=True)
        curve1 = self.get_graph(lambda x : sin(x), x_min=0,x_max=2.3,color=RED)
        curve2 = self.get_graph(lambda x : x, x_min=0,x_max=2.3,color=DARK_BLUE)
        curve3 = self.get_graph(lambda x : 1.4, x_min=0,x_max=2.3,color=GREEN)
        text1 = TextMobject(r"$f(x)$").scale(0.5).shift(1.77*DOWN+0.55*RIGHT)
        
        text2 = TextMobject(r"$g(x)$").scale(0.5).shift(0.15*DOWN+0.55*RIGHT)
        text3 = TextMobject(r"$h(x)$").scale(0.5).shift(1.03*DOWN+0.55*RIGHT)

        self.play(ShowCreation(curve1),ShowCreation(text1))
        self.wait(1)
        self.play(ShowCreation(curve2),ShowCreation(text2))
        self.wait(1)
        self.play(ShowCreation(curve3),ShowCreation(text3))
        self.wait(2)
        curve4 = self.get_graph(lambda x : sin(x) + x, x_min=0,x_max=2.3,color=YELLOW)
        text4 = TextMobject(r"$f(x) + g(x)$").scale(0.5).shift(0.6*UP+1*RIGHT)
        self.wait(1.5)

        self.play(ShowCreation(curve4),ShowCreation(text4),FadeOut(curve2),FadeOut(text2),FadeOut(curve1),FadeOut(text1))
        self.wait(1.5)
        text5 = TextMobject(r"\text{$<f(x) + g(x), h(x)>$ = ",r"\text{$\int_{a}^{b} (f(x) + g(x))h(x)$ $dx$}").scale(0.57).shift(4*RIGHT+3.5*UP)
        text5[1].set_color(ORANGE)
        self.play(ShowCreation(text5))

        curve5 = self.get_graph(lambda x : (sin(x) + x)*1.6, x_min=0,x_max=2.3,color=ORANGE)
        text6 = TextMobject(r"$(f(x) + g(x))\cdot h(x)$").scale(0.5).shift(2.2*UP+1.4*RIGHT)
        area1 = self.get_area(curve5,0,2.3)
        area1.set_color(ORANGE)
        self.wait(1)
        self.play(FadeOut(curve4),FadeOut(text4),FadeOut(curve3),FadeOut(text3),ShowCreation(curve5),ShowCreation(text6),ShowCreation(area1))
        self.wait(2)
        text7 = TextMobject(r"\text{$<f(x), h(x)>$ = ",r"\text{$\int_{a}^{b} (f(x)h(x)$ $dx$}").scale(0.57).shift(5*RIGHT+3*UP)
        text7[1].set_color(BLUE)
        self.play(ShowCreation(text7))
        self.wait(1.5)
        curve6 = self.get_graph(lambda x : (sin(x))*1.6, x_min=0,x_max=2.3,color=BLUE)
        text8 = TextMobject(r"$f(x)\cdot h(x)$").scale(0.5).shift(1.4*DOWN+0.8*RIGHT)
        area2 = self.get_area(curve6,0,2.3)
        self.play(ShowCreation(curve6),ShowCreation(text8),ShowCreation(area2))
        self.wait(1.5)
        text9 = TextMobject(r"\text{$<g(x), h(x)>$ = ",r"\text{$\int_{a}^{b} (g(x)h(x)$ $dx$}").scale(0.57).shift(5*RIGHT+2.5*UP)
        text9[1].set_color(MAROON_B)
        self.play(ShowCreation(text9))
        self.wait(1.5)
        curve7 = self.get_graph(lambda x : x*1.6, x_min=0,x_max=2.3,color=MAROON_B)
        text10 = TextMobject(r"$g(x)\cdot h(x)$").scale(0.5).shift(0.8*RIGHT+1*UP)
        area3 = self.get_area(curve7,0,2.3)
        area3.set_color(MAROON_B)
        self.play(ShowCreation(curve7),ShowCreation(text10),ShowCreation(area3))
        self.wait(2.6)
        curve8 = self.get_graph(lambda x : (sin(x))*1.6 + x*1.6, x_min=0,x_max=2.3,color=RED_C)
        area4 = self.get_area(curve8,0,2.3)
        area4.set_color(RED_C)
        text11 = TextMobject(r"$f(x)h(x) + g(x)h(x)$").scale(0.5).shift(2.2*UP + 1.4*RIGHT)
        self.play(FadeOut(curve6),FadeOut(text8),FadeOut(curve7),FadeOut(text10),FadeOut(area2),FadeOut(area3),ShowCreation(curve8),ShowCreation(area4))
        self.wait(1)
        self.play(Transform(text6,text11))
        self.wait(1.7)
        text12 = TextMobject(r"$<f(x) + g(x), h(x)>$ = $<f(x), h(x)>$ + $<g(x), h(x)>$").scale(0.465).shift(0.7*UP+4*RIGHT)
        rect1 = Rectangle(height=0.5)
        rect1.surround(text12)
        self.play(ShowCreation(text12),ShowCreation(rect1))
        self.wait(3)
        self.play(FadeOut(text6),FadeOut(text5),FadeOut(text7),FadeOut(text9),FadeOut(text12),FadeOut(rect1),FadeOut(curve8),FadeOut(area4),FadeOut(text11),FadeOut(curve5),FadeOut(area1))

        curve2.set_color(ORANGE)
        self.play(ShowCreation(curve1),ShowCreation(text1))
        self.wait(1)
        self.play(ShowCreation(curve2),ShowCreation(text2))
        self.wait(2)
        curve9 = self.get_graph(lambda x : 2*sin(x), x_min=0,x_max=2.3,color=GREEN)
        text13 = TextMobject(r"$2f(x)$").scale(0.5).shift(1.1*DOWN+0.55*RIGHT)
        self.play(Transform(curve1,curve9),Transform(text1,text13))
        self.wait(1.5)

        text14 = TextMobject(r"\text{$<2f(x), g(x)>$ = ",r"\text{$\int_{a}^{b} (2f(x))g(x)$ $dx$}").scale(0.57).shift(4*RIGHT+3.5*UP)
        text14[1].set_color(YELLOW)
        self.play(ShowCreation(text14))
        self.wait(2.2)
        curve10 = self.get_graph(lambda x : 2*sin(x)*x, x_min=0,x_max=2.3,color=YELLOW)
        text15 = TextMobject(r"$2f(x)\cdot g(x)$").scale(0.5).shift(1*RIGHT+0.97*UP)
        area5 = self.get_area(curve10,0,2.3)
        area5.set_color(YELLOW)
        self.play(ShowCreation(area5),ShowCreation(curve10),ShowCreation(text15),FadeOut(curve1),FadeOut(text1),FadeOut(curve2),FadeOut(text2))
        self.wait(2)
        text16 = TextMobject(r"\text{$<f(x), g(x)>$ = ",r"\text{$\int_{a}^{b} f(x)g(x)$ $dx$}").scale(0.57).shift(3.8*RIGHT+2.9*UP)
        text16[1].set_color(TEAL)
        self.play(ShowCreation(text16))
        self.wait(1.7)
        curve11 = self.get_graph(lambda x : sin(x)*x, x_min=0,x_max=2.3,color=TEAL)
        area6 = self.get_area(curve11,0,2.3)
        area6.set_color(TEAL)
        text17 = TextMobject(r"$f(x)\cdot g(x)$").scale(0.5).shift(0.9*RIGHT+0.7*DOWN)
        self.play(ShowCreation(curve11),ShowCreation(text17),ShowCreation(area6))
        self.wait(2)

        text18 = TextMobject(r"\text{$2 <f(x), g(x)>$ = ",r"\text{$2 \int_{a}^{b} f(x)g(x)$ $dx$}").scale(0.57).shift(4*RIGHT+2.3*UP)
        text18[1].set_color(DARK_BLUE)
        self.play(ShowCreation(text18))
        self.wait(2)
        curve12 = self.get_graph(lambda x : 2*sin(x)*x, x_min=0,x_max=2.3,color=DARK_BLUE)
        area7 = self.get_area(curve12,0,2.3)
        area7.set_color(DARK_BLUE)
        text19 = TextMobject(r"= $2( f(x)\cdot g(x) )$").scale(0.5).shift(2.5*RIGHT+0.97*UP)
        self.play(ShowCreation(curve12),ShowCreation(area7),ShowCreation(text19),FadeOut(text17),FadeOut(area6),FadeOut(curve11))

        self.wait(2.5)
        text20 = TextMobject(r"$<2f(x), g(x)>$ = $2<f(x), g(x)>$").scale(0.57).shift(0.6*DOWN+4*RIGHT)
        rect2 = Rectangle(height=0.5)
        rect2.surround(text20)
        self.play(ShowCreation(text20),ShowCreation(rect2))
        self.wait(3)

        self.play(FadeOut(text14),FadeOut(text15),FadeOut(text19),FadeOut(text16),FadeOut(text18),FadeOut(rect2),FadeOut(curve10),FadeOut(area5),FadeOut(curve12),FadeOut(area7),FadeOut(text20))
        curve1 = self.get_graph(lambda x : sin(x), x_min=0,x_max=2.3,color=YELLOW)
        text1 = TextMobject(r"$f(x)$").scale(0.5).shift(1.77*DOWN+0.55*RIGHT)
        self.play(ShowCreation(curve1),ShowCreation(text1))
        self.wait(1.5)
        self.play(ShowCreation(curve2),ShowCreation(text2))
        self.wait(1.7)
        text21 = TextMobject(r"\text{$<f(x), g(x)>$ = ",r"\text{$\int_{a}^{b} f(x)g(x)$ $dx$}").scale(0.57).shift(3.5*RIGHT+3*UP)
        text21[1].set_color(GREEN)
        self.play(ShowCreation(text21))
        self.wait(2)
        curve13 = self.get_graph(lambda x : sin(x)*x, x_min=0,x_max=2.3,color=GREEN)
        area8 = self.get_area(curve13,0,2.3)
        area8.set_color(GREEN)
        text22 = TextMobject(r"$f(x)\cdot g(x)$").scale(0.5).shift(0.8*RIGHT+0.7*DOWN)
        self.play(ShowCreation(curve13),ShowCreation(area8),ShowCreation(text22),FadeOut(curve1),FadeOut(text1),FadeOut(curve2),FadeOut(text2))
        self.wait(2.2)
        curve14 = self.get_graph(lambda x : sin(x)*x, x_min=0,x_max=2.3,color=RED)
        area9 = self.get_area(curve14,0,2.3)
        area9.set_color(RED)
        self.play(ShowCreation(curve14),ShowCreation(area9))
        text23 = TextMobject(r"= $\overline{f(x)\cdot g(x)}$").scale(0.5).shift(0.7*DOWN+2.1*RIGHT)
        self.play(ShowCreation(text23))
        self.wait(2)
        text24 = TextMobject(r"For all the real functions").scale(0.5).shift(2*RIGHT+2*UP)
        text25 = TextMobject(r"$<\overline{f(x), g(x)}>$ = $<f(x), g(x)>$").scale(0.5).shift(2*RIGHT+1.4*UP)
        rect3 = Rectangle(height=0.7)
        rect3.surround(text25)
        self.play(ShowCreation(text24),ShowCreation(text25),ShowCreation(rect3))
        self.wait(3)

        














