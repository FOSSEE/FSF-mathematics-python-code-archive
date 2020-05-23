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

        bottomText1=TextMobject("Apply $f(x)=T_{n}(x)$")
        bottomText2=TextMobject("Then apply $f'(x)=T_{n}'(x)$")
        bottomText3=TextMobject("Then apply $f''(x)=T_{n}''(x)$")
        bottomText4=TextMobject("and so on..")

        bottomText1.scale(0.5)
        bottomText2.scale(0.5)
        bottomText3.scale(0.5)
        bottomText4.scale(0.5)

        bottomText1.shift(3*RIGHT+2*DOWN)
        bottomText2.shift(3*RIGHT+2*DOWN)
        bottomText3.shift(3*RIGHT+2*DOWN)
        bottomText4.shift(3*RIGHT+2*DOWN)

        equations=[self.get_graph(lambda x:math.log2(2),color=BLUE),
                    self.get_graph(lambda x:math.log2(2)+(x-2)/2,color=BLUE),
                    self.get_graph(lambda x:math.log2(2)+(x-2)/2-((x-2)**2)/8,color=BLUE),
                    self.get_graph(lambda x:math.log2(2)+(x-2)/2-((x-2)**2)/8+((x-2)**3)/24,color=BLUE),
                    self.get_graph(lambda x:math.log2(2)+(x-2)/2-((x-2)**2)/8+((x-2)**3)/24-((x-2)**4)/64,color=BLUE),
                    self.get_graph(lambda x:math.log2(2)+(x-2)/2-((x-2)**2)/8+((x-2)**3)/24-((x-2)**4)/64+((x-2)**5)/160,color=BLUE),
                    self.get_graph(lambda x:math.log2(2)+(x-2)/2-((x-2)**2)/8+((x-2)**3)/24-((x-2)**4)/64+((x-2)**5)/160-((x-2)**6)/384,color=BLUE)]
        
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
        self.play(Write(bottomText1))
        self.wait(0.5)
        self.play(ShowCreation(equations[0]),Write(terms[0]),Write(terms[1]))
        self.wait(1)
        self.play(ReplacementTransform(bottomText1,bottomText2))
        self.wait(0.5)
        self.play(ReplacementTransform(equations[0],equations[1]),Write(terms[2]))
        self.wait(1)
        self.play(ReplacementTransform(bottomText2,bottomText3))
        self.wait(0.5)
        self.play(ReplacementTransform(equations[1],equations[2]),Write(terms[3]))
        self.wait(1)
        self.play(ReplacementTransform(bottomText3,bottomText4),Write(terms[4]))
        self.wait(1.5)
        
        self.play(FadeOut(terms[0]),FadeOut(terms[1]),FadeOut(terms[2]),FadeOut(terms[3]),FadeOut(terms[4]),FadeOut(bottomText4))
        
        dline=DashedLine(start=ORIGIN+8*y_each_unit*UP,end=ORIGIN+8*y_each_unit*DOWN)
        dline.shift(ORIGIN+x_each_unit*4*RIGHT)

        bottomText5=TextMobject("Here","after $x=4$",", the graph","continuously diverges away","from $ln(x)$")
        bottomText5.scale(0.3)
        bottomText5.shift(4.5*RIGHT+2*DOWN)
        bottomText5.set_color_by_tex_to_color_map({"after $x=4$":YELLOW,"continuously diverges away":BLUE})

        self.play(Write(bottomText5),Write(dline))
        self.wait(1)
        self.play(ReplacementTransform(equations[2],equations[3]))
        self.wait(0.3)
        self.play(ReplacementTransform(equations[3],equations[4]))
        self.wait(0.3)
        self.play(ReplacementTransform(equations[4],equations[5]))
        self.wait(0.3)
        self.play(ReplacementTransform(equations[5],equations[6]),FadeOut(bottomText5))
        self.wait(1)

        circle=Circle(radius=ORIGIN+x_each_unit*2,color=PURPLE_E)
        circle.shift(ORIGIN+RIGHT*x_each_unit*2)
        radiusLine=Line(start=ORIGIN+x_each_unit*RIGHT*2,end=ORIGIN+x_each_unit*4*RIGHT,color=PURPLE_E)
        radius=TextMobject("$R$")
        radius.set_color(RED)
        radius.scale(0.5)
        radius.shift(ORIGIN+RIGHT*x_each_unit*2.45+DOWN*y_each_unit*0.6)

        self.play(FadeOut(equations[6]),Write(circle))
        self.wait(0.6)
        self.play(Write(radiusLine))
        self.play(FadeIn(radius))
        self.wait(2)