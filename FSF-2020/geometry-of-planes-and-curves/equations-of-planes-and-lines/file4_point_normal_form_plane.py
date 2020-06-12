from manimlib.imports import *

class pointnormal(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        self.set_camera_orientation(phi = 75*DEGREES, theta=45*DEGREES)
        normal = Arrow((0,-0.15,-0.25), (-3,0,3), color = YELLOW)
        plane1 = Polygon(np.array([1,0,2]),np.array([-1,2.5,1]),np.array([-3,2,1]),np.array([-1,-1,2]), color = GREEN_E, fill_color = WHITE, fill_opacity=0.5)
        plane2 = Polygon(np.array([1,0,2]),np.array([-1,2.5,1]),np.array([-3,2,1]),np.array([-1,-1,2]), color = BLUE, fill_color = WHITE, fill_opacity=0.3)
        normalLabel = TextMobject(r'$\overrightarrow{n}$').shift((2,2.5,0))
        pointLabel = TextMobject(r'$P$').shift((2,1.2,0))
        xlabel = TextMobject(r'$x$').shift(4.5*LEFT + 1.7*DOWN)
        ylabel = TextMobject(r'$y$').shift(4.5*RIGHT + 1.8*DOWN)
        zlabel = TextMobject(r'$z$').shift(3.3*UP+0.5*RIGHT)

        planetext = TextMobject(r'A single vector is normal \\ to infinitely many planes.').scale(0.6).shift(2*UP + 2.5*LEFT)
        pointtext = TextMobject(r'Given a fixed point $P$, \\ a plane is obtained as:').scale(0.6).shift(2*UP + 2.5*LEFT)

        point = Dot(color = RED).shift((1.6,1.3,0))
        self.play(FadeIn(axes))
        self.add_fixed_in_frame_mobjects(xlabel, ylabel, zlabel)
        self.wait(1)
        self.play(FadeIn(normal))
        self.add_fixed_in_frame_mobjects(normalLabel)
        self.wait(2)
        self.add_fixed_in_frame_mobjects(planetext)
        self.play(FadeIn(planetext))
        self.play(MoveAlongPath(plane1, normal), run_time = 6)
        self.add_fixed_in_frame_mobjects(pointtext)
        self.play(ReplacementTransform(planetext, pointtext))
        self.add_fixed_in_frame_mobjects(point, pointLabel)
        self.wait(1)
        self.play(Transform(plane1, plane2))
        self.wait(2)
        self.play(FadeOut(axes), FadeOut(plane2), FadeOut(plane1), FadeOut(point), FadeOut(pointLabel), FadeOut(normal), FadeOut(normalLabel), FadeOut(planetext), FadeOut(pointtext), FadeOut(VGroup(*[xlabel, ylabel, zlabel])))
        self.wait(1)
