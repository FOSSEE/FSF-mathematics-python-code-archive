from manimlib.imports import *

class cone(ThreeDScene):
    CONFIG = {
    "x_axis_label": "$x$",
    "y_axis_label": "$y$",
    "z_axis_label": "$z$"
    }
    def construct(self):
        axes = ThreeDAxes()
        axes.add(axes.get_axis_labels())
        eqn = TextMobject(r'$z^{2} = x^{2} + y^{2}$')

        conecurve = ParametricFunction(
            lambda t: np.array([
                t*np.cos(TAU*t),
                t*np.sin(TAU*t),
                t
            ]), t_min = -3, t_max = 3
        )

        coneup = ParametricSurface(
            lambda u,v: np.array([
                3*np.sin(u)*np.cos(TAU*v),
                3*np.sin(u)*np.sin(TAU*v),
                3*u
            ])
        )

        conedown = ParametricSurface(
            lambda u,v: np.array([
                3*np.sin(u)*np.cos(TAU*v),
                3*np.sin(u)*np.sin(TAU*v),
               -3*u
            ])
        )
        self.play(FadeIn(eqn))
        self.wait(2)
        self.play(FadeOut(eqn))
        self.set_camera_orientation(phi = 70*DEGREES, theta=65*DEGREES)
        self.play(FadeIn(axes), DrawBorderThenFill(conecurve, run_time = 3))
        self.play(FadeOut(conecurve), FadeIn(coneup), FadeIn(conedown))
        self.begin_ambient_camera_rotation(rate=0.03)
        self.wait(2)
        self.play(FadeOut(axes), FadeOut(coneup), FadeOut(conedown))
        self.wait(2)