from manimlib.imports import *

class helix_(ThreeDScene):
    CONFIG = {
    "x_min": -6,
    "x_max": 6,
    "y_min": -6,
    "y_max": 6,
    "graph_origin": ORIGIN
    }
    def construct(self):
        axes = ThreeDAxes()
        helix = ParametricFunction(
            lambda t: np.array([
                1.5*np.cos(TAU*t),
                1.5*np.sin(TAU*t),
                2*t
            ]), t_min = -1, t_max = 2, color = RED
        )
        cylinder = ParametricSurface(
        lambda u, v: np.array([
        1.5*np.cos(TAU*v),
        1.5*np.sin(TAU*v),
        2*u
        ]), u_min = -1, u_max = 2, fill_opacity = -.4, fill_color = WHITE, color = WHITE
        )
        self.set_camera_orientation(phi=60* DEGREES,theta=45*DEGREES)
        self.play(FadeIn(axes), FadeIn(cylinder), ShowCreation(helix, run_time = 4))
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(5)
        self.play(FadeOut(axes),FadeOut(helix), FadeOut(cylinder))
