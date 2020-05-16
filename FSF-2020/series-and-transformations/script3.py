from manimlib.imports import*
import math

class intro(Scene):
    def construct(self):
        introText1=TextMobject("Let's analyse")
        introText2=TextMobject("for")
        function_main=TextMobject("$\sum { { (-1) }^{ n }{ x }^{ 2n } }$")
        function_main.set_color(GREEN)
        introText1.scale(1.2)
        introText1.shift(2*UP)
        introText2.scale(0.7)
        introText2.shift(UP)
        function_main.scale(2)
        function_main.shift(DOWN)
        function_expan=TextMobject("$1-{ x }^{ 2 }+{ x }^{ 4 }-{ x }^{ 6 }+{ x }^{ 8 }+..$")
        function_expan.set_color(RED)
        function_expan.scale(1.2)
        function_expan.shift(2*UP)

        self.play(Write(introText1))
        self.play(FadeIn(introText2))
        self.wait(0.5)
        self.play(Write(function_main))
        self.wait(1)

        self.play(FadeOut(introText1),FadeOut(introText2))
        self.play(ApplyMethod(function_main.shift,3*UP))
        self.wait(0.5)
        self.play(ReplacementTransform(function_main,function_expan))
        self.wait(1)
        self.play(ApplyMethod(function_expan.scale,0.5))
        function_expan.to_edge(UP+RIGHT)
        self.play(ReplacementTransform(function_expan,function_expan))
        self.wait(1)


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
        "x_labeled_nums": range(-1, 2, 1),
        "y_labeled_nums": range(0,2,1)
    }

    def construct(self):

        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)

        function_expan=TextMobject("$1-{ x }^{ 2 }+{ x }^{ 4 }-{ x }^{ 6 }+{ x }^{ 8 }+..$")
        function_expan.set_color(RED)
        function_expan.scale(0.6)
        function_expan.to_edge(UP+RIGHT)
        self.add(function_expan)

        self.setup_axes(animate=True)

        eqText=[TextMobject("$1$"),TextMobject("$1-{ x }^{ 2 }$"),TextMobject("$1-{ x }^{ 2 }+{ x }^{ 4 }$"),TextMobject("$1-{ x }^{ 2 }+{ x }^{ 4 }-{ x }^{ 6 }$")]
        for i in range(0,len(eqText)):
            eqText[i].scale(0.6)
            eqText[i].set_color(BLUE)
            eqText[i].shift(ORIGIN+UP*2*y_each_unit+RIGHT*3.3*x_each_unit)
        eqTextTerm=TextMobject("And so on..!")
        eqTextTerm.set_color(BLUE)
        eqTextTerm.scale(0.6)
        eqTextTerm.shift(ORIGIN+UP*2*y_each_unit+3*RIGHT*x_each_unit)
        equation1 = self.get_graph(lambda x : 1,color = RED,x_min = -8,x_max=8)
        equation2 = self.get_graph(lambda x : 1-math.pow(x,2),color = RED,x_min = -1.7,x_max=1.7)
        equation3 = self.get_graph(lambda x : 1-math.pow(x,2)+math.pow(x,4),color = RED,x_min = -1.6,x_max=1.6)
        equation4 = self.get_graph(lambda x : 1-math.pow(x,2)+math.pow(x,4)-math.pow(x,6),color = RED,x_min = -1.45,x_max=1.45)
        equation5 = self.get_graph(lambda x : 1-math.pow(x,2)+math.pow(x,4)-math.pow(x,6)+math.pow(x,8),color = RED,x_min = -1.35,x_max=1.35)
        equation6 = self.get_graph(lambda x : 1-math.pow(x,2)+math.pow(x,4)-math.pow(x,6)+math.pow(x,8)-math.pow(x,10),color = RED,x_min = -1.3,x_max=1.3)
        equation7 = self.get_graph(lambda x : 1-math.pow(x,2)+math.pow(x,4)-math.pow(x,6)+math.pow(x,8)-math.pow(x,10)+math.pow(x,12),color = RED,x_min = -1.25,x_max=1.25)
        equation8 = self.get_graph(lambda x : 1-math.pow(x,2)+math.pow(x,4)-math.pow(x,6)+math.pow(x,8)-math.pow(x,10)+math.pow(x,12)-math.pow(x,14),color = RED,x_min = -1.2,x_max=1.2)
        equation9 = self.get_graph(lambda x : 1-math.pow(x,2)+math.pow(x,4)-math.pow(x,6)+math.pow(x,8)-math.pow(x,10)+math.pow(x,12)-math.pow(x,14)+math.pow(x,16),color = RED,x_min = -1.15,x_max=1.15)
        equation10 = self.get_graph(lambda x : 1-math.pow(x,2)+math.pow(x,4)-math.pow(x,6)+math.pow(x,8)-math.pow(x,10)+math.pow(x,12)-math.pow(x,14)+math.pow(x,16)-math.pow(x,18),color = RED,x_min = -1.15,x_max=1.15)

        textBtwAnim1=TextMobject("Here the graph just","oscilates")
        textBtwAnim1.set_color_by_tex_to_color_map({"oscilates":BLUE})
        textBtwAnim2=TextMobject("after","the","point","(as we add higher order terms)")
        textBtwAnim2.set_color_by_tex_to_color_map({"after":BLUE,"point":YELLOW})
        textBtwAnim3=TextMobject("$x=1$")
        textBtwAnim1.scale(0.4)
        textBtwAnim2.scale(0.4)
        textBtwAnim3.scale(1.2)
        textBtwAnim1.shift(2.1*DOWN+4.3*RIGHT)
        textBtwAnim2.shift(2.4*DOWN+4.1*RIGHT)
        textBtwAnim3.shift(2.9*DOWN+4.3*RIGHT)

        self.play(ShowCreation(equation1),run_time=0.8)
        self.add(eqText[0])
        self.wait(1)
        self.play(ReplacementTransform(equation1,equation2),ReplacementTransform(eqText[0],eqText[1]))
        self.wait(0.5)
        self.play(ReplacementTransform(equation2,equation3),ReplacementTransform(eqText[1],eqText[2]))
        self.wait(0.4)
        self.play(ReplacementTransform(equation3,equation4),ReplacementTransform(eqText[2],eqText[3]))
        self.wait(0.3)
        self.play(FadeOut(eqText[3]))
        self.play(FadeIn(eqTextTerm))
        self.play(Write(textBtwAnim1),Write(textBtwAnim2))
        self.play(FadeIn(textBtwAnim3))
        self.play(ReplacementTransform(equation4,equation5))
        self.wait(0.2)
        self.play(ReplacementTransform(equation5,equation6))
        self.wait(0.2)
        self.play(ReplacementTransform(equation6,equation7))
        self.wait(0.2)
        self.play(ReplacementTransform(equation7,equation8))
        self.wait(0.2)
        self.play(ReplacementTransform(equation8,equation9))
        self.wait(0.2)
        self.play(ReplacementTransform(equation9,equation10))    
        self.wait(1)

        self.play(FadeOut(textBtwAnim1),FadeOut(textBtwAnim2),FadeOut(textBtwAnim3),FadeOut(equation10),FadeOut(eqTextTerm))
        self.wait(1)
        
        convergeLine=Line(start=ORIGIN+x_each_unit*LEFT,end=ORIGIN+x_each_unit*RIGHT,color=WHITE)
        divergeLineLeft=Line(start=ORIGIN+x_each_unit*LEFT,end=ORIGIN+x_each_unit*LEFT*8,color=RED)
        divergeLineRight=Line(start=ORIGIN+x_each_unit*RIGHT,end=ORIGIN+x_each_unit*8*RIGHT,color=RED)
        circle1=Circle(radius=0.01,color=PURPLE_E)
        circle2=Circle(radius=0.01,color=PURPLE_E)
        circle1.shift(ORIGIN+LEFT*x_each_unit)
        circle2.shift(ORIGIN+RIGHT*x_each_unit)
        convergeText=TextMobject("Converges")
        divergeText1=TextMobject("Diverges")
        divergeText2=TextMobject("Diverges")
        convergeText.set_color(GREEN)
        divergeText1.set_color(RED)
        divergeText2.set_color(RED)
        convergeText.scale(0.5)
        divergeText1.scale(0.5)
        divergeText2.scale(0.5)
        convergeText.shift(1.6*UP)
        divergeText1.shift(0.3*UP+1.5*LEFT)
        divergeText2.shift(0.3*UP+1.5*RIGHT)
        self.play(Write(divergeLineLeft),Write(divergeLineRight))
        self.play(FadeIn(convergeLine))
        self.wait(0.5)
        self.play(FadeOut(self.axes))
        self.play(Write(circle1),Write(circle2))
        self.wait(0.5)
        self.play(ApplyMethod(convergeLine.shift,1.3*UP),ApplyMethod(function_expan.shift,5*LEFT+DOWN))
        self.play(FadeIn(convergeText),FadeIn(divergeText1),FadeIn(divergeText2))
        self.wait(2)        

