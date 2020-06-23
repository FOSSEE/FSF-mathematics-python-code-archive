from manimlib.imports import *
import math
import pylatex

def func(x,t):
    if(x>-t and x<t):
        return 1/(2*t)
    else:
        return 0
        

class formation(GraphScene):
    CONFIG = {
        "x_min": -7,
        "x_max": 7,
        "y_min": -2,
        "y_max": 2,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$t$",
        "y_axis_label": "$y$",
        "y_labeled_nums":range(-2,3),
        "y_axis_height":4,
        "x_axis_width":7
    }
    def construct(self):
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)

        text1=TextMobject("Consider the","following function's graph!")
        text1.set_color_by_tex_to_color_map({"following function's graph!":BLUE})
        text1.scale(0.6)

        equation1=TextMobject("$\delta _{ \\tau  }(t)=\\frac { 1 }{ 2\\tau  } \quad$","$-\\tau <t<\\tau$")
        equation2=TextMobject("$\delta _{ \\tau  }(t)=0\quad \quad$","$t\in (-\infty ,-\\tau ]\cup [\\tau ,\infty )$")
        equation1.scale(0.7)
        equation2.scale(0.7)
        equation1.shift(0.2*UP)
        equation2.shift(0.4*DOWN+RIGHT*0.8)
        equation1.set_color_by_tex_to_color_map({"$-\\tau <t<\\tau$":RED})
        equation2.set_color_by_tex_to_color_map({"$t\in (-\infty ,-\\tau ]\cup [\\tau ,\infty )$":RED})

        self.play(Write(text1))
        self.play(ApplyMethod(text1.shift,3*UP))
        self.play(Write(equation1))
        self.play(Write(equation2)) 
        self.wait(1)

        self.play(FadeOut(equation1),FadeOut(equation2))
        self.wait(0.5)

        pointes1=TextMobject("$-\\tau$")
        pointes2=TextMobject("$\\tau$")
        pointes1.set_color(RED)
        pointes2.set_color(RED)
        pointes1.scale(0.65)
        pointes2.scale(0.65)
        
        bottomText1=TextMobject("Here","$\int _{ -\infty  }^{ \infty  }{ \delta _{ \\tau  }(t)dt }$","=","$1$")
        bottomText2=TextMobject("Now as","$\\tau \\rightarrow 0$")
        bottomText3=TextMobject("We get our","Dirac Function!")
        bottomText4=TextMobject("i.e.","$\lim _{ \\tau \\rightarrow 0 }{ \delta _{ \\tau  }(t)}$","$=$","$\delta (t)$")
        textFinal=TextMobject("Area=1")
        bottomText1.set_color_by_tex_to_color_map({"$\int _{ -\infty  }^{ \infty  }{ \delta _{ \\tau  }(t)dt }$":BLUE,"$1$":YELLOW})
        textFinal.set_color(PURPLE_B)
        bottomText2.set_color_by_tex_to_color_map({"$\\tau \\rightarrow 0$":YELLOW})
        bottomText3.set_color_by_tex_to_color_map({"Dirac Function!":RED})
        bottomText4.set_color_by_tex_to_color_map({"$\lim _{ \\tau \\rightarrow 0 }{ \delta _{ \\tau  }(t)}$":BLUE,"$\delta (t)$":YELLOW})

        bottomText1.scale(0.6)
        bottomText2.scale(0.6)
        bottomText3.scale(0.6)
        bottomText4.scale(0.6)
        textFinal.scale(0.9)

        bottomText1.shift(4*RIGHT+3*DOWN)
        bottomText2.shift(4*RIGHT+3*DOWN)
        bottomText3.shift(4*RIGHT+3*DOWN)
        bottomText4.shift(4*RIGHT+3*DOWN)
        textFinal.shift(5*RIGHT+2*UP)
        
        self.setup_axes(animate=True)

        graphs=[
            self.get_graph(lambda x:func(x,3),x_min=-7,x_max=7,color=RED),
            self.get_graph(lambda x:func(x,2),x_min=-7,x_max=7,color=RED),
            self.get_graph(lambda x:func(x,1),x_min=-7,x_max=7,color=RED),
            self.get_graph(lambda x:func(x,0.5),x_min=-7,x_max=7,color=RED),
            self.get_graph(lambda x:func(x,0.3),x_min=-7,x_max=7,color=RED),
            self.get_graph(lambda x:func(x,0.15),x_min=-7,x_max=7,color=RED),
            self.get_graph(lambda x:func(x,0.05),x_min=-7,x_max=7,color=RED),
            self.get_graph(lambda x:func(x,0.01),x_min=-7,x_max=7,color=RED)
        ]
        pointes1.shift(self.graph_origin+3*LEFT*x_each_unit+0.4*DOWN*y_each_unit)
        pointes2.shift(self.graph_origin+3*RIGHT*x_each_unit+0.4*DOWN*y_each_unit)

        functionUpLine=Line(start=self.graph_origin,end=self.graph_origin+UP*y_each_unit*2,color=RED)
        functionDownLine=Line(start=self.graph_origin+UP*y_each_unit*2,end=self.graph_origin,color=RED)
        functinLeftLine=Line(start=self.graph_origin+LEFT*x_each_unit*7,end=self.graph_origin,color=RED)
        functionRightLine=Line(start=self.graph_origin,end=self.graph_origin+RIGHT*x_each_unit*7,color=RED)
        functionUpLine.shift(0.02*LEFT)
        functionRightLine.shift(0.02*RIGHT)

        self.play(Write(pointes1),Write(pointes2),ShowCreation(graphs[0]))
        self.play(Write(bottomText1))
        self.wait(0.7)
        
        self.play(ReplacementTransform(bottomText1,bottomText2),Write(textFinal))
        self.wait(0.5)
        self.play(ReplacementTransform(graphs[0],graphs[1]),ApplyMethod(pointes2.shift,LEFT*x_each_unit),ApplyMethod(pointes1.shift,RIGHT*x_each_unit))
        self.play(ReplacementTransform(graphs[1],graphs[2]),ApplyMethod(pointes2.shift,LEFT*x_each_unit),ApplyMethod(pointes1.shift,RIGHT*x_each_unit))
        self.wait(0.5)
        self.play(ReplacementTransform(graphs[2],graphs[3]),FadeOut(pointes1),FadeOut(pointes2))
        self.play(ReplacementTransform(graphs[3],graphs[4]))
        self.wait(1)
        self.play(ReplacementTransform(bottomText2,bottomText3))
        self.wait(1)
        self.play(FadeOut(graphs[4]),ReplacementTransform(bottomText3,bottomText4))
        self.wait(0.5)
        self.play(ShowCreation(functinLeftLine))
        self.play(ShowCreation(functionUpLine))
        self.play(ShowCreation(functionDownLine))
        self.play(ShowCreation(functionRightLine))
        self.wait(2)

        self.play(FadeOut(bottomText4),FadeOut(textFinal))
        graphGrup=VGroup(self.axes,functinLeftLine,functionDownLine,functionRightLine,functionUpLine)
        self.play(ApplyMethod(graphGrup.scale,0.5))
        box=Square(side_length=2,fill_color=BLUE,fill_opacity=0.6)
        boxtext=TextMobject("$\mathscr{L}$")
        boxtext.scale(0.8)
        self.play(ApplyMethod(graphGrup.shift,4.9*LEFT))
        self.play(ShowCreation(box),Write(boxtext))
        outText=TextMobject("$f(0)$")
        outText.set_color(GREEN)
        outText.scale(0.65)
        outText.shift(1.5*RIGHT)
        self.play(ApplyMethod(graphGrup.shift,2*RIGHT))
        self.play(FadeOut(graphGrup),FadeIn(outText))
        self.play(ApplyMethod(outText.shift,RIGHT))
        self.wait(2)