from manimlib.imports import*
import numpy as np

class intro(GraphScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 3,
        "x_axis_width": 6,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": 10.5*LEFT,
        "axes_color": BLUE,
        "exclude_zero_label": True,
        "x_labeled_nums": range(-2, 3, 1),
    }
    def func(self,t,n1,n2):
        s=0
        for i in range(n1,n2+1):
            s+=((-2/(i*np.pi))*((-1)**i)*np.sin(2*np.pi*i*t))
        return s
    
    def construct(self):
        image=ImageMobject('image.png').shift(5.5*LEFT+2.5*UP).scale(1.5)
        self.play(ShowCreation(image))

        self.setup_axes(scalee=1)
        
        mainGraphs=[
            self.get_graph(lambda x:self.func(x,2,7),x_max=2,x_min=-2).shift(9.3*RIGHT+3*UP).set_color([ORANGE,GREEN_B,RED_E,YELLOW_E,RED_D,YELLOW_D]).scale(1.4),
            self.get_graph(lambda x:self.func(x,3,7),x_max=2,x_min=-2).shift(10.8*RIGHT+3*UP).set_color([GREEN_B,ORANGE,RED_D,YELLOW_E,YELLOW_D]).scale(1.4),
            self.get_graph(lambda x:self.func(x,4,7),x_max=2,x_min=-2).shift(10.8*RIGHT+3*UP).set_color([GREEN_B,YELLOW_E,ORANGE,YELLOW_D]).scale(1.4),
            self.get_graph(lambda x:self.func(x,5,7),x_max=2,x_min=-2).shift(10.8*RIGHT+3*UP).set_color([YELLOW_E,GREEN_B,YELLOW_D]).scale(1.4),
            self.get_graph(lambda x:self.func(x,6,7),x_max=2,x_min=-2).shift(10.8*RIGHT+3*UP).set_color([YELLOW_D,GREEN_B]).scale(1.4),
            self.get_graph(lambda x:self.func(x,7,7),x_max=2,x_min=-2,color=GREEN_B).shift(10.8*RIGHT+3*UP).scale(1.4),
        ]
        self.play(ApplyMethod(mainGraphs[0].shift,1.5*RIGHT))

        graph1=self.get_graph(lambda x:self.func(x,2,2),x_max=2,x_min=-2,color=RED_E).shift(10.8*RIGHT+3*UP).scale(1.5)
        graph2=self.get_graph(lambda x:self.func(x,3,3),x_max=2,x_min=-2,color=RED_D).shift(10.8*RIGHT+3*UP).scale(1.5)
        graph3=self.get_graph(lambda x:self.func(x,4,4),x_max=2,x_min=-2,color=ORANGE).shift(10.8*RIGHT+3*UP).scale(1.5)
        graph4=self.get_graph(lambda x:self.func(x,5,5),x_max=2,x_min=-2,color=YELLOW_E).shift(10.8*RIGHT+3*UP).scale(1.5)
        graph5=self.get_graph(lambda x:self.func(x,6,6),x_max=2,x_min=-2,color=YELLOW_D).shift(10.8*RIGHT+3*UP).scale(1.5)
       
        coeff=[
            TextMobject("$\\frac { -1 }{ \pi  } sin(4\pi t)$").scale(0.5).shift(DOWN+4.6*RIGHT+3*UP).set_color(RED_E),
            TextMobject("$\\frac { 2 }{ 3\pi  } sin(6\pi t)$").scale(0.5).shift(2*DOWN+4.6*RIGHT+3*UP).set_color(RED_D),
            TextMobject("$\\frac { -1 }{ 2\pi  } sin(8\pi t)$").scale(0.5).shift(3*DOWN+4.6*RIGHT+3*UP).set_color(ORANGE),
            TextMobject("$\\frac { 2 }{ 5\pi  } sin(10\pi t)$").scale(0.5).shift(4*DOWN+4.6*RIGHT+3*UP).set_color(YELLOW_E),
            TextMobject("$\\frac { -1 }{ 3\pi  } sin(12\pi t)$").scale(0.5).shift(5*DOWN+4.6*RIGHT+3*UP).set_color(YELLOW_D),
            TextMobject("$\\frac { 2 }{ 7\pi  } sin(14\pi t)$").scale(0.5).shift(6*DOWN+4.6*RIGHT+3*UP).set_color(GREEN_B)
        ]

        self.wait(0.6)
        self.play(ApplyMethod(graph1.shift,1*DOWN),ReplacementTransform(mainGraphs[0],mainGraphs[1]))
        self.play(Write(coeff[0]))
        self.play(ApplyMethod(graph2.shift,2*DOWN),ReplacementTransform(mainGraphs[1],mainGraphs[2]))
        self.play(Write(coeff[1]))
        self.play(ApplyMethod(graph3.shift,3*DOWN),ReplacementTransform(mainGraphs[2],mainGraphs[3]))
        self.play(Write(coeff[2]))
        self.play(ApplyMethod(graph4.shift,4*DOWN),ReplacementTransform(mainGraphs[3],mainGraphs[4]))
        self.play(Write(coeff[3]))
        self.play(ApplyMethod(graph5.shift,5*DOWN),ReplacementTransform(mainGraphs[4],mainGraphs[5]))
        self.play(Write(coeff[4]))
        self.play(ApplyMethod(mainGraphs[5].shift,6*DOWN))
        self.play(Write(coeff[5]))

        pluses=[TextMobject("+"),TextMobject("+"),TextMobject("+"),TextMobject("+"),TextMobject("+")]
        for t in pluses:
            t.scale(0.5).shift((2.2-1.5*pluses.index(t))*LEFT)
        
        finalGraph=self.get_graph(lambda x:self.func(x,2,7),x_max=2,x_min=-2).shift(10.8*RIGHT+3*UP)
        finalGraph.set_color([GREEN_B,YELLOW_D,YELLOW_E,ORANGE,RED_D,RED_E])
        finalGroup=VGroup(graph1,graph2,graph3,graph4,graph5,mainGraphs[5])
        self.play(ReplacementTransform(finalGroup,finalGraph))
        self.play(ApplyMethod(coeff[0].scale,0.7),ApplyMethod(coeff[1].scale,0.7),ApplyMethod(coeff[2].scale,0.7),ApplyMethod(coeff[3].scale,0.7),ApplyMethod(coeff[4].scale,0.7),ApplyMethod(coeff[5].scale,0.7))
        #self.play(ApplyMethod(coeff[0].shift,7*LEFT+1.6*DOWN),ApplyMethod(coeff[1].shift,5.5*LEFT+0.8*DOWN),ApplyMethod(coeff[2].shift,4*LEFT),ApplyMethod(coeff[3].shift,2.5*LEFT+0.8*UP),ApplyMethod(coeff[4].shift,LEFT+1.6*UP),ApplyMethod(coeff[5].shift,0.5*RIGHT+2.4*DOWN))
        self.play(ApplyMethod(coeff[0].shift,7.6*LEFT+2*DOWN),ApplyMethod(coeff[1].shift,6.1*LEFT+DOWN),ApplyMethod(coeff[2].shift,4.6*LEFT),ApplyMethod(coeff[3].shift,3.1*LEFT+UP),ApplyMethod(coeff[4].shift,1.6*LEFT+2*UP),ApplyMethod(coeff[5].shift,0.1*LEFT+3*UP))
        equal=TextMobject("=").scale(1.5).shift(1.5*UP)
        self.play(Write(equal))
        self.play(Write(pluses[0]),Write(pluses[1]),Write(pluses[2]),Write(pluses[3]),Write(pluses[4]))
        group=VGroup(pluses[0],pluses[1],pluses[2],pluses[3],pluses[4],coeff[0],coeff[1],coeff[2],coeff[3],coeff[4],coeff[5])
        self.play(ApplyMethod(group.scale,1.5))
        self.wait(2)
