from manimlib.imports import *

class tangent(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi = 125*DEGREES, theta = 135*DEGREES)
        h = ParametricFunction(
            lambda t: np.array([
                4*(t**3) + 5,
                t**2 + 2*(t**4),
                -2*np.log(2*t)
            ]), t_min = -3, t_max = 1.18
        ).shift(5*LEFT)
        tgtR = Line((4,3,-2*np.log(2)), (19.5, 16, -4.772588), color=YELLOW)
        tgtL =Line((4,3,-2*np.log(2)), (-11.5, -10, 2), color=YELLOW)
        dot = Dot((4,3,-2*np.log(2)), color=RED, radius=0.2)
        self.play(FadeIn(axes),FadeIn(h), FadeIn(dot))
        self.begin_ambient_camera_rotation(rate=0.4)
        self.wait(2)
        self.play(FadeIn(tgtL), FadeIn(tgtR))
        self.wait(5)
        self.play(FadeOut(axes), FadeOut(h), FadeOut(dot), FadeOut(tgtL), FadeOut(tgtR))