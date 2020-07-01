from manimlib.imports import*
import math
import numpy as np

class coinsAnalogy(Scene):
    def construct(self):
        text1=TextMobject("Consider we have","Rs 39").shift(2*UP).scale(0.75).set_color_by_tex_to_color_map({"Rs 39":[YELLOW,PURPLE]})
        text2=TextMobject("and we want to represent them only in terms of","Rs 2","and","Rs 5").shift(UP).scale(0.6).set_color_by_tex_to_color_map({"Rs 2":YELLOW,"Rs 5":PURPLE})
        text3=TextMobject("How many","Rs 2 coins","and","Rs 5 coins","do","we need?").scale(0.8).set_color_by_tex_to_color_map({"Rs 2 coins":YELLOW,"Rs 5 coins":PURPLE,"we need?":RED})
        text4=TextMobject("We","perform","the following!").scale(0.75).shift(DOWN).set_color_by_tex_to_color_map({"perform":GREEN})

        self.play(FadeIn(text1))
        self.wait(0.6)
        self.play(Write(text2))
        self.wait(0.5)
        self.play(Write(text3))
        self.wait(0.7)
        self.play(FadeIn(text4))
        self.wait(1)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3),FadeOut(text4))

        g1=self.group("Rs 39")
        g1.shift(3*LEFT+0.75*UP)
        l1=self.line()
        l1.shift(4*LEFT)
        f1=self.fiveGroup()
        t1=self.twoGroup()
        f1.shift(3.5*LEFT+0.7*DOWN)
        andT=TextMobject("and").next_to(f1,buff=-0.1).scale(0.3)
        t1.next_to(andT,buff=0.2)
        equal1=TextMobject("$=$")
        equal1.next_to(l1,buff=0.2)

        self.play(ShowCreation(g1))
        self.play(ShowCreation(l1))
        self.play(ShowCreation(f1),Write(andT),ShowCreation(t1))
        self.play(ShowCreation(equal1))
        self.wait(0.6)

        f2=self.fiveGroup().next_to(equal1,buff=0.4)
        multiple1=TextMobject("$X7$","$\quad +$").next_to(f2,buff=0.2).set_color_by_tex_to_color_map({"$X7$":PURPLE})
        l2=self.line().next_to(multiple1,buff=0.4)
        g2=self.group("Rs 4").shift(2.75*RIGHT+0.75*UP)
        t2=self.twoGroup().shift(2.75*RIGHT+0.7*DOWN)

        self.play(ShowCreation(f2))
        self.play(ShowCreation(multiple1))
        self.play(ShowCreation(g2))
        self.play(ShowCreation(l2))
        self.play(ShowCreation(t2))
        self.wait(1)

        tempGrup=VGroup(g2,l2,t2)

        t3=self.twoGroup().next_to(multiple1,buff=0.4)
        multiple2=TextMobject("$X2$").next_to(t3,buff=0.2).set_color_by_tex_to_color_map({"$X2$":YELLOW})

        self.play(ReplacementTransform(tempGrup,t3))
        self.play(Write(multiple2))
        self.wait(2)

    def line(self):
        l=Line(start=[0,0,0],end=[2,0,0])
        return l

    def twoGroup(self):
        two=Circle(radius=0.25,color=BLACK,fill_color=YELLOW,fill_opacity=0.7)
        twoText=TextMobject("Rs 2").scale(0.25).set_color(BLACK)
        twoGrup=VGroup(two,twoText)
        return twoGrup

    def fiveGroup(self):
        five=Circle(radius=0.35,color=BLACK,fill_color=PURPLE,fill_opacity=0.7)
        fiveText=TextMobject("Rs 5").scale(0.3).set_color(BLACK)
        fiveGrup=VGroup(five,fiveText)
        return fiveGrup

    def group(self,money):
        coins=[
            Circle(radius=0.35,color=GREY,fill_color=GREY,fill_opacity=0.75),
            Circle(radius=0.35,color=GREY,fill_color=GREY,fill_opacity=0.8),
            Circle(radius=0.35,color=GREY,fill_color=GREY,fill_opacity=0.7),
            Circle(radius=0.35,color=GREY,fill_color=GREY,fill_opacity=0.75),
            Circle(radius=0.35,color=GREY,fill_color=GREY,fill_opacity=0.8),
            Circle(radius=0.35,color=GREY,fill_color=GREY,fill_opacity=0.7)
        ]
        coinsText=TextMobject(money).set_color(BLACK)
        coinsText.scale(0.35)

        coins[1].shift(0.2*RIGHT+0.2*UP)
        coins[2].shift(0.2*RIGHT+0.1*DOWN)
        coins[3].shift(0.2*DOWN)
        coins[4].shift(0.2*UP+0.2*LEFT)
        coins[5].shift(0.2*LEFT+0.1*LEFT)

        coinsGrup=VGroup(coins[0],coins[1],coins[2],coins[3],coins[4],coins[5],coinsText)
        return coinsGrup

