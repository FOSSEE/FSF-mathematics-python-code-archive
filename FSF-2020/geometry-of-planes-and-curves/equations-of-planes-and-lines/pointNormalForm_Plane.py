from manimlib.imports import *

class pointnormal(ThreeDScene):
    CONFIG = {
        'x_axis_label': '$x$',
        'y_axis_label': '$y$'
    }
    def construct(self):
        axes = ThreeDAxes()
        axes.add(axes.get_axis_labels())
        self.set_camera_orientation(phi = 75*DEGREES, theta=45*DEGREES)
        normal = Arrow((-2,0,1), (-3,0,2))
        plane1 = Polygon(np.array([1,0,2]),np.array([-1,2.5,1]),np.array([-3,2,1]),np.array([-1,-1,2]))
        plane2 = Polygon(np.array([1,0,2]),np.array([-1,2.5,1]),np.array([-3,2,1]),np.array([-1,-1,2])).shift(2.5*RIGHT+1.1*UP).scale(0.85)
        plane3 = Polygon(np.array([1,0,2]),np.array([-1,2.5,1]),np.array([-3,2,1]),np.array([-1,-1,2])).shift(4.5*RIGHT+1.9*UP).scale(0.75)
        normalLabel = TextMobject(r'$\overrightarrow{n}$').shift((2,2.5,0))
        pointLabel = TextMobject(r'$P$').shift((2,1.2,0))
        point = Dot(color = RED).shift((1.6,1.3,0))
        self.play(FadeIn(axes))
        self.wait(1)
        self.play(FadeIn(plane1))
        self.wait(1)
        self.play(FadeIn(normal))
        self.add_fixed_in_frame_mobjects(normalLabel)    
        self.wait(2)
        self.play(FadeIn(plane2))
        self.wait(2)
        self.play(FadeIn(plane3))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(point, pointLabel)
        self.wait(1)
        self.play(FadeOut(plane2), FadeOut(plane3))
        self.wait(2)
        self.play(FadeOut(axes), FadeOut(plane1), FadeOut(point), FadeOut(pointLabel), FadeOut(normal), FadeOut(normalLabel))
