from manimlib.imports import *

class interpretation(Scene):
    def construct(self):
        tgt = Vector((1, 2, 0), color = YELLOW)
        tgtText = TextMobject(r'$r\prime (t)$').next_to(tgt, UP, buff = 0).scale(0.7)
        tgt2 = DashedLine((0,0,0),(1, 2, 0), color = GRAY).shift(DOWN + 2*RIGHT)

        nm = Vector((2, -1, 0), color = BLUE)
        nmText = TextMobject(r'$r\prime\prime (t)$').next_to(nm, DOWN+RIGHT, buff = 0).scale(0.7)
        nm2 = DashedLine((0,0,0),(2, -1, 0), color = GRAY).shift(2*UP + RIGHT)
        square = Square(fill_color = WHITE, fill_opacity = 0.2).rotate(63*DEGREES).shift(0.5*UP +1.5*RIGHT).scale(1.1)
        square.set_stroke(width = 0.1)
        arrow = CurvedArrow(square.get_center() + np.array([2,1,0]), square.get_center() + np.array([0.5,0,0]))
        arrowText = TextMobject(r'$r\prime (t)\times r\prime\prime (t)$').next_to(arrow.get_start(), DOWN+1*RIGHT, buff = 0).scale(0.7)

        text1 = TextMobject(r'$\left|\frac{dT}{ds}\right| = \frac{\left|\frac{dT}{dt}\right|}{\left|\frac{ds}{dt}\right|}$').shift(UP+3*LEFT)
        text2 = TextMobject(r'$\left|\frac{dT}{ds}\right| = \frac{\frac{r\prime\prime (t)}{\left| r\prime (t)\right|}\times\frac{r\prime (t)}{\left| r\prime (t)\right|}}{\left|r\prime (t)\right|}$').next_to(text1, DOWN, buff = 0.1)
        unit = VGroup(*[tgt, tgt2, nm, nm2])

        # self.play(FadeIn(VGroup(*[tgt, tgt2, nm, nm2, nmText, tgtText, square, arrow, arrowText])))
        tgt2text = TextMobject(r'$\frac{r\prime (t)}{\left| r\prime (t)\right|}$').shift(1.1*UP).scale(0.7).rotate(63*DEGREES  )
        nm2text = TextMobject(r'$\frac{dT}{dt} = \frac{r\prime\prime (t)}{\left| r\prime (t)\right|}$').scale(0.6).shift(0.5*RIGHT+0.6*DOWN).rotate(-25*DEGREES)
        unit2 = unit.copy().scale(0.5).shift(0.75*LEFT+0.25*DOWN)

        self.play(FadeIn(VGroup(*[tgt, tgtText])))
        self.wait(1)
        self.play(FadeIn(VGroup(*[nm, nmText])))
        self.wait(1)
        self.play(FadeIn(VGroup(*[tgt2, nm2])))
        self.wait(1)
        self.play(FadeIn(VGroup(*[square, arrow, arrowText])))
        self.wait(1)
        self.play(FadeIn(unit2))
        self.wait(1)
        self.play(FadeIn(VGroup(*[tgt2text, nm2text])))
        self.wait(1)
        self.play(FadeIn(text1))
        self.wait(1)
        self.play(FadeIn(text2))
        self.wait(2)
        self.play(FadeOut(VGroup(*[tgt2text, nm2text, text1, text2, tgt, tgtText,nm, nmText,tgt2, nm2,square, arrow, arrowText,unit2])))
