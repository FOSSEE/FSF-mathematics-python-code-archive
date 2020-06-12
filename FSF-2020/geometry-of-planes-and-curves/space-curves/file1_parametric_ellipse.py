from manimlib.imports import *

class parametricEllipse(ThreeDScene):
    def construct(self):
        ax1 = ThreeDAxes().scale(0.5).shift(3*LEFT)
        ax2 = ThreeDAxes().scale(0.3).shift(3*RIGHT + 2*UP)
        ax3 = ThreeDAxes().scale(0.3).shift(3*RIGHT + 2*DOWN)

        t_value = ValueTracker(-3.14)
        t_tex = DecimalNumber(t_value.get_value()).add_updater(lambda v: v.set_value(t_value.get_value()))
        t_label = TexMobject("t = ")
        group = VGroup(t_tex,t_label).shift(3*DOWN)
        t_label.next_to(t_tex,LEFT, buff=0.2,aligned_edge=t_label.get_bottom())

        asint_text = TextMobject(r'$x = a\sin{t}$').scale(0.7).shift(4*RIGHT + 3*UP)
        xlabel1 = TextMobject(r'$x$').shift(3.3*RIGHT + 3.7*UP).scale(0.7)
        tlabel1 = TextMobject(r'$t$').shift(4.8*RIGHT + 2*UP).scale(0.7)
        up_text = VGroup(*[asint_text, xlabel1, tlabel1])
        asint = ParametricFunction(
        lambda t: np.array([
        t,
        np.sin(t),
        0
        ]), t_min = -np.pi, t_max = np.pi, color = GREEN_E
        ).shift(3*RIGHT + 2*UP).scale(0.4)

        bcost_text = TextMobject(r'$y = b\cos{t}$').scale(0.7).shift(4*RIGHT + DOWN)
        ylabel1 = TextMobject(r'$y$').shift(3.3*RIGHT+0.3*DOWN).scale(0.7)
        tlabel2 = TextMobject(r'$t$').shift(4.8*RIGHT + 2*DOWN).scale(0.7)
        down_text = VGroup(*[bcost_text, ylabel1, tlabel2])
        bcost = ParametricFunction(
        lambda t: np.array([
        t,
        1.5*np.cos(t),
        0
        ]), t_min = -np.pi, t_max = np.pi, color = BLUE
        ).shift(3*RIGHT + 2*DOWN).scale(0.4)

        up_dot = Dot(color = RED)
        down_dot = Dot(color = RED)
        ellipse_dot = Dot(color = RED)

        ylabel2 = TextMobject(r'$y$').scale(0.7).shift(3*UP + 3*LEFT)
        xlabel2 = TextMobject(r'$x$').scale(0.7)
        ellipse_text = TextMobject(r'$x = a\sin{t}$ \\ $y = b\cos{t}$').scale(0.7).shift(2*UP + 1.3*LEFT)
        main_text = VGroup(*[xlabel2, ylabel2, ellipse_text])
        ellipse = ParametricFunction(
                lambda t: np.array([
                1.5*np.cos(t),
                np.sin(t),
                0
                ]), t_min = -np.pi, t_max = np.pi, color = WHITE
                ).shift(3*LEFT)
        self.play(FadeIn(ax1), FadeIn(ax2), FadeIn(ax3), FadeIn(asint), FadeIn(bcost), FadeIn(ellipse), FadeIn(up_text), FadeIn(down_text), FadeIn(main_text), FadeIn(group))
        self.wait(1)
        self.play(MoveAlongPath(up_dot, asint, run_time = 7), MoveAlongPath(down_dot, bcost, run_time = 7), MoveAlongPath(ellipse_dot, ellipse, run_time = 7), t_value.set_value,3.14, rate_func=linear, run_time=7)
        self.wait(1)
        self.play(FadeOut(VGroup(*[ax1, ax2, ax3, asint, bcost, ellipse, up_text, down_text, main_text, up_dot, down_dot, ellipse_dot, group])))
        self.wait(1)
