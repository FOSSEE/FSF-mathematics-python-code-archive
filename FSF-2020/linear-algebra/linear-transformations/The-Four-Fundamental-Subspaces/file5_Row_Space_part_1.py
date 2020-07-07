from manimlib.imports import *
class LS(Scene):
    def construct(self):
        text1 = TextMobject(r"Consider a matrix $A =$")
        text2 = TextMobject(r"[")
        text3 = TextMobject(r"$\begin{array}{c c} 1 & -2\end{array}$")
        text4 = TextMobject(r"$\begin{array}{c c} 1 & -1\end{array}$")
        text5 = TextMobject(r"]")

        text2.scale(2)
        text5.scale(2)

        text1.set_color(DARK_BLUE)
        text2.set_color(DARK_BLUE)
        text3.set_color(PURPLE)
        text4.set_color(YELLOW)
        text5.set_color(DARK_BLUE)

        text1.move_to(3.5*LEFT+3*UP+2*RIGHT)
        text2.move_to(0.75*LEFT+3*UP+2*RIGHT)
        text3.move_to(3.25*UP+2*RIGHT)
        text4.move_to(2.75*UP+2*RIGHT)
        text5.move_to(0.75*RIGHT+3*UP+2*RIGHT)

        self.play(FadeIn(text1), FadeIn(text2), FadeIn(text3), FadeIn(text4), FadeIn(text5))
        self.wait()

        ttext1 = TextMobject(r"$A^T =$")
        ttext2 = TextMobject(r"[")
        ttext3 = TextMobject(r"$\begin{array}{c} 1 \\ -2\end{array}$")
        ttext4 = TextMobject(r"$\begin{array}{c} 1 \\ -1\end{array}$")
        ttext5 = TextMobject(r"]")

        ttext2.scale(2)
        ttext5.scale(2)

        ttext1.set_color(DARK_BLUE)
        ttext2.set_color(DARK_BLUE)
        ttext3.set_color(PURPLE)
        ttext4.set_color(YELLOW)
        ttext5.set_color(DARK_BLUE)

        ttext1.move_to(2*LEFT+1.5*UP+2*RIGHT)
        ttext2.move_to(1*LEFT+1.5*UP+2*RIGHT)
        ttext3.move_to(0.5*LEFT+1.5*UP+2*RIGHT)
        ttext4.move_to(0.5*RIGHT+1.5*UP+2*RIGHT)
        ttext5.move_to(1*RIGHT+1.5*UP+2*RIGHT)

        self.play(FadeIn(ttext1), FadeIn(ttext2), FadeIn(ttext3), FadeIn(ttext4), FadeIn(ttext5))

        rtext = TextMobject(r"Row Space of $A$ = Column Space of $A^T = a_1$",r"$\left[\begin{array}{c} 1 \\ -2\end{array}\right]$",r"$+a_2$",r"$\left[\begin{array}{c} 1 \\ -1\end{array}\right]$")
        rtext[1].set_color(PURPLE)
        rtext[3].set_color(YELLOW)
        rtext.move_to(2*DOWN+1.5*LEFT)
        rtext.scale(0.75)

        self.play(Write(rtext))
        self.wait()

        arrow1 = Arrow(start = 1.5*RIGHT+UP, end = 1.25*(DOWN+RIGHT))
        arrow2 = Arrow(start = 2.5*RIGHT+UP, end = 1.25*DOWN+3.25*RIGHT)
        arrow1.scale(1.25)
        arrow2.scale(1.25)
        arrow1.set_color(PURPLE)
        arrow2.set_color(YELLOW)

        self.play(ShowCreation(arrow1), ShowCreation(arrow2))
        self.wait(2)
