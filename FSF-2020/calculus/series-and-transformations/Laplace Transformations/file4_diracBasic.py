from manimlib.imports import *
import math
import pylatex

class intro(GraphScene,Scene):
    CONFIG = {
        "x_min": -9,
        "x_max": 9,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN+DOWN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$x$",
        "y_axis_label": "$\delta (x)$",
        "y_axis_height":4,
        "x_axis_width":7
    }
    def setup(self):
        GraphScene.setup(self)
        Scene.setup(self)
    def construct(self):
        introText=TextMobject("Dirac","Delta","Function")
        introText.set_color_by_tex_to_color_map({"Dirac":BLUE,"Delta":YELLOW})
        introText.scale(0.8)
        self.play(Write(introText))
        self.wait(0.5)
        self.play(ApplyMethod(introText.shift,3*UP))
        formulaa=TextMobject("$\delta (x)=\infty$","$x=0$")
        formulab=TextMobject("$\delta (x)=0$","$x\\neq 0$")
        formulaa.set_color_by_tex_to_color_map({"$x=0$":RED})
        formulab.set_color_by_tex_to_color_map({"$x\\neq 0$":RED})
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

        functionUpLine=Line(start=self.graph_origin,end=self.graph_origin+UP*y_each_unit*5,color=RED)
        functionDownLine=Line(start=self.graph_origin+UP*y_each_unit*5,end=self.graph_origin,color=RED)
        functinLeftLine=Line(start=self.graph_origin+LEFT*x_each_unit*9,end=self.graph_origin,color=RED)
        functionRightLine=Line(start=self.graph_origin,end=self.graph_origin+RIGHT*x_each_unit*9,color=RED)
        functionUpLine.shift(0.02*LEFT)
        functionRightLine.shift(0.02*RIGHT)

        self.play(ShowCreation(functinLeftLine))
        self.play(ShowCreation(functionUpLine))
        self.play(ShowCreation(functionDownLine))
        self.play(ShowCreation(functionRightLine))
        self.wait(1.5)

        self.play(FadeOut(self.axes),FadeOut(introText),FadeOut(functinLeftLine),FadeOut(functionRightLine),FadeOut(functionUpLine),FadeOut(functionDownLine))
        self.wait(0.5)
