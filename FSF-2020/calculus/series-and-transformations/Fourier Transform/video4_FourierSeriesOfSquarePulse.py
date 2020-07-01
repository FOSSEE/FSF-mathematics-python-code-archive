from manimlib.imports import *
import numpy as np

def returnSum(k,x):
    summ=0
    for i in range(1,k+1,2):
        summ+=((np.sin(2*np.pi*i*x))/i)
    return summ

def returnFunc(self,k):
    graph=self.get_graph(lambda x:(4/np.pi)*returnSum(k,x),color=WHITE,x_max=1,x_min=-1)
    return graph

class fourierSeries(GraphScene,MovingCameraScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 3,
        "x_axis_width": 13,
        "y_min": -3,
        "y_max": 3,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": BLUE,
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "exclude_zero_label": True,
        "x_labeled_nums": range(-2, 3, 1),
    }
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)
    def construct(self):
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)   

        equation=TextMobject("$f(x)=\\frac { 4 }{ \pi  } \sum _{ k=1,3,5.. }^{ \infty  }{ \\frac { 1 }{ k } \sin { 2\pi kx }  }$").shift(5*RIGHT+3*UP).set_color(RED).scale(0.4)
        self.add(equation)
        self.setup_axes(animate=True)
        line1=Line(start=(-x_each_unit,y_each_unit,0),end=(-(1/2)*x_each_unit,y_each_unit,0),color=RED)
        line2=Line(start=(-(1/2)*x_each_unit,y_each_unit,0),end=(-(1/2)*x_each_unit,-y_each_unit,0),color=RED)
        line3=Line(start=(-(1/2)*x_each_unit,-y_each_unit,0),end=(0,-y_each_unit,0),color=RED)
        line4=Line(start=(0,-y_each_unit,0),end=(0,y_each_unit,0),color=RED)
        line5=Line(start=(0,y_each_unit,0),end=((1/2)*x_each_unit,y_each_unit,0),color=RED)
        line6=Line(start=((1/2)*x_each_unit,y_each_unit,0),end=((1/2)*x_each_unit,-y_each_unit,0),color=RED)
        line7=Line(start=((1/2)*x_each_unit,-y_each_unit,0),end=(x_each_unit,-y_each_unit,0),color=RED)
        self.play(ShowCreation(line1))
        self.play(ShowCreation(line2))
        self.play(ShowCreation(line3))
        self.play(ShowCreation(line4))
        self.play(ShowCreation(line5))
        self.play(ShowCreation(line6))
        self.play(ShowCreation(line7))
        self.wait(0.5)

        labels=[
            TextMobject("$f_{ k=1 }(x)$"),
            TextMobject("$f_{ k=3 }(x)$"),
            TextMobject("$f_{ k=5 }(x)$"),
            TextMobject("$f_{ k=7 }(x)$"),
            TextMobject("$f_{ k=9 }(x)$"),
            TextMobject("$f_{ k=11 }(x)$"),
            TextMobject("$f_{ k=13 }(x)$"),
            TextMobject("$f_{ k=15 }(x)$"),
            TextMobject("$f_{ k=17 }(x)$"),
            TextMobject("$f_{ k=19 }(x)$"),
            TextMobject("$f_{ k=85 }(x)$")
        ]
        p=0
        for i in range(1,20,2):
            if(i==1):
                graphInitial=returnFunc(self,1)
                label=labels[p].scale(0.5).shift(y_each_unit*1.5*UP+RIGHT*x_each_unit*0.3)
                self.play(ShowCreation(graphInitial),Write(labels[0]))
                old=graphInitial
                oldLabel=label
            else:
                graph=returnFunc(self,i)
                graphLabel=labels[p].scale(0.5).shift(y_each_unit*1.5*UP+RIGHT*x_each_unit*0.3)
                self.play(ReplacementTransform(old,graph),ReplacementTransform(oldLabel,graphLabel))
                old=graph
                oldLabel=graphLabel
            p+=1
        graphFinal=returnFunc(self,85)
        labelFinal=labels[10].scale(0.5).shift(y_each_unit*1.5*UP+RIGHT*x_each_unit*0.3)
        self.play(FadeOut(old),FadeOut(oldLabel))
        self.play(ShowCreation(graphFinal),Write(labelFinal))
        self.wait(1)
        self.camera_frame.save_state()
        self.play(self.camera_frame.set_width, 2.25,self.camera_frame.move_to, y_each_unit*UP+RIGHT*x_each_unit*0.3)
        self.wait(1)
        self.play(self.camera_frame.set_width,14,self.camera_frame.move_to,0)
        self.wait(2)
