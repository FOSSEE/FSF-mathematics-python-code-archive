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