from manimlib.imports import *

class PartialDerivX(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v),
                -2*2*np.sin(u)*np.sin(u)+2
            ]),u_min=0,u_max=PI/2,v_min=0,v_max=2*PI,checkerboard_colors=[PINK, PURPLE],
            resolution=(15, 32)).scale(1)

        paraboloid_copy = paraboloid.copy()

 
        paraboloid_x = ParametricSurface(
            lambda u, v: np.array([
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v),
                -2*2*np.sin(u)*np.sin(u)+2
            ]),u_min=0,u_max=PI/2,v_min=PI,v_max=2*PI,checkerboard_colors=[PINK, PURPLE],
            resolution=(15, 32)).scale(1)


        parabola =ParametricFunction(
                lambda u : np.array([
                u,
                0,
                -(u*u) + 2
            ]),color="#006400",t_min=-2,t_max=2,
            )
        
        plane = Polygon(np.array([-2.2,0,-2.5]),np.array([2.2,0,-2.5]),np.array([2.2,0,2.5]),np.array([-2.2,0,2.5]),np.array([-2.2,0,-2.5]), color = GREEN, fill_color = GREEN, fill_opacity = 0.2)
        plane_text = TextMobject(r"$y = 0$", color = GREEN_C).move_to(2*UP + 3*RIGHT)

        surface_eqn = TextMobject("Surface", r"$z = f(x,y) = 2 - x^2 - y^2$", color = BLUE_C).scale(0.6).move_to(np.array([3*LEFT +3*UP]))
        surface_eqn[0].set_color(PINK)

        line = Line(np.array([-2,0,0]), np.array([2,0,0]), color = RED_C)
        
 
        self.add(axes)

        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(3.7*UP)

        self.add_fixed_in_frame_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1])


        self.set_camera_orientation(phi=80 * DEGREES, theta = 0*DEGREES)

        self.play(Write(paraboloid))

        self.add_fixed_in_frame_mobjects(surface_eqn)
        #self.move_camera(phi=80* DEGREES,theta=95*DEGREES)
        self.move_camera(phi=80* DEGREES,theta=45*DEGREES)
        self.play(ShowCreation(plane))
        self.add_fixed_in_frame_mobjects(plane_text)
        self.wait()
        self.play(ReplacementTransform(paraboloid, paraboloid_x))
        self.play(FadeOut(plane), FadeOut(plane_text))
        self.play(ShowCreation(parabola), ShowCreation(line))

        text1 = TextMobject("Moving small", r"$dx$", r"steps").scale(0.6).move_to(3*UP + 3.5*RIGHT).set_color_by_gradient(RED, ORANGE, YELLOW, BLUE, PURPLE)
    
        text2 = TextMobject("Observing change in function, keeping", r"$y$", r"constant").scale(0.6).move_to(2.6*UP + 3.5*RIGHT).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        
        slope_text = TexMobject("Slope =", "{\\partial", "f", "\\over", "\\partial", "x}").scale(0.6).move_to(2*UP + 3.5*RIGHT)
        slope_text[0].set_color(BLUE_E)
        slope_text.set_color_by_tex("\\partial",PINK)
        slope_text.set_color_by_tex("f","#006400")
        slope_text[5].set_color(RED_C)

        self.add_fixed_in_frame_mobjects(text1, text2)
        self.wait()
        self.add_fixed_in_frame_mobjects(slope_text)
        #add_fixed_orientation_mobjects
        
        
        dot = Dot().rotate(PI/2).set_color(RED_C)
        alpha = ValueTracker(0)
        vector = self.get_tangent_vector(alpha.get_value(),parabola,scale=1.5)
        dot.add_updater(lambda m: m.move_to(vector.get_center()))
        self.play(
            ShowCreation(parabola),
            GrowFromCenter(dot),
            GrowArrow(vector)
            )
        vector.add_updater(
            lambda m: m.become(
                    self.get_tangent_vector(alpha.get_value()%1,parabola,scale=1.5)
                )
            )
        self.add(vector,dot)
        self.play(alpha.increment_value, 1, run_time=10, rate_func=linear)
        self.wait()


        '''
        for i in np.arange(-2,2,0.2):
            self.play(ReplacementTransform(Line(np.array([i,0,0]), np.array([i,0,-i*i + 2]), color = GREEN_C), Line(np.array([i+0.2,0,0]), np.array([i+0.2,0,-(i+0.2)**2 + 2]), color = GREEN_C)))
            #self.wait()
        '''

        self.wait()
        self.play(FadeOut(parabola), FadeOut(line), FadeOut(vector), FadeOut(dot), FadeOut(text1), FadeOut(text2), FadeOut(slope_text),FadeOut(surface_eqn))

        #self.move_camera(phi=80* DEGREES,theta= 0*DEGREES)
        self.play(ReplacementTransform(paraboloid_x, paraboloid_copy))
        self.wait()


    def get_tangent_vector(self, proportion, curve, dx=0.001, scale=1):
        coord_i = curve.point_from_proportion(proportion)
        coord_f = curve.point_from_proportion(proportion + dx)
        reference_line = Line(coord_i,coord_f)
        unit_vector = reference_line.get_unit_vector() * scale
        vector = Line(coord_i - unit_vector, coord_i + unit_vector, color = BLUE_E, buff=0)
        return vector


