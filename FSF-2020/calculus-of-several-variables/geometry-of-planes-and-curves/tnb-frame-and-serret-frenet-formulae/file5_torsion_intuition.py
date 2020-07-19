from manimlib.imports import *

class t(SpecialThreeDScene):
    CONFIG = {
         "axes_config": {
            "x_min": -5,
            "x_max": 5,
            "y_min": -5,
            "y_max": 5,
            "z_min": -4,
            "z_max": 4,
            "x_axis_config": {
                "tick_frequency": 100,
            },
            "y_axis_config": {
                "tick_frequency": 100,
            },
            "z_axis_config": {
                "tick_frequency": 100,
            },
            "num_axis_pieces": 1,
        }
    }
    def construct(self):

        text = TextMobject(r'Torsion can be intuitively \\ thought of as the measure \\ of "twisting" of a curve.').scale(0.7).shift(2.5*UP + 4.2*LEFT)


        dot = Dot().rotate(PI/2)
        f1 = ParametricFunction(
            lambda t: np.array([
                2*np.sin(TAU*t),
                2*np.cos(TAU*t),
                2*t
                ]), t_min = -2, t_max = 2, color = BLUE
            ).scale(0.5)
        d1 = Dot(color = RED).next_to(f1.get_center(), 2*DOWN + LEFT, buff = 0).shift(1.2*UP + 2.4*RIGHT)
        t1 = self.get_torsion(2, 0.174)
        t1 = "{:.2f}".format(t1)
        t1 = TextMobject(fr'At the given point, $\tau = {t1}$').shift(3.5*DOWN).scale(0.7)

        f2 = ParametricFunction(
            lambda t: np.array([
                3*np.sin(TAU*t),
                3*np.cos(TAU*t),
                2*t
                ]), t_min = -2, t_max = 2, color = BLUE
            ).scale(0.5)
        d2 = Dot(color = RED).next_to(f2.get_center(), 2*DOWN + LEFT, buff = 0).shift(1.2*UP + 2.95*RIGHT)
        t2 = self.get_torsion(3, 0.1765)
        t2 = "{:.2f}".format(t2)
        t2 = TextMobject(fr'At the given point, $\tau = {t2}$').shift(3.5*DOWN).scale(0.7)

        f3 = ParametricFunction(
            lambda t: np.array([
                4*np.sin(TAU*t),
                4*np.cos(TAU*t),
                2*t
                ]), t_min = -2, t_max = 2, color = BLUE
            ).scale(0.5)
        d3 = Dot(color = RED).next_to(f3.get_center(), 2*DOWN + LEFT, buff = 0).shift(1.2*UP + 3.45*RIGHT)
        t3 = self.get_torsion(4, 0.179)
        t3 = "{:.2f}".format(t3)
        t3 = TextMobject(fr'At the given point, $\tau = {t3}$').shift(3.5*DOWN).scale(0.7)

        f4 = ParametricFunction(
            lambda t: np.array([
                1.5*np.sin(TAU*t),
                1.5*np.cos(TAU*t),
                2*t
                ]), t_min = -2, t_max = 2, color = BLUE
            ).scale(0.5)
        d4 = Dot(color = RED).next_to(f4.get_center(), 2*DOWN + LEFT, buff = 0).shift(1.215*UP + 2.128*RIGHT)
        t4 = self.get_torsion(1.5, 0.173)
        t4 = "{:.2f}".format(t4)
        t4 = TextMobject(fr'At the given point, $\tau = {t4}$').shift(3.5*DOWN).scale(0.7)

        f5 = ParametricFunction(
            lambda t: np.array([
                np.sin(TAU*t),
                np.cos(TAU*t),
                2*t
                ]), t_min = -2, t_max = 2, color = BLUE
            ).scale(0.5)

        d5 = Dot(color = RED).next_to(f5.get_center(), 2*DOWN + LEFT, buff = 0).shift(1.3*UP + 1.858*RIGHT)
        t5 = self.get_torsion(1, 0.17)
        t5 = "{:.2f}".format(t5)
        t5 = TextMobject(fr'At the given point, $\tau = {t5}$').shift(3.5*DOWN).scale(0.7)

        axes = ThreeDAxes(**self.axes_config)
        self.set_camera_orientation(phi = 60*DEGREES, theta=45*DEGREES)
        self.add_fixed_in_frame_mobjects(t1, text)
        self.play(FadeIn(VGroup(*[f1, d1, t1, axes, text])))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(t2)
        self.play(ReplacementTransform(d1, d2), ReplacementTransform(f1, f2), ReplacementTransform(t1, t2))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(t3)
        self.play(ReplacementTransform(d2, d3), ReplacementTransform(f2, f3), ReplacementTransform(t2, t3))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(t4)
        self.play(ReplacementTransform(d3, d4), ReplacementTransform(f3, f4), ReplacementTransform(t3, t4))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(t5)
        self.play(ReplacementTransform(d4, d5), ReplacementTransform(f4, f5), ReplacementTransform(t4, t5))
        self.wait(2)
        self.play(FadeOut(VGroup(*[d5, f5, t5, text, axes])))

    def get_torsion(self, a, t):
        rprime = np.array([a*np.cos(t), -a*np.sin(t), 2])
        T = rprime / np.sqrt(np.dot(rprime, rprime))
        rpp = np.array([-a*np.sin(t), -a*np.cos(t), 0])
        n = rpp / np.dot(rpp, rpp)
        b = np.cross(T, n)
        dbdt = np.array([-2*np.sin(t), -2*np.cos(t), 0])
        tor = np.dot(dbdt, n)

        return tor
