from manimlib.imports import *
import math
import pylatex

class intro(GraphScene,Scene):
    CONFIG = {
        "x_min": -8,
        "x_max": 8,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN+DOWN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$t$",
        "y_axis_label": "$\mu_{c}(t)$",
        "exclude_zero_label": True,
        "y_axis_height":4,
        "x_axis_width":7
    }
    def setup(self):
        GraphScene.setup(self)
        Scene.setup(self)
    def construct(self):
        introText=TextMobject("Unit","Step","Function")
        introText.set_color_by_tex_to_color_map({"Unit":BLUE,"Step":YELLOW})
        introText.scale(0.8)
        self.play(Write(introText))
        self.wait(0.5)
        self.play(ApplyMethod(introText.shift,3*UP))
        formulaa=TextMobject("$\mu _{ c }(t)=0\quad$","$t<c$")
        formulab=TextMobject("$\mu _{ c }(t)=1\quad$","$t\ge c$")
        formulaa.set_color_by_tex_to_color_map({"$t<c$":RED})
        formulab.set_color_by_tex_to_color_map({"$t\ge c$":RED})
        formulaa.scale(0.8)
        formulab.scale(0.8)
        formulab.shift(0.5*DOWN)
        self.play(FadeIn(formulaa),FadeIn(formulab))
        self.wait(1)

        self.play(FadeOut(formulaa),FadeOut(formulab))

        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)

        self.setup_axes(animate=True)
        self.wait(0.8)
        
        c=TextMobject("c")
        c.scale(0.5)
        c.set_color(RED)
        c.shift(self.graph_origin+3*x_each_unit*RIGHT+y_each_unit*0.4*DOWN)
        self.play(Write(c))
        smallCircle=Circle(radius=0.03,fill_color=WHITE,color=WHITE)
        smallCircle.shift(self.graph_origin+3*x_each_unit*RIGHT)
        downLine=Line(start=self.graph_origin,end=self.graph_origin+RIGHT*3*x_each_unit,color=BLUE)
        upLine=Line(start=self.graph_origin+3*x_each_unit*RIGHT+y_each_unit*UP,end=self.graph_origin+8*x_each_unit*RIGHT+y_each_unit*UP,color=BLUE)
        
        self.play(Write(downLine))
        self.play(Write(smallCircle))
        self.play(Write(upLine))
        self.wait(1.5)
        self.play(FadeOut(self.axes),FadeOut(smallCircle),FadeOut(c),FadeOut(upLine),FadeOut(downLine),FadeOut(introText))
        self.wait(0.5)


class example(GraphScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 8,
        "y_min": -4,
        "y_max": 5,
        "graph_origin": ORIGIN+LEFT+DOWN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$t$",
        "y_axis_label": "$y$",
        "exclude_zero_label": True,
        "y_axis_height":4,
        "x_axis_width":6
    }
    def construct(self):
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)

        text1=TextMobject("Consider the","formation","of","following graph!"," (a part of $f(t))$")
        text1.set_color_by_tex_to_color_map({"following graph!":BLUE,"formation":YELLOW})
        text1.scale(0.6)
        ft=TextMobject("$f(t)$")
        ftminusc=TextMobject("$f(t-c)$")
        final=TextMobject("$\mu_{c}(t)f(t-c)$")
        ft.set_color(PURPLE_C)
        ftminusc.set_color(PURPLE_C)
        final.set_color(PURPLE_C)
        c=TextMobject("c")
        c.scale(0.5)
        c.set_color(RED)
        c.shift(self.graph_origin+RIGHT*x_each_unit*3+DOWN*y_each_unit*0.5)
        ft.scale(0.5)
        ftminusc.scale(0.5)
        final.scale(0.5)

        self.play(Write(text1))
        self.play(ApplyMethod(text1.shift,3*UP))

        self.setup_axes(animate=True)
        y=self.get_graph(lambda x:(math.pow((x-3),3)/3)-math.pow((x-3),2)-(x-3)+3,x_min=3,x_max=7,color=RED)
        f=self.get_graph(lambda x:(math.pow(x,3)/3)-math.pow(x,2)-x+3,x_min=-2,x_max=4,color=RED)
        yFull=self.get_graph(lambda x:(math.pow((x-3),3)/3)-math.pow((x-3),2)-(x-3)+3,x_min=1,x_max=7,color=RED)

        self.play(Write(c))
        self.play(ShowCreation(y))
        self.wait(1)
        self.play(FadeOut(self.axes),FadeOut(y),FadeOut(c))

        belowText1=TextMobject("Consider its","normal form",", $f(t)$")
        belowText1.set_color_by_tex_to_color_map({"normal form":BLUE})
        belowText2=TextMobject("Shift it to","x=c")
        belowText2.set_color_by_tex_to_color_map({"x=c":RED})
        belowText3a=TextMobject("Now to remove the","left part","of","$c$,")
        belowText3a.set_color_by_tex_to_color_map({"left part":YELLOW,"$c$,":YELLOW})
        belowText3b=TextMobject("multiply it with the","unit step function",", $\mu_{c}(t)$")
        belowText3b.set_color_by_tex_to_color_map({"unit step function":BLUE})
        belowText1.scale(0.4)
        belowText2.scale(0.4)
        belowText3a.scale(0.4)
        belowText3b.scale(0.4)
        belowText1.shift(2.7*DOWN+4*RIGHT)
        belowText2.shift(2.7*DOWN+4*RIGHT)
        belowText3a.shift(2.7*DOWN+4*RIGHT)
        belowText3b.shift(3.1*DOWN+4*RIGHT)
        self.setup_axes(animate=True)
        self.play(Write(belowText1))
        self.play(ShowCreation(f))
        ft.shift(1.5*RIGHT+UP*0.8)
        self.play(FadeIn(ft))
        self.play(ReplacementTransform(belowText1,belowText2))
        ftminusc.shift(3.5*RIGHT+UP*0.8)
        self.play(ReplacementTransform(f,yFull),ReplacementTransform(ft,ftminusc),Write(c))
        self.wait(1)

        self.play(ReplacementTransform(belowText2,belowText3a))
        self.play(Write(belowText3b))
        final.shift(3.7*RIGHT+UP*0.8)
        self.play(ReplacementTransform(ftminusc,final),ReplacementTransform(yFull,y))

        finalText=TextMobject("We got our required Graph!")
        finalText.scale(0.55)
        finalText.shift(2.7*DOWN+4*RIGHT)
        self.play(FadeOut(belowText3b),ReplacementTransform(belowText3a,finalText))
        self.wait(1.5)

        self.play(FadeOut(finalText),FadeOut(text1))

        graphGrup=VGroup(self.axes,c,final,y)
        self.play(ApplyMethod(graphGrup.scale,0.45))
        box=Square(side_length=2,fill_color=BLUE,fill_opacity=0.7)
        boxtext=TextMobject("$\mathscr{L}$")
        boxtext.scale(0.8)
        self.play(ApplyMethod(graphGrup.shift,5.5*LEFT+UP))
        self.play(ShowCreation(box),Write(boxtext))
        outText=TextMobject("${ e }^{ -cs }F(s)$")
        outText.set_color(GREEN)
        outText.scale(0.65)
        outText.shift(2*RIGHT)
        self.play(ApplyMethod(graphGrup.shift,2*RIGHT))
        self.play(FadeOut(graphGrup),FadeIn(outText))
        self.play(ApplyMethod(outText.shift,RIGHT))
        self.wait(2)
