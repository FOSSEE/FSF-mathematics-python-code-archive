from manimlib.imports import *
import numpy as np

def intro_text():
    return TextMobject("Cauchy")

class intro(Scene):
    def construct(self):
        text=intro_text()
        text1=TextMobject("Sequence")
        text1.scale(1)
        text.set_color_by_tex_to_color_map({"Cauchy": BLUE})
        text.scale(4)
        text.move_to(1*UP+1*LEFT)
        
        self.play(Write(text))
        self.play(FadeIn(text1))
        self.wait(1)

        self.play(ApplyMethod(text.shift,1.5*UP),ApplyMethod(text1.shift,2.3*UP+3.2*RIGHT))
        self.wait(1)

        text2=TextMobject("what does","it","mean")
        question=TextMobject("?")
        text2.set_color_by_tex_to_color_map({"it":GREEN})
        text2.shift(0.5*LEFT)
        text2.scale(1.5)
        question.scale(4)
        question.next_to(text2,RIGHT,buff=0.6)

        self.play(Write(text2))
        self.play(ShowCreation(question))
        self.wait(0.5)
        
        self.play(ApplyMethod(question.scale,-1))
        self.wait(1)
        
        text3=TextMobject("Here goes the formal definition..")
        self.play(FadeOut(question))
        self.play(ReplacementTransform(text2,text3))
        self.wait(3)

class definition(Scene):
    def construct(self):
        definition_text_1=TextMobject("A sequence, $(x_n)$ is said to be a" ,"Cauchy", "Sequence if ","for all", "$\\epsilon > 0$")
        definition_text_2=TextMobject("$\\exists$ \\ K($\\epsilon$) such that ","for all m,n $\geq$ $ K(\\epsilon)$,","$|x_m-x_n|<\\epsilon$")
        definition_text_1.shift(UP)
        definition_text_1.set_color_by_tex_to_color_map({"Cauchy": YELLOW,"$\\epsilon > 0$": BLUE,"for all":RED})
        definition_text_2.set_color_by_tex_to_color_map({"$|x_m-x_n|<\\epsilon$": YELLOW," \\ K($\\epsilon$) ":BLUE,"for all m,n $\geq$ $ K(\\epsilon)$,":BLUE})

        self.play(Write(definition_text_1))
        self.play(Write(definition_text_2))
	#self.play(Applymethod())
        self.wait(5.5)

class to_graph(Scene):
    def construct(self):
        t1=TextMobject("Let us understand it", "graphically")
        t1.scale(1.8)
        t2=TextMobject("Consider the following graph of sequence")
        t3=TextMobject("$X_n = (20 \\frac{(-1)^n}{n}) + 4$")
        t3.set_color_by_tex_to_color_map({"$X_n = (20 \\frac{(-1)^n}{n}) + 4$":GREEN})
        t1.set_color_by_tex_to_color_map({"graphically": YELLOW})

        self.play(Write(t1))
        self.wait(2)
        self.play(ApplyMethod(t1.shift,2.3*UP))
        self.play(Write(t2))
        self.wait(1)
        self.play(ReplacementTransform(t2,t3))
        self.wait(3)

