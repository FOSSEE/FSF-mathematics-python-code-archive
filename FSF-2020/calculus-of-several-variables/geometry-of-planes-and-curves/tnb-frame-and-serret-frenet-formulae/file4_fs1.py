from manimlib.imports import *
class fs1(GraphScene):
    CONFIG = {
        "x_min": -2,
        "x_max": 2,
        "y_min": -6,
        "y_max": 6,
        "graph_origin": ORIGIN
    }
    def construct(self):

        text = TextMobject(r'$\frac{dT}{ds} = \kappa N$ \\ $\frac{dT}{ds}$ gives the direction of N, \\ while $\kappa$ gives its magnitude.').scale(0.7).shift(3*UP + 3*LEFT)

        self.setup_axes()
        def curve_(x):
            return x**3 - 2*x

        def nm(x):
            return abs(6 * x / ((9*(x**4) - 6*(x**2) + 5)**1.5))

        figure = self.get_graph(curve_)


        dot = Dot().rotate(PI/2)
        alpha = ValueTracker(0)
        t2_ = ValueTracker(-2)
        t2 = t2_.get_value
        t = alpha.get_value
        vector_x = self.get_tangent_vector(t(),figure,scale=2)
        vector_y = self.get_normal_vector(t(),figure,scale=2)

        kappa = TextMobject(r'$\kappa = $').scale(0.7).shift(3*DOWN + 3*RIGHT)

        t_text = always_redraw(
            lambda: DecimalNumber(
                nm(t2()),
                color=WHITE,
            ).scale(0.7).next_to(kappa)
        ).scale(0.6)

        self.play(
            ShowCreation(figure),
            GrowFromCenter(dot),
            GrowArrow(vector_x),
            GrowArrow(vector_y)
            )
        vector_x.add_updater(
            lambda m: m.become(
                    self.get_tangent_vector(t(),figure,scale=2)
                )
            )
        vector_y.add_updater(
            lambda m: m.become(
                    self.get_normal_vector(t(),figure,scale=2)
                )
            )
        dot.add_updater(lambda m: m.move_to(vector_x.get_start()))
        circle = Circle(radius = 2, color = GREEN_SCREEN). shift(2.63*RIGHT + 2.8*UP)
        dot2 = Dot(np.array([2, curve_(2), 0]), color = WHITE).shift(2*DOWN + 2.5*RIGHT)

        self.add(vector_x, vector_y,dot, t_text, kappa, text)
        self.play(t2_.set_value, 2, alpha.set_value, 1, run_time=18, rate_func=smooth)
        self.play(FadeIn(dot2), FadeIn(circle))
        self.wait(2)
        self.play(FadeOut(VGroup(*[self.axes, dot2, figure, circle, text, kappa, t_text])))


    def get_tangent_vector(self, proportion, curve, dx=0.001, scale=0.5):
        coord_i = curve.point_from_proportion(proportion)
        coord_f = curve.point_from_proportion(proportion + dx)
        reference_line = Line(coord_i,coord_f)
        unit_vector = reference_line.get_unit_vector() * 0.7
        vector = Arrow(coord_i , coord_i + unit_vector, color = YELLOW, buff=0)
        return vector

    def get_normal_vector(self, proportion, curve, dx=0.001, scale=1):
        t = proportion.copy()/6
        coord_i = curve.point_from_proportion(proportion)
        coord_f = curve.point_from_proportion(proportion + dx)
        length = 6 * t / ((9*(t**4) - 6*(t**2) + 5)**1.5)
        if coord_i[0] <=  0 and coord_i[0] >  -0.5:
            reference_line = Line(coord_i,coord_f).rotate(PI/2).set_width(0).scale(2)
        elif coord_i[0] >  0 and (coord_i[0] < 0.5 or coord_i[0] > 2.7):
            reference_line = Line(coord_i,coord_f).rotate(PI/2).set_width(0).scale(2)
        elif coord_i[0] >  0:
            reference_line = Line(coord_i,coord_f).rotate(PI/2).set_width(length).scale(2)
        else:
            reference_line = Line(coord_i,coord_f).rotate(-PI/2).set_width(length).scale(2)
        unit_vector = reference_line.get_vector() * scale
        vector = Arrow(coord_i , coord_i + unit_vector, color = RED_C, buff=0)
        return vector
