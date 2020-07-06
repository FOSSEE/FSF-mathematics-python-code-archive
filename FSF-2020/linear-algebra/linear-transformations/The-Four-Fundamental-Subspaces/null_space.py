from manimlib.imports import *
class null_space(LinearTransformationScene):
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
        o2 = TextMobject(r"span of a particular vector $\left(\begin{array}{c} 1 \\ 1 \end{array}\right)$")
        o1.move_to(2*DOWN+3*RIGHT)
        o2.move_to(2.75*DOWN+3*RIGHT)
        o1.scale(0.7)
        o2.scale(0.7)
        o1.add_background_rectangle()
        o2.add_background_rectangle()
        self.play(Write(o1))
        self.play(Write(o2))

        arrow = Arrow(start = ORIGIN, end = UP+RIGHT)
        arrow1 = Arrow(start = ORIGIN, end = 2*(UP+RIGHT))
        arrow2 = Arrow(start = ORIGIN, end = 3*(UP+RIGHT))
        arrow3 = Arrow(start = ORIGIN, end = 4*(UP+RIGHT))
        arrow4 = Arrow(start = ORIGIN, end = DOWN+LEFT)
        arrow5 = Arrow(start = ORIGIN, end = 2*(DOWN+LEFT))
        arrow6 = Arrow(start = ORIGIN, end = 3*(DOWN+LEFT))
        arrow7 = Arrow(start = ORIGIN, end = 4*(DOWN+LEFT))

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

        self.add_transformable_mobject(arrow)
        self.add_transformable_mobject(arrow1)
        self.add_transformable_mobject(arrow2)
        self.add_transformable_mobject(arrow3)
        self.add_transformable_mobject(arrow4)
        self.add_transformable_mobject(arrow5)
        self.add_transformable_mobject(arrow6)
        self.add_transformable_mobject(arrow7)

        o1 = TextMobject("Notice, entire set of vectors which belong to the vector")
        o2 = TextMobject(r"subspace(Linear Span of $\left(\begin{array}{c} 1 \\ 1 \end{array}\right)$) transforms to zero")
        o1.move_to(2*DOWN+2.5*RIGHT)
        o2.move_to(2.75*DOWN+2.5*RIGHT)
        o1.scale(0.7)
        o2.scale(0.7)
        o1.add_background_rectangle()
        o2.add_background_rectangle()
        self.play(Write(o1))
        self.play(Write(o2))
        self.wait()

        matrix = [[1,-1],[1,-1]]
        self.apply_matrix(matrix)
        self.wait()

        self.play(FadeOut(o1), FadeOut(o2))

        o = TextMobject(r"Hence, the vector space formed by linear span of $\left(\begin{array}{c} 1 \\ 1 \end{array}\right)$ is the null space of $A$")
        o.move_to(DOWN)
        o.scale(0.75)
        o.add_background_rectangle()
        self.play(Write(o))
        self.wait(2)
        self.play(FadeOut(o), FadeOut(arrow), FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3), FadeOut(arrow4), FadeOut(arrow5), FadeOut(arrow6), FadeOut(arrow7))