class graph(GraphScene):
    CONFIG = {
        "x_min": -2.5,
        "x_max": 35,
        "y_min": -10,
        "y_max": 10,
        "graph_origin": ORIGIN+4*LEFT,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$n$",
        "y_axis_label": "$x_n$",
        "exclude_zero_label": True,
        "x_labeled_nums": range(0, 36, 5),
        "y_labeled_nums": range(-10,11,2)
    }
    def construct(self):
        t3=TextMobject("$X_n = (20 \\frac{(-1)^n}{n}) + 4$")
        t3.scale(0.7)
        t3.to_edge(UP+RIGHT)
        t3.set_color(RED)
        self.add(t3)
        self.setup_axes(animate=True)
        self.wait(1)

        mathfunc = lambda x: 20*((-1)**x)/x + 4

        points = [ Dot(color = RED, radius = 0.03) for dot in range(1,34) ]
       
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)
        [points[counter].shift(self.graph_origin + counter * (RIGHT * x_each_unit) + mathfunc(counter) * (UP * y_each_unit)) for counter in range(1, len(points))] 
        for i in range(1,len(points)):
            self.add(points[i])
            self.wait(0.15)
        self.wait(2)
         
        limit=4
        epsilon=2

        limit_line=DashedLine(start=self.graph_origin,end=4.2*RIGHT,color=BLUE)
        limit_line.shift(y_each_unit*limit*UP)
        
        self.play(Write(limit_line))
        self.wait(2)
        
        intro_arrow=TextMobject("Since" ,"$\\epsilon$"," value is","arbitary")
        intro_arrow.shift(2.8*UP)
        intro_arrow.set_color_by_tex_to_color_map({"arbitary":YELLOW,"$\\epsilon$":YELLOW})
        intro_arrow.scale(0.8)
        self.play(Write(intro_arrow))
        self.wait(2)
        arrow_text=TextMobject("Let epsilon $=$ 3")
        arrow_text.scale(0.8)
        arrow_text.shift(2.8*UP)
        self.play(ReplacementTransform(intro_arrow,arrow_text))
        self.wait(1)
        
        epsilon_line=Line(start=(4-(20/7))*y_each_unit*UP,end=4*UP*y_each_unit)
        epsilon_line.shift(self.graph_origin+x_each_unit*RIGHT*7)
        self.play(Write(epsilon_line))
        self.wait(2)
        
        text=TextMobject("$\\epsilon=3$")
        text.shift(self.graph_origin+RIGHT*5*x_each_unit+UP*3*y_each_unit)
        text.scale(0.7)
        self.play(Write(text),FadeOut(arrow_text))

        arrow_text1=TextMobject("Now according to definition,","$\\exists K(\\epsilon)$")
        arrow_text1.shift(2.8*UP+0.2*RIGHT)
        arrow_text1.set_color_by_tex_to_color_map({"$\\exists K(\\epsilon)$":BLUE})
        arrow_text1.scale(0.8)

        self.play(Write(arrow_text1))
        self.wait(1)
        point=Dot(color=BLUE,radius=0.06)
        point.shift(self.graph_origin+RIGHT*7*x_each_unit)
        self.add(point)
        point_text=TextMobject("K($\\epsilon$)")
        point_text.scale(0.7)
        point_text.shift(self.graph_origin+RIGHT*7.2*x_each_unit+y_each_unit*1.4*DOWN)
        self.play(FadeIn(point_text))
        self.wait(1.5)

        arrow_text2=TextMobject("such that" ,"$\\forall$ natural numbers")
        arrow_text2.set_color_by_tex_to_color_map({"$\\forall$ natural numbers":YELLOW})
        arrow_text2a=TextMobject("m,n $\geq$ K($\\epsilon$)")
        arrow_text2a.set_color(BLUE)
        arrow_text2.scale(0.8)
        arrow_text2a.scale(0.8)
        arrow_text2.shift(2.8*UP+0.3*RIGHT)
        arrow_text2a.shift(2.2*UP+0.3*RIGHT)
        arrow_group=VGroup(arrow_text2,arrow_text2a)
        self.play(ReplacementTransform(arrow_text1,arrow_group))
        self.wait(2)
        
        m_and_n_points=[Dot(color=WHITE, radius=0.05) for point in range(1,29)]
        [m_and_n_points[i].shift(self.graph_origin+RIGHT*8*x_each_unit+RIGHT*i*x_each_unit) for i in range(0,28)]
        for j in range(0,28):
            self.add(m_and_n_points[j])
            self.wait(0.1)

        #here show all m,n by zoming out
        self.wait(2)
        
        text1=TextMobject("(Consider any two points)")
        text1.shift(2*DOWN+RIGHT)
        self.play(Write(text1))
        self.wait(1)
        self.play(FadeOut(text1))
        for k in range(28):
            self.remove(m_and_n_points[k])

        self.wait(1)

        pointm1=Dot(color=BLUE,radius=0.05)
        pointm1.shift(self.graph_origin + 9*RIGHT*x_each_unit)
        pointn1=Dot(color=BLUE,radius=0.05)
        pointn1.shift(self.graph_origin + 11*RIGHT*x_each_unit)
        self.play(Write(pointm1),Write(pointn1))
        
        m=TextMobject("m")
        m.shift(self.graph_origin+9*x_each_unit*RIGHT+y_each_unit*DOWN*0.7)
        m.set_color(RED)
        m.scale(0.4)
        self.play(Write(m))

        n=TextMobject("n")
        n.shift(self.graph_origin+11*x_each_unit*RIGHT+y_each_unit*DOWN*0.7)
        n.set_color(RED)
        n.scale(0.4)
        self.play(Write(n))

        self.wait(1)

        self.play(ApplyMethod(pointm1.move_to,self.graph_origin + 9*RIGHT*x_each_unit + (4-(20/9))*UP*y_each_unit),ApplyMethod(pointn1.move_to,self.graph_origin + 11*RIGHT*x_each_unit + (4-(20/11))*UP*y_each_unit))
        self.wait(1)

        arrow_text3=TextMobject("$|X_m-X_n| < \\epsilon$")
        arrow_text3.set_color_by_tex_to_color_map({"$|X_m-X_n| < \\epsilon$":YELLOW})
        arrow_text3.shift(2.8*UP+0.3*RIGHT)
        self.play(ReplacementTransform(arrow_group,arrow_text3))
        self.wait(2)

        upline=Line(start=(4-20/9)*UP*y_each_unit,end=(4-20/11)*UP*y_each_unit)
        upline.shift(self.graph_origin+9*RIGHT*x_each_unit)
        leftline=Line(start=11*RIGHT*x_each_unit,end=9*RIGHT*x_each_unit)
        leftline.shift(self.graph_origin+(4-20/11)*UP*y_each_unit)
        self.play(Write(leftline))
        self.wait(0.4)
        self.play(Write(upline))
        
        self.wait(2)
        self.play(ApplyMethod(epsilon_line.move_to,self.graph_origin+6*DOWN*y_each_unit+7*RIGHT*x_each_unit),ApplyMethod(upline.move_to,self.graph_origin+6*DOWN*y_each_unit+12*RIGHT*x_each_unit))
        
        self.play(FadeOut(text),FadeOut(leftline),FadeOut(pointm1),FadeOut(pointn1),FadeOut(m),FadeOut(n))
        self.wait(1)
        x1=TextMobject("$\\epsilon$")
        x2=TextMobject("$|X_m-X_n|$")
        x1.shift(self.graph_origin+7*RIGHT*x_each_unit+9*DOWN*y_each_unit)
        x1.scale(0.8)
        x2.shift(self.graph_origin+14*RIGHT*x_each_unit+9*DOWN*y_each_unit)
        x2.scale(0.5)

        self.play(FadeIn(x1),FadeIn(x2))
        self.wait(1)
        greater=TextMobject("$>$")
        greater.shift(self.graph_origin+10*RIGHT*x_each_unit+6*DOWN*y_each_unit)
        self.add(greater)
        self.wait(1)
        greater1=TextMobject("$>$")
        greater1.scale(0.5)
        greater1.shift(self.graph_origin+10*RIGHT*x_each_unit+9*DOWN*y_each_unit)
        self.add(greater1)
        self.wait(2.8)
        self.play(FadeOut(x1),FadeOut(x2),FadeOut(greater1))
        self.play(FadeOut(greater),FadeOut(upline))
        self.wait(0.4)
        
        self.play(ApplyMethod(epsilon_line.move_to,self.graph_origin+(2.5)*UP*y_each_unit+7*RIGHT*x_each_unit))
        
        self.wait(1.9)

        
        
