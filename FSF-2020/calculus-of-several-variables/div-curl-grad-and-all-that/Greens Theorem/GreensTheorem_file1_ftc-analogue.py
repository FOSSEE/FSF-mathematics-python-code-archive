from manimlib.imports import *


def vector_field_func(coordinate):
    x,y = coordinate[:2]
    return np.array([
            x,
            y,
            0
    ])
def curl(coordinate):
	x,y = coordinate[:2]
	U = (x**2 + y**2)	
	return np.array([
			-y/(x**2 + y**2),
			x/(x**2 + y**2),
			0
	])





class GreensVisual(Scene):

    def construct(self):
        axes_config = {"x_min": -6,
                       "x_max": 6,
                       "y_min": -6,
                       "y_max": 6,
                       "z_axis_config": {},
                       "z_min": -1,
                       "z_max": 1,
                       "z_normal": DOWN,
                       "light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
                       "number_line_config": {
                           "include_tip": False,
                       },
                       }

        axes = Axes(**axes_config)

        field = VectorField(vector_field_func).fade(0.5)
        self.add(field)

        title = TexMobject(r"\textit{According to Green's Theorem, }").shift(3*UP)

        eq1 = TexMobject(r"\int_{C} \vec F . dr = \int \int_{D} \nabla \times \vec F dA").shift(3*DOWN)
        eq5 = TexMobject(r"\int_{C} \vec F . dr = \int \int_{D} \nabla \times \vec F dA").shift(3*DOWN)

        generalisation = TexMobject()

        eq2 = TexMobject(r"\int_{C} \vec F . dr = \int_{C_1} \vec F . dr + \int_{C_{2}} \vec F . dr").shift(3*DOWN)
        eq3 = TexMobject(r"\int_{C} \vec F . dr = \int_{C_{1}} \vec F . dr + \int_{C_{2}} \vec F . dr + \int_{C_{3}} \vec F . dr + \int_{C_{4}} \vec F . dr...").shift(3*DOWN)
        eq4 = TexMobject(r"\int_{C_{r}} \vec F dr \approx \int\int_{D} \nabla \times \vec F dA").shift(3*DOWN)
        eq = TexMobject(r"\int_{C_{r}} \textit{macroscopic curl} = \int\int_{D} \text{sum of all microscopic curls}").shift(3*UP)

        text_1 = TexMobject(r"\textit{Split C into 2 parts and calculate curl of each one of the smaller regions seperately}").shift(3*UP)
        #text_2 = TexMobject(r"\textit{}").shift(3*UP)
        text_3 = TexMobject(r"\textit{By splitting C into n segments, the area of each region approaches the limit 0}", r"\textit{The macroscopic circulation along the curve }", r"\textit{is equivalent to the sum of microscopic circulation of all these small regions }")
        text_3[0].move_to(3.8*UP)
        text_3[1].set_color(YELLOW_E).next_to(text_3[0], DOWN, buff = SMALL_BUFF)
        text_3[2].set_color(BLUE_E).next_to(text_3[1], DOWN, buff = SMALL_BUFF)



        curl_rep_1 = StreamLines(
			curl,
            virtual_time=4,
            min_magnitude=0,
            max_magnitude=2,
            dt = 0.1,
            x_min = -0.5, x_max = 0.5, y_min = -0.5, y_max = 0.5,
            ).set_color_by_gradient([BLUE_E, TEAL, WHITE])
        flow_1 = AnimatedStreamLines(
            curl_rep_1,
            line_anim_class=ShowPassingFlashWithThinningStrokeWidth
        )

        static = VMobject()
        for p in range(0, 8, 4):
            curl_rep_n = [*StreamLines(
			curl,
            virtual_time=2,
            min_magnitude=0,
            max_magnitude=1,
            dt = 0.1,
            x_min = -0.5, x_max = 0.5, y_min = -0.5, y_max = 0.5,
                ).scale(0.5).move_to(np.array([-2+p, 0,0]))]
            static.add(*curl_rep_n)
        static_1 = VMobject()
        for p in range(-3, 4, 2):
            curl_rep_1 = [*StreamLines(
			curl,
            virtual_time=2,
            min_magnitude=0,
            max_magnitude=1,
            dt = 0.1,
            x_min = -0.5, x_max = 0.5, y_min = -0.5, y_max = 0.5,
                ).scale(0.25).move_to(np.array([p, 0.6,0]))]
            static_1.add(*curl_rep_1)

        static_2 = VMobject()
        for p in range(-3, 4, 2):
            curl_rep_2 = [*StreamLines(
			curl,
            virtual_time=2,
            min_magnitude=0,
            max_magnitude=1,
            dt = 0.1,
            x_min = -0.5, x_max = 0.5, y_min = -0.5, y_max = 0.5,
                ).scale(0.25).move_to(np.array([p, -0.6,0]))]
            static_2.add(*curl_rep_2)



        surface_6 = ParametricSurface(
            self.surface,
            u_min=-3,
            u_max=3,
            v_min=-3,
            v_max=3,
            fill_color=BLACK,
            checkerboard_colors=[BLACK, BLACK],
            stroke_color=BLUE_E,
            resolution = [64,64]
        ).set_fill(opacity=0.2).scale(1.5)

        boundary = ParametricSurface(
            self.surface,
            u_min=-3,
            u_max=3,
            v_min=-3,
            v_max=3,
            fill_color=BLACK,
            checkerboard_colors=[BLACK, BLACK],
            stroke_color=YELLOW_E,
            resolution = [2,1]
        ).set_fill(opacity=0).scale(1.75)




        g1 = VGroup(surface_1, c)
        g2 = VGroup( c1, c2, text_1)
        g3 = VGroup(c1a, c2a, c3a, c4a)

        tr = Ellipse(width = 9, height = 3)
        line = Line(tr.get_center()+1.5*UP, tr.get_center()+1.5*DOWN)
        b = VMobject(stroke_color = "#F4EDED")
        b.set_points_smoothly([tr.get_center()+1.5*UP, np.array([-2.25, 1.26, 0]), tr.get_center()+4.5*LEFT, np.array([-2.25, -1.26, 0]), tr.get_center()+1.5*DOWN])


        self.add(title)
        self.play(ShowCreation(g1), ShowCreation(eq1))
        self.wait(3)
        self.remove(flow_1)
        self.play(ShowCreation(surface_2), ReplacementTransform(eq1, eq2))
        self.remove(g1)
        self.wait()
        self.play(ReplacementTransform(surface_2, surface_3), ReplacementTransform(eq2, eq3))
        self.wait()
        self.wait()
        self.play(FadeOut(surface_3), ShowCreation(surface_4), ReplacementTransform(eq3, eq4), ReplacementTransform(title, eq))
        self.play(FadeOut(surface_4), ShowCreation(surface_5))
        self.play(FadeOut(surface_5), ShowCreation(surface_6))
        self.wait()
        #self.add(tr, line)
        self.wait()
        grd = ScreenGrid()

        g = ParametricFunction(func, t_min = 0, t_max = 2*PI).scale(1.5)
        self.add(grd, g)
        self.wait()


