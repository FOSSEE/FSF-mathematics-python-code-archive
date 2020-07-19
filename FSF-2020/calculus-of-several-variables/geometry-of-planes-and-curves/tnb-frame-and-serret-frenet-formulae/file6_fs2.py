from manimlib.imports import *

class fs2(SpecialThreeDScene):
    CONFIG = {
        "x_min": -2,
        "x_max": 2,
        "y_min": -6,
        "y_max": 6,
        "graph_origin": ORIGIN
    }
    def construct(self):
        axes = ThreeDAxes()
        # text = TextMobject(r'$\frac{dB}{ds} = -\tau N$ \\ $\frac{dB}{ds}$ gives the direction of N, \\ while $\tau$ gives its magnitude.').scale(0.7).shift(3*UP + 3*LEFT)
        self.set_camera_orientation(phi = 75*DEGREES, theta=135*DEGREES)
        # self.move_camera(distance=0)

        # rprime = np.array([2*np.cos(t), -np.sin(t) - (2*np.sin(2*t)), 0])
        # t = rprime / np.sqrt(np.dot(rprime, rprime))
        # rpp = np.array([-2*np.sin(t), -np.cos(t) - (4*np.cos(2*t)), 0])
        # n = rpp / np.dot(rpp, rpp)
        # b = np.cross(rprime, rpp)
        text = TextMobject(r'$\frac{dB}{ds}$', r'$= -\tau$', r'$N$').shift(2*UP + 4*LEFT)
        text.set_color_by_tex_to_color_map({
        r'$\frac{dB}{ds}$': YELLOW,
        r'$N$': RED_C
        })

        dot = Dot().rotate(PI/2)
        alpha = ValueTracker(0)
        t = alpha.get_value
        figure = ParametricFunction(
            lambda t: np.array([
                np.sinh(t),
                np.cosh(t),
                2*t
                ]), t_min = -3, t_max = 3, color=BLUE
            ).scale(0.5).move_to(ORIGIN)
        vector_x = self.get_tangent_vector(t()%1, figure,scale=2)
        vector_y = self.get_normal_vector(t(),figure,scale=2)
        vector_x.add_updater(
            lambda m: m.become(
                    self.get_tangent_vector(t()%1,figure,scale=2)
                )
            )
        vector_y.add_updater(
            lambda m: m.become(
                    self.get_normal_vector(t(),figure,scale=2)
                )
            )
        dot.add_updater(lambda m: m.move_to(vector_y.get_start()))



        self.add_fixed_in_frame_mobjects(text)
        self.play(FadeIn(figure), FadeIn(axes), FadeIn(text))
        self.begin_ambient_camera_rotation(rate = 0.1)
        self.wait(1)
        self.add(vector_x, vector_y,dot)
        self.play(alpha.increment_value, 0.999, run_time=20, rate_func=rush_from)
        self.wait(1)
        self.remove(figure, vector_x, vector_y,dot)
        self.play(FadeOut(figure), FadeOut(axes), FadeOut(text))

    def get_tangent_vector(self, proportion, curve, dx=0.001, scale=1):
        t = proportion.copy()
        coord_i = curve.point_from_proportion(proportion)
        rprime = np.array([np.cosh(t), np.sinh(t), 2])
        T = rprime / np.sqrt(np.dot(rprime, rprime))
        rpp = np.array([np.sinh(t), np.cosh(t), 0])
        n = rpp / np.dot(rpp, rpp)
        # b = (np.cross(T, n)[0] - 0.5, np.cross(T, n)[1], coord_i[2] + 1)
        b = np.cross(T, n)
        # coord_f = curve.point_from_proportion(proportion + dx)
        coord_f = b
        reference_line = Line(coord_i,coord_f)
        unit_vector = reference_line.get_unit_vector() * 1
        vector = Arrow(coord_i , coord_i + unit_vector, color = YELLOW, buff=0)
        return vector

    def get_normal_vector(self, proportion, curve, dx=0.001, scale=1):
        coord_i = curve.point_from_proportion(proportion)
        coord_f = curve.point_from_proportion(proportion + dx)
        t = proportion.copy()/7
        rpp = np.array([np.sinh(t), np.cosh(t), 0])
        length = np.sqrt(np.dot(rpp, rpp))
        length = 1/(1 + np.exp(-length))
        reference_line = Line(coord_i,coord_f).rotate(PI/2).set_width(length).scale(2)
        unit_vector = reference_line.get_vector() * 0.7
        vector = Arrow(coord_i, coord_i + unit_vector, color = RED_C, buff=0)
        return vector
