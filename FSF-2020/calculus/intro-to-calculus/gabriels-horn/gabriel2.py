from manimlib.imports import *
class surface(GraphScene, ThreeDScene):
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
            "stroke_color": RED,
        }
    }
    def construct(self):
        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)

        self.setup_axes()
        text1 = TexMobject(r"y=\frac { 1 }{ x }").move_to(np.array([3,2,0]))
        text2 = TexMobject(r"\int _{ 1 }^{ \infty  }{ \frac { 1 }{ x } dx }", r"\text{ diverges}").to_corner(UL)
        text3 = TexMobject(r"\text{Hence }", r"\int _{ 1 }^{ \infty  }{ \frac { 1 }{ x } dx=\infty }").to_corner(UL)
        text4 = TextMobject("Which means surface area is infinity").to_corner(UL)
        graph1 = self.get_graph(lambda x : 1/x, x_min = 1, x_max = 10)
        self.play(FadeIn(self.axes))
        self.play(ShowCreation(graph1), FadeIn(text1))
        self.wait(5)
        axes = ThreeDAxes(**self.CONFIG)
        self.move_camera(phi = 60*DEGREES, theta=45*DEGREES,distance = 200, run_time=5)
        horn2 = ParametricSurface(lambda u, v : np.array([1*u, (1*np.cos(TAU*v))/u,(1*np.sin(TAU*v))/u]), u_min = 1, v_min = 0.001, u_max = 10, fill_opacity = 0.1)
        horn3 = ParametricSurface(lambda u, v : np.array([1*u, (1*np.cos(TAU*v))/u,(1*np.sin(TAU*v))/u]), u_min = 1, v_min = 0.001, u_max = 10, fill_opacity = 1)
        self.play(Transform(graph1, horn2))
        self.play(FadeOut(text1))
        self.add_fixed_in_frame_mobjects(text2)
        self.wait(3)
        self.play(FadeOut(text2))
        self.add_fixed_in_frame_mobjects(text3)
        self.wait(3)
        self.play(ShowCreation(horn3))
        self.play(FadeOut(text3))
        self.add_fixed_in_frame_mobjects(text4)
        self.wait(5)