from manimlib.imports import *
import numpy as np


class convergence(Scene):
    def construct(self):
        originalFormula=TextMobject("$\sum _{ n=0 }^{ \infty  }{ { a }_{ n }{ x }^{ n } }$")
        originalFormula.set_color(RED)
        self.play(Write(originalFormula))
        self.wait(1)
        self.play(ApplyMethod(originalFormula.shift,2.7*UP))
        self.wait(1)

        colors=[PURPLE_E,PURPLE_D,MAROON_D,RED_E,RED_D,RED_C,ORANGE,YELLOW_E,YELLOW_D,YELLOW_B]
        terms=["$a_{ 0 }$","$a_{ 1 }x$","$a_{ 2 }x^{ 2 }$","$a_{ 3 }x^{ 3 }$","$a_{ 4 }x^{ 4 }$","$a_{ 5 }x^{ 5 }$","$a_{ 6 }x^{ 6 }$","$a_{ 7 }x^{ 7 }$","$a_{ 8 }x^{ 8 }$","$a_{ 9 }x^{ 9 }$"]
        termsTogetherString="+".join(terms)
        #termsTogether=TextMobject(termsTogetherString+"...")
        termsTogether=TextMobject("$a_{ 0 }$","+","$a_{ 1 }x$","+","$a_{ 2 }x^{ 2 }$","+","$a_{ 3 }x^{ 3 }$","+","$a_{ 4 }x^{ 4 }$","+","$a_{ 5 }x^{ 5 }$","+","$a_{ 6 }x^{ 6 }$","+","$a_{ 7 }x^{ 7 }$","+","$a_{ 8 }x^{ 8 }$","+","$a_{ 9 }x^{ 9 }$","+..")
        termsTogether.set_color_by_tex_to_color_map({"$a_{ 0 }$":colors[0],
                                                    "$a_{ 1 }x$":colors[1],
                                                    "$a_{ 2 }x^{ 2 }$":colors[2],
                                                    "$a_{ 3 }x^{ 3 }$":colors[3],
                                                    "$a_{ 4 }x^{ 4 }$":colors[4],
                                                    "$a_{ 5 }x^{ 5 }$":colors[5],
                                                    "$a_{ 6 }x^{ 6 }$":colors[6],
                                                    "$a_{ 7 }x^{ 7 }$":colors[7],
                                                    "$a_{ 8 }x^{ 8 }$":colors[8],
                                                    "$a_{ 9 }x^{ 9 }$":colors[9]})
        termsTogether.scale(0.8)
        termsTogether.shift(2.7*UP)
        self.play(ReplacementTransform(originalFormula,termsTogether))
        self.wait(1)

        termMobjectRect=[0]*10
        termMobject=TextMobject(terms[0]).set_color(colors[0])
        termMobject.shift(2.7*UP+6.2*LEFT)
        for i in range(1,11):
            termMobjectOld=termMobject
            termMobjectOld.scale(0.8)
            if(i<10):
                termMobject=TextMobject(terms[i])
                termMobject.set_color(colors[i])
                termMobject.next_to(termMobjectOld,buff=0.5)
            if(i==1):
                rectDefine=TextMobject("Here","each rectangle","represents the","value of the term")
                rectDefine.set_color_by_tex_to_color_map({"each rectangle":BLUE,"value of the term":YELLOW})
                rectDefine.scale(0.7)
                rectDefine.shift(3.2*DOWN)
                self.play(Write(rectDefine))
                self.wait(1)
            if(i==2):
                ratio=TextMobject("If $\\frac { a_{ n+1 } }{ { a }_{ n } } < 1$")
                ratio.set_color(RED)
                ratio.scale(0.7)
                ratio.move_to(3.2*DOWN)
                inequality=TextMobject("$a_{ n+1 } < a_{ n }$")
                inequality.set_color(RED)
                inequality.scale(0.7)
                inequality.move_to(3.2*DOWN)
                self.play(FadeOut(rectDefine))
                self.play(Write(ratio))
                self.wait(1)
                self.play(ReplacementTransform(ratio,inequality))
                self.wait(1)
            #self.play(ApplyMethod(termMobjectOld.move_to,(2-0.3*i)*DOWN+RIGHT*0.2*i))
            termMobjectRect[i-1]=Rectangle(height=0.1,width=(4.2-0.4*i),color=colors[i-1])
            termMobjectRect[i-1].move_to((2-0.2*i)*DOWN+RIGHT*0.2*i)
            #rectangles[p] = termMobjectRect
            #p+=1
            self.play(ReplacementTransform(termMobjectOld,termMobjectRect[i-1]))

        uparrow=TextMobject("$\\uparrow$")
        uparrow.set_color(GREEN)
        uparrow.scale(5)
        uparrow.shift(4*RIGHT+0.7*DOWN)
        self.play(ShowCreation(uparrow))
        self.wait(1)

        converges=TextMobject("Converges!")
        converges.set_color(RED)
        converges.scale(0.6)
        converges.next_to(uparrow)
        self.play(FadeIn(converges))
        self.wait(2)

        self.play(FadeOut(converges),FadeOut(uparrow),FadeOut(inequality))
        self.wait(0.5)
        rect=VGroup(termMobjectRect[0],termMobjectRect[1],termMobjectRect[2],termMobjectRect[3],termMobjectRect[4],termMobjectRect[5],termMobjectRect[6],termMobjectRect[7],termMobjectRect[8],termMobjectRect[9])    
        self.play(ApplyMethod(rect.scale,0.2))
        for i in range(0,10):
            self.play(ApplyMethod(termMobjectRect[i].shift,i*0.04*DOWN+(11-(3-0.11*i)*i)*LEFT*0.3))
        func=TextMobject("$\\approx$","$f(x)$")
        func.set_color_by_tex_to_color_map({"$f(x)$":RED})
        func.scale(0.8)
        func.shift(DOWN+4.5*RIGHT+0.1*UP)
        self.play(FadeIn(func))

        rightarrow=TextMobject("$\\rightarrow$")
        rightarrow.set_color(GREEN)
        rightarrow.scale(4)
        rightarrow.shift(2*DOWN)
        converges=TextMobject("Hence even the","sum converges!")
        converges.set_color_by_tex_to_color_map({"sum converges!":RED})
        converges.move_to(3*DOWN)
        converges.scale(0.7)
        self.play(Write(rightarrow),FadeIn(converges))
        self.wait(2)
