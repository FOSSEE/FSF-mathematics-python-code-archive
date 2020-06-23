# Plotting Graphs
from manimlib.imports import *

class PlotGraphs(GraphScene):
    CONFIG = {
    "x_min": -5,
    "x_max": 5,
    "y_min": 0,
    "y_max": 4,
    "graph_origin": ORIGIN + 2.5* DOWN,
    "x_labeled_nums": list(range(-5, 6)),
    "y_labeled_nums": list(range(0, 5)),
    }
    def construct(self):

        topic = TextMobject("Domain and Range")
        topic.scale(2)
        topic.set_color(YELLOW)
        self.play(Write(topic))
        self.play(FadeOut(topic))
        self.wait(1)


        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)

        self.setup_axes(animate = True)

        graphobj = self.get_graph(lambda x :  np.sqrt(x + 4), x_min = -4, x_max = 5)
        graph_lab = self.get_graph_label(graphobj, label = r"\sqrt{x + 4}")


        rangeline1 = Arrow(self.graph_origin+2.2*YTD*UP+5*XTD*LEFT, self.graph_origin+4.1*YTD*UP+5*XTD*LEFT)
        rangeline2 = Arrow(self.graph_origin+1.7*YTD*UP+5*XTD*LEFT, self.graph_origin+5*XTD*LEFT)
        rangeline1.set_color(RED)
        rangeline2.set_color(RED)

        rangeMsg = TextMobject(r"Range: $y \geq 0$")
        rangeMsg.move_to(self.graph_origin+2*YTD*UP+5*XTD*LEFT)
        rangeMsg.scale(0.5)
        rangeMsg.set_color(YELLOW)

        domainline1 = Line(self.graph_origin+0.6*YTD*DOWN+1.2*XTD*LEFT, self.graph_origin+0.6*YTD*DOWN + 4*XTD*LEFT)
        domainline2 = Arrow(self.graph_origin+0.6*YTD*DOWN+1.1*XTD*RIGHT, self.graph_origin+0.6*YTD*DOWN + 5.3*XTD*RIGHT)
        domainline1.set_color(PINK)
        domainline2.set_color(PINK)

        domainMsg = TextMobject(r"Domain: $x \geq -4$")
        domainMsg.move_to(self.graph_origin+0.6*YTD*DOWN)
        domainMsg.scale(0.5)
        domainMsg.set_color(GREEN)


    
        
        self.play(ShowCreation(graphobj))
        self.play(ShowCreation(graph_lab))
        self.wait(1)
        self.play(GrowArrow(rangeline1))
        self.play(GrowArrow(rangeline2))
        self.play(Write(rangeMsg))
        self.wait(1)
        self.play(GrowArrow(domainline1))
        self.play(GrowArrow(domainline2))
        self.play(Write(domainMsg))
        self.wait(3)

        self.wait(2)




class PlotSineGraphs(GraphScene):
    CONFIG = {
    "x_min": -8,
    "x_max": 8,
    "y_min": -1,
    "y_max": 1,
    "graph_origin": ORIGIN,
    "x_labeled_nums": list(range(-8, 9)),
    "y_labeled_nums": list(range(-1, 2)),
    }
    def construct(self):
        


        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)

        self.setup_axes(animate = True)

        sineobj = self.get_graph(lambda x :  np.sin(x), x_min = -7, x_max = 8)
        sine_lab = self.get_graph_label(sineobj, label = "\\sin(x)")


        rangeline1 = Line(8*XTD*LEFT,1*YTD*UP+8*XTD*LEFT)
        rangeline2 = Line(8*XTD*LEFT,1*YTD*DOWN+8*XTD*LEFT)
        rangeline1.set_color(RED)
        rangeline2.set_color(RED)

        rangeMsg = TextMobject(r"Range: $-1 \leq y \leq  1$")
        rangeMsg.move_to(1.1*YTD*UP+8.5*XTD*LEFT)
        rangeMsg.scale(0.5)
        rangeMsg.set_color(YELLOW)


        domainline1 = Arrow(1.1*YTD*DOWN+2*XTD*LEFT, 1.1*YTD*DOWN + 8.5*XTD*LEFT)
        domainline2 = Arrow(1.1*YTD*DOWN+2*XTD*RIGHT, 1.1*YTD*DOWN + 8.5*XTD*RIGHT)
        domainline1.set_color(PINK)
        domainline2.set_color(PINK)

        domainMsg = TextMobject(r"Domain: $[-\infty, \infty]$")
        domainMsg.move_to(1.1*YTD*DOWN)
        domainMsg.scale(0.5)
        domainMsg.set_color(GREEN)



        self.play(ShowCreation(sineobj))
        self.play(ShowCreation(sine_lab))
        self.wait(1)
        self.play(GrowArrow(rangeline1))
        self.play(GrowArrow(rangeline2))
        self.play(Write(rangeMsg))
        self.wait(1)
        self.play(GrowArrow(domainline1))
        self.play(GrowArrow(domainline2))
        self.play(Write(domainMsg))
        self.wait(3)


    