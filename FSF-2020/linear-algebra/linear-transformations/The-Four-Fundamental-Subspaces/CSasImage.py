from manimlib.imports import *

class Column_Space(Scene):
    def construct(self):

        A = TextMobject(r"$A = $",r"$\left( \begin{array}{c c c} 1 & 2 & 1 \\ 1 & 3 & 1 \\ 2 & 1 & 4 \\ 3 & 2 & 3 \end{array} \right)$")
        A.move_to(2*UP)
        A[1].set_color(color = DARK_BLUE)
        A.scale(0.75)

        self.play(Write(A),run_time = 1)      

        CS_A = TextMobject(r"Column Space of $A = x_{1}$",r"$\left( \begin{array}{c} 1 \\ 1 \\ 2 \\ 3 \end{array} \right)$",r"$+x_{2}$",r"$ \left( \begin{array}{c} 2 \\ 3 \\ 1 \\ 2 \end{array} \right)$",r"$ + x_{3}$",r"$\left( \begin{array}{c} 1 \\ 1 \\ 4 \\ 3 \end{array} \right)$")
        CS_A.move_to(1.5*LEFT+1*DOWN)
        CS_A[1].set_color(color = DARK_BLUE)
        CS_A[3].set_color(color = DARK_BLUE)
        CS_A[5].set_color(color = DARK_BLUE)
        CS_A.scale(0.75)

        self.play(Write(CS_A),run_time = 2)

        arrow1 = Arrow(start = 1.25*UP,end = 0.25*DOWN+1.75*LEFT)
        arrow2 = Arrow(start = 1.35*UP+0.5*RIGHT,end = 0.25*DOWN+0.5*RIGHT)
        arrow3 = Arrow(start = 1.25*UP+0.75*RIGHT,end = 0.25*DOWN+2.9*RIGHT)

        Defn = TextMobject("Linear Combination of Columns of Matrix")
        Defn.move_to(3*DOWN)

        self.play(Write(Defn), ShowCreation(arrow1), ShowCreation(arrow2), ShowCreation(arrow3),run_time = 1)
        self.wait(1)

class solution(LinearTransformationScene):
    def construct(self):

        self.setup()
        self.wait()
        
        o = TextMobject(r"Consider the vector space $R^2$")
        o.move_to(2*DOWN)
        o.scale(0.75)
        o.add_background_rectangle()
        self.play(Write(o))
        self.wait()
        self.play(FadeOut(o))

        A = TextMobject(r"Let $A$(= ",r"$\left[\begin{array}{c c} 1 & -1 \\ 1 & -1 \end{array}\right]$",r")denote the matrix the of this linear transformation.")
        A.move_to(2*DOWN)
        A.scale(0.75)
        A.add_background_rectangle()
        self.play(Write(A))
        matrix = [[1,-1],[1,-1]]
        self.apply_matrix(matrix)
        self.wait()
        self.play(FadeOut(A))

        o = TextMobject(r"This is the transformed vector space")
        o.move_to(2*DOWN)
        o.scale(0.75)
        o.add_background_rectangle()
        self.play(Write(o))
        self.wait()
        self.play(FadeOut(o))

        texti = TextMobject(r"$\left[\begin{array}{c}1\\1\end{array}\right]$")
        textj = TextMobject(r"$\left[\begin{array}{c}-1\\-1\end{array}\right]$")
        texti.set_color(GREEN)
        textj.set_color(RED)
        texti.scale(0.7)
        textj.scale(0.7)
        texti.move_to(1.35*RIGHT+0.5*UP)
        textj.move_to(-(1.5*RIGHT+0.5*UP))

        text1 = TextMobject("[")
        text2 = TextMobject(r"$\begin{array}{c} 1 \\ 1 \end{array}$")
        text3 = TextMobject(r"$\begin{array}{c} -1 \\ -1 \end{array}$")
        text4 = TextMobject("]")

        text2.set_color(GREEN)
        text3.set_color(RED)

        text1.scale(2)
        text4.scale(2)
        text2.scale(0.7)
        text3.scale(0.7)

        text1.move_to(2.5*UP+6*LEFT)
        text2.move_to(2.5*UP+5.75*LEFT)
        text3.move_to(2.5*UP+5.25*LEFT)
        text4.move_to(2.5*UP+5*LEFT)

        self.play(Write(texti), Write(textj))
        self.wait()
        self.play(FadeIn(text1), Transform(texti,text2), Transform(textj,text3), FadeIn(text4))
        self.wait()

        o = TextMobject(r"Now, you can observe the Image of Linear Transformation")
        o1 = TextMobject(r"and Column Space(i.e. span of columns of matrix $A$) are same")
        o.move_to(2.5*DOWN)
        o1.move_to(3*DOWN)
        o.scale(0.75)
        o1.scale(0.75)
        o.add_background_rectangle()
        o1.add_background_rectangle()
        self.play(Write(o))
        self.play(Write(o1))
        self.wait()
        self.play(FadeOut(o),FadeOut(o1))

class solution2nd(LinearTransformationScene):
    def construct(self):

        self.setup()
        self.wait()
        
        arrow1 = Arrow(start = ORIGIN,end = 2*DOWN+RIGHT)
        arrow2 = Arrow(start = ORIGIN,end = UP+LEFT)
        arrow3 = Arrow(start = ORIGIN,end = 3*UP+4*RIGHT)
        arrow1.set_color(YELLOW)
        arrow2.set_color(YELLOW)
        arrow3.set_color(YELLOW)
        arrow1.scale(1.3)
        arrow2.scale(1.5)
        arrow3.scale(1.1)

        self.play(ShowCreation(arrow1), ShowCreation(arrow2), ShowCreation(arrow3))

        self.add_transformable_mobject(arrow1)
        self.add_transformable_mobject(arrow2)
        self.add_transformable_mobject(arrow3)
        o = TextMobject(r"Consider any vector in the original vector space $R^2$")
        o.move_to(2.5*DOWN)
        o.scale(0.75)
        o.add_background_rectangle()
        self.play(Write(o))
        self.wait()
        self.play(FadeOut(o))

        A = TextMobject(r"Matrix the of this linear transformation is $A$(= ",r"$\left[\begin{array}{c c} 1 & -1 \\ 1 & -1 \end{array}\right]$",r") again.")
        A.move_to(2*DOWN)
        A.scale(0.75)
        A.add_background_rectangle()
        self.play(Write(A))
        matrix = [[1,-1],[1,-1]]
        self.apply_matrix(matrix)
        self.wait()
        self.play(FadeOut(A))

        o = TextMobject(r"This is the transformed vector space")
        o.move_to(2*DOWN)
        o.scale(0.75)
        o.add_background_rectangle()
        self.play(Write(o))
        self.wait()
        self.play(FadeOut(o))

        o = TextMobject(r"Each and every vector of original vector space $R^2$ will transform")
        o1 = TextMobject(r"to this new vector space which is spanned by $\mathbf{CS}(A)$")
        o.move_to(2.5*DOWN)
        o1.move_to(3*DOWN)
        o.scale(0.75)
        o1.scale(0.75)
        o.add_background_rectangle()
        o1.add_background_rectangle()
        self.play(Write(o))
        self.play(Write(o1))
        self.wait()
        self.play(FadeOut(o))
        self.play(FadeOut(o1))