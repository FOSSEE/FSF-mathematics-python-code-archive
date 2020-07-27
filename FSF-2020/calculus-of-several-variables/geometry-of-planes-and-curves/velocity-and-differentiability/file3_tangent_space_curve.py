from manimlib.imports import *

class tangent(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        text = TextMobject(r'Tangent', r' to the ', 'space curve', r' \\ at point ', r'$P_{1}$', ' is given by:').scale(0.7).shift(3*UP + 3.5*LEFT)
        text.set_color_by_tex_to_color_map({
            "Tangent": YELLOW,
            '$P_{1}$': RED,
            'space curve': BLUE
        })
        text.bg=BackgroundRectangle(text,fill_opacity=1, color = BLACK)
        text_gr =VGroup(text.bg,text)
        self.set_camera_orientation(phi = 125*DEGREES, theta = 135*DEGREES)
        h = ParametricFunction(
            lambda t: np.array([
                4*(t**3) + 5,
                t**2 + 2*(t**4),
                -2*np.log(2*t)
            ]), t_min = -3, t_max = 1.18, color = BLUE
        ).shift(5*LEFT)
        tgtR = Line((4,3,-2*np.log(2)), (19.5, 16, -4.772588), color=YELLOW)
        tgtL =Line((4,3,-2*np.log(2)), (-11.5, -10, 2), color=YELLOW)
        dot = Dot((4,3,-2*np.log(2)), color=RED, radius=0.08)
        dotl = TextMobject(r'$P_{1}$', color = RED).scale(0.7).shift(2*DOWN + 5*LEFT)
        self.add_fixed_in_frame_mobjects(text_gr, dotl)
        self.play(FadeIn(axes),FadeIn(h), FadeIn(dot), FadeIn(dotl))
        self.wait(2)
        self.play(FadeIn(tgtL), FadeIn(tgtR))
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(FadeOut(dotl))
        self.wait(5)
        self.play(FadeOut(axes), FadeOut(h), FadeOut(text_gr), FadeOut(dot), FadeOut(tgtL), FadeOut(tgtR))
