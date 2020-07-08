from manimlib.imports import *

class MaximaMinima(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 
       
        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                3.5*np.sin(u)*np.cos(v),
                3.5*np.sin(u)*np.sin(v),
                3.5*3.5*np.sin(u)*np.sin(u)*(1+2*np.sin(v)*np.sin(v))*np.exp(1 - 3.5*3.5*np.sin(u)*np.sin(u) ) 
            ]),u_min=0,u_max=PI,v_min=0,v_max=2*PI, color = BLUE_C, fill_color = BLUE_C, fill_opacity = 0.1,
            resolution=(15, 32)).scale(1)

        paraboloid_copy1 = paraboloid.copy()
        paraboloid_copy2 = paraboloid.copy()

        paraboloid_x = ParametricSurface(
            lambda u, v: np.array([
                3.5*np.sin(u)*np.cos(v),
                3.5*np.sin(u)*np.sin(v),
                3.5*3.5*np.sin(u)*np.sin(u)*(1+2*np.sin(v)*np.sin(v))*np.exp(1 - 3.5*3.5*np.sin(u)*np.sin(u) ) 
            ]),u_min=0,u_max=PI,v_min=PI,v_max=2*PI, color = BLUE_C, fill_color = BLUE_C, fill_opacity = 0.1,
            resolution=(15, 32)).scale(1)

        paraboloid_y = ParametricSurface(
            lambda u, v: np.array([
                3.5*np.sin(u)*np.cos(v),
                3.5*np.sin(u)*np.sin(v),
                3.5*3.5*np.sin(u)*np.sin(u)*(1+2*np.sin(v)*np.sin(v))*np.exp(1 - 3.5*3.5*np.sin(u)*np.sin(u) ) 
            ]),u_min=0,u_max=PI,v_min=PI/2,v_max=3*PI/2, color = BLUE_C, fill_color = BLUE_C, fill_opacity = 0.1,
            resolution=(15, 32)).scale(1)
        
        parabola_x_out =ParametricFunction(
                lambda u : np.array([
                u,
                0,
                (u*u )*np.exp(1-u*u)
            ]),color=RED_E,t_min=-3.5,t_max=3.5,
            )
    
        parabola_y_out =ParametricFunction(
                lambda u : np.array([
                0,
                u,
                (3*u*u)*np.exp(1-u*u)
            ]),color=PINK,t_min=-3.5,t_max=3.5,
            )

        plane1 = Polygon(np.array([-3.5,0,-3]),np.array([3.5,0,-3]),np.array([3.5,0,3]),np.array([-3.5,0,3]),np.array([-3.5,0,-3]), color = RED_C, fill_color = RED_C, fill_opacity = 0.2)
        plane_text_x = TextMobject(r"$y = 0$", color = RED_C).move_to(2*UP + 4.5*RIGHT)

        plane2 = Polygon(np.array([0,-3.5,-3]),np.array([0,3.5,-3]),np.array([0,3.5,3]),np.array([0,-3.5,3]),np.array([0,-3.5,-3]), color = PINK, fill_color = PINK, fill_opacity = 0.2)
        plane_text_y = TextMobject(r"$x = 0$", color = PINK).move_to(2*UP + 4.5*RIGHT)

        surface_eqn = TextMobject("Surface", r"$z = (x^2 + 3y^2)e^{(1 - x^2 - y^2)}$", color = YELLOW_C).scale(0.6).move_to(np.array([3.5*LEFT +3.5*UP]))
        surface_eqn[0].set_color(BLUE_C)

        self.set_camera_orientation(phi=60 * DEGREES, theta = 45*DEGREES)

        self.add(axes)
        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(np.array([0,0,3.7]))

        self.add_fixed_orientation_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1])

        self.play(ShowCreation(paraboloid))


        #self.move_camera(phi=60 * DEGREES, theta = 45*DEGREES,run_time=3)

        
        plane_x = Polygon(np.array([-3.5,2,-3]),np.array([3.5,2,-3]),np.array([3.5,2,3]),np.array([-3.5,2,3]),np.array([-3.5,2,-3]), color = YELLOW_C, fill_color = YELLOW_A, fill_opacity = 0.2)
        
        plane_y = Polygon(np.array([2,-3.5,-3]),np.array([2,3.5,-3]),np.array([2,3.5,3]),np.array([2,-3.5,3]),np.array([2,-3.5,-3]), color = GREEN_C, fill_color = GREEN_A, fill_opacity = 0.2) 
        
        text_x = TextMobject(r"$x$", "is fixed on this" ,"plane").scale(0.7).to_corner(UL)
        text_y = TextMobject(r"$y$", "is fixed on this" ,"plane").scale(0.7).to_corner(UR)
             
        text_x[0].set_color(RED_C)
        text_y[0].set_color(PINK)
        text_x[1].set_color(BLUE_C)
        text_y[1].set_color(BLUE_C)
        text_x[2].set_color(GREEN_C)
        text_y[2].set_color(YELLOW_C)

        self.add_fixed_in_frame_mobjects(text_x, text_y)
        
        for i in range(2,-4,-1):
            
            parabola_x =ParametricFunction(lambda u : np.array([u,i,(u*u + 3*i*i)*np.exp(1- u*u - i*i)]),color=RED_C,t_min=-3.5,t_max=3.5,)

            parabola_y =ParametricFunction(lambda u : np.array([i,u,(i*i + 3*u*u)*np.exp(1-  u*u - i*i)]),color=PINK,t_min=-3.5,t_max=3.5,)

            if(i==2):
             self.play(ShowCreation(plane_x), ShowCreation(plane_y))
             parabola_copy_x = parabola_x.copy()
             parabola_copy_y = parabola_y.copy()


             self.play(ShowCreation(parabola_copy_x), ShowCreation(parabola_copy_y))
             self.wait()
             self.play(FadeOut(parabola_copy_x), FadeOut(parabola_copy_y))

            else:
             self.play(ApplyMethod(plane_x.move_to, np.array([0,i,0])),ReplacementTransform(parabola_copy_x, parabola_x),ApplyMethod(plane_y.move_to, np.array([i,0,0])),ReplacementTransform(parabola_copy_y, parabola_y))
             self.play(FadeOut(parabola_x), FadeOut(parabola_y))
             self.wait()
            
            parabola_copy_x = parabola_x.copy()
            parabola_copy_y = parabola_y.copy()
            
        self.play(FadeOut(plane_x), FadeOut(plane_y), FadeOut(text_x), FadeOut(text_y))
        

        self.add_fixed_in_frame_mobjects(surface_eqn)

        self.move_camera(phi=80 * DEGREES, theta = 95*DEGREES)

        self.play(ShowCreation(plane1))
        self.add_fixed_in_frame_mobjects(plane_text_x)
        self.wait()
        self.play(ReplacementTransform(paraboloid, paraboloid_x))
        self.play(FadeOut(plane1), FadeOut(plane_text_x))

        line_x = Line(np.array([-3.5,0,0]), np.array([3.5,0,0]), color = YELLOW_E)

        self.play(ShowCreation(parabola_x_out), ShowCreation(line_x))

        slope_text_x = TexMobject("Slope =", "{\\partial", "f", "\\over", "\\partial", "x}").scale(0.6).move_to(2*UP + 3.5*RIGHT)
        slope_text_x[0].set_color(ORANGE)
        slope_text_x.set_color_by_tex("\\partial",GREEN_E)
        slope_text_x.set_color_by_tex("f",RED_E)
        slope_text_x[5].set_color(YELLOW_E)

        self.add_fixed_in_frame_mobjects(slope_text_x)


        dot_x = Dot().rotate(PI/2).set_color(YELLOW_E)
        alpha_x = ValueTracker(0)
        vector_x = self.get_tangent_vector(alpha_x.get_value(),parabola_x_out,scale=1.5)
        dot_x.add_updater(lambda m: m.move_to(vector_x.get_center()))
        self.play(
            ShowCreation(parabola_x_out),
            GrowFromCenter(dot_x),
            GrowArrow(vector_x)
            )
        vector_x.add_updater(
            lambda m: m.become(
                    self.get_tangent_vector(alpha_x.get_value()%1,parabola_x_out,scale=1.5)
                )
            )
        self.add(vector_x,dot_x)
        self.play(alpha_x.increment_value, 1, run_time=10, rate_func=linear)

        self.wait(2)
        self.play(FadeOut(parabola_x_out), FadeOut(line_x), FadeOut(vector_x), FadeOut(dot_x), FadeOut(slope_text_x))

        self.move_camera(phi=80* DEGREES,theta= 5*DEGREES)
        self.play(ReplacementTransform(paraboloid_x, paraboloid_copy1))
        self.wait()

        

        self.play(ShowCreation(plane2))
        self.add_fixed_in_frame_mobjects(plane_text_y)
        self.wait()
        self.play(ReplacementTransform(paraboloid_copy1, paraboloid_y))
        self.play(FadeOut(plane2), FadeOut(plane_text_y))

        line_y = Line(np.array([0,-3.5,0]), np.array([0,3.5,0]), color = GREEN_E)

        self.play(ShowCreation(parabola_y_out), ShowCreation(line_y))

        slope_text_y = TexMobject("Slope =", "{\\partial", "f", "\\over", "\\partial", "y}").scale(0.6).move_to(2*UP + 3.5*RIGHT)
        slope_text_y[0].set_color(ORANGE)
        slope_text_y.set_color_by_tex("\\partial",YELLOW_E)
        slope_text_y.set_color_by_tex("f",PINK)
        slope_text_y[5].set_color(GREEN_E)

        self.add_fixed_in_frame_mobjects(slope_text_y)


        dot_y = Dot().rotate(PI/2).set_color(GREEN_E)
        alpha_y = ValueTracker(0)
        vector_y = self.get_tangent_vector(alpha_y.get_value(),parabola_y_out,scale=1.5)
        dot_y.add_updater(lambda m: m.move_to(vector_y.get_center()))
        self.play(
            ShowCreation(parabola_y_out),
            GrowFromCenter(dot_y),
            GrowArrow(vector_y)
            )
        vector_y.add_updater(
            lambda m: m.become(
                    self.get_tangent_vector(alpha_y.get_value()%1,parabola_y_out,scale=1.5)
                )
            )
        self.add(vector_y,dot_y)
        self.play(alpha_y.increment_value, 1, run_time=10, rate_func=linear)

        self.wait(2)
        self.play(FadeOut(parabola_y_out), FadeOut(line_y), FadeOut(vector_y), FadeOut(dot_y), FadeOut(slope_text_y))

        self.move_camera(phi=60* DEGREES,theta= 45*DEGREES)
        self.play(ReplacementTransform(paraboloid_y, paraboloid_copy2))
        self.wait()







        

    def get_tangent_vector(self, proportion, curve, dx=0.001, scale=1):
        coord_i = curve.point_from_proportion(proportion)
        coord_f = curve.point_from_proportion(proportion + dx)
        reference_line = Line(coord_i,coord_f)
        unit_vector = reference_line.get_unit_vector() * scale
        vector = Line(coord_i - unit_vector , coord_i + unit_vector, color = ORANGE, buff=0)
        return vector    

