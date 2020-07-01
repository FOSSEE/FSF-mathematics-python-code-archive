from manimlib.imports import *

class tnb(ThreeDScene):
    def construct(self):
        t = TextMobject(r'T', color = YELLOW)
        n = TextMobject(r'N', color = BLUE).next_to(t, RIGHT, buff=0)
        b = TextMobject(r'B', color = GREEN_E).next_to(n, RIGHT, buff=0)
        frame = TextMobject(r'Frame').next_to(b, RIGHT, buff=0.2)
        f1 = TextMobject(r'$\overrightarrow{B}$ ', color = GREEN_E)
        f2 = TextMobject(r' = $\overrightarrow{T}$', color = YELLOW).next_to(f1, RIGHT, buff=0.2)
        f3 = TextMobject(r'$\times\overrightarrow{N}$', color = BLUE).next_to(f2, RIGHT, buff=0.1)
        formula = VGroup(*[f1, f2, f3]).move_to(ORIGIN).shift(3*UP)

        # text = VGroup(*[t,n,b,frame]).move_to(ORIGIN).shift(3*UP)
        curve = ParametricFunction(
        lambda t: np.array([
        np.sin(TAU*t),
        np.cos(TAU*t),
        0
        ])
        ).scale(2.5)
        dot = Dot(color = RED).scale(1.5).shift(1.05*LEFT)
        tgt = Arrow(dot.get_center(), (-2, 2, 0), color = YELLOW).shift(0.3*DOWN + 0.09*RIGHT)
        normal = Arrow(tgt.get_start(), (1, 1, 0), color = BLUE).shift(0.2*LEFT + 0.05*DOWN)
        binormal = Arrow(dot.get_center() - np.array([0,0,0.3]), (tgt.get_start()[0], tgt.get_start()[1],2), color = GREEN)
        square = Square(color = DARK_BROWN, fill_color = WHITE, fill_opacity=0.3).move_to(tgt.get_start()).rotate(27*DEGREES).shift(UP+0.4*RIGHT).scale(1.2)
        group = VGroup(*[dot, tgt, normal, square, binormal]).shift(np.array([-1.24,-1,0]))

        self.add_fixed_in_frame_mobjects(formula)
        self.add(curve, group)
        self.wait(1)
        self.move_camera(phi = 75*DEGREES, theta=45*DEGREES, run_time = 2)
        self.add_fixed_in_frame_mobjects(formula)
        self.begin_ambient_camera_rotation(rate = 0.5)
        self.wait(5)
        self.play(FadeOut(VGroup(*[formula, curve, dot, tgt, normal, square, binormal])))
