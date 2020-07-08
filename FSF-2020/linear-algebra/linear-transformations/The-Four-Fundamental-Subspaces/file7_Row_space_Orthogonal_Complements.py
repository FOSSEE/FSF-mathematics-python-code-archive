from manimlib.imports import *
class row_space(LinearTransformationScene):
    def construct(self):

        self.setup()
        self.wait()
        
        o = TextMobject(r"This is the original vector space $R^2$(before Linear Transformation)")
        o.move_to(DOWN)
        o.scale(0.75)
        o.add_background_rectangle()
        self.play(Write(o))
        self.wait()
        self.play(FadeOut(o))

        o1 = TextMobject("Consider a set of vectors which are linear")
        o2 = TextMobject(r"span of a $\left(\begin{array}{c} 1 \\ 1 \end{array}\right)$i.e. the null space.")
        o1.move_to(2*DOWN+3*RIGHT)
        o2.move_to(2.75*DOWN+3*RIGHT)
        o1.scale(0.7)
        o2.scale(0.7)
        o1.add_background_rectangle()
        o2.add_background_rectangle()
        self.play(Write(o1))
        self.play(Write(o2))

        arrow = Arrow(start = ORIGIN, end = UP+RIGHT)
        arrow.set_color(YELLOW)
        arrow1 = Arrow(start = ORIGIN, end = 2*(UP+RIGHT))
        arrow1.set_color(YELLOW)
        arrow2 = Arrow(start = ORIGIN, end = 3*(UP+RIGHT))
        arrow2.set_color(YELLOW)
        arrow3 = Arrow(start = ORIGIN, end = 4*(UP+RIGHT))
        arrow3.set_color(YELLOW)
        arrow4 = Arrow(start = ORIGIN, end = DOWN+LEFT)
        arrow4.set_color(YELLOW)
        arrow5 = Arrow(start = ORIGIN, end = 2*(DOWN+LEFT))
        arrow5.set_color(YELLOW)
        arrow6 = Arrow(start = ORIGIN, end = 3*(DOWN+LEFT))
        arrow6.set_color(YELLOW)
        arrow7 = Arrow(start = ORIGIN, end = 4*(DOWN+LEFT))
        arrow7.set_color(YELLOW)

        arrow.scale(1.5)
        arrow1.scale(1.2)
        arrow2.scale(1.15)
        arrow3.scale(1.1)
        arrow4.scale(1.5)
        arrow5.scale(1.2)
        arrow6.scale(1.15)
        arrow7.scale(1.1)

        self.play(ShowCreation(arrow),
        ShowCreation(arrow1),
        ShowCreation(arrow2),
        ShowCreation(arrow3),
        ShowCreation(arrow4),
        ShowCreation(arrow5),
        ShowCreation(arrow6),
        ShowCreation(arrow7),
        )

        self.wait(2)
        self.play(FadeOut(o1), FadeOut(o2))

        o1 = TextMobject("Consider a set of vectors which are linear")
        o2 = TextMobject(r"span of a $\left(\begin{array}{c} 1 \\ -1 \end{array}\right)$i.e. the row space.")
        o1.move_to(2*DOWN+3*RIGHT)
        o2.move_to(2.75*DOWN+3*RIGHT)
        o1.scale(0.7)
        o2.scale(0.7)
        o1.add_background_rectangle()
        o2.add_background_rectangle()
        self.play(Write(o1))
        self.play(Write(o2))

        rarrow = Arrow(start = ORIGIN, end = -UP+RIGHT)
        rarrow.set_color(PURPLE)
        rarrow1 = Arrow(start = ORIGIN, end = 2*(-UP+RIGHT))
        rarrow1.set_color(PURPLE)
        rarrow2 = Arrow(start = ORIGIN, end = 3*(-UP+RIGHT))
        rarrow2.set_color(PURPLE)
        rarrow3 = Arrow(start = ORIGIN, end = 4*(-UP+RIGHT))
        rarrow3.set_color(PURPLE)
        rarrow4 = Arrow(start = ORIGIN, end = -DOWN+LEFT)
        rarrow4.set_color(PURPLE)
        rarrow5 = Arrow(start = ORIGIN, end = 2*(-DOWN+LEFT))
        rarrow5.set_color(PURPLE)
        rarrow6 = Arrow(start = ORIGIN, end = 3*(-DOWN+LEFT))
        rarrow6.set_color(PURPLE)
        rarrow7 = Arrow(start = ORIGIN, end = 4*(-DOWN+LEFT))
        rarrow7.set_color(PURPLE)

        rarrow.scale(1.5)
        rarrow1.scale(1.2)
        rarrow2.scale(1.15)
        rarrow3.scale(1.1)
        rarrow4.scale(1.5)
        rarrow5.scale(1.2)
        rarrow6.scale(1.15)
        rarrow7.scale(1.1)

        self.play(ShowCreation(rarrow),
        ShowCreation(rarrow1),
        ShowCreation(rarrow2),
        ShowCreation(rarrow3),
        ShowCreation(rarrow4),
        ShowCreation(rarrow5),
        ShowCreation(rarrow6),
        ShowCreation(rarrow7),
        )

        self.wait(2)
        self.play(FadeOut(o1), FadeOut(o2))

        self.add_transformable_mobject(arrow)
        self.add_transformable_mobject(arrow1)
        self.add_transformable_mobject(arrow2)
        self.add_transformable_mobject(arrow3)
        self.add_transformable_mobject(arrow4)
        self.add_transformable_mobject(arrow5)
        self.add_transformable_mobject(arrow6)
        self.add_transformable_mobject(arrow7)

        self.add_transformable_mobject(rarrow)
        self.add_transformable_mobject(rarrow1)
        self.add_transformable_mobject(rarrow2)
        self.add_transformable_mobject(rarrow3)
        self.add_transformable_mobject(rarrow4)
        self.add_transformable_mobject(rarrow5)
        self.add_transformable_mobject(rarrow6)
        self.add_transformable_mobject(rarrow7)

        o1 = TextMobject("Notice, entire set of vectors which belong to the null space of $A$ transforms to zero")
        o2 = TextMobject(r"and entire set of vectors which belong to the row space of $A$ transforms to column space of $A$.")
        o1.move_to(2.5*DOWN)
        o2.move_to(3.5*DOWN)
        o1.scale(0.7)
        o2.scale(0.7)
        o1.add_background_rectangle()
        o2.add_background_rectangle()
        self.play(Write(o1))
        self.play(Write(o2))
        self.wait()

        matrix = [[1,-1],[1,-1]]
        self.apply_matrix(matrix)
        self.wait(3)

        self.play(FadeOut(o1), FadeOut(o2))