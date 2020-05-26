from manimlib.imports import *

class Ver_Shear(GraphScene):
    CONFIG = {
        "x_min" : -5,
        "x_max" : 5,
        "y_min" : -5,
        "y_max" : 5,
        "graph_origin" : ORIGIN+3.5*LEFT,
        "x_axis_width" : 7,
        "y_axis_height" : 7
        #"x_labeled_nums" : list(range(-5,6)),
        #"y_labeled_nums" : list(range(-5,6)),
    }

    def construct(self):
        XTD = self.x_axis_width/(self.x_max-self.x_min)
        YTD = self.y_axis_height/(self.y_max-self.y_min)

        Text1 = TextMobject("Before"," Vertical")
        Text1[0].set_color(YELLOW)
        Text2 = TextMobject("Shear Transformation")

        Text1.move_to(4*RIGHT+2*UP)
        Text2.move_to(4*RIGHT+1*UP)
        
        self.setup_axes(animate=False)
        arrow_i = Arrow(stroke_width = 3, start = self.graph_origin + 0.25*LEFT, end = self.graph_origin+1*XTD*RIGHT+ 0.25*RIGHT)
        arrow_j = Arrow(stroke_width = 3, start = self.graph_origin + 0.25*DOWN, end = self.graph_origin+1*XTD*UP+0.25*UP)
        arrow_i.set_color(YELLOW)
        arrow_j.set_color(YELLOW)

        square = Polygon(self.graph_origin,self.graph_origin+2*XTD*RIGHT, self.graph_origin+2*XTD*RIGHT+2*YTD*UP,  self.graph_origin+2*YTD*UP)
        square.set_color(DARK_BLUE)
        self.play(ShowCreation(square), Write(Text1), Write(Text2), ShowCreation(arrow_i), ShowCreation(arrow_j))
        self.wait(1)

        Text3 = TextMobject("After"," Vertical")
        Text3[0].set_color(RED)
        Text4 = TextMobject("Shear Transformation")

        Text3.move_to(4*RIGHT+2*UP)
        Text4.move_to(4*RIGHT+1*UP)
        
        trans_arrow_i = Arrow(stroke_width = 3, start = self.graph_origin + 0.15*DOWN + 0.15*LEFT, end = self.graph_origin+1*XTD*UP+1*YTD*RIGHT+0.25*UP+0.25*RIGHT)
        trans_arrow_j = Arrow(stroke_width = 3, start = self.graph_origin + 0.25*DOWN, end = self.graph_origin+1*XTD*UP+ 0.25*UP)
        trans_arrow_i.set_color(RED)
        trans_arrow_j.set_color(RED)
        
        rhombus = Polygon(self.graph_origin,self.graph_origin+2*XTD*UP, self.graph_origin+2*XTD*RIGHT+4*YTD*UP,  self.graph_origin+2*XTD*RIGHT+2*YTD*UP)
        self.play(Transform(arrow_i,trans_arrow_i), Transform(arrow_j,trans_arrow_j), FadeOut(square), ShowCreation(rhombus), Transform(Text1,Text3), Transform(Text2,Text4))
        self.wait(1)