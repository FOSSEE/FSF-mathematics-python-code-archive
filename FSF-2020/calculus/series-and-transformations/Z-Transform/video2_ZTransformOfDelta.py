from manimlib.imports import *
import numpy as np
import math

class deltaTransformation(GraphScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 3,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": BLUE,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)$",
        "x_labeled_nums": range(-3, 4, 1),
        # "y_axis_height": 4,
        # "x_axis_width": 6,
    }
    def construct(self):
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)   
        self.setup_axes(animate=True,scalee=0.8)  
        function=TextMobject("$f(t) = 2{ \delta  }_{ 0 }(t)+3{ \delta  }_{ 1 }(t)+4{ \delta  }_{ 2 }(t)$").scale(0.4).shift(5*RIGHT+3*UP).set_color(RED)
        self.play(FadeIn(function))
        twoDGraph=[
                    Line(start=(0,0,0),end=(0,2*y_each_unit,0),color=GREEN),
                    Line(start=(1*x_each_unit,0,0),end=(x_each_unit,3*y_each_unit,0),color=GREEN),
                    Line(start=(2*x_each_unit,0,0),end=(2*x_each_unit,4*y_each_unit,0),color=GREEN)
        ]
        groupGraph=VGroup(twoDGraph[1],twoDGraph[2],self.axes,twoDGraph[0])
        self.play(Write(twoDGraph[0]),ShowCreation(twoDGraph[1]),ShowCreation(twoDGraph[2]))
        self.wait(1.2)
        self.play(ApplyMethod(groupGraph.scale,0.7))
        self.play(ApplyMethod(groupGraph.shift,5*LEFT),ApplyMethod(function.move_to,5*LEFT+3*UP))
        self.graph_origin=2*RIGHT+2.5*DOWN
        self.x_axis_width=6
        self.x_axis_label="$|z|$"
        self.y_axis_label="$|F(t)|$"
        self.x_min=-3
        self.x_max=6
        self.y_min=-1
        self.y_max=7
        self.x_labeled_nums=range(-3,7,1)
        self.setup_axes(animate=True,scalee=0.6)
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)   
        rightSideGraphs=[
                        self.get_graph(lambda x:2,x_min=0,x_max=6,color=GREEN),
                        self.get_graph(lambda x:2+3/x,x_min=0.6,x_max=6,color=GREEN),
                        self.get_graph(lambda x:2+(3/x)+(4/x**2),x_min=1.24,x_max=6,color=GREEN)
        ]
        graphCoeff=[
                    TextMobject("$2$").scale(0.4).shift(self.graph_origin+x_each_unit*RIGHT*2+UP*y_each_unit*2+DOWN*y_each_unit*0.5).set_color(RED),
                    TextMobject("$2+\\frac { 3 }{ |z| }$").scale(0.4).shift(self.graph_origin+x_each_unit*RIGHT*3+UP*y_each_unit*2).set_color(RED),
                    TextMobject("$2+\\frac { 3 }{ |z| } +\\frac { 4 }{ { |z| }^{ 2 } } $").scale(0.4).shift(self.graph_origin+x_each_unit*RIGHT*3.5+UP*y_each_unit*2).set_color(RED)
        ]
        self.play(ReplacementTransform(twoDGraph[0],rightSideGraphs[0]),FadeIn(graphCoeff[0]))
        self.wait(0.5)
        self.play(FadeOut(rightSideGraphs[0]),ReplacementTransform(twoDGraph[1],rightSideGraphs[1]),ReplacementTransform(graphCoeff[0],graphCoeff[1]))
        self.wait(0.5)
        self.play(FadeOut(rightSideGraphs[1]),ReplacementTransform(twoDGraph[2],rightSideGraphs[2]),ReplacementTransform(graphCoeff[1],graphCoeff[2]))
        
        self.wait(2)


class graphCont(GraphScene,MovingCameraScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 6,
        "y_min": -1,
        "y_max": 7,
        "graph_origin": 2*RIGHT+2.5*DOWN,
        "function_color": RED,
        "axes_color": BLUE,
        "x_axis_label": "$|z|$",
        "y_axis_label": "$|F(t)|$",
        "exclude_zero_label": True,
        "x_labeled_nums": range(-3, 7, 1),
        "x_axis_width": 6,
    }
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)   

        coeff=TextMobject("$2+\\frac { 3 }{ |z| } +\\frac { 4 }{ { |z| }^{ 2 } } $").scale(0.4).shift(self.graph_origin+x_each_unit*RIGHT*3.5+UP*y_each_unit*2).set_color(RED)
        self.setup_axes(scalee=0.6)
        graph=self.get_graph(lambda x:2+(3/x)+(4/x**2),x_min=1.24,x_max=6,color=GREEN)
        xAxis=self.get_graph(lambda x:0,x_min=1.24,x_max=6).shift(3*LEFT)
        self.add(graph)
        self.add(coeff)
        self.play(ApplyMethod((self.axes).shift,3*LEFT),ApplyMethod(coeff.shift,3*LEFT),ApplyMethod(graph.shift,3*LEFT))      
        topText=TextMobject("Here we get","output","for","any value of $|z|$").scale(0.4).shift(3*UP+3*RIGHT).set_color_by_tex_to_color_map({"output":YELLOW,"any value of $|z|$":BLUE})
        topText1=TextMobject("Except for $|z|=0$").scale(0.7).shift(2.5*UP+3*RIGHT).set_color(RED)
        dot1=Dot(color=WHITE,radius=0.06)
        dot2=Dot(color=WHITE,radius=0.06)
        self.play(Write(topText))
        self.play(MoveAlongPath(dot1,graph),MoveAlongPath(dot2,xAxis),run_time=2)
        self.play(Write(topText1))
        self.play(FadeOut(dot1),FadeOut(dot2))
        self.wait(0.5)
        path=self.get_graph(lambda x:2+(3/x)+(4/x**2),x_min=1.24,x_max=0.8)
        path1=self.get_graph(lambda x:0,x_min=1.24,x_max=0.8)
        graphUpdated=self.get_graph(lambda x:2+(3/x)+(4/x**2),x_min=0.8,x_max=6,color=GREEN)
        self.camera_frame.save_state()
        self.play(FadeOut(graph),Write(graphUpdated))
        self.play(self.camera_frame.set_width, 30,
                    MoveAlongPath(dot1,path),MoveAlongPath(dot2,path1),run_time=2)
        self.wait(1)

        self.play(FadeOut(dot1),FadeOut(dot2),FadeOut(graphUpdated),FadeIn(graph),self.camera_frame.set_width,15)
        self.wait(1)



        

