from manimlib.imports import *

class tnb(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 75*DEGREES, theta=45*DEGREES)

        t = TextMobject(r'T', color = YELLOW)
        n = TextMobject(r'N', color = BLUE).next_to(t, RIGHT, buff=0)
        b = TextMobject(r'B', color = GREEN_E).next_to(n, RIGHT, buff=0)
        frame = TextMobject(r'Frame').next_to(b, RIGHT, buff=0.2)

        text = VGroup(*[t,n,b,frame]).move_to(ORIGIN).shift(3*UP)

        c1 = TextMobject(r'$r(t) = \left\langle\cos{t}, \sin{t}, 0.4t\right\rangle\quad r\prime (t) =\left\langle -\sin{t}, \cos{t}, 0.4\right\rangle$').next_to(text, DOWN, buff = 0.1).scale(0.7)


        helix1 = ParametricFunction(
                lambda t: np.array([
                np.cos(TAU*t),
                np.sin(TAU*t),
                0.4*t
                ]), t_min = -2*np.pi/3, t_max = -1.638*np.pi/3, color = WHITE
                )

        helix2 = ParametricFunction(
                lambda t: np.array([
                np.cos(TAU*t),
                np.sin(TAU*t),
                0.4*t
                ]), t_min = -1.638*np.pi/3, t_max = -1.33*np.pi/3, color = WHITE
                )

        helix3 = ParametricFunction(
                lambda t: np.array([
                np.cos(TAU*t),
                np.sin(TAU*t),
                0.4*t
                ]), t_min = -1.33*np.pi/3, t_max = -np.pi/3, color = WHITE
                )

        helix4 = ParametricFunction(
                lambda t: np.array([
                np.cos(TAU*t),
                np.sin(TAU*t),
                0.4*t
                ]), t_min = -np.pi/3, t_max = -1.3*np.pi/6, color = WHITE
                )

        helix5 = ParametricFunction(
                lambda t: np.array([
                np.cos(TAU*t),
                np.sin(TAU*t),
                0.4*t
                ]), t_min = -1.3*np.pi/6, t_max = 0, color = WHITE
                )

        helix_dot = Dot(radius = 0.16, color = RED)

        t_tracker = ValueTracker(-2*np.pi/3)
        t=t_tracker.get_value

        # t_label = TexMobject(
        #     "t = ",color=WHITE
        #     ).next_to(helix1,DOWN, buff=0.2).scale(0.6)

        cval1 = TextMobject(r'r(').next_to(c1, DOWN+16.5*LEFT, buff = 0.1).scale(0.7)

        t_text = always_redraw(
            lambda: DecimalNumber(
                t(),
                color=WHITE,
            ).next_to(cval1, RIGHT, buff=0.05).scale(0.7)
        ).scale(0.6)


        cval2 = always_redraw(
            lambda: TextMobject(r') = $\left\langle$').scale(0.7).next_to(t_text, RIGHT, buff = 0.05)
            )

        cos = always_redraw(
            lambda: DecimalNumber(
                np.cos(t()),
                color=WHITE,
            ).next_to(cval2, RIGHT, buff=0.1).scale(0.7)
        ).scale(0.6)

        sin = always_redraw(
            lambda: DecimalNumber(
                np.sin(t()),
                color=WHITE,
            ).next_to(cos, RIGHT, buff=0.1).scale(0.7)
        ).scale(0.6)

        zpart = always_redraw(
            lambda: DecimalNumber(
                0.4* t(),
                color=WHITE,
            ).next_to(sin, RIGHT, buff=0.1).scale(0.7)
        ).scale(0.6)

        cvalend = always_redraw(
        lambda: TextMobject(r' $\right\rangle$').next_to(zpart, RIGHT, buff = 0.2).scale(0.7)
        ).scale(0.6)


        valgroup = VGroup(*[cval1, cval2,cos,sin,zpart, cvalend])

        rp1 = always_redraw(
        lambda: TextMobject(r'$r\prime ($').scale(0.7).next_to(cvalend, RIGHT, buff = 0.6)
        )

        t_text2 = always_redraw(
            lambda: DecimalNumber(
                t(),
                color=WHITE,
            ).next_to(rp1, RIGHT, buff=0.05).scale(0.7)
        ).scale(0.6)

        rp2 = always_redraw(
        lambda: TextMobject(r') = $\left\langle$').scale(0.7).next_to(t_text2, RIGHT, buff = 0.05)
        )

        rps = always_redraw(
            lambda: DecimalNumber(
                -np.sin(t()),
                color=WHITE,
            ).next_to(rp2, RIGHT, buff=0.1).scale(0.7)
        ).scale(0.6)


        rpc = always_redraw(
            lambda: DecimalNumber(
                np.cos(t()),
                color=WHITE,
            ).next_to(rps, RIGHT, buff=0.1).scale(0.7)
        ).scale(0.6)


        const = always_redraw(
        lambda: TextMobject(r'0.4 $\right\rangle$').next_to(rpc, RIGHT, buff = 0.2).scale(0.7)
        ).scale(0.6).shift(0.1*DOWN)

        val2group = VGroup(*[rp1, rp2, rps, rpc, const])

        #group = VGroup(t_text, t_text2).scale(1.5).move_to(ORIGIN).shift(3.7*DOWN)


        dot0 = Dot(np.array([np.cos(-2*np.pi/3), np.sin(-2*np.pi/3), -0.8*np.pi/3]), radius = 0.16, color=RED).shift(np.array([4.65,0,-0.8]))
        tgt0 = Arrow((0,0,0), (1,2,0), color = YELLOW).shift(dot0.get_center() - np.array([0.04,0.2,0]))
        nm0 = Arrow((0,0,0), (-2,1,0), color = BLUE).shift(dot0.get_center() + np.array([0.3,0,0]))
        bnm0 = Arrow((0,0,0), (0,2,0), color = GREEN_E).shift(6.1*LEFT + 3*DOWN)
        plane0 = Square(color = DARK_BROWN, fill_color = WHITE, fill_opacity=0.3).shift(dot0.get_center() + np.array([-0.35, 0.85, 0])).scale(1.2).rotate(65*DEGREES)
        point0 = VGroup(*[dot0, tgt0, nm0, bnm0, plane0]).scale(0.8).shift(np.array([1,0,0]))

        dot1 = Dot(np.array([np.cos(-np.pi/3), np.sin(-np.pi/3), -0.4*np.pi/3]) + np.array([0,0.2,0]), radius = 0.16, color=RED)
        tgt1 = Arrow((0,0,0), (-2,-0.55,0), color = YELLOW).shift(dot1.get_center() + np.array([0.18,0.04,0]))
        nm1 = Arrow((0,0,0), (0.4,-2,0), color = BLUE).shift(dot1.get_center() + np.array([0,0.26,0]))
        bnm1 = Arrow((0,0,0), (0,2,0), color=GREEN_E).shift(3.68*RIGHT+2.48*DOWN)
        plane1 = Square(color = DARK_BROWN, fill_color = WHITE, fill_opacity=0.3).shift(dot1.get_center() + np.array([-0.4, -0.6, 0])).rotate(13*DEGREES).scale(1.2)
        point1 = VGroup(*[dot1, tgt1, nm1, plane1]).scale(0.8).shift(np.array([1,6.25,0]))

        dot2 = Dot(np.array([np.cos(-np.pi/6), np.sin(-np.pi/6), -0.2*np.pi/3]) - np.array([1.9,0,0]), radius=0.16,color=RED)
        tgt2 = Arrow((0,0,0), (1,-2,0), color = YELLOW).shift(dot2.get_center() + np.array([-0.2,0.2,0]))
        nm2 = Arrow((0,0,0), (2,1,0), color = BLUE).shift(dot2.get_center() + np.array([-0.2,-0.06,0]))
        bnm2 = Arrow((0,0,0), (0,2,0), color=GREEN_E).shift(0.4*RIGHT + 0.16*DOWN)
        plane2 = Square(color = DARK_BROWN, fill_color = WHITE, fill_opacity=0.3).shift(dot2.get_center() + np.array([0.92, -0.5, 0])).rotate(23*DEGREES).scale(1.2)
        point2 = VGroup(*[dot2, tgt2, nm2, bnm2, plane2])

        helix = VGroup(*[helix1, helix2, helix3, helix4, helix5])
        self.add_fixed_in_frame_mobjects(text, c1)
        self.play(FadeIn(helix), FadeIn(text), FadeIn(c1))
        self.play(ApplyMethod(helix.scale, 4))
        self.add_fixed_in_frame_mobjects(bnm0, valgroup, val2group, t_text, t_text2)
        self.play(FadeIn(point0), FadeIn(t_text), FadeIn(t_text2), FadeIn(valgroup), FadeIn(val2group))
        self.play(ApplyMethod(point0.set_color, GRAY, opacity = 0.1, run_time = 0.5), MoveAlongPath(helix_dot, helix1, run_time=5), t_tracker.set_value,-1.638*np.pi/3, rate_func=linear, run_time=5)

        self.add_fixed_in_frame_mobjects(bnm1)
        self.play(FadeIn(point1))
        self.play(ApplyMethod(point1.set_color, GRAY, opacity = 0.1, run_time = 0.5), ApplyMethod(bnm1.set_color, GRAY, opacity = 0.1, run_time = 0.5), MoveAlongPath(helix_dot, helix2, run_time = 5), t_tracker.set_value,-1.33*np.pi/3, rate_func=linear, run_time=5)

        self.add_fixed_in_frame_mobjects(bnm2)
        self.play(FadeIn(point2))
        self.play(ApplyMethod(point2.set_color, GRAY, opacity = 0.1, run_time = 0.5), MoveAlongPath(helix_dot, helix3, run_time=5), t_tracker.set_value,-np.pi/3, rate_func=linear, run_time=5)

        dot3 = Dot(np.array([np.cos(-np.pi/3), np.sin(-np.pi/3), -0.4*np.pi/3]) + np.array([3.3,-0.25,0]), radius = 0.16, color=RED)
        tgt3 = Arrow((0,0,0), (0,2,0), color = YELLOW).shift(helix_dot.get_center() - np.array([-0.05,0.2,0]))
        nm3 = Arrow((0,0,0), (-2,0,0), color = BLUE).shift(helix_dot.get_center() + np.array([0.25,0,0]))
        bnm3 = Arrow((0,0,0), (0,2,0), color = GREEN_E).shift(3.87*LEFT + 1.24*DOWN)
        plane3 = Square(color = DARK_BROWN, fill_color = WHITE, fill_opacity=0.3).shift(helix_dot.get_center() + np.array([-0.5, 0.62, 0]))
        point3 = VGroup(*[dot3, tgt3, nm3, bnm3, plane3]).shift(np.array([0,0,0]))

        dot4 = Dot(np.array([np.cos(-np.pi/12), np.sin(-np.pi/12), -0.1*np.pi/3]) + np.array([-3.4,3.4,0]), radius = 0.16, color=RED)
        tgt4 = Arrow((0,0,0), (-2,-0.85,0), color = YELLOW).shift(dot4.get_center() - np.array([-0.05,0,0]))
        nm4 = Arrow((0,0,0), (0.8,-2,0), color = BLUE).shift(dot4.get_center() + np.array([-0.1,0.25,0]))
        bnm4 = Arrow((0,0,0), (0,2,0), color = GREEN_E).shift(4.03*RIGHT + 0.5*DOWN)
        plane4 = Square(color = DARK_BROWN, fill_color = WHITE, fill_opacity=0.3).shift(dot4.get_center() + np.array([-0.4,-1,0])).rotate(22*DEGREES).scale(1.2)
        point4 = VGroup(*[dot4, tgt4, nm4, bnm4, plane4])

        dot5 = Dot((1,0,0) + np.array([2.3,-1,1]))
        tgt5 = Arrow((0,0,0), (0,2,0), color = YELLOW).shift(dot5.get_center() - np.array([-0.05,0.2,0]))
        nm5 = Arrow((0,0,0), (-2,0,0), color = BLUE).shift(dot5.get_center() + np.array([0.25,0,0]))
        bnm5 = Arrow((0,0,0), (0,2,0), color = GREEN_E).shift(3.34*LEFT+0.3*UP)
        plane5 = Square(color = DARK_BROWN, fill_color = WHITE, fill_opacity=0.3).shift(dot5.get_center() + np.array([-0.5,0.5,0]))
        point5 = VGroup(*[tgt5, nm5, bnm5, plane5])

        self.add_fixed_in_frame_mobjects(bnm3)
        self.play(FadeIn(point3))
        self.play(ApplyMethod(point3.set_color, GRAY, opacity = 0.1, run_time = 0.5), MoveAlongPath(helix_dot, helix4, run_time=5), t_tracker.set_value,-1.3*np.pi/6, rate_func=linear, run_time=5)

        self.add_fixed_in_frame_mobjects(bnm4)
        self.play(FadeIn(point4))
        self.play(ApplyMethod(point4.set_color, GRAY, opacity = 0.1, run_time = 0.5), MoveAlongPath(helix_dot, helix5, run_time=5), t_tracker.set_value,0, rate_func=linear, run_time=5)

        self.add_fixed_in_frame_mobjects(bnm5)
        self.play(FadeIn(point5))
        self.wait(2)

        self.play(FadeOut(VGroup(*[valgroup, val2group, t_text, t_text2, c1, text, helix, bnm1, point0, point1, point2, point3, point4, point5, helix_dot])))