class PartialDerivY(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v),
                -2*2*np.sin(u)*np.sin(u)+2
            ]),u_min=0,u_max=PI/2,v_min=0,v_max=2*PI,checkerboard_colors=[PINK, PURPLE],
            resolution=(15, 32)).scale(1)

        paraboloid_copy = paraboloid.copy()

 
        paraboloid_y = ParametricSurface(
            lambda u, v: np.array([
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v),
                -2*2*np.sin(u)*np.sin(u)+2
            ]),u_min=0,u_max=PI/2,v_min=PI/2,v_max=3*PI/2,checkerboard_colors=[PINK, PURPLE],
            resolution=(15, 32)).scale(1)


        parabola =ParametricFunction(
                lambda u : np.array([
                0,
                u,
                -(u*u) + 2
            ]),color=YELLOW_C,t_min=-2,t_max=2,
            )
        
        plane = Polygon(np.array([0,-2.2,-2.5]),np.array([0,2.2,-2.5]),np.array([0,2.2,2.5]),np.array([0,-2.2,2.5]),np.array([0,-2.2,-2.5]), color = BLUE, fill_color = BLUE, fill_opacity = 0.2)
        plane_text = TextMobject(r"$x = 0$", color = BLUE_C).move_to(2*UP + 3*RIGHT)

        surface_eqn = TextMobject("Surface", r"$z = f(x,y) = 2 - x^2 - y^2$", color = BLUE_C ).scale(0.6).move_to(np.array([3*LEFT +3*UP]))
        surface_eqn[0].set_color(PINK)
        
        line = Line(np.array([0,-2,0]), np.array([0,2,0]), color = RED_C)
 
        self.add(axes)

        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(3.7*UP)

        self.add_fixed_in_frame_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1])

        self.set_camera_orientation(phi=80 * DEGREES, theta = 45*DEGREES)

        self.play(Write(paraboloid))

        self.add_fixed_in_frame_mobjects(surface_eqn)
        #self.move_camera(phi=80* DEGREES,theta=5*DEGREES)
        self.play(ShowCreation(plane))
        self.add_fixed_in_frame_mobjects(plane_text)
        self.wait()
        self.play(ReplacementTransform(paraboloid, paraboloid_y))
        self.play(FadeOut(plane), FadeOut(plane_text))
        self.play(ShowCreation(parabola), ShowCreation(line))

        text1 = TextMobject("Moving small", r"$dy$", r"steps").scale(0.6).move_to(3*UP + 3.5*RIGHT).set_color_by_gradient(RED, ORANGE, YELLOW, BLUE, PURPLE)
        
        text2 = TextMobject("Observing change in function, keeping", r"$x$", r"constant").scale(0.6).move_to(2.6*UP + 3.5*RIGHT).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        
        slope_text = TexMobject("Slope =", "{\\partial", "f", "\\over", "\\partial", "y}").scale(0.6).move_to(2*UP + 3.5*RIGHT)
        slope_text[0].set_color("#006400")
        slope_text.set_color_by_tex("\\partial",PINK)
        slope_text.set_color_by_tex("f",YELLOW_C)
        slope_text[5].set_color(RED_C)

        self.add_fixed_in_frame_mobjects(text1, text2)
        self.wait()
        self.add_fixed_in_frame_mobjects(slope_text)

        dot = Dot().rotate(PI/2).set_color(RED_C)
        alpha = ValueTracker(0)
        vector = self.get_tangent_vector(alpha.get_value(),parabola,scale=1.5)
        dot.add_updater(lambda m: m.move_to(vector.get_center()))
        self.play(
            ShowCreation(parabola),
            GrowFromCenter(dot),
            GrowArrow(vector)
            )
        vector.add_updater(
            lambda m: m.become(
                    self.get_tangent_vector(alpha.get_value()%1,parabola,scale=1.5)
                )
            )
        self.add(vector,dot)
        self.play(alpha.increment_value, 1, run_time=10, rate_func=linear)
        self.wait()
        
        '''
        for i in np.arange(-2,2,0.2):
            self.play(ReplacementTransform(Line(np.array([0,i,0]), np.array([0,i,-i*i + 2]), color = BLUE_C), Line(np.array([0,i+0.2,0]), np.array([0,i+0.2,-(i+0.2)**2 + 2]), color = BLUE_C)))
            #self.wait()
        '''


        self.wait()
        self.play(FadeOut(parabola), FadeOut(line), FadeOut(vector), FadeOut(dot), FadeOut(text1), FadeOut(text2), FadeOut(slope_text),FadeOut(surface_eqn))

        #self.move_camera(phi=80* DEGREES,theta= 90*DEGREES)
        self.play(ReplacementTransform(paraboloid_y, paraboloid_copy))
        self.wait()   

    def get_tangent_vector(self, proportion, curve, dx=0.001, scale=1):
        coord_i = curve.point_from_proportion(proportion)
        coord_f = curve.point_from_proportion(proportion + dx)
        reference_line = Line(coord_i,coord_f)
        unit_vector = reference_line.get_unit_vector() * scale
        vector = Line(coord_i - unit_vector, coord_i + unit_vector, color = "#006400", buff=0)
        return vector         

        