from manimlib.imports import *

class interpretation(ZoomedScene):
    CONFIG = {
    "zoomed_display_height": 3,
    "zoomed_display_width": 3,
    "zoom_factor": 0.15,
    "zoomed_display_center": ORIGIN + 4*LEFT + DOWN,
    }
    def construct(self):

        tgt = Vector((1, 2, 0), color = YELLOW).shift(0.005*RIGHT + 0.007*DOWN)
        dot = Dot(tgt.get_start(),color = RED)
        curve = ParametricFunction(
        lambda t: np.array([
        2*(t**2),
        4*t,
        0
        ]), t_min = -5, t_max = 5
        ).scale(0.3).move_to(ORIGIN + 4*RIGHT).rotate(6*DEGREES)

        ds = ParametricFunction(
        lambda t: np.array([
        2*(t**2),
        4*t,
        0
        ]), t_min = 0, t_max = 0.05, color = GREEN_SCREEN
        ).scale(0.9).shift(3.09*LEFT).rotate(-27.5*DEGREES).move_to(ORIGIN).shift(0.07*UP + 0.05*RIGHT).set_stroke(width=20)

        dsl = TextMobject(r'$ds$', color = GREEN_SCREEN).scale(0.2).next_to(ds, RIGHT, buff = 0)


        tgtText = TextMobject(r'$r\prime (t)$').next_to(tgt, UP, buff = 0).scale(0.7)
        tgt2 = DashedLine((0,0,0),(1, 2, 0), color = GRAY).shift(DOWN + 2*RIGHT)
        circle = Circle(radius = 0.9, color = GREEN_SCREEN).shift(0.85*RIGHT + 0.38*DOWN)
        circle.set_stroke(opacity = 1)
        dl = DashedLine(circle.get_center(), dot.get_center())
        dltext = TextMobject(r'$R = 2.795$').scale(0.5).next_to(circle.get_center(), DOWN, buff = 0.1)

        main = TextMobject(r'r(t) = $\left\langle t^{2}, 2t, 0 \right\rangle\quad r\prime (t) = \left\langle 2t, 2, 0 \right\rangle\quad$ \\ $r\prime\prime (t) = \left\langle 2, 0, 0 \right\rangle$').scale(0.7).shift(3*UP + 3*LEFT)
        main2 = TextMobject(r'Curvature at an arbitrary point \\ say r(t = 0.5) can be given as: \\ $\kappa = \frac{1}{R} = \frac{1}{2.795} = 0.357$').scale(0.7).shift(3.5*LEFT)
        main3 = TextMobject(r'The ',  'tangent', r' and ', 'normal', r' vectors \\ can be represented as:').scale(0.7).shift(3.5*LEFT)
        main3.set_color_by_tex_to_color_map({
            "tangent": YELLOW,
            "normal": BLUE
        })
        main4 = TextMobject(r'These vectors travel along \\ a small interval ', r'$ds$').scale(0.7).shift(1.5*UP + 3*LEFT)
        main4.set_color_by_tex_to_color_map({
            "$ds$": GREEN_SCREEN
        })

        nm = Vector((2, -1, 0), color = BLUE).shift(0.005*RIGHT + 0.007*DOWN)
        nmText = TextMobject(r'$r\prime\prime (t)$').next_to(nm, DOWN+RIGHT, buff = 0).scale(0.7)
        nm2 = DashedLine((0,0,0),(2, -1, 0), color = GRAY).shift(2*UP + RIGHT)
        square = Square(fill_color = WHITE, fill_opacity = 0.2).rotate(63*DEGREES).shift(0.5*UP +1.5*RIGHT).scale(1.1)
        square.set_stroke(width = 0.1)
        arrow = CurvedArrow(square.get_center() + np.array([2,1,0]), square.get_center() + np.array([0.5,0,0]))
        arrowText = TextMobject(r'$r\prime (t)\times r\prime\prime (t)$').next_to(arrow.get_start(), DOWN+1*RIGHT, buff = 0).scale(0.7)

        text1 = TextMobject(r'$\left|\frac{dT}{ds}\right| = \frac{\left|\frac{dT}{dt}\right|}{\left|\frac{ds}{dt}\right|}$').shift(UP+3*LEFT).scale(0.7)
        text2 = TextMobject(r'$\left|\frac{dT}{ds}\right| = \frac{\frac{r\prime\prime (t)}{\left| r\prime (t)\right|}\times\frac{r\prime (t)}{\left| r\prime (t)\right|}}{\left|r\prime (t)\right|}$').next_to(text1, DOWN, buff = 0.1).scale(0.7)
        text3 = TextMobject(r'$= \frac{4}{(4t^{2} + 4)^{\frac{3}{2}}}$ \\ $= \frac{1}{2\sqrt{(1 + (0.5)^{2})^{3}}}$').next_to(text2, DOWN, buff = 0.1).scale(0.7)
        text4 = TextMobject(r'$ = 0.357$').scale(0.7).next_to(text3, DOWN, buff = 0.2)
        unit = VGroup(*[tgt, tgt2, nm, nm2])

        tgt2text = TextMobject(r'$\frac{r\prime (t)}{\left| r\prime (t)\right|}$').shift(1.1*UP).scale(0.7).rotate(63*DEGREES  )
        nm2text = TextMobject(r'$\frac{r\prime\prime (t)}{\left| r\prime (t)\right|}$').scale(0.7).shift(0.7*RIGHT+0.8*DOWN).rotate(-25*DEGREES)
        unit2 = unit.copy().scale(0.5).shift(0.75*LEFT+0.25*DOWN)

        self.play(FadeIn(curve), FadeIn(main))
        self.wait(1)
        self.play(ApplyMethod(curve.scale, 3), ApplyMethod(curve.shift, ORIGIN + 3.31*RIGHT))
        # self.wait(2)
        self.play(FadeIn(main2), FadeIn(dot))
        self.play(FadeIn(circle), FadeIn(dl), FadeIn(dltext))
        self.wait()
        self.play(ReplacementTransform(main2, main3), FadeOut(circle), FadeOut(dl), FadeOut(dltext), FadeIn(VGroup(*[tgt, tgtText])))
        self.wait(1)
        self.play(FadeIn(VGroup(*[nm, nmText])))
        self.wait(1)
        self.remove(dot)
        self.setup()
        #self.camera_frame.set_width(4)
        self.activate_zooming(animate = True)
        self.play(FadeIn(ds), FadeIn(dsl), FadeOut(main3))
        self.wait(1)
        self.play(FadeIn(main4))
        self.play(ApplyMethod(tgt.shift, 0.16*UP + 0.09*RIGHT), ApplyMethod(nm.shift, 0.16*UP + 0.09*RIGHT), run_time = 5)
        self.wait(1)
        self.play(FadeOut(ds), FadeOut(dsl), FadeOut(main4),  FadeOut(self.zoomed_display, run_time = 1), FadeOut(self.zoomed_camera.frame, run_time = 1))
        # tgt = tgt.shift(0.16*DOWN + 0.08*LEFT)
        # nm = nm.shift(0.16*DOWN + 0.08*LEFT)
        self.play(ApplyMethod(tgt.shift, 0.16*DOWN + 0.09*LEFT, run_time = 1), ApplyMethod(nm.shift, 0.16*DOWN + 0.09*LEFT, run_time = 1))
        self.play(FadeIn(dot), FadeIn(VGroup(*[tgt2, nm2])))
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
        self.wait(1)
        self.play(FadeIn(text3))
        self.wait(1)
        self.play(FadeIn(text4))
        self.wait(2)
        self.play(FadeOut(VGroup(*[main, curve, dot, tgt2text, nm2text, text1, text2, text3, text4, tgt, tgtText,nm, nmText,tgt2, nm2,square, arrow, arrowText,unit2])))
