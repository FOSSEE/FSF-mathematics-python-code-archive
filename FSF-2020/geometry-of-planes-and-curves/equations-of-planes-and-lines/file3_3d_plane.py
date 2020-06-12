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

        plane = Polygon(
            np.array([2,0,2.7]),
            np.array([0,0,0.4]),
            np.array([-3.2,0,0.55]),
            np.array([-3,-2,2.5]), 
            fill_color = WHITE, fill_opacity = 0.25)

        normal = Arrow((0.25,2,0), (1.5,3.5,0))
        normalLabel = TextMobject(r'$\overrightarrow{n}$').shift((1.5,2.8,0))

        point = Dot(color = RED).shift((1.6,1.3,0))
        pointLabel = TextMobject(r'$P_{0}$').shift((2,1.2,0))

        point2 = Dot(color = RED).shift((-0.2,1.8,0))
        point2Label = TextMobject(r'$P$').shift((-0.3,2,0))
        
        arrow1 = Arrow((0,-0.25,-0.2), (-2.55,0,1), color = YELLOW).set_stroke(width=3)
        arrow2 = Arrow((0,0,-0.25), (0.3,0,2), color = YELLOW).set_stroke(width=3)
        res = Arrow((1.8,1.23,0),(-0.35,1.85,0), color = BLUE).set_stroke(width=3)

        arrow1label = TextMobject(r'$\overrightarrow{r_{0}}$').next_to(arrow2, UP).shift(RIGHT + 0.16*DOWN).scale(0.7)
        arrow2label = TextMobject(r'$\overrightarrow{r}$').next_to(arrow2, UP).shift(0.7*LEFT).scale(0.7)
        reslabel = TextMobject(r'$\overrightarrow{r} - \overrightarrow{r_{0}}$').next_to(arrow2, UP).shift(0.7*RIGHT + 1.2*UP).scale(0.7)
        
        self.play(FadeIn(axes), FadeIn(plane))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(normal, normalLabel)    
        self.wait(1)
        self.add_fixed_in_frame_mobjects(point, pointLabel)
        self.add_fixed_in_frame_mobjects(point2, point2Label)
        self.play(Write(arrow1), Write(arrow2))
        self.add_fixed_in_frame_mobjects(arrow2label, arrow1label)
        self.wait(1)
        self.add_fixed_in_frame_mobjects(res, reslabel)
        self.play(Write(res), FadeIn(reslabel))
        self.wait(1)
        self.play(FadeOut(axes), FadeOut(plane), FadeOut(point), FadeOut(pointLabel), FadeOut(normal), FadeOut(normalLabel), FadeOut(point2), FadeOut(point2Label), FadeOut(arrow1label), FadeOut(arrow2label), FadeOut(reslabel), FadeOut(arrow1), FadeOut(arrow2), FadeOut(res))