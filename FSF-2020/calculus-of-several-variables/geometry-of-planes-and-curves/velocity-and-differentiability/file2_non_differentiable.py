from manimlib.imports import *

class nd(Scene):
    def construct(self):
        ld1 = Line().rotate(20*DEGREES)
        pd1 = Dot(ld1.get_end(), fill_opacity = 0)
        pd1.set_stroke(width = 0.5)
        ld2 = Line().rotate(40*DEGREES).shift(1.4*UP + 1.7*RIGHT)
        pd2 = Dot(ld2.get_start(), fill_opacity  = 1, color = PURPLE)
        t1 = TextMobject('A discontinuous function.').scale(0.7).shift(UP + 2*RIGHT)

        obj1 = VGroup(*[ld1, pd1, ld2, pd2]).shift(4*LEFT)
        self.play(FadeIn(obj1), FadeIn(t1))
        self.wait(2)

        ld3 = ld2.copy().rotate(-60*DEGREES).shift(1.4*DOWN + 0.2*RIGHT)
        pd3 = Dot(ld1.get_end(), fill_opacity  = 1, color = PURPLE)
        t2 = TextMobject('Graph containing a sharp corner.').scale(0.7).shift( 2*RIGHT)

        obj2 = VGroup(*[ld3, pd3])

        self.play(Transform(VGroup(*[ld2, pd2]), obj2), ReplacementTransform(t1, t2))

        self.wait(2)

        ld4 = Line().rotate(90*DEGREES)
        pd4 = Dot(ld4.get_center(), color = PURPLE)
        a1 = Arc(start_angle = -180*DEGREES, angle = 90*DEGREES).move_to(ld4.get_end()).rotate(-90*DEGREES).shift(0.5*(UP+RIGHT))
        a2 = Arc(start_angle = -180*DEGREES, angle = 90*DEGREES).move_to(ld4.get_start()).rotate(90*DEGREES).shift(0.5*(DOWN+LEFT))
        t3 = TextMobject('Graph with a vertical line.').scale(0.7).shift(2*RIGHT)

        obj3 = VGroup(*[ld4, pd4, a1, a2]).shift(3*LEFT)

        self.play(FadeOut(obj1), Transform(obj2, obj3), ReplacementTransform(t2, t3))
        self.wait(2)
        self.play(FadeOut(obj2), FadeOut(t3))
