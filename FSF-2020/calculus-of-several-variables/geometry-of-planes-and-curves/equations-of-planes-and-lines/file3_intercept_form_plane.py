from manimlib.imports import *

class pointnormal(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_min = 0, y_min = 0, z_min = 0)
        self.set_camera_orientation(phi = 75*DEGREES, theta=45*DEGREES)

        plane1 = Polygon(np.array([2,-3,2.5]),np.array([-1.45,2,2.5]),np.array([-0.5,4.5,-0.1]),np.array([3.5,-1,-0.2]), fill_color = WHITE, fill_opacity=0.3)

        xlabel = TextMobject(r'$x$').shift(5*LEFT + 1.5*DOWN)
        ylabel = TextMobject(r'$y$').shift(5*RIGHT + 1.5*DOWN)
        zlabel = TextMobject(r'$z$').shift(3.3*UP + 0.5*LEFT)

        zintercept = Dot().shift(2.5*UP)
        zinterceptlabel = TextMobject(r'$(0,0,c\prime)$').shift(2.8*UP + RIGHT).scale(0.7)

        yintercept = Dot().shift(3.7*RIGHT + 0.925*DOWN)
        yinterceptlabel = TextMobject(r'$(0,b\prime ,0)$').shift(3.7*RIGHT+1.5*DOWN).scale(0.7)

        xintercept = Dot().shift(2.9*LEFT + 0.75*DOWN)
        xinterceptlabel = TextMobject(r'$(a\prime ,0,0)$').shift(3*LEFT+1.3*DOWN).scale(0.7)

        self.play(FadeIn(axes), FadeIn(plane1))
        self.add_fixed_in_frame_mobjects(xlabel, ylabel, zlabel, zintercept, zinterceptlabel, yintercept, yinterceptlabel, xintercept, xinterceptlabel)
        self.wait(2)
        self.remove(zintercept, zinterceptlabel, yintercept, yinterceptlabel, xintercept, xinterceptlabel, xlabel, ylabel, zlabel)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(5)
        self.play(FadeOut(axes), FadeOut(plane1))
