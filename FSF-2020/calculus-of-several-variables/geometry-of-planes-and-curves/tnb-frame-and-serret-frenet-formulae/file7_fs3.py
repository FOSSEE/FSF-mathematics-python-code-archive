from manimlib.imports import *

class f(SpecialThreeDScene):
    CONFIG = {
         "axes_config": {
            "x_min": -5,
            "x_max": 5,
            "y_min": -5,
            "y_max": 5,
            "z_min": -4,
            "z_max": 4,
            "x_axis_config": {
                "tick_frequency": 100,
            },
            "y_axis_config": {
                "tick_frequency": 100,
            },
            "z_axis_config": {
                "tick_frequency": 100,
            },
            "num_axis_pieces": 1,
        }
    }
    def construct(self):
        axes = ThreeDAxes(**self.axes_config)
        text = TextMobject(r'$r(t) = \left\langle\sinh{t}, \cosh{t}, 2t\right\rangle$').scale(0.7).shift(3*UP + 3*LEFT)
        self.set_camera_orientation(phi = 75*DEGREES, theta=225*DEGREES)



        figure = ParametricFunction(
            lambda t: np.array([
                np.sinh(t),
                np.cosh(t),
                2*t
                ]), t_min = -3, t_max = 3, color=ORANGE
            ).scale(0.5).move_to(ORIGIN)

        dot = Dot(color=RED)
        alpha = ValueTracker(0)
        t = alpha.get_value

        vector_x = self.get_binormal_vector(t()%1, figure,scale=2)
        vector_y = self.get_normal_vector(t(),figure,scale=2)
        vector_z = self.get_tangent_vector(t(), figure, scale=2)

        vector_x.add_updater(
            lambda m: m.become(
                    self.get_binormal_vector(t()%1,figure,scale=2)
                )
            )
        vector_y.add_updater(
            lambda m: m.become(
                    self.get_normal_vector(t(),figure,scale=2)
                )
            )
        vector_z.add_updater(
            lambda m: m.become(
                    self.get_tangent_vector(t(),figure,scale=2)
                )
            )
        dot.add_updater(
        lambda m: m.move_to(vector_x.get_start())
        )
        def curvature(t):
            r = np.array([np.sinh(t), np.cosh(t), 2*t])
            rp = np.array([np.cosh(t), np.sinh(t), 2])
            rpp = np.array([np.sinh(t), np.cosh(t), 0])
            cp = np.cross(rp, rpp)
            k = cp / (np.dot(rp, rp)**1.5)
            return abs(k[0])

        def torsion(t):
            r = np.array([np.sinh(t), np.cosh(t), 2*t])
            rp = np.array([np.cosh(t), np.sinh(t), 2])
            rpp = np.array([np.sinh(t), np.cosh(t), 0])
            n = rpp / np.dot(rpp, rpp)
            dbdt = np.array([2*np.sinh(t), 2*np.cosh(t), 0])
            tor = np.dot(dbdt, n)
            return tor



        k = curvature(0.3)
        k = "{:.2f}".format(k)
        tor = torsion(0.3)
        tor = "{:.2f}".format(tor)
        kt1 = TextMobject(rf'At the given point, \\ $\kappa =$ {k} \\').scale(0.7).shift(3*UP + 4*RIGHT)
        kt2 = TextMobject('$\implies \kappa$',r'$T$',r' is scaled as:').scale(0.7).next_to(kt1, DOWN, buff=0.1)
        kt2.set_color_by_tex_to_color_map({
        '$T$': YELLOW
        })
        tbt1 = TextMobject(rf'At the given point, \\ $\tau =$ {tor} \\').scale(0.7).shift(3*UP + 4*RIGHT)
        tbt2 = TextMobject(r'$\implies \tau$',r'$B$',r' is scaled as:').scale(0.7).next_to(tbt1, DOWN, buff=0.1)
        tbt2.set_color_by_tex_to_color_map({
        '$B$': GREEN_E
        })
        ft = TextMobject(r'$\frac{dN}{ds}$',r'$ = -\kappa$',r'$T$', r'$ + \tau$',r'$B$ \\', r'and is given as:').scale(0.7).shift(3*UP + 4*RIGHT)
        ft.set_color_by_tex_to_color_map({
        r'$\frac{dN}{ds}$': GREEN_SCREEN,
        '$T$': YELLOW,
        r'$B$ \\': GREEN_E
        })

        self.add_fixed_in_frame_mobjects(text)
        self.play(FadeIn(figure), FadeIn(axes), FadeIn(text))
        # self.begin_ambient_camera_rotation(rate = 0.13)
        self.wait(1)
        self.add(vector_x, vector_y,vector_z,dot)
        self.play(alpha.increment_value, 0.3, run_time=10, rate_func=rush_from)
        self.wait(1)
        # self.stop_ambient_camera_rotation()
        # self.move_camera(phi = 75*DEGREES, theta=225*DEGREES)
        square = Rectangle(width=3.2, fill_color=WHITE, fill_opacity=0.3, color=RED_C).rotate(40*DEGREES).shift(0.8*DOWN+1.2*RIGHT)
        mat = [[0.7, 0.3], [1.0, -0.7]]
        square = square.apply_matrix(mat).rotate(17*DEGREES).shift(2.1*DOWN+RIGHT)
        tl, nl, bl = TextMobject(r'$T$', color=YELLOW).shift(2.8*RIGHT+0.5*DOWN), TextMobject(r'$N$', color=BLUE).shift(RIGHT), TextMobject(r'$B$', color=GREEN_E).shift(0.6*LEFT+0.5*DOWN)
        self.add_fixed_in_frame_mobjects(tl, nl, bl)
        self.play(FadeIn(VGroup(*[tl, nl, bl])))
        self.wait(3)
        self.add_fixed_in_frame_mobjects(square)
        self.play(FadeIn(square), FadeOut(VGroup(*[tl, nl, bl])))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(kt1)
        self.play(FadeIn(kt1))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(kt2)
        self.play(FadeIn(kt2))
        self.wait(2)
        kt = self.get_tangent_vector(0.3, figure, scale = -4*float(k))
        tb = self.get_binormal_vector(0.3, figure, scale = 2*float(tor))
        self.play(
        ReplacementTransform(vector_z, kt)
        )
        self.wait(3)
        self.add_fixed_in_frame_mobjects(tbt1)
        self.play(FadeOut(VGroup(*[kt1, kt2])), FadeIn(tbt1))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(tbt2)
        self.play(FadeIn(tbt2))
        self.wait(2)
        self.play(
        ReplacementTransform(vector_x, tb)
        )
        self.wait(2)
        self.add_fixed_in_frame_mobjects(ft)
        self.play(FadeOut(VGroup(*[tbt1, tbt2])), FadeIn(ft))
        self.wait(2)
        dnds = Arrow(dot.get_center() + np.array([-0.1,-0.25,0]), np.array([-4,-1,2]), color=GREEN_SCREEN)
        dndsl = TextMobject(r'$\frac{dN}{ds}$', color=GREEN_SCREEN).shift(2.5*LEFT + 1.2*UP)
        self.add_fixed_in_frame_mobjects(dndsl)
        self.play(FadeIn(dnds), FadeIn(dndsl))
        self.wait(5)
        self.play(FadeOut(VGroup(*[square, dot,vector_y, dnds, dndsl, text, ft, tb, kt])))
        self.play(FadeOut(figure), FadeOut(axes))


    def get_binormal_vector(self, proportion, curve, dx=0.001, scale=1):
        t = proportion
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
        unit_vector = reference_line.get_unit_vector() * scale
        vector = Arrow(coord_i , coord_i + unit_vector, color = GREEN_E, buff=0)
        return vector

    def get_normal_vector(self, proportion, curve, dx=0.001, scale=1):
        coord_i = curve.point_from_proportion(proportion)
        coord_f = curve.point_from_proportion(proportion + dx)
        t = proportion.copy()/7
        rpp = np.array([np.sinh(t), np.cosh(t), 0])
        length = np.sqrt(np.dot(rpp, rpp))
        length = 1/(1 + np.exp(-length))
        reference_line = Line(coord_i,coord_f).rotate(PI/2).set_width(length).scale(2)
        unit_vector = reference_line.get_unit_vector() * scale
        vector = Arrow(coord_i, coord_i + unit_vector, color = BLUE, buff=0)
        return vector

    def get_tangent_vector(self, proportion, curve, dx=0.001, scale=1):
        coord_i = curve.point_from_proportion(proportion)
        coord_f = curve.point_from_proportion(proportion + dx)
        reference_line = Line(coord_i,coord_f).scale(2)
        if scale < 0:
            reference_line = Line(coord_i,coord_f).scale(2).rotate(360*DEGREES)
        unit_vector = reference_line.get_unit_vector() * scale
        vector = Arrow(coord_i, coord_i + unit_vector, color = YELLOW, buff=0)
        return vector
