from manimlib.imports import *
class sphere(GraphScene, ThreeDScene):
    CONFIG = {
    'x_min': 0,
    'x_max': 10,
    'y_min': -3,
    'y_max': 3,
    'graph_origin': ORIGIN,
    "x_axis_width": 10,
    "y_axis_height": 10,
    "default_graph_style": {
            "stroke_width": 2,
            "stroke_color": WHITE,
        }
    }
    def construct(self):
        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)

        text1 = TexMobject(r"y=\frac { 1 }{ x }").move_to(np.array([3,2,0]))
        text1a = TexMobject(r"y=\frac { 1 }{ x }, x \ge 1").move_to(np.array([3,2,0]))
        text2 = TexMobject(r"y=\frac { 1 }{ x }", r"\text{ is rotated in 3-dimensions}").to_corner(UL)
        text3 = TextMobject("For calculating volume, consider a disc as shown").to_corner(UL)
        text4 = TextMobject("Imagine the disc to move along the length of the horn").to_corner(UL)
        text5 = TextMobject("In this way complete volume is covered").to_corner(UL)
        arrow = Vector(np.array([0, np.sin(60*DEGREES), np.cos(60*DEGREES)])).shift(1*RIGHT)
        text6 = TexMobject(r"\text{Area of circle is }", r"\pi {r}^{2}").to_corner(UL)
        text7 = TextMobject("The disc moves along the length of hyperbolic curve").to_corner(UL)

        axes = ThreeDAxes(**self.CONFIG)
        self.setup_axes()
        graph1 = self.get_graph(lambda x : 1/x, x_min = 1, x_max = 10)
        graph2 = self.get_graph(lambda x : 1/x, x_min = 0.1, x_max = 10)
        self.play(FadeIn(self.axes))
        self.play(ShowCreation(graph2), FadeIn(text1))
        self.wait(3)
        self.play(Transform(graph2, graph1), ReplacementTransform(text1, text1a))
        axes = ThreeDAxes(**self.CONFIG)
        self.move_camera(phi = 90*DEGREES, theta=0*DEGREES,distance = 200, run_time=5)
        horn2 = ParametricSurface(lambda u, v : np.array([1*u, (1*np.cos(TAU*v))/u,(1*np.sin(TAU*v))/u]), u_min = 1, v_min = 0.001, u_max = 10, fill_opacity = 0.1)
        self.play(Transform(graph2, horn2), FadeOut(text1), FadeOut(graph2),  ShowCreation(text2), FadeOut(text1a))
        self.wait(2)
        self.play(FadeOut(text2))
        self.add_fixed_in_frame_mobjects(text3)
        self.wait(1)
        disc = ParametricSurface(lambda u, v : np.array([0, 1*v*np.sin(TAU*u), 1*v*np.cos(TAU*u)]), fill_opacity = 1, fill_color = PINK).shift(1*RIGHT)
        self.play(ShowCreation(disc), ShowCreation(arrow))
        self.play(FadeOut(text3))
        self.add_fixed_in_frame_mobjects(text6)
        self.wait(3)
        self.play(FadeOut(text6))
        self.add_fixed_in_frame_mobjects(text7)
        self.wait(2)
        self.move_camera(phi = 60*DEGREES, theta= -45*DEGREES, distance = 200, run_time=5)
        #self.play(FadeOut(text6))
        #self.add_fixed_in_frame_mobjects(text7)
        k=0
        while k<9:
            disc1 = ParametricSurface(lambda u, v : np.array([0, (1/(1+k))*v*np.sin(TAU*u), (1/(1+k))*v*np.cos(TAU*u)]), fill_opacity = 0.5, fill_color = PINK).shift((1+k)*RIGHT)
            self.play(FadeIn(disc1), run_time = 0.1)
            k = k+0.1
        self.play(FadeOut(text7))
        self.add_fixed_in_frame_mobjects(text5)
        self.wait(2)
        self.begin_ambient_camera_rotation(rate = 0.4)
        self.wait(10)
        self.stop_ambient_camera_rotation()