class conclusion(Scene):
    def construct(self):
        endformula=TextMobject("$|X_m-X_n|<\\epsilon$")
        endformula.set_color_by_tex_to_color_map({"$|X_m-X_n|<\\epsilon$":YELLOW})
        endformula.shift(2.8*UP+0.3*RIGHT)
        self.add(endformula)
        self.wait(1)
        
        self.play(ApplyMethod(endformula.move_to,1.5*UP))
        self.wait(1.3)
        endtext=TextMobject("Similarlly","the condition is true","$\\forall$ natural numbers","m,n$\geq$$K(\\epsilon)$")
        endtext.set_color_by_tex_to_color_map({"it is true":YELLOW,"$\\forall$ natural numbers":BLUE})
        self.play(Write(endtext))
        self.wait(2.7)
        

class conclusion_final(Scene):
    def construct(self):
        final1=TextMobject("Since the","equation","satisfies the","condition")
        final1.set_color_by_tex_to_color_map({"equation":YELLOW,"condition":BLUE})
        final1.shift(UP)
        final2=TextMobject("$|X_m-X_n|<\\epsilon$")
        final2.set_color(RED)
        final2.scale(1.5)
        final3=TextMobject("$\\forall \\epsilon>0$"," and ","$\\forall$ m,n$\geq$$K(\\epsilon)$")
        final3.set_color_by_tex_to_color_map({"$\\forall \\epsilon>0$":BLUE,"$\\forall$ m,n$\geq$$K(\\epsilon)$":BLUE})
        final3.shift(DOWN)

        self.play(Write(final1))
        self.wait(1)
        self.play(FadeIn(final2))
        self.wait(0.6)
        self.play(Write(final3))
        
        self.wait(3.5)

        group1=VGroup(final1,final2,final3)

        t1=TextMobject("That is,","for any","small positive distance","$\\epsilon$")
        self.wait(0.5)
        t1.set_color_by_tex_to_color_map({"for any":YELLOW,"small positive distance":BLUE})
        self.play(ReplacementTransform(group1,t1))
        self.play(ApplyMethod(t1.move_to,1.5*UP))
        t2=TextMobject("a","finite number","of elements of the sequence are","less than")
        t2.set_color_by_tex_to_color_map({"finite number":RED,"less than":YELLOW})
        t2.shift(0.5*UP)
        t3=TextMobject("that","given distance","from each other and the elements","become")
        t3.set_color_by_tex_to_color_map({"given distance":YELLOW,"become":BLUE})
        t3.shift(0.5*DOWN)
        t4=TextMobject("arbitarily close","to each other","as the sequence progresses.")
        t4.set_color_by_tex_to_color_map({"arbitarily close":BLUE,"as the sequence progresses.":RED})
        t4.shift(1.5*DOWN)
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Write(t4))
        self.wait(3)
        
        group3=VGroup(t2,t3,t4)

        group4=VGroup(t1,t2,t3,t4)

        text1=TextMobject("Hence it is called")
        text1.shift(UP)
        text2=TextMobject("Cauchy","Sequence")
        text2.scale(1.7)
        text2.set_color_by_tex_to_color_map({"Cauchy":GREEN,"Sequence":RED})
        group2=VGroup(text1,text2)
        self.play(ReplacementTransform(group4,group2))
        self.wait(4.5)
    

