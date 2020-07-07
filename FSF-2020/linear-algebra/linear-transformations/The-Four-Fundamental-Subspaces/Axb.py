from manimlib.imports import *

class Axb(Scene):
    
    def construct(self):
        
        text0 = TextMobject("Linear System Of Equations")
        text1 = TextMobject(r"$x_{1}+x_{2}+x_{3} =b_{1}$")
        text2 = TextMobject(r"$x_{1}+2x_{2}+x_{3} =b_{2}$")
        text3 = TextMobject(r"$x_{1}+x_{2}+3x_{3} =b_{3}$")
        text0.move_to(UP*2+LEFT*2)
        text0.set_color(DARK_BLUE)
        text1.move_to(UP)
        text2.move_to(ORIGIN)
        text3.move_to(DOWN)

        text0.scale(0.75)
        text1.scale(0.75)
        text2.scale(0.75)
        text3.scale(0.75)
        self.play(Write(text0))
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(ApplyMethod(text0.move_to,3*UP+LEFT*2), ApplyMethod(text1.move_to,2.5*UP), ApplyMethod(text2.move_to,2*UP), ApplyMethod(text3.move_to,1.5*UP))

        A = TextMobject(r"$\left( \begin{array}{c c c} 1 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 3 \end{array}\right) \left[ \begin{array} {c} x_{1} \\ x_{2} \\ x_{3} \end{array}\right] =$", r"$\left[ \begin{array}{c} x_{1}+x_{2}+x_{3} \\ x_{1}+2x_{2}+x_{3} \\ x_{1}+x_{2}+3x_{3} \end{array}\right]$")
        A.scale(0.75)
        self.play(FadeIn(A))

        textA = TextMobject("A")
        textx = TextMobject("x")
        textb = TextMobject("Ax")

        textA.move_to(DOWN+3*LEFT)
        textx.move_to(1.1*DOWN+0.5*LEFT)
        textb.move_to(DOWN-2*LEFT)

        self.play(Write(textA), Write(textx), Write(textb))

        circle1 = Circle(radius = 0.24)
        circle2 = Circle(radius = 0.24)
        square = Square(side_length = 0.6)

        circle1.move_to(UP*0.5+LEFT*3.05)
        circle2.move_to(UP*0.4+LEFT*0.5)
        square.move_to(UP*0.4+RIGHT*1.3)

        self.play(FadeIn(circle1), FadeIn(circle2),FadeIn(square))

        self.play(ApplyMethod(circle1.move_to,UP*0.5+LEFT*2.45), ApplyMethod(circle2.move_to,LEFT*0.5), ApplyMethod(square.move_to,UP*0.4+RIGHT*2.2))
        self.play(ApplyMethod(circle1.move_to,UP*0.5+LEFT*1.85), ApplyMethod(circle2.move_to,DOWN*0.5+LEFT*0.5), ApplyMethod(square.move_to,UP*0.4+RIGHT*3.1))

        self.play(ApplyMethod(circle1.move_to,LEFT*3.05), ApplyMethod(circle2.move_to,UP*0.4+LEFT*0.5), ApplyMethod(square.move_to,RIGHT*1.3))
        self.play(ApplyMethod(circle1.move_to,LEFT*2.45), ApplyMethod(circle2.move_to,LEFT*0.5), ApplyMethod(square.move_to,RIGHT*2.2))
        self.play(ApplyMethod(circle1.move_to,LEFT*1.85), ApplyMethod(circle2.move_to,DOWN*0.5+LEFT*0.5), ApplyMethod(square.move_to,RIGHT*3.1))

        self.play(ApplyMethod(circle1.move_to,0.4*DOWN+LEFT*3.05), ApplyMethod(circle2.move_to,UP*0.4+LEFT*0.5), ApplyMethod(square.move_to,0.4*DOWN+RIGHT*1.3))
        self.play(ApplyMethod(circle1.move_to,0.4*DOWN+LEFT*2.45), ApplyMethod(circle2.move_to,LEFT*0.5), ApplyMethod(square.move_to,0.4*DOWN+RIGHT*2.2))
        self.play(ApplyMethod(circle1.move_to,0.4*DOWN+LEFT*1.85), ApplyMethod(circle2.move_to,DOWN*0.5+LEFT*0.5), ApplyMethod(square.move_to,0.4*DOWN+RIGHT*3.1))

        self.play(FadeOut(circle1), FadeOut(circle2), FadeOut(square))
        self.play(FadeOut(A[0]), ApplyMethod(A[1].move_to,2*LEFT),ApplyMethod(textb.move_to,DOWN+1.7*LEFT), FadeOut(textx), FadeOut(textA))
        b = TextMobject(r"$=\left[ \begin{array}{c} b_{1} \\ b_{2} \\ b_{3} \end{array}\right]$")
        b.move_to(RIGHT)
        textB = TextMobject("b")
        textB.move_to(1.2*DOWN+1.1*RIGHT)
        self.play(FadeIn(b),FadeIn(textB))

        self.wait()

        self.play(FadeOut(text0), FadeOut(text1), FadeOut(text2), FadeOut(text3))

        axb = TextMobject("Ax = b")
        self.play(FadeIn(axb), FadeOut(textb), FadeOut(textB), FadeOut(b), FadeOut(A[1]))

        self.wait()