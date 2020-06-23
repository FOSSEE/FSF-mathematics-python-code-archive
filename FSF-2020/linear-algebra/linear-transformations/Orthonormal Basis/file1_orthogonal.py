from manimlib.imports import *

class Orthogonal(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.play(ShowCreation(axes))
        self.move_camera(phi=30*DEGREES,theta=-45*DEGREES,run_time=3)
        line1 = Line(start = ORIGIN,end = -3*LEFT)
        line1.set_color(DARK_BLUE)
        tip1 = Polygon(-LEFT,-0.8*LEFT-0.2*DOWN,-0.8*LEFT-0.2*UP)
        tip1.move_to(-3*LEFT)
        tip1.set_opacity(1)
        tip1.set_fill(DARK_BLUE)
        tip1.set_color(DARK_BLUE)

        arrow2 = Line(start = ORIGIN,end = -3*UP)
        arrow2.set_color(DARK_BLUE)
        tip2 = Polygon(DOWN,0.8*DOWN-0.2*RIGHT,0.8*DOWN-0.2*LEFT)
        tip2.move_to(3*DOWN)
        tip2.set_opacity(1)
        tip2.set_fill(DARK_BLUE)
        tip2.set_color(DARK_BLUE)
        arrow2.set_color(DARK_BLUE)

        arrow3 = Line(start = ORIGIN,end = [0,0,3])
        arrow3.set_color(DARK_BLUE)
        tip3 = Polygon([0,0,3],[0,0,2.8]-0.2*RIGHT,[0,0,2.8]-0.2*LEFT)
        tip3.set_opacity(1)
        tip3.set_fill(DARK_BLUE)
        tip3.set_color(DARK_BLUE)

        self.play(ShowCreation(line1), ShowCreation(tip1), ShowCreation(arrow2), ShowCreation(tip2), ShowCreation(arrow3), ShowCreation(tip3))
        
        self.wait()