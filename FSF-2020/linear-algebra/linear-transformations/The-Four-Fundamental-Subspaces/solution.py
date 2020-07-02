from manimlib.imports import *
class solution(LinearTransformationScene):
    def construct(self):

        self.setup()
        self.wait()
        
        o = TextMobject(r"This is the original $2D$ vector space(before Linear Transformation)")
        o.move_to(DOWN)
        o.scale(0.75)
        o.add_background_rectangle()
        self.play(Write(o))
        self.wait()
        self.play(FadeOut(o))

        A = TextMobject("Let $A$ denote the matrix the of this linear transformation.")
        A.move_to(DOWN)
        A.scale(0.75)
        A.add_background_rectangle()
        self.play(Write(A))
        matrix = [[1,-1],[1,-1]]
        self.apply_matrix(matrix)
        self.wait()
        self.play(FadeOut(A))

        o = TextMobject(r"This is the transformed vector space i.e. a line ($1D$)")
        o.move_to(DOWN)
        o.scale(0.75)
        o.add_background_rectangle()
        self.play(Write(o))
        self.wait()
        self.play(FadeOut(o))
        
        arrow2 = Arrow(start = ORIGIN, end = 2*DOWN+2*LEFT)
        arrow2.set_color(DARK_BLUE)
        arrow2.scale(1.2)
        self.play(ShowCreation(arrow2))
        self.wait()

        o1 = TextMobject("If the vector lies in the transformed vector space")
        o2 = TextMobject("(the line) then the solution exist")
        o1.move_to(2*DOWN+2*RIGHT)
        o2.move_to(2.5*DOWN+2*RIGHT)
        o1.scale(0.75)
        o2.scale(0.75)
        o1.add_background_rectangle()
        o2.add_background_rectangle()
        self.play(Write(o1))
        self.play(Write(o2))
        self.wait()
        self.play(FadeOut(o1), FadeOut(o2))

        self.play(FadeOut(arrow2))

        arrow1 = Arrow(start = ORIGIN, end = 2*UP+RIGHT)
        arrow1.set_color(DARK_BLUE)
        arrow1.scale(1.3)
        self.play(ShowCreation(arrow1))
        self.wait()

        o1 = TextMobject("If the vector does lies in the transformed")
        o2 = TextMobject("vector space then the does not solution exist")
        o1.move_to(2*DOWN+2*RIGHT)
        o2.move_to(2.5*DOWN+2*RIGHT)
        o1.scale(0.75)
        o2.scale(0.75)
        o1.add_background_rectangle()
        o2.add_background_rectangle()
        self.play(Write(o1))
        self.play(Write(o2))
        self.wait()
        self.play(FadeOut(o1), FadeOut(o2))

        self.play(FadeOut(arrow1))
        