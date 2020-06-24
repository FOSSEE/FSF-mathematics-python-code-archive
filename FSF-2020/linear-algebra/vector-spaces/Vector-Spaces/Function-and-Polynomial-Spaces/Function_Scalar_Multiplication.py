from manimlib.imports import *
from scipy import exp
class FunctionScalarMultiplication(GraphScene):
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
        curve1 = self.get_graph(lambda x : 1/3*(x**2)+1, x_min=-2,x_max=2.5,color=ORANGE)
        curve2 = self.get_graph(lambda x : 2*(1/3*(x**2)+1), x_min=-2,x_max=2.5,color=GOLD)
        fx= TextMobject("$f(x)$").scale(0.6).shift(1.25*UP + 2.2*LEFT)
        gx= TextMobject("$2 \cdot f(x)$").scale(0.6).shift(0.5*UP + 2.1*LEFT)
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
        self.play(ShowCreation(curve1),ShowCreation(fx))
        self.wait(1.5)
        self.play(ShowCreation(f1),ShowCreation(f2),ShowCreation(f3),ShowCreation(f4),ShowCreation(f5),ShowCreation(f6),ShowCreation(f7),ShowCreation(f8),ShowCreation(f9),ShowCreation(f10))
        self.wait(1.7)
        line1=Line(color=YELLOW).shift(5*LEFT+1.8*UP).scale(0.5)
        line1.rotate(np.pi/2)
        scalar = TextMobject("2 x").scale(0.65).shift(5.5*LEFT+1.9*UP)
        equal = TextMobject("=").scale(0.65).shift(4.5*LEFT+1.9*UP)
        line2=Line(color=BLUE).shift(4*LEFT+2.3*UP)
        line2.rotate(np.pi/2)
        self.play(ShowCreation(line1),ShowCreation(scalar),ShowCreation(equal),ShowCreation(line2))
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
        self.wait(2)
        fx2=TextMobject("2$\cdot f(x)$").scale(0.6).shift(2.6*UP+2.3*LEFT)
        self.play(ShowCreation(curve2),ShowCreation(fx2))
        self.wait(1.5)
        self.play(FadeOut(curve1),FadeOut(fx))
        sc_mult=TextMobject("$(2 f(x)) = 2f(x)$",color=GOLD).scale(0.65).shift(0.65*UP + 5*LEFT)
        rect = Rectangle(height=0.5,width=2)
        rect.surround(sc_mult)
        self.play(ShowCreation(sc_mult),ShowCreation(rect))
        self.wait(3)

