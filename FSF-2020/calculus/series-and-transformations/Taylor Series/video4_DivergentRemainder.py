from manimlib.imports import*
import math


class graphScene(GraphScene):
    CONFIG = {
        "x_min": -8,
        "x_max": 8,
        "y_min": -8,
        "y_max": 8,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "exclude_zero_label": True,
        "x_labeled_nums": range(-8, 8, 1),
    }
    def construct(self):

        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)

        self.setup_axes(animate=True)
        lnx=self.get_graph(lambda x:math.log2(x),color=RED,x_min=0.01,x_max=8)
        equation=self.get_graph(lambda x:math.log2(2)+(x-2)/2-((x-2)**2)/8+((x-2)**3)/24-((x-2)**4)/64+((x-2)**5)/160-((x-2)**6)/384,color=BLUE)

        terms=[TextMobject("$T_{n}:=$"),TextMobject("$ln(2)$"),TextMobject("$+\\frac { x-2 }{ 2 } $"),TextMobject("$-\\frac { (x-2)^{2} }{ 8 }$"),TextMobject("+..")]
        for obj in terms:
            obj.scale(0.5)
        
        terms[0].shift(3*UP+3*RIGHT)
        terms[1].next_to(terms[0],buff=0.1)
        terms[2].next_to(terms[1],buff=0.1)
        terms[3].next_to(terms[2],buff=0.1)
        terms[4].next_to(terms[3],buff=0.1)

        self.play(ShowCreation(lnx))
        self.wait(1)
        self.play(FadeIn(equation),FadeIn(terms[0]),FadeIn(terms[1]),FadeIn(terms[2]),FadeIn(terms[3]),FadeIn(terms[4]))
        self.wait(1)

        bottomText1=TextMobject("$R_{n}(x)=\\frac { d }{ dx } ($","area bounded","$)$")

        bottomText1.set_color_by_tex_to_color_map({"area bounded":ORANGE})
        #bottomText2.set_color_by_tex_to_color_map({"area bounded":BLUE})
        arrow=TextMobject("$\downarrow$")
        arrow.scale(2.5)
        arrow.shift(ORIGIN+x_each_unit*RIGHT*9.5+UP*y_each_unit)
        increasingText=TextMobject("Increases!")
        increasingText.set_color(GREEN)
        followupText=TextMobject("as n increase!")
        followupText.scale(0.3)
        followupText.shift(ORIGIN+x_each_unit*11*RIGHT+UP*y_each_unit*1.1)
        increasingText.shift(ORIGIN+x_each_unit*11*RIGHT+UP*y_each_unit*1.6)
        increasingText.scale(0.4)

        bottomText1.scale(0.5)
        #bottomText2.scale(0.5)
        #bottomText3.scale(0.5)

        bottomText1.shift(3.5*LEFT+2*DOWN)
        #bottomText2.shift(3.5*LEFT+2.4*DOWN)
        #bottomText3.shift(3.5*LEFT+2.8*DOWN)

        dline=DashedLine(start=ORIGIN+8*y_each_unit*UP,end=ORIGIN+8*y_each_unit*DOWN)
        dline.shift(ORIGIN+x_each_unit*4*RIGHT)

        area1=self.get_riemann_rectangles(lnx,x_max=8,x_min=4,dx=0.01,start_color=BLUE,end_color=RED,stroke_width=0,fill_opacity=0.8)
        area2=self.get_riemann_rectangles(equation,x_max=5.2,x_min=4,dx=0.025,start_color=BLACK,end_color=BLACK,stroke_width=0,fill_opacity=1)

        self.play(Write(dline))
        self.wait(0.5)
        self.play(ShowCreation(area1),ShowCreation(area2),Write(bottomText1))
        # self.play(Write(bottomText2))
        # self.play(FadeIn(bottomText3))
        self.play(Write(arrow))
        self.wait(0.7)
        self.play(Write(increasingText))
        self.play(FadeIn(followupText))
        self.wait(2)
        
