from manimlib.imports import *

class Hill(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 

        function = ParametricSurface(
            lambda u, v: np.array([
                1.2*np.sin(u)*np.cos(v),
                1.2*np.sin(u)*np.sin(v),
                -1.2*1.2*np.sin(u)*np.sin(u)*(1+0.5*np.sin(v)*np.sin(v))+2
            ]),u_min=0,u_max=PI/2,v_min=0,v_max=2*PI,checkerboard_colors=[GREEN_C, GREEN_E],
            resolution=(15, 32)).scale(1)

        func_x =ParametricFunction(
                lambda u : np.array([
                u,
                0,
                2 - u*u
            ]),color=RED_E,t_min=0,t_max=1.2,
            )
    
        func_y =ParametricFunction(
                lambda u : np.array([
                0,
                u,
                2 - 1.5*u*u
            ]),color=PINK,t_min=0,t_max=1.2,
            )

        self.set_camera_orientation(phi=60 * DEGREES, theta = 0*DEGREES)
        #self.set_camera_orientation(phi=45 * DEGREES, theta = -20*DEGREES)

        self.add(axes)
        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(np.array([0,0,3.7]))

        self.add_fixed_orientation_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1])

        self.play(ShowCreation(function))
        self.wait()

        self.move_camera(phi=60 * DEGREES, theta = 45*DEGREES)
        #self.play(ShowCreation(func_x))

        text_x = TextMobject("Slope of the hill along", r"$x$", "axis", color = YELLOW_C).scale(0.6).move_to(2.7*UP + 3.5*RIGHT)
        text_x[1].set_color(PINK)


        slope_text_x = TexMobject("Slope =", "{\\partial", "f", "\\over", "\\partial", "x}", "=").scale(0.6).move_to(2*UP + 3.5*RIGHT)
        slope_text_x[0].set_color(BLUE_E)
        slope_text_x.set_color_by_tex("\\partial",YELLOW_C)
        slope_text_x.set_color_by_tex("f",RED_E)
        slope_text_x[5].set_color(PINK)

        number_x = DecimalNumber(0,color=RED_C).scale(0.7).next_to(slope_text_x, RIGHT)

        prev_x_x = 0.01
        prev_x_z = 2

        self.add_fixed_in_frame_mobjects(text_x, slope_text_x, number_x)

        dot_x = Dot().rotate(PI/2).set_color(YELLOW_E)
        alpha_x = ValueTracker(0)
        vector_x = self.get_tangent_vector(alpha_x.get_value(),func_x,scale=1.5)
        dot_x.add_updater(lambda m: m.move_to(vector_x.get_center()))
        number_x.add_updater(lambda m: m.set_value((dot_x.get_center()[2] - prev_x_z)/(dot_x.get_center()[0] - prev_x_x)))
        number_x.add_updater(lambda m: self.add_fixed_in_frame_mobjects(m))

        prev_x_x = (dot_x.get_center()[0])
        prev_x_z = (dot_x.get_center()[2])

        self.play(
            ShowCreation(func_x),
            GrowFromCenter(dot_x),
            GrowArrow(vector_x)
            )
        vector_x.add_updater(
            lambda m: m.become(
                    self.get_tangent_vector(alpha_x.get_value()%1,func_x,scale=1.5)
                )
            )
        
        self.add(vector_x,dot_x)
        
        self.play(alpha_x.increment_value, 1, run_time=3, rate_func=linear)

        #self.move_camera(phi=60 * DEGREES, theta = 0*DEGREES)
        self.play(FadeOut(number_x), FadeOut(vector_x), FadeOut(dot_x), FadeOut(func_x), FadeOut(text_x), FadeOut(slope_text_x))

        text_y = TextMobject("Slope of the hill along", r"$y$", "axis", color = YELLOW_C).scale(0.6).move_to(2.7*UP + 3.5*RIGHT)
        text_y[1].set_color(RED_C)


        slope_text_y = TexMobject("Slope =", "{\\partial", "f", "\\over", "\\partial", "y}").scale(0.6).move_to(2*UP + 3.5*RIGHT)
        slope_text_y[0].set_color(BLUE_E)
        slope_text_y.set_color_by_tex("\\partial",YELLOW_C)
        slope_text_y.set_color_by_tex("f",PINK)
        slope_text_y[5].set_color(RED_C)

        number_y = DecimalNumber(0,color=RED_C).scale(0.7).next_to(slope_text_y, RIGHT)

        prev_y_x = 0.01
        prev_y_z = 2

        self.add_fixed_in_frame_mobjects(text_y, slope_text_y, number_y)

        dot_y = Dot().rotate(PI/2).set_color(BLUE_E)
        alpha_y = ValueTracker(0)
        vector_y = self.get_tangent_vector(alpha_y.get_value(),func_y,scale=1.5)
        dot_y.add_updater(lambda m: m.move_to(vector_y.get_center()))
        number_y.add_updater(lambda m: m.set_value((dot_y.get_center()[2] - prev_y_z)/(dot_y.get_center()[0] - prev_y_x)))
        number_y.add_updater(lambda m: self.add_fixed_in_frame_mobjects(m))

        prev_y_x = (dot_y.get_center()[0])
        prev_y_z = (dot_y.get_center()[2])


        self.play(
            ShowCreation(func_y),
            GrowFromCenter(dot_y),
            GrowArrow(vector_y)
            )
        vector_y.add_updater(
            lambda m: m.become(
                    self.get_tangent_vector(alpha_y.get_value()%1,func_y,scale=1.5)
                )
            )

        self.add(vector_y,dot_y)
        self.play(alpha_y.increment_value, 1, run_time=3, rate_func=linear)
        self.play(FadeOut(number_y), FadeOut(vector_y), FadeOut(dot_y), FadeOut(func_y), FadeOut(text_y), FadeOut(slope_text_y))
        self.wait(2)

    def get_tangent_vector(self, proportion, curve, dx=0.001, scale=1):
        coord_i = curve.point_from_proportion(proportion)
        coord_f = curve.point_from_proportion(proportion + dx)
        reference_line = Line(coord_i,coord_f)
        unit_vector = reference_line.get_unit_vector() * scale
        vector = Line(coord_i - unit_vector, coord_i + unit_vector, color = ORANGE, buff=0)
        return vector       