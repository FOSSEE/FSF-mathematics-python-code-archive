from manimlib.imports import *

class line_(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        xlabel = TextMobject(r'$x$').shift(4.5*LEFT + 1.7*DOWN)
        ylabel = TextMobject(r'$y$').shift(4.5*RIGHT + 1.8*DOWN)
        zlabel = TextMobject(r'$z$').shift(3.3*UP+0.5*RIGHT)

        self.set_camera_orientation(phi = 75*DEGREES, theta=45*DEGREES)
        pointLabel = TextMobject(r'$P$').shift((2.28,2.12,0)).scale(0.7)
        point = Dot(color = RED).shift((1.95,1.9,0))

        vlabel = TextMobject(r'$\overrightarrow{v}$').shift((0.5,1.3,0)).scale(0.7)

        inf_text = TextMobject(r'Infinitely many lines pass \\ through a single point.').scale(0.6).shift(2*UP + 2.5*LEFT)
        pointtext = TextMobject(r'Given a direction vector $\overrightarrow{v}$, \\ a line is obtained as:').scale(0.6).shift(2*UP + 2.5*LEFT)


        line = Line((0.7,0.7,0), (2,3,0)).shift(0.06*UP+0.6*RIGHT)
        v = Vector((0.8,1,0), color = GREEN_E)
        #finalLine = Line((-1.56,0,0.5),(-4,0,2.42), color = YELLOW)
        finalLine = Line((1,0.8,0),(3,3,0), color = YELLOW).shift(0.05*LEFT)
        self.play(FadeIn(axes))
        self.add_fixed_in_frame_mobjects(zlabel, ylabel, xlabel)
        self.wait(1)
        self.add_fixed_in_frame_mobjects(point, pointLabel)
        self.wait(1)
        self.add_fixed_in_frame_mobjects(inf_text)
        self.wait(1)
        self.add_fixed_in_frame_mobjects(line)

        for i in range(9):
            self.play(ApplyMethod(line.rotate, -np.pi/12), run_time = 0.7)
            if i == 8:
                self.add_fixed_in_frame_mobjects(pointtext)
                self.play(ReplacementTransform(inf_text, pointtext))
                self.add_fixed_in_frame_mobjects(v, vlabel)
            # if i == 13:
            #     self.add_fixed_in_frame_mobjects(pointtext)

        self.add_fixed_in_frame_mobjects(finalLine)
        self.play(FadeIn(finalLine))
        self.play(Transform(line, finalLine), run_time = 4)
        #self.play(FadeOut(line), FadeIn(finalLine))
        self.wait(1.5)
        self.play(FadeOut(VGroup(*[axes, xlabel, ylabel, zlabel, finalLine, v, vlabel, point, pointLabel, pointtext, line])))
