from manimlib.imports import *

class brachistochrone(Scene):
    def construct(self):
        curve = ParametricFunction(
        lambda t: np.array([
        0.5*(t - np.sin(t)),
        0.5*(1 - np.cos(t)),
        0
        ]), t_max = np.pi
        ).scale(5).rotate(540*DEGREES)
        dot = Dot(color = RED, radius = 0.2)
        self.play(FadeIn(curve), MoveAlongPath(dot, curve, run_time = 2))