def circ(coordinate):
    x,y = coordinate[:2]
    for x in range(0, -5) and y in range(-1,1):
        cr = Ellipse()
    return cr

def func(t):
	return np.array([
		np.sin(t),
		np.cos(t),
		0])

def surf(t,u):
	return np.array([
		u*np.sin(t),
		np.cos(t),
		0])

class Analogy(GraphScene):
	CONFIG = {
		"x_min": -1,
		"x_max": 4,
		"y_min": 0,
		"y_max": 2,
		"y_tick_frequency": 2.5,
		"n_rect_iterations": 6,
		"default_right_x": 3,
	}

	def construct(self):


		ftc = TexMobject(r"\int_a^b f'(x) \ dx", r" = f(b) - f(a)").shift(3*UP).set_color("#F9DB6D").scale(0.7)
		greens = TexMobject(r"\int \int_{R} curl \left(\vec F \right) \ dxdy", r" = \int_{C} \vec F \ dr").shift(3*UP).set_color("#F9DB6D").scale(0.7) 
		ftc[0].set_color("#36827F")
		greens[1].set_color("#36827F")


		two_to_one = TexMobject(r"\textit{2D region} \to", r"\textit{1D curve}").shift(3.6*DOWN).scale(0.7).set_color("#F9DB6D")
		one_to_zero = TexMobject(r"\textit{1D curve}", r" \to \textit{0D points}").shift(3.6*DOWN).set_color("#F9DB6D").scale(0.7)
		two_to_one[1].set_color("#36827F")
		one_to_zero[0].set_color("#36827F")
		greens_title = TexMobject(r"\textit{Green's Theorem}").scale(0.8).next_to(two_to_one, UP, buff = SMALL_BUFF).set_color("#F4EDED")
		ftc_title = TexMobject(r"\textit{Fundamental Theorem of Calculus}").scale(0.8).next_to(two_to_one, UP, buff = SMALL_BUFF).set_color("#F4EDED")

		surf= VMobject(fill_color = "#ED6A5A", stroke_color =  "#ED6A5A", fill_opacity = 0.6)
		surf.set_points_smoothly([np.array([-2, 1.8,0]),np.array([-1.6, 0.5,0]),np.array([-3.2, -1.2,0]),np.array([2.6, -1.5,0]),np.array([1, 0,0]),np.array([3.5,2.3, 0]), np.array([-2,1.8, 0])])
		dot = Dot(np.array([-2,1.8, 0])).set_color("#F4EDED")
		boundary = VMobject(stroke_color = "#F4EDED")
		boundary.set_points_smoothly([np.array([-2, 1.8,0]),np.array([-1.6, 0.5,0]),np.array([-3.2, -1.2,0]),np.array([2.6, -1.5,0]),np.array([1, 0,0]),np.array([3.5,2.3, 0]), np.array([-2,1.8, 0])])
		c = TexMobject(r"C").next_to(surf,RIGHT+UP).set_color("#F4EDED")
		r = TexMobject(r"R").move_to(np.array([-0.2, 0.6, 0])).set_color("#F4EDED")

		self.play(ShowCreation(surf), ShowCreation(r))
		self.wait(2)
		self.play(ShowCreation(boundary), MoveAlongPath(dot, boundary), Write(c), Write(greens),Write(greens_title), run_time= 1.5)
		self.wait(2)
		self.play(ReplacementTransform(surf, boundary), FadeOut(r), Write(two_to_one), FadeOut(dot))
		self.wait(2)

		self.setup_axes()

		grapher = self.get_graph(self.funk)
		grapher.set_color("#E94F37")
		l1 = self.get_vertical_line_to_graph(1, grapher, color = "#F4EDED")
		l2 =self.get_vertical_line_to_graph(3, grapher, color = "#F4EDED")
		label_coord_1 = self.input_to_graph_point(1,grapher)
		label_coord_2 = self.input_to_graph_point(3,grapher)


		a = TexMobject(r"a").next_to(label_coord_1,RIGHT+UP).set_color("#F4EDED")
		b = TexMobject(r"b").next_to(label_coord_2,RIGHT+UP).set_color("#F4EDED")





		point_a = Dot(label_coord_1).set_color("#827081")
		point_b = Dot(label_coord_2).set_color("#827081")


		self.play(ReplacementTransform(boundary, grapher), FadeOut(c), FadeIn(a), FadeIn(b), FadeIn(point_a), FadeIn(point_b), ReplacementTransform(greens, ftc), ReplacementTransform(greens_title, ftc_title))
		self.wait(2)
		self.play(Uncreate(grapher), ReplacementTransform(two_to_one, one_to_zero))
		self.wait(2)


	def funk(self,x):
		return 0.2*(x-2)**2 +1