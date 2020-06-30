from manimlib.imports import *
import numpy as np
import math

class graph1(GraphScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 5,
        "y_min": -1,
        "y_max": 1,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": BLUE,
        "x_axis_label": "$n$",
        "y_axis_label": "$x(n)$",
        "x_labeled_nums": range(-3, 6, 1),
        "y_axis_height": 7,
        "y_tick_frequency": 0.1,
    }
    def func(self,x,n):
        summ=0
        for i in range(n+1):
            summ+=(1/(math.pow(x,i)))
        return summ

    def finalFunc(self,x):
        if(x!=0):
            return 1/(1-(1/(2*x)))
            

    def construct(self):
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)   
        self.setup_axes(animate=True,scalee=0.8)  
        function=TextMobject("$X(t)=\sum _{ n=0 }^{ \infty  }{ { (0.5) }^{ n }{ z }^{ -n } }$").scale(0.4).shift(5*RIGHT+3*UP).set_color(RED)
        self.play(FadeIn(function))
        twoDGraph=[]
        for i in range(5):
            twoDGraph.append(Line(start=(i*x_each_unit,0,0),end=(i*x_each_unit,math.pow(0.5,i)*y_each_unit,0),color=GREEN))

        groupGraph=VGroup(self.axes,twoDGraph[0],twoDGraph[1],twoDGraph[2],twoDGraph[3],twoDGraph[4])
        self.play(Write(twoDGraph[0]),ShowCreation(twoDGraph[1]),ShowCreation(twoDGraph[2]),ShowCreation(twoDGraph[3]),ShowCreation(twoDGraph[4]))
        self.wait(1.2)

        self.play(ApplyMethod(groupGraph.scale,0.7))
        self.play(ApplyMethod(groupGraph.shift,6*LEFT),ApplyMethod(function.move_to,5*LEFT+3*UP))
        
        someText1=TextMobject("Since it is a","summation","of","infinite terms",", it might").shift(2*RIGHT+2*UP).scale(0.5).set_color_by_tex_to_color_map({"summation":YELLOW,"infinite terms":BLUE})
        someText2=TextMobject("Converge","or","Diverge").shift(2*RIGHT+0.5*DOWN+2*UP).scale(0.7).set_color_by_tex_to_color_map({"Converge":GREEN,"Diverge":RED})
        someText3=TextMobject("depending upon","$|z|$").shift(2*RIGHT+UP).scale(0.5).set_color_by_tex_to_color_map({"$|z|$":YELLOW})
        self.play(Write(someText1))
        self.play(FadeIn(someText2))
        self.play(Write(someText3))
        self.wait(1)
        self.play(FadeOut(someText1),FadeOut(someText2),FadeOut(someText3))

        self.graph_origin=2*RIGHT+DOWN
        self.x_axis_width=6
        self.y_axis_height=5
        self.y_tick_frequency=1
        self.x_axis_label="$|z|$"
        self.y_axis_label="$|X(n)|$"
        self.x_min=-3
        self.x_max=5
        self.y_min=-1
        self.y_max=5
        self.x_labeled_nums=range(-3,6,1)
        self.setup_axes(animate=True,scalee=0.6)
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)   
        rightSideGraphs=[]
        xmins=[0,0.25,0.65,0.9,1]
        for i in range(5):
            rightSideGraphs.append(self.get_graph(lambda x:self.func(x,i),x_min=xmins[i],x_max=5,color=GREEN))
        rightSideGraphs.append(self.get_graph(lambda x:1/(1-(1/(2*x))),x_min=0.63,x_max=5,color=GREEN))

        graphCoeff=[
                    TextMobject("$1$").scale(0.4).shift(self.graph_origin+x_each_unit*RIGHT*2+0.65*UP*y_each_unit*2+DOWN*y_each_unit*0.5).set_color(RED),
                    TextMobject("$1+\\frac { 1 }{ 2|z| }$").scale(0.4).shift(self.graph_origin+x_each_unit*RIGHT*2+UP*y_each_unit).set_color(RED),
                    TextMobject("$1+\\frac { 1 }{ 2|z| } +\\frac { 1 }{ { 2|z| }^{ 2 } } $").scale(0.4).shift(self.graph_origin+x_each_unit*RIGHT*2+UP*y_each_unit).set_color(RED),
                    TextMobject("$1+\\frac { 1 }{ 2|z| } +\\frac { 1 }{ { (2|z|) }^{ 2 } } +\\frac { 1 }{ { (2|z|) }^{ 3 } }$").scale(0.4).shift(self.graph_origin+x_each_unit*RIGHT*2+UP*y_each_unit).set_color(RED),
                    TextMobject("$1+\\frac { 1 }{ 2|z| } +\\frac { 1 }{ { (2|z|) }^{ 2 } } +\\frac { 1 }{ { (2|z|) }^{ 3 } } +\\frac { 1 }{ (2|z|)^{ 4 } } $").scale(0.4).shift(self.graph_origin+x_each_unit*RIGHT*2+UP*y_each_unit).set_color(RED),
                    TextMobject("$\\frac { 1 }{ (1-\\frac { 1 }{ 2z } ) } $").scale(0.4).shift(self.graph_origin+x_each_unit*RIGHT*2+UP*y_each_unit).set_color(RED)
        ]

        self.play(ReplacementTransform(twoDGraph[0],rightSideGraphs[0]),FadeIn(graphCoeff[0]))
        self.wait(0.5)
        self.play(FadeOut(rightSideGraphs[0]),ReplacementTransform(twoDGraph[1],rightSideGraphs[1]),ReplacementTransform(graphCoeff[0],graphCoeff[1]))
        self.wait(0.5)
        self.play(FadeOut(rightSideGraphs[1]),ReplacementTransform(twoDGraph[2],rightSideGraphs[2]),ReplacementTransform(graphCoeff[1],graphCoeff[2]))
        self.wait(0.5)
        self.play(FadeOut(rightSideGraphs[2]),ReplacementTransform(twoDGraph[3],rightSideGraphs[3]),ReplacementTransform(graphCoeff[2],graphCoeff[3]))
        self.wait(0.5)
        self.play(FadeOut(rightSideGraphs[3]),ReplacementTransform(twoDGraph[4],rightSideGraphs[4]),ReplacementTransform(graphCoeff[3],graphCoeff[4]))
        self.wait(0.5)
        self.play(FadeOut(rightSideGraphs[4]),ShowCreation(rightSideGraphs[5]),ReplacementTransform(graphCoeff[4],graphCoeff[5]))
        
        self.wait(2)
        # #self.play(FadeOut(self.axes),FadeOut(function),FadeOut(twoDGraph[0]),FadeOut(twoDGraph[1]),FadeOut(twoDGraph[2]))


class graphCont(GraphScene,MovingCameraScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 5,
        "y_min": -1,
        "y_max": 5,
        "graph_origin": 2*RIGHT+DOWN,
        "function_color": RED,
        "axes_color": BLUE,
        "x_axis_label": "$|z|$",
        "y_axis_label": "$|X(n)|$",
        "x_labeled_nums": range(-3, 6, 1),
        "x_axis_width": 6,
        "y_axis_height": 5
    }
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)   

        coeff=TextMobject("$\\frac { 1 }{ (1-\\frac { 1 }{ 2z } ) } $").scale(0.4).shift(self.graph_origin+x_each_unit*RIGHT*2+UP*y_each_unit).set_color(RED)
        self.setup_axes(scalee=0.6)
        graph=self.get_graph(lambda x:1/(1-(1/(2*x))),x_min=0.63,x_max=5,color=GREEN)
        
        self.add(graph)
        self.add(coeff)
        
        self.play(ApplyMethod((self.axes).shift,3*LEFT),ApplyMethod(coeff.shift,3*LEFT),ApplyMethod(graph.shift,3*LEFT))      
        self.wait(1)

        dashLine=DashedLine(start=self.graph_origin+3*LEFT+0.5*x_each_unit*RIGHT,end=self.graph_origin+3*LEFT+0.5*x_each_unit*RIGHT+y_each_unit*UP*5,color=YELLOW)
        pt=TextMobject("0.5").scale(0.3).shift(self.graph_origin+3*LEFT+0.5*x_each_unit*RIGHT+DOWN*y_each_unit*0.3)
        self.play(Write(dashLine))
        self.play(Write(pt))
        self.wait(0.6)
        rectRegion=Rectangle(height=y_each_unit*5,width=x_each_unit*5,fill_color=WHITE,fill_opacity=0.3,opacity=0.3,color=BLACK).shift(1.6*RIGHT*x_each_unit+0.5*DOWN*y_each_unit+1.5*UP)
        self.play(ShowCreation(rectRegion))
        text=TextMobject("Region Of Convergence!").scale(0.4).shift(4.6*RIGHT+1.5*UP).set_color(GREEN)
        self.play(FadeIn(text))
        self.wait(2)
