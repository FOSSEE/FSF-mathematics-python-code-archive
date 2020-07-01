from manimlib.imports import *

class fs1(ThreeDScene):
    def construct(self):


        self.set_camera_orientation(phi = 75*DEGREES, theta=45*DEGREES)
        dot1 = Dot(np.array([np.cos(-np.pi/3), np.sin(-np.pi/3), -0.4*np.pi/3]) + np.array([0,0.2,0]), radius = 0.16, color=RED)
        tgt1 = Arrow((0,0,0), (-2,-0.55,0), color = YELLOW).shift(dot1.get_center() + np.array([0.18,0.04,0]))
        nm1 = Arrow((0,0,0), (0.4,-2,0), color = BLUE).shift(dot1.get_center() + np.array([0,0.26,0])).shift(np.array([0.8,4.76,0])).rotate(-15*DEGREES).scale(0.8)
        bnm1 = Arrow((0,0,0), (0,2,0), color=GREEN_E).shift(2.1*RIGHT+2*DOWN)

        bnms = Line((0,0,0), (0,0,1.6), color = GREEN_E).shift(np.array([3.1,5.2,0])).scale(0.6)
        bnmsa = ArrowTip(color = GREEN_E).next_to(bnms, np.array([0,0,1]), buff = 0).rotate(45*DEGREES)
        bns = VGroup(*[bnms, bnmsa])

        plane1 = Square(color = DARK_BROWN, fill_color = WHITE, fill_opacity=0.3).shift(dot1.get_center() + np.array([-0.4, -0.6, 0])).rotate(13*DEGREES).scale(1.2)
        point1 = VGroup(*[dot1, tgt1, plane1]).scale(0.8).shift(np.array([1,4.86,0])).rotate(-15*DEGREES)
        t = TextMobject(r'$T$', color = YELLOW).move_to(ORIGIN).shift(3.2*RIGHT + DOWN)
        n = TextMobject(r'$N$', color = BLUE).shift(DOWN + RIGHT)
        b = TextMobject(r'$B$', color = GREEN_E).next_to(bnm1, UP, buff = 0.1)
        text = VGroup(*[t, n, b])
        self.add_fixed_in_frame_mobjects(bnm1, text)
        self.play(FadeIn(point1), FadeIn(text), FadeIn(bnm1))
        self.wait()
        self.play(TransformFromCopy(bnms, nm1, run_time = 3))
        self.wait(2)
        self.play(FadeOut(VGroup(*[bnms, text, point1, nm1, bnm1])))
