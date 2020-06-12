from manimlib.imports import *

class cone(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        eqn = TextMobject(r'$z^{2} = x^{2} + y^{2}$')

        conecurve = ParametricFunction(
            lambda t: np.array([
                t*np.cos(TAU*t),
                t*np.sin(TAU*t),
                t
            ]), t_min = -2.6, t_max = 2.6
        ).scale(0.85)

        conesurface = ParametricSurface(
            lambda u,v: np.array([
                3*np.sin(u)*np.cos(TAU*v),
                3*np.sin(u)*np.sin(TAU*v),
                2.7*u
            ]), u_min = -1
        ).scale(0.85)

        self.play(FadeIn(eqn))
        self.wait(2)
        self.play(FadeOut(eqn))
        self.set_camera_orientation(phi = 75*DEGREES, theta=50*DEGREES)
        self.play(FadeIn(axes), ShowCreation(conecurve, run_time = 3))
        self.play(FadeOut(conecurve), FadeIn(conesurface))
        self.begin_ambient_camera_rotation(rate=0.03)
        self.wait(2)
        self.play(FadeOut(axes), FadeOut(conesurface))
        self.wait(2)
