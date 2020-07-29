from manimlib.imports import *
import numpy as np

class intro(Scene):
    def construct(self):
        t1=TextMobject("Nichomachus")
        t2=TextMobject("Theorem")
        t1.scale(3)
        t2.scale(0.8)
        t1.set_color(GREEN)
        t2.set_color(WHITE)
        t1.shift(UP+0.8*LEFT)
        t2.move_to(0.3*DOWN+1.6*RIGHT)

        self.play(Write(t1))
        self.play(FadeIn(t2))
        self.wait(2)
        self.play(FadeOut(t1),FadeOut(t2))

class definition(Scene):
    def construct(self):
        t1=TextMobject("What","does","it","mean")
        question=TextMobject("?")
        question.set_color(RED)
        question.scale(4)
        t1.set_color_by_tex_to_color_map({"it":GREEN,"What":YELLOW})
        t1.scale(1.4)
        t1.move_to(0.5*LEFT+0.3*UP)
        question.next_to(t1,RIGHT,buff=0.6)
        self.play(Write(t1))
        self.play(ShowCreation(question))
        self.wait(0.5)
        self.play(ApplyMethod(question.scale,-1))
        self.wait(2)
        self.play(ApplyMethod(question.scale,-1))
        self.play(ApplyMethod(t1.shift,2.6*UP),ApplyMethod(question.shift,2.6*UP))
        self.wait(1)
        
        formula1=TextMobject("$(1+2+3+...n)^{ 2 }$")
        formula1.shift(1.6*LEFT+0.8*UP)
        equal=TextMobject("$=$")
        equal.scale(2.7)
        equal.set_color(GREEN)
        equal.shift(0.2*DOWN+0.3*LEFT)
        formula2=TextMobject("$(1)^{ 3 }+(2)^{ 3 }+(3)^{ 3 }+...(n)^{ 3 }$")
        formula2.shift(RIGHT+1.2*DOWN)

        self.play(Write(formula1))
        self.play(Write(equal))
        self.play(Write(formula2))
        self.wait(3)

# class formulaProof(Scene):
#     def construct(self):
#         t1=TextMobject("Formulated","proof")
#         t1.set_color_by_tex_to_color_map({"Formulated":BLUE,"proof":YELLOW})
#         t1.shift(0.7*LEFT+0.3*UP)
#         t1.scale(1.7)
#         self.play(Write(t1))
#         self.wait(1)
#         self.play(ApplyMethod(t1.shift,2.5*UP))
#         self.wait(2)

#         f1=TextMobject("$(\\sum { n } )^{ 2 }$")
#         equal1=TextMobject("$=$")
#         equal2=TextMobject("$=$")
#         equal3=TextMobject("$=$")
#         equal1.set_color(GREEN)
#         equal2.set_color(GREEN)
#         equal3.set_color(GREEN)
#         f2=TextMobject("$((n(n+1))/2)^{ 2 }$")
#         f3=TextMobject("$(n^{ 2 }(n+1)^{ 2 })/4$")
#         f4=TextMobject("$\\sum { n^{ 3 } }$")
#         f1.shift(UP+LEFT)
#         equal1.shift(0.1*UP+LEFT)
#         equal1.scale(2)
#         f2.shift(2.6*LEFT+0.8*DOWN)
#         equal2.next_to(f2,RIGHT,buff=0.6)
#         f3.next_to(equal2,RIGHT,buff=0.6)
#         equal3.shift(1.7*DOWN+LEFT)
#         equal3.scale(2)
#         f4.shift(2.6*DOWN+LEFT)
#         self.play(FadeIn(f1))
#         self.play(Write(equal1))
#         self.play(Write(f2))
#         self.play(Write(equal2))
#         self.play(Write(f3))
#         self.play(Write(equal3))
#         self.play(FadeIn(f4))
#         self.wait(2)

class connection1(Scene):
    def construct(self):
        t1=TextMobject("Let's understand it","pictorially","..")
        factorial=TextMobject("!")
        t1.set_color_by_tex_to_color_map({"pictorially":YELLOW})
        t1.scale(1.5)
        factorial.scale(2.3)
        factorial.next_to(t1,RIGHT,buff=0.6)
        factorial.set_color(GREEN)

        self.play(Write(t1))
        self.play(Write(factorial))
        self.wait(2)

class pictorialProof(Scene):
    def construct(self):
        t1=TextMobject("Pictorial","representation")
        t1.set_color_by_tex_to_color_map({"Pictorial":BLUE,"representation":YELLOW})
        t1.shift(0.6*LEFT+0.3*UP)
        t1.scale(1.7)

        self.play(Write(t1))
        self.wait(2)
        # self.play(FadeOut(t1))
        # self.wait(1)
        self.play(ApplyMethod(t1.move_to,0.6*LEFT+2.5*UP))
        self.wait(1)
        t2=TextMobject("Let's consider an example..")
        t2.scale(1.3)
        t2.shift(0.7*LEFT+0.3*UP)
        t=TextMobject("Let n=3")
        t.scale(1.6)
        t.shift(0.7*LEFT+0.3*UP)

        self.play(Write(t2))
        self.wait(1.5)
        
        self.play(Transform(t2,t))
        self.wait(2)

        self.play(FadeOut(t2),FadeOut(t1))
        self.wait(1)

        t3=TextMobject("Consider n=3")
        t3.to_edge(UP+RIGHT)
        t3.set_color(RED)
        self.add(t3)

        sq=[[Square() for i in range(7)] for j in range(7)]
        for i in range(7):
            for j in range(7):
                sq[i][j].scale(0.25)
                if(i==0 and j==0):
                    sq[i][j].shift(2*LEFT+3.3*UP)
                #self.play(Write(sq[i][j]))
                #sq[i][j].shift(j*RIGHT)
                #sq[i][j].shift(i*DOWN)
        sq[5][0].set_fill(RED, opacity=0.5)
        for j in range(2):
            for i in range(3-j):
                sq[3+j][i].set_fill(BLUE,opacity=0.5)
                sq[i+3+j][2-j].set_fill(BLUE,opacity=0.5)

        for i in range(6):
            if(i<3):
                for j in range(6):
                    sq[i][j].set_fill(GREEN,opacity=0.5)
            else:
                for j in range(3):
                    sq[i][j+3].set_fill(GREEN,opacity=0.5)

        for j in range(6):
            for i in range(6):
                sq[j][i+1].next_to(sq[j][i],RIGHT,buff=0.01)
            sq[j+1][0].next_to(sq[j][0],DOWN,buff=0.01)

        self.play(Write(sq[0][0]),Write(sq[0][1]),Write(sq[0][2]),Write(sq[0][3]),Write(sq[0][4]),Write(sq[0][5]),
                    Write(sq[1][0]),Write(sq[1][1]),Write(sq[1][2]),Write(sq[1][3]),Write(sq[1][4]),Write(sq[1][5]),
                    Write(sq[2][0]),Write(sq[2][1]),Write(sq[2][2]),Write(sq[2][3]),Write(sq[2][4]),Write(sq[2][5]),
                    Write(sq[3][0]),Write(sq[3][1]),Write(sq[3][2]),Write(sq[3][3]),Write(sq[3][4]),Write(sq[3][5]),
                    Write(sq[4][0]),Write(sq[4][1]),Write(sq[4][2]),Write(sq[4][3]),Write(sq[4][4]),Write(sq[4][5]),
                    Write(sq[5][0]),Write(sq[5][1]),Write(sq[5][2]),Write(sq[5][3]),Write(sq[5][4]),Write(sq[5][5]))
        
        t4=TextMobject("(Here each box is a square of length one unit)")
        t4.shift(2*DOWN+0.6*LEFT)
        t4.set_color(RED)
        self.play(Write(t4))
        self.wait(1.5)
        self.play(FadeOut(t4))        
        self.wait(1.5)

        t5a=TextMobject("Area : ")
        t5b=TextMobject("$(6)^{ 2 }$")
        t5c=TextMobject("$(1+2+3)^{  2 }$")
        t5a.shift(2*UP+2.5*RIGHT)
        t5b.next_to(t5a,RIGHT,buff=0.5)
        t5c.next_to(t5a,RIGHT,buff=0.5)

        self.play(Write(t5a))
        self.play(Write(t5b))
        self.wait(1.5)
        self.play(Transform(t5b,t5c))
        self.wait(2)

        t5=VGroup(t5a,t5c)

        plus1=TextMobject("+")
        plus2=TextMobject("+")
        plus1.scale(2)
        plus2.scale(2)
        plus1.shift(2.1*DOWN+3.7*LEFT)
        plus2.shift(2.1*DOWN+1.8*RIGHT)

        self.play(ApplyMethod(sq[5][0].move_to,1.8*DOWN+6*LEFT))
        
        two=VGroup(sq[3][0],sq[3][1],sq[3][2],sq[4][0],sq[4][1],sq[4][2],sq[5][1],sq[5][2])        
        self.play(ApplyMethod(two.move_to,1.8*DOWN+LEFT))

        three=VGroup(sq[0][0],sq[0][1],sq[0][2],sq[0][3],sq[0][4],sq[0][5],
                    sq[1][0],sq[1][1],sq[1][2],sq[1][3],sq[1][4],sq[1][5],
                    sq[2][0],sq[2][1],sq[2][2],sq[2][3],sq[2][4],sq[2][5],
                    sq[3][3],sq[3][4],sq[3][5],sq[4][3],sq[4][4],sq[4][5],
                    sq[5][3],sq[5][4],sq[5][5])
        self.play(ApplyMethod(three.move_to,1.8*DOWN+5*RIGHT))
        self.wait(0.3)

        self.play(Write(plus1),Write(plus2))
        self.wait(1.8)

        self.play(FadeOut(t5a))
        self.play(ApplyMethod(t5b.shift,6*LEFT+0.8*UP))
        self.wait(1.5)

        vad=VGroup(sq[5][1],sq[5][2])
        vas=VGroup(sq[3][0],sq[4][0])
        vad.rotate(PI/2)

        self.play(ApplyMethod(vas.shift,0.1*LEFT))
        self.play(ApplyMethod(vad.shift,3*UP/4+5*LEFT/4+0.1*LEFT+0.02*UP))
        self.wait(1)

        #self.play(ApplyMethod(sq[3][1].shift,0.1*RIGHT),ApplyMethod(sq[3][2].shift,0.1*RIGHT),ApplyMethod(sq[4][1].shift,0.1*RIGHT),ApplyMethod(sq[4][2].shift,0.1*RIGHT))
        #self.play(ApplyMethod(sq[5][1].shift,LEFT+UP),ApplyMethod(sq[5][2].shift,sq[4][0]))
        vbl=VGroup(sq[0][0],sq[0][1],sq[0][2],sq[1][0],sq[1][1],sq[1][2],sq[2][0],sq[2][1],sq[2][2])
        vbm=VGroup(sq[0][3],sq[0][4],sq[0][5],sq[1][3],sq[1][4],sq[1][5],sq[2][3],sq[2][4],sq[2][5])
        vbd=VGroup(sq[3][3],sq[3][4],sq[3][5],sq[4][3],sq[4][4],sq[4][5],sq[5][3],sq[5][4],sq[5][5])

        self.play(ApplyMethod(vbl.shift,0.1*LEFT))
        self.play(ApplyMethod(vbd.shift,0.1*DOWN))
        self.wait(2)

        text1=TextMobject("1 1X1 square")
        text2=TextMobject("2 2X2 squares")
        text3=TextMobject("3 3X3 squares")
        text1.shift(2.5*DOWN+6*LEFT)
        text2.shift(2.5*DOWN+LEFT)
        text3.shift(2.5*DOWN+4*RIGHT)
        text1.scale(0.4)
        text2.scale(0.4)
        text3.scale(0.4)

        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait(2.5)

        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3))
        self.wait(1)

        cube1=TextMobject("$1^{  3 }$")
        cube2=TextMobject("$2^{  3 }$")
        cube3=TextMobject("$3^{  3 }$")
        cube1.shift(2*DOWN+6*LEFT)
        cube2.shift(2*DOWN+LEFT)
        cube3.shift(2*DOWN+5*RIGHT)
        cube1.set_color(RED)
        cube2.set_color(BLUE)
        cube3.set_color(GREEN)
        self.play(Transform(sq[5][0],cube1))
        self.play(Transform(two,cube2))
        self.play(Transform(three,cube3))
        self.wait(2)

        equalto=TextMobject("=")
        equalto.scale(2.4)
        equalto.shift(0.3*UP+LEFT)
        equalto.set_color(GREEN)
        self.play(Write(equalto))
        self.wait(3)
        
class final(Scene):
    def construct(self):
        t=TextMobject("Similarly","it","is","true","$\\forall n \\in N $")
        t.scale(1.7)
        t.set_color_by_tex_to_color_map({"it":BLUE,"true":YELLOW})
        self.play(Write(t))
        self.wait(3)
