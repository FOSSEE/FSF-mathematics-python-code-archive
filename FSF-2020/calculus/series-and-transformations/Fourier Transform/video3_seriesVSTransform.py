from manimlib.imports import *
import numpy as np

class compare(GraphScene,MovingCameraScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 3,
        "x_axis_width": 6,
        "y_min": -5,
        "y_max": 5,
        "y_axis_label":"$\\frac { { x }^{ 2 } }{ 2 } $",
        "graph_origin": ORIGIN,
        "axes_color": BLUE,
        "exclude_zero_label": True,
        "x_labeled_nums": range(-2, 3, 1),
    }
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)
    def returnPairLines(self,left,right,y_each_unit):
        lineLeft=DashedLine(start=(0,5*y_each_unit,0),end=(0,-5*y_each_unit,0)).shift(left)
        lineRight=DashedLine(start=(0,5*y_each_unit,0),end=(0,-5*y_each_unit,0)).shift(right)
        return lineLeft,lineRight

    def resultFunc(self,x,n,l):
        s=(l**2)/6
        for n in range(1,n+1):
            s+=(2*((-1)**n))*((l**2)*np.cos(n*np.pi*x/l))*(1/((np.pi**2)*(n**2)))
        return s

    def returnPartFunction(self,left,right):
        return self.get_graph(lambda x:(x**2)/2,x_min=left,x_max=right,color=RED)
    
    def returnPartResult(self,l,n):
        return self.get_graph(lambda x:self.resultFunc(x,n,l),x_min=-3,x_max=3,color=RED)
    
    def construct(self):
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)   
        axes=[]
        self.setup_axes(animate=True,scalee=1)
        axes.append(self.axes)
        partFunction1=self.returnPartFunction(-1,1).shift(4*LEFT)
        partFunction2=self.returnPartFunction(-2,2).shift(4*LEFT)
        functionText=TextMobject("$\\frac { { x }^{ 2 } }{ 2 } $")
        function=self.get_graph(lambda x:(x**2)/2,x_min=-3,x_max=3,color=GREEN)
        text1=TextMobject("Non-Periodic function").scale(0.5).shift(3*DOWN+3*RIGHT).set_color(RED)
        self.play(ShowCreation(function))
        self.play(FadeIn(text1))
        self.wait(1)
        self.play(FadeOut(text1))
        self.play(ApplyMethod(axes[0].shift,4*LEFT),ApplyMethod(function.shift,4*LEFT))
        text2=TextMobject("For a","given","interval of $x$,").scale(0.5).shift(2.5*RIGHT+UP).set_color_by_tex_to_color_map({"given":YELLOW,"interval of $x$,":BLUE})
        text3=TextMobject("We can get the","Fourier Series","of that","particular part!").scale(0.4).shift(2.5*RIGHT+0.5*UP).set_color_by_tex_to_color_map({"particular part!":YELLOW,"Fourier Series":RED})
        self.play(Write(text2))
        left,right=self.returnPairLines((4+x_each_unit)*LEFT,(4-x_each_unit)*LEFT,y_each_unit)
        self.play(ShowCreation(left),ShowCreation(right))
        self.play(Write(text3))
        self.wait(0.5)
        self.play(FadeOut(text2),FadeOut(text3))
        self.graph_origin=3.5*RIGHT
        self.y_axis_label="$\\frac { { l }^{ 2 } }{ 6 } +\sum _{ n=1 }^{ \infty  }{ \\frac { 2{ (-1) }^{ n }{ l }^{ 2 }cos(\\frac { n\pi x }{ l } ) }{ { \pi  }^{ 2 }{ n }^{ 2 } }  }$"
        self.setup_axes(animate=True,scalee=1)
        axes.append(self.axes)      
        coeffResult=[
            TextMobject("$\\frac { { 1 }^{ 2 } }{ 6 } +\sum _{ n=1 }^{ 1 }{ \\frac { 2{ (-1) }^{ n }{ 1 }^{ 2 }cos(\\frac { n\pi x }{ 1 } ) }{ { \pi  }^{ 2 }{ n }^{ 2 } }  } $").scale(0.3).shift(4.5*RIGHT+UP).set_color(YELLOW),
            TextMobject("$\\frac { { 1 }^{ 2 } }{ 6 } +\sum _{ n=1 }^{ 3 }{ \\frac { 2{ (-1) }^{ n }{ 1 }^{ 2 }cos(\\frac { n\pi x }{ 1 } ) }{ { \pi  }^{ 2 }{ n }^{ 2 } }  } $").scale(0.3).shift(4.5*RIGHT+UP).set_color(YELLOW),
            TextMobject("$\\frac { { 1 }^{ 2 } }{ 6 } +\sum _{ n=1 }^{ 5 }{ \\frac { 2{ (-1) }^{ n }{ 1 }^{ 2 }cos(\\frac { n\pi x }{ 1 } ) }{ { \pi  }^{ 2 }{ n }^{ 2 } }  } $").scale(0.3).shift(4.5*RIGHT+UP).set_color(YELLOW),
            TextMobject("$\\frac { { 1 }^{ 2 } }{ 6 } +\sum _{ n=1 }^{ 7 }{ \\frac { 2{ (-1) }^{ n }{ 1 }^{ 2 }cos(\\frac { n\pi x }{ 1 } ) }{ { \pi  }^{ 2 }{ n }^{ 2 } }  } $").scale(0.3).shift(4.5*RIGHT+UP).set_color(YELLOW),
            TextMobject("$\\frac { { 1 }^{ 2 } }{ 6 } +\sum _{ n=1 }^{ 9 }{ \\frac { 2{ (-1) }^{ n }{ 1 }^{ 2 }cos(\\frac { n\pi x }{ 1 } ) }{ { \pi  }^{ 2 }{ n }^{ 2 } }  } $").scale(0.3).shift(4.5*RIGHT+UP).set_color(YELLOW),
            TextMobject("$\\frac { { 1 }^{ 2 } }{ 6 } +\sum _{ n=1 }^{ 11 }{ \\frac { 2{ (-1) }^{ n }{ 1 }^{ 2 }cos(\\frac { n\pi x }{ 1 } ) }{ { \pi  }^{ 2 }{ n }^{ 2 } }  }$").scale(0.3).shift(4.5*RIGHT+UP).set_color(YELLOW),
            TextMobject("$\\frac { { 1 }^{ 2 } }{ 6 } +\sum _{ n=1 }^{ 13 }{ \\frac { 2{ (-1) }^{ n }{ 1 }^{ 2 }cos(\\frac { n\pi x }{ 1 } ) }{ { \pi  }^{ 2 }{ n }^{ 2 } }  }$").scale(0.3).shift(4.5*RIGHT+UP).set_color(YELLOW)
        ]
        result1a=self.returnPartResult(1,1)
        result1b=self.returnPartResult(1,3)
        result1c=self.returnPartResult(1,5)
        result1d=self.returnPartResult(1,7)
        result1e=self.returnPartResult(1,9)
        result1f=self.returnPartResult(1,11)
        result1g=self.returnPartResult(1,13)
        self.play(ApplyMethod(partFunction1.shift,0.2*UP))
        self.wait(0.5)
        
        self.play(ReplacementTransform(partFunction1,result1a),Write(coeffResult[0]))
        self.play(FadeOut(axes[0]),FadeOut(left),FadeOut(right),FadeOut(function))
        self.camera_frame.save_state()
        self.play(self.camera_frame.set_width, 5,self.camera_frame.move_to, 3.5*RIGHT)
        
        
        self.play(ReplacementTransform(result1a,result1b),ReplacementTransform(coeffResult[0],coeffResult[1]))
        self.play(ReplacementTransform(result1b,result1c),ReplacementTransform(coeffResult[1],coeffResult[2]))
        self.play(ReplacementTransform(result1c,result1d),ReplacementTransform(coeffResult[2],coeffResult[3]))
        self.play(ReplacementTransform(result1d,result1e),ReplacementTransform(coeffResult[3],coeffResult[4]))
        self.play(ReplacementTransform(result1e,result1f),ReplacementTransform(coeffResult[4],coeffResult[5]))
        self.play(ReplacementTransform(result1f,result1g),ReplacementTransform(coeffResult[5],coeffResult[6]))
        
        self.wait(0.5)
        self.play(self.camera_frame.set_width, 14,self.camera_frame.move_to, 0)

        text4=TextMobject("Here the","obtained function","will always be","periodic","with period equal to the chosen interval").scale(0.4).shift(3.3*DOWN).set_color_by_tex_to_color_map({"obtained function":YELLOW,"periodic":RED})
        self.play(Write(text4))

        self.wait(0.8)

        self.play(FadeOut(text4))
        text5=TextMobject("As we","increase","the","interval of $x$,").scale(0.5).shift(3*DOWN).set_color_by_tex_to_color_map({"increase":RED,"interval of $x$,":YELLOW})
        text6=TextMobject("We get","approximation","for","higher intervals!").scale(0.5).shift(3.5*DOWN).set_color_by_tex_to_color_map({"approximation":GREEN,"higher intervals!":YELLOW})
        self.play(FadeIn(axes[0]),FadeIn(left),FadeIn(right),FadeIn(function))
        self.play(Write(text5))
        self.play(Write(text6))
        result2=self.returnPartResult(1.5,20)
        result3=self.returnPartResult(2,20)
        result4=self.returnPartResult(2.5,20)
        result5=self.returnPartResult(3,20)
        finalCoeff=coeffResult[6]
        coeffResult=[
            TextMobject("$\\frac { { 1.5 }^{ 2 } }{ 6 } +\sum _{ n=1 }^{ 20 }{ \\frac { 2{ (-1) }^{ n }{ 1.5 }^{ 2 }cos(\\frac { n\pi x }{ 2 } ) }{ { \pi  }^{ 2 }{ n }^{ 2 } }  }$").scale(0.4).shift(5*RIGHT+1.5*UP).set_color(YELLOW),
            TextMobject("$\\frac { { 2 }^{ 2 } }{ 6 } +\sum _{ n=1 }^{ 20 }{ \\frac { 2{ (-1) }^{ n }{ 2 }^{ 2 }cos(\\frac { n\pi x }{ 2 } ) }{ { \pi  }^{ 2 }{ n }^{ 2 } }  } $").scale(0.4).shift(5*RIGHT+1.5*UP).set_color(YELLOW),
            TextMobject("$\\frac { { 2.5 }^{ 2 } }{ 6 } +\sum _{ n=1 }^{ 20 }{ \\frac { 2{ (-1) }^{ n }{ 2.5 }^{ 2 }cos(\\frac { n\pi x }{ 2 } ) }{ { \pi  }^{ 2 }{ n }^{ 2 } }  } $").scale(0.4).shift(5*RIGHT+2.2*UP).set_color(YELLOW),
            TextMobject("$\\frac { { 3 }^{ 2 } }{ 6 } +\sum _{ n=1 }^{ 20 }{ \\frac { 2{ (-1) }^{ n }{ 3 }^{ 2 }cos(\\frac { n\pi x }{ 2 } ) }{ { \pi  }^{ 2 }{ n }^{ 2 } }  } $").scale(0.4).shift(5*RIGHT+2.2*UP).set_color(YELLOW),
            ]
        self.play(ApplyMethod(left.shift,LEFT*x_each_unit*0.5),ApplyMethod(right.shift,RIGHT*x_each_unit*0.5),ReplacementTransform(result1g,result2),ReplacementTransform(finalCoeff,coeffResult[0]))
        self.play(ApplyMethod(left.shift,LEFT*x_each_unit*0.5),ApplyMethod(right.shift,RIGHT*x_each_unit*0.5),ReplacementTransform(result2,result3),ReplacementTransform(coeffResult[0],coeffResult[1]))
        self.play(ApplyMethod(left.shift,LEFT*x_each_unit*0.5),ApplyMethod(right.shift,RIGHT*x_each_unit*0.5),ReplacementTransform(result3,result4),ReplacementTransform(coeffResult[1],coeffResult[2]))
        self.play(ApplyMethod(left.shift,LEFT*x_each_unit*0.5),ApplyMethod(right.shift,RIGHT*x_each_unit*0.5),ReplacementTransform(result4,result5),ReplacementTransform(coeffResult[2],coeffResult[3]))



        self.wait(2)
