from manimlib.imports import *

class Orthogonal(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.play(ShowCreation(axes))
        self.move_camera(phi=60*DEGREES,theta=45*DEGREES,run_time=3)

        text = TextMobject(r"$\hat{i}$",r"$\hat{j}$",r"$\hat{k}$")
        text[0].move_to(0.7*DOWN+0.8*LEFT)
        text[1].move_to(0.75*DOWN+0.7*RIGHT)
        text[2].move_to(0.75*UP+0.4*RIGHT)
        self.add_fixed_in_frame_mobjects(text)
        self.play(Write(text))

        line1 = Line(start = ORIGIN,end = RIGHT)
        line1.set_color(DARK_BLUE)
        tip1 = Polygon(-0.95*LEFT,-0.8*LEFT-0.1*DOWN,-0.8*LEFT-0.1*UP)
        tip1.set_opacity(1)
        tip1.set_fill(DARK_BLUE)
        tip1.set_color(DARK_BLUE)

        arrow2 = Line(start = ORIGIN,end = UP)
        arrow2.set_color(DARK_BLUE)
        tip2 = Polygon(0.95*UP,0.8*UP-0.1*RIGHT,0.8*UP-0.1*LEFT)
        tip2.set_opacity(1)
        tip2.set_fill(DARK_BLUE)
        tip2.set_color(DARK_BLUE)
        arrow2.set_color(DARK_BLUE)

        arrow3 = Line(start = ORIGIN,end = [0,0,1])
        arrow3.set_color(DARK_BLUE)
        tip3 = Polygon([0,0,0.95],[0,0,0.8]-0.1*RIGHT,[0,0,0.8]-0.1*LEFT)
        tip3.set_opacity(1)
        tip3.set_fill(DARK_BLUE)
        tip3.set_color(DARK_BLUE)

        self.play(ShowCreation(line1), ShowCreation(tip1), ShowCreation(arrow2), ShowCreation(tip2), ShowCreation(arrow3), ShowCreation(tip3))
        
        self.wait()
