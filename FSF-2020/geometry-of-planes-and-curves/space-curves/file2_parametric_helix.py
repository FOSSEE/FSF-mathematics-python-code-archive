from manimlib.imports import *

class parametricHelix(ThreeDScene, GraphScene):
    def construct(self):
        self.x_min = -3
        self.y_min = -4
        self.graph_origin = ORIGIN
        self.x_max = 3
        self.y_max = 4
        self.x_axis_label =  ""
        self.y_axis_label =  ""
        self.x_axis_width = 7.5
        self.y_axis_height = 7.5
        ax1 = ThreeDAxes().scale(0.65).shift(2.6*RIGHT+DOWN+np.array([0,0,0.5]))
        axes_group = []

        self.setup_axes()
        self.axes.shift(3*RIGHT + 2*UP).scale(0.5)
        axes_group.append(self.axes)

        self.setup_axes()
        self.axes.shift(3*RIGHT + 2*DOWN).scale(0.5)
        axes_group.append(self.axes)

        axes_group = VGroup(*axes_group)

        asint_text = TextMobject(r'$x = a\sin{t}$').scale(0.7).shift(4*RIGHT + 3*UP)
        xlabel1 = TextMobject(r'$x$').shift(3.3*RIGHT + 3.7*UP).scale(0.7)
        tlabel1 = TextMobject(r'$t$').shift(5*RIGHT + 2*UP).scale(0.7)
        up_text = VGroup(*[asint_text, xlabel1, tlabel1])
        asint = ParametricFunction(
                    lambda t: np.array([
                    t,
                    np.sin(t),
                    0
                    ]), t_min = -np.pi, t_max = np.pi, color = GREEN_E
                    ).shift(3*RIGHT + 2*UP).scale(0.4)

        acost_text = TextMobject(r'$y = a\cos{t}$').scale(0.7).shift(4*RIGHT + DOWN)
        ylabel1 = TextMobject(r'$y$').shift(3.3*RIGHT+0.3*DOWN).scale(0.7)
        tlabel2 = TextMobject(r'$t$').shift(5*RIGHT + 2*DOWN).scale(0.7)
        down_text = VGroup(*[acost_text, ylabel1, tlabel2])
        acost = ParametricFunction(
                    lambda t: np.array([
                    t,
                    np.cos(t),
                    0
                    ]), t_min = -np.pi, t_max = np.pi, color = BLUE
                    ).shift(3*RIGHT + 2*DOWN).scale(0.4)

        up_dot = Dot(color = RED)
        down_dot = Dot(color = RED)
        helix_dot = Dot(radius = 0.16, color = RED)

        zlabel = TextMobject(r'$z$').scale(0.7).shift(3*UP + 2.8*LEFT)
        ylabel2 = TextMobject(r'$y$').scale(0.7).shift(0.3*DOWN+0.15*RIGHT)
        xlabel2 = TextMobject(r'$x$').scale(0.7).shift(0.5*DOWN + 6.4*LEFT)
        helix_text = TextMobject(r'$x = a\sin{t}$ \\ $y = a\cos{t}$ \\ $z = ct$').scale(0.7).shift(2.3*UP + 1.3*LEFT)
        main_text = VGroup(*[xlabel2, ylabel2, zlabel, helix_text])
        helix = ParametricFunction(
                lambda t: np.array([
                np.cos(TAU*t),
                np.sin(TAU*t),
                0.4*t
                ]), t_min = -np.pi, t_max = np.pi, color = WHITE
                ).shift(ax1.get_center())

        self.set_camera_orientation(phi = 75*DEGREES, theta=45*DEGREES)

        t_tracker = ValueTracker(-3.14)
        t=t_tracker.get_value

        t_label = TexMobject(
            "t = ",color=WHITE
            ).next_to(helix_text,DOWN, buff=0.2).scale(0.6)

        t_text = always_redraw(
            lambda: DecimalNumber(
                t(),
                color=WHITE,
            ).next_to(t_label, RIGHT, buff=0.2)
        ).scale(0.6)

        group = VGroup(t_text,t_label).scale(1.5).move_to(ORIGIN).shift(2*DOWN)
        self.add_fixed_in_frame_mobjects(axes_group, main_text, up_text, down_text, acost, asint)
        self.play(FadeIn(ax1), FadeIn(axes_group), FadeIn(asint), FadeIn(acost), FadeIn(helix), FadeIn(up_text), FadeIn(down_text), FadeIn(main_text))
        #self.begin_ambient_camera_rotation(rate = 0.06)
        self.add_fixed_in_frame_mobjects(up_dot, down_dot, group)
        self.play(MoveAlongPath(up_dot, asint, run_time = 7), MoveAlongPath(down_dot, acost, run_time = 7), MoveAlongPath(helix_dot, helix, run_time = 7), t_tracker.set_value,3.14, rate_func=linear, run_time=7)
        self.play(FadeOut(VGroup(*[ax1, axes_group, asint, acost, helix, up_text, down_text, main_text, up_dot, down_dot, helix_dot, group])))
        self.wait(1)
