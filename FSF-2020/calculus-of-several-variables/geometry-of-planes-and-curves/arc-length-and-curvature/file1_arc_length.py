from manimlib.imports import *


class arcl(MovingCameraScene):
    def construct(self):
        # self.setup()
        def curve_(x):
            return 3 - (3653*x**2)/5292 + (2477*x**3)/31752 + (13*x**4)/784 - (17*x**5)/5292 + (17*x**6)/63504

        curve = FunctionGraph(curve_, x_min=-2, x_max=6, stroke_width = 2, color = BLUE).scale(0.1).move_to(ORIGIN)
        lines = [Line(length = 0.05, color = RED).scale(0.2).move_to(ORIGIN).shift(np.array([-4 + 0.1*i, curve_(-2.5 + 0.1*i), 0])).rotate(-25*DEGREES) for i in range(4)]
        lines2 = [Line(length = 0.05, color = RED).scale(0.2).move_to(ORIGIN).shift(np.array([-4 + 0.125*i, curve_(-2.5 + 0.1*i), 0])).rotate(-25*DEGREES) for i in range(4, 9)]
        # lines[0].rotate(-25*DEGREES).shift(np.array([-4,curve_(-2.5), 0]))
        # lines[1].rotate(-25*DEGREES).shift(np.array([-3.78,curve_(-2.3), 0]))
        # lines3 = [Line(length = 0.05, color = RED).scale(0.2).move_to(ORIGIN + 1.5*UP + 0.6*RIGHT).shift(np.array([-1 + 0.2*i, -1.5 - 0.2*i, 0])).rotate(30*DEGREES) for i in range(4)]
        # lines2b = VGroup(*lines3).rotate(-8*DEGREES)
        # lines4 = [Line(length = 0.05, color = RED).scale(0.2).move_to(ORIGIN + 1.6*UP + 0.5*RIGHT).shift(np.array([-1 + 0.18*i, -1.65 - 0.2*i, 0])).rotate(22*DEGREES) for i in range(4, 9)]
        # lines5 = [Line(length = 0.05, color = RED).scale(0.2).move_to(ORIGIN + 7*RIGHT).shift(np.array([-4 + 0.1*i, curve_(-2.5 + 0.1*i), 0])).rotate(-25*DEGREES) for i in range(4)]
        # lines6 = [Line(length = 0.05, color = RED).scale(0.2).move_to(ORIGIN +7.25*RIGHT).shift(np.array([-4 + 0.053*i, curve_(-2.5 + 0.1*i), 0])).rotate(-26*DEGREES) for i in range(4, 9)]

        # lc1 = [Line(length = 0.05, color = RED).scale(0.2).rotate((-25 + i*2) * DEGREES).shift(np.array([-1 + 0.125*i, curve_(-1.5 + 0.1*i), 0])) for i in range(2)]
        # lc1b = VGroup(*lc1).shift(1.7*LEFT + 0.2*DOWN)

        text = TextMobject(r'$r(t) = \left\langle t, t^{3} - 2t, 0\right\rangle$ \\ $r\prime (t) = \left\langle 1, 3t^{2} - 2, 0\right\rangle$').scale(0.7).shift(3*UP + 4*RIGHT)

        # l = VGroup(*lines, *lines2, lines2b, *lines4, *lines5, *lines6, lc1b).shift(curve.get_center())
        l = VGroup(*lines, *lines2)
        arc = Line(lines[3].get_center(), lines2[0].get_center() + np.array([0.005, 0 ,0]), color = GREEN_SCREEN).rotate(12*DEGREES)
        arctext = TextMobject(r'$ds$', color = GREEN_SCREEN).scale(0.15).next_to(arc.get_center(), 0.001*DOWN + 0.01*RIGHT,buff = 0.01)
        dy = Arrow(arc.get_start(), np.array([arc.get_start()[0], lines2[0].get_center()[1] + 0.01, 0]), color = YELLOW)
        dx = Arrow(arc.get_start(), np.array([lines2[0].get_center()[0] - 0.01, arc.get_start()[1], 0]), color = BLUE)
        dxt = DashedLine(dy.get_end(), dy.get_end() + np.array([0.13, 0 ,0]))
        dyt = DashedLine(dx.get_end(), dx.get_end() + np.array([0, 0.3 ,0]))
        dxtext = TextMobject(r'$dx$').scale(0.2).next_to(dx, RIGHT, buff = 0.01)
        dytext = TextMobject(r'$dy$').scale(0.2).next_to(dy, LEFT, buff = 0.01)
        formula = TextMobject(r"Consider a very small interval ", r'$ds$. \\', r"Using Pythagoras' theorem, \\",  r'$ds$', r" = $\sqrt{(dx)^{2} + (dy)^{2}}$").scale(0.25).shift(5*LEFT + 0.5*UP)
        formula.set_color_by_tex_to_color_map({
            "$ds$. \\": GREEN_SCREEN,
            "$ds$": GREEN_SCREEN
        })

        formula2 = TextMobject(r'To compute the arc length \\ from $a$ to $b$, we need to \\ sum over all intervals ', r'$ds$').scale(0.25).shift(5.2*LEFT + 0.7*UP)
        formula2.set_color_by_tex_to_color_map({
            "$ds$": GREEN_SCREEN
        })

        formula3 = TextMobject(r'$L = \int_{a}^{b} ds$ \\ $= \int_{a}^{b} \sqrt{(\frac{dx}{dt})^{2} + (\frac{dy}{dt})^{2} + (\frac{dz}{dt})^{2}}\quad dt$').scale(0.25).shift(5.2*LEFT + 0.1*UP)

        bl = DashedLine(lines2[4].get_center(), lines2[4].get_center() + np.array([1,0,0]))
        blt = TextMobject(r'$b$').scale(0.5).next_to(bl.get_center(), DOWN, buff=0.1)
        al = DashedLine(lines[0].get_center(), lines[0].get_center() + np.array([1,0,0]))
        alt = TextMobject(r'$a$').scale(0.5).next_to(al.get_center(), UP, buff=0.1)
        pts = VGroup(*[bl, blt, al, alt])

        compute = TextMobject(r'To compute the arc length from \\ $t = -1.4$ to $t = -1.1$, \\ summation of small intervals $ds$ \\ is given by $L = \int_{-1.4}^{-1.1} ds$ \\').scale(0.7).shift(6.8*LEFT + 2.5*UP)
        compute_ = TextMobject(r'L  = $ \int_{-1.4}^{-1.1} \sqrt{(\frac{dx}{dt})^{2} + (\frac{dy}{dt})^{2} + (\frac{dz}{dt})^{2}}\quad dt$ \\ = $\int_{-1.4}^{-1.1} \sqrt{1^{2} + (3t^{2} - 2)^{2} + 0^{2}}\quad dt$').scale(0.7).shift(6.8*LEFT + -0.6*DOWN)
        #compute = VGroup(*[compute, compute_])
        compute2 = TextMobject(r'$ = \int_{-1.4}^{-1.1} \sqrt{9t^{4} - 12t^{2} + 5}\quad dt$').scale(0.7).shift(6.8*LEFT + 0.7*DOWN)
        compute3 = TextMobject(r'$L = 0.8693$').scale(0.7).shift(6.8*LEFT + 1.2*DOWN)
        arclen = compute3.copy()
        arclen = arclen.scale(0.8).next_to(arc.get_center(), RIGHT, buff = 0.1)
        dsd = TextMobject(r'We can divide the curve \\ into multiple small arcs ', r'$ds$').scale(0.25).shift(5.2*LEFT + 0.2*UP)
        dsd.set_color_by_tex_to_color_map({
            "$ds$": GREEN_SCREEN
        })

        # 13th sec, consider a v small interval ds, show Pythagoras
        # reduce text size
        # then show we can divide curve into small ds
        # all red ds
        # To compute arc length, we need to sum over all intervals ds
        # a and b show and give dashes dy dx for first and last
        # give dz in formula and show it's zero
        # Zooom out, Remove red bars, draw yellow line
        # Consider t = -1.4 to -1.1
        # at end show l = 0.693 near yellow line, smaller size

        ax1 = Vector((0,1,0), color = YELLOW)
        ax1l = TextMobject(r'$y$').next_to(ax1, LEFT, buff = 0)
        ax2 = Vector((1,0,0), color = BLUE)
        ax2l = TextMobject(r'$x$').next_to(ax2, RIGHT, buff = 0)
        ax = VGroup(*[ax1, ax1l, ax2, ax2l]).scale(0.6).shift(3*DOWN + 6*LEFT)

        self.play(FadeIn(curve), FadeIn(ax))
        self.play(ApplyMethod(curve.scale, 10), FadeIn(text))
        # self.play(FadeIn(l))
        self.wait(2)
        self.play(FadeOut(text))
        self.play(self.camera_frame.set_width, 5,
                    self.camera_frame.move_to, 3.8*LEFT+0.4*DOWN,
                    ax.shift, UP,
                    ax.scale, 0.5, run_time = 4)
        long = ArcBetweenPoints(lines[1].get_center() + 0.01, lines2[3].get_center(), color = YELLOW, angle = 10*DEGREES).rotate(180*DEGREES)


        self.play(Write(formula),FadeIn(VGroup(*[arc, arctext, dy, dx, dxt, dyt, dxtext, dytext])), FadeIn(VGroup(*[lines[3], lines2[0]])))
        self.wait(2)
        self.play(ReplacementTransform(formula, dsd), TransformFromCopy(VGroup(*[lines[3], lines2[0]]) , l))
        #Transform(l, VGroup(*[lines[3], lines2[0]])), )
        self.wait(2)
        self.play(ReplacementTransform(dsd, formula2), FadeIn(pts))
        self.wait(3)
        self.play(FadeIn(formula3))
        self.wait(2)
        self.play(FadeOut(VGroup(*[formula3, l, pts,  formula2, arc, arctext, dy, dx, dxt, dyt, dxtext, dytext])))
        self.play(
                    self.camera_frame.set_width, 15,
                    self.camera_frame.move_to, 3*LEFT,
                    ax.shift, DOWN + 3*LEFT,
                    ax.scale, 2.3,
                    run_time = 4)
        text = text.shift(2*LEFT)
        self.play(FadeIn(long), FadeIn(compute), FadeIn(text))
        self.wait(2)
        self.play(FadeIn(compute_))
        self.wait(2)
        self.play(FadeIn(compute2))
        self.wait(1)
        self.play(FadeIn(compute3))
        self.wait(1)
        self.play(TransformFromCopy(compute3, arclen))
        self.wait(2)
        self.play(FadeOut(VGroup(*[ax, arclen, compute_, curve, text, compute, compute2, compute3, long])))