class divideFunction(GraphScene):
    CONFIG = {
        "x_min": -6,
        "x_max": 6,
        "y_min": -300,
        "y_max": 300,
        "x_tick_frequency": 2,
        "y_tick_frequency": 300,
        "graph_origin": 3*LEFT+1.5*UP+6*LEFT,
        "function_color": RED,
        "axes_color": BLUE,
        "x_axis_label": "$t$",
        "y_axis_label": "$y$",
        "x_labeled_nums": [-6,0,6],
        "y_labeled_nums": [-300,0,300],
        "x_axis_width": 1.5,
        "y_axis_height": 1
    }
    def line(self):
        l=Line(start=[0,0,0],end=[2,0,0])
        return l
    def construct(self):
        text1=TextMobject("Similarly,").scale(0.8).shift(UP).set_color(RED)
        text2=TextMobject("To find the amount of","each frequency","present in","$f(x)$").scale(0.6).set_color_by_tex_to_color_map({"each frequency":[YELLOW,RED],"$f(x)$":RED})
        text3=TextMobject("We","perform","the following!").scale(0.7).shift(DOWN).set_color_by_tex_to_color_map({"perform":GREEN})
        
        self.play(FadeIn(text1))
        self.wait(0.6)
        self.play(Write(text2))
        self.wait(0.7)
        self.play(FadeIn(text3))

        self.wait(1)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3))

        boxUP=Square(side_length=1.7,fill_color=BLUE_C,fill_opacity=0.5,color=BLACK).shift(3*LEFT+UP)
        boxDOWN=Square(side_length=1.7,fill_color=BLUE_C,fill_opacity=0.5,color=BLACK).shift(3*LEFT+DOWN)    

        axes=[]
        self.graph_origin=10*LEFT+1.5*UP
        self.setup_axes(scalee=1)
        axes.append(self.axes)
        fx=self.get_graph(lambda x:math.pow(x,3)-math.pow(x,2)+x-2,x_min=-2*math.pi,x_max=2*math.pi,color=RED).shift(7*RIGHT+0.5*DOWN)
        
        l=self.line().shift(4*LEFT)

        self.graph_origin=10*LEFT+1.5*DOWN
        self.y_min=-2
        self.y_max=1
        self.y_tick_frequency=1
        self.y_labeled_nums=[-1,0,1]
        self.setup_axes(scalee=1)
        axes.append(self.axes)
        sinx=self.get_graph(lambda x:np.sin(x),x_min=-2*math.pi,x_max=2*math.pi,color=PURPLE_C).shift(7*RIGHT+0.5*UP)
        
        equal=TextMobject("$=$").next_to(l,buff=0.3)
        result1=TextMobject("Amount of").scale(0.6).next_to(equal,buff=0.3)
        boxRIGHT=Square(side_length=1.7,fill_color=GOLD_B,fill_opacity=0.5,color=BLACK).next_to(result1,buff=0.2)
        self.graph_origin=10*LEFT
        sinxResult=self.get_graph(lambda x:np.sin(x),color=PURPLE_C).next_to(result1,buff=0.3)
        axes.append(self.axes)
        result2=TextMobject("in","$f(x)$").scale(0.6).next_to(sinxResult,buff=0.2).set_color_by_tex_to_color_map({"$f(x)$":RED})

        self.play(FadeIn(boxUP))
        self.play(ShowCreation(fx))
        self.play(ShowCreation(l))
        self.play(FadeIn(boxDOWN))
        self.play(ShowCreation(sinx))
        self.wait(0.4)
        self.play(Write(equal))
        self.play(Write(result1))
        self.play(FadeIn(boxRIGHT))
        self.play(ShowCreation(sinxResult))
        self.play(Write(result2))
        aText1=TextMobject("and").scale(0.65).shift(4*RIGHT+2*DOWN).set_color(GREEN)
        self.play(Write(aText1))
        self.wait(0.7)

        self.graph_origin=10*LEFT
        cos4x=self.get_graph(lambda x:np.cos(4*x),color=PURPLE_A).shift(7*RIGHT+0.5*UP)
        axes.append(self.axes)
        self.graph_origin=10*LEFT
        cos4xResult=self.get_graph(lambda x:np.cos(4*x),color=PURPLE_A).next_to(result1,buff=0.3)
        axes.append(self.axes)
        self.play(ReplacementTransform(sinx,cos4x),ReplacementTransform(sinxResult,cos4xResult))
        self.wait(0.7)

        soText=TextMobject("And so on..!").scale(0.65).shift(4*RIGHT+2*DOWN).set_color(GREEN)
        self.play(ReplacementTransform(aText1,soText))

        self.graph_origin=10*LEFT
        cosx=self.get_graph(lambda x:np.cos(x),color=GREEN_E).shift(7*RIGHT+0.5*UP)
        axes.append(self.axes)
        self.graph_origin=10*LEFT
        cosxResult=self.get_graph(lambda x:np.cos(x),color=GREEN_E).next_to(result1,buff=0.3)
        axes.append(self.axes)
        self.play(ReplacementTransform(cos4x,cosx),ReplacementTransform(cos4xResult,cosxResult))      

        self.graph_origin=10*LEFT
        cos3x=self.get_graph(lambda x:np.cos(3*x),color=GREEN_C).shift(7*RIGHT+0.5*UP)
        axes.append(self.axes)
        self.graph_origin=10*LEFT
        cos3xResult=self.get_graph(lambda x:np.cos(3*x),color=GREEN_C).next_to(result1,buff=0.3)
        axes.append(self.axes)
        self.play(ReplacementTransform(cosx,cos3x),ReplacementTransform(cosxResult,cos3xResult))

        self.graph_origin=10*LEFT
        const=self.get_graph(lambda x:1,color=YELLOW_B).shift(7*RIGHT+0.5*UP)
        axes.append(self.axes)
        self.graph_origin=10*LEFT
        constResult=self.get_graph(lambda x:1,color=YELLOW_B).next_to(result1,buff=0.3)
        axes.append(self.axes)
        self.play(ReplacementTransform(cos3x,const),ReplacementTransform(cos3xResult,constResult))

        self.wait(1)

        self.play(FadeOut(soText),FadeOut(const),FadeOut(constResult),FadeOut(l),FadeOut(equal),FadeOut(result1),FadeOut(result2),FadeOut(fx),FadeOut(boxRIGHT),FadeOut(boxUP),FadeOut(boxDOWN))

        finalFormula1=TexMobject(r"Therefore,",r"F(s)",r"=",r"\int _{ -\infty  }^{ \infty  }",r"{f(t)",r"\over",r"sines",r"\enspace and \enspace",r"cosines}",r"dt }").scale(0.7).set_color_by_tex_to_color_map({"F(s)":RED,"sines":BLUE,"cosines}":YELLOW,"{f(t)":GREEN})
        finalFormula2=TexMobject(r"F(s)",r"=",r"\int _{ -\infty  }^{ \infty  }",r"{f(t)",r"\over",r"{ e }^",r"{ i\theta  }}",r"dt }").set_color_by_tex_to_color_map({"F(s)":RED,"{f(t)":GREEN})
        subFinalFormula=TextMobject("where","$\\theta =2\pi st$").scale(0.5).shift(DOWN+2*RIGHT).set_color_by_tex_to_color_map({"$\\theta =2\pi st$":RED})

        self.play(Write(finalFormula1))
        self.wait(1)
        self.play(ReplacementTransform(finalFormula1,finalFormula2))
        self.play(Write(subFinalFormula))
        self.wait(2)
