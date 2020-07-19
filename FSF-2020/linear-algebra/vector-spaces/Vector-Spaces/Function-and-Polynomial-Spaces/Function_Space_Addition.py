from manimlib.imports import *
from scipy import sin,exp
class FunctionalVectorSpace(GraphScene):
    CONFIG = {
        "x_min" : -5,
        "x_max" : 5,
        "y_min" : -5,
        "y_max" : 5,
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 
        "axes_color":LIGHT_GRAY,
        "graph_origin": ORIGIN,
        

    }
    def construct(self):
        self.setup_axes(animate = True)
        curve1 = self.get_graph(lambda x : exp(x) + 0.5, x_min=-2,x_max=2.5,color=ORANGE)
        curve2 = self.get_graph(lambda x : 1/3*(x**2)+1, x_min=-2,x_max=2.5,color=DARK_BLUE)
        curve3 = self.get_graph(lambda x : 1/3*(x**2)+1 + exp(x) + 0.5, x_min=-2,x_max=2.5,color=BLACK)
        fx= TextMobject("$f(x)$").scale(0.6).shift(1.25*UP + 2.1*LEFT)
        gx= TextMobject("$g(x)$").scale(0.6).shift(0.5*UP + 2.1*LEFT)
        f1 = self.get_vertical_line_to_graph(-2,curve1,color=YELLOW)
        f2 = self.get_vertical_line_to_graph(-1.5,curve1,color=YELLOW)
        f3 = self.get_vertical_line_to_graph(-1,curve1,color=YELLOW)
        f4 = self.get_vertical_line_to_graph(-0.5,curve1,color=YELLOW)
        f5 = self.get_vertical_line_to_graph(0,curve1,color=YELLOW)
        f6 = self.get_vertical_line_to_graph(0.5,curve1,color=YELLOW)
        f7 = self.get_vertical_line_to_graph(1,curve1,color=YELLOW)
        f8 = self.get_vertical_line_to_graph(1.5,curve1,color=YELLOW)
        f9 = self.get_vertical_line_to_graph(2,curve1,color=YELLOW)
        f10 = self.get_vertical_line_to_graph(2.5,curve1,color=YELLOW)

        self.play(ShowCreation(curve1),ShowCreation(gx))
        self.wait(1.2)
        self.play(ShowCreation(curve2),ShowCreation(fx))
        self.wait(1.2)
        self.play(ShowCreation(f1),ShowCreation(f2),ShowCreation(f3),ShowCreation(f4),ShowCreation(f5),ShowCreation(f6),ShowCreation(f7),ShowCreation(f8),ShowCreation(f9),ShowCreation(f10))
        self.wait(1.7)
        g1 = self.get_vertical_line_to_graph(-2,curve2,color=BLUE)
        g2 = self.get_vertical_line_to_graph(-1.5,curve2,color=BLUE)
        g3 = self.get_vertical_line_to_graph(-1,curve2,color=BLUE)
        g4 = self.get_vertical_line_to_graph(-0.5,curve2,color=BLUE)
        g5 = self.get_vertical_line_to_graph(0,curve2,color=BLUE)
        g6 = self.get_vertical_line_to_graph(0.5,curve2,color=BLUE)
        g7 = self.get_vertical_line_to_graph(1,curve2,color=BLUE)
        g8 = self.get_vertical_line_to_graph(1.5,curve2,color=BLUE)
        g9 = self.get_vertical_line_to_graph(2,curve2,color=BLUE)
        g10 = self.get_vertical_line_to_graph(2.5,curve2,color=BLUE)
        self.play(ShowCreation(g1),ShowCreation(g2),ShowCreation(g3),ShowCreation(g4),ShowCreation(g5),ShowCreation(g6),ShowCreation(g7),ShowCreation(g8),ShowCreation(g9),ShowCreation(g10))
        line1=Line(color=BLUE).shift(5*LEFT+2.3*UP).scale(0.25)
        line1.rotate(np.pi/2)
        line2=Line(color=YELLOW).shift(6*LEFT+2.5*UP).scale(0.5)
        line2.rotate(np.pi/2)
        line3=Line(color=PURPLE_B).shift(4*LEFT+2.7*UP).scale(0.75)
        line3.rotate(np.pi/2)
        add=TextMobject("+").shift(2.4*UP+5.5*LEFT).scale(0.7)
        equal=TextMobject("=").shift(2.4*UP+4.5*LEFT).scale(0.7)
        self.play(ShowCreation(line2),ShowCreation(line1),ShowCreation(add),ShowCreation(equal),ShowCreation(line3))
        self.wait(2)
        self.play(FadeOut(curve1),FadeOut(curve2))
        self.wait(3)
        h1 = self.get_vertical_line_to_graph(-2,curve3,color=PURPLE_B)
        h2 = self.get_vertical_line_to_graph(-1.5,curve3,color=PURPLE_B)
        h3 = self.get_vertical_line_to_graph(-1,curve3,color=PURPLE_B)
        h4 = self.get_vertical_line_to_graph(-0.5,curve3,color=PURPLE_B)
        h5 = self.get_vertical_line_to_graph(0,curve3,color=PURPLE_B)
        h6 = self.get_vertical_line_to_graph(0.5,curve3,color=PURPLE_B)
        h7 = self.get_vertical_line_to_graph(1,curve3,color=PURPLE_B)
        h8 = self.get_vertical_line_to_graph(1.5,curve3,color=PURPLE_B)
        h9 = self.get_vertical_line_to_graph(2,curve3,color=PURPLE_B)
        h10 = self.get_vertical_line_to_graph(2.5,curve3,color=PURPLE_B)
        
        line1.shift(1*LEFT+0.9*UP)
        equal.shift(0.3*LEFT+0.2*UP)
        f=TextMobject("$f(x)$").scale(0.5).shift(5.6*LEFT+3.2*UP)
        g=TextMobject("$g(x)$").scale(0.5).shift(5.6*LEFT+2.4*UP)
        fg=TextMobject("$(f + g)(x)$").scale(0.5).shift(2.85*UP+3.3*LEFT)
        self.play(FadeOut(add),ShowCreation(equal),ShowCreation(line1),ShowCreation(f),ShowCreation(g),ShowCreation(fg),FadeOut(fx),FadeOut(gx))
        self.wait(1.7)
        self.play(ShowCreation(h1),ShowCreation(h2),ShowCreation(h3),ShowCreation(h4),ShowCreation(h5),ShowCreation(h6),ShowCreation(h7),ShowCreation(h8),ShowCreation(h9),ShowCreation(h10))
        curve3 = self.get_graph(lambda x : 1/3*(x**2)+1 + exp(x) + 0.5, x_min=-2,x_max=2.5,color=RED_A)
        fgx=TextMobject("$(f + g)(x)$").scale(0.5).shift(1.65*UP+2.4*LEFT)
        self.play(ShowCreation(curve3),ShowCreation(fgx))
        sum=TextMobject("$(f + g)(x) = f(x) + g(x)$",color=GOLD).scale(0.65).shift(0.8*UP + 5*LEFT)
        rect = Rectangle(height=0.5,width=2)
        rect.surround(sum)
        self.play(ShowCreation(sum),ShowCreation(rect))
        self.wait(3)