from manimlib.imports import *

class line_(ThreeDScene):
    CONFIG = {
        'x_axis_label': '$x$',
        'y_axis_label': '$y$'
    }
    def construct(self):
        axes = ThreeDAxes()
        axes.add(axes.get_axis_labels())
        self.set_camera_orientation(phi = 75*DEGREES, theta=45*DEGREES)
        pointLabel = TextMobject(r'$P$').shift((2.28,2.12,0)).scale(0.7)
        point = Dot(color = RED).shift((1.95,1.9,0))
        line1 = Line((-3,0,0.5), (-3,0,3))
        line2 = Line((-1.56,0,0.5),(-4,0,2.42))
        line3 = Line((-1,0,1.6),(-5,0,1.6))
        line4 = Line((-1.53,0,2.5),(-4.7,0,0.5))
        lines = VGroup(*[line1, line2, line3, line4])
        self.play(FadeIn(axes))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(point, pointLabel)
        self.wait(1)
        self.play(FadeIn(lines))
        self.wait(2)
        finalLine = Line((-1.56,0,0.5),(-4,0,2.42), color = YELLOW)
        self.play(FadeIn(finalLine))
        self.wait(1)
        self.play(FadeOut(lines))
        self.wait(1.5)
        self.play(FadeOut(axes),FadeOut(point), FadeOut(pointLabel), FadeOut(finalLine))
