from manimlib.imports import *

class ClariantRule(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 
       
        function = ParametricSurface(
            lambda u, v: np.array([
                3.5*np.sin(u)*np.cos(v),
                3.5*np.sin(u)*np.sin(v),
                3.5*3.5*np.sin(u)*np.sin(u)*(1+2*np.sin(v)*np.sin(v))*np.exp(1 - 3.5*3.5*np.sin(u)*np.sin(u) ) 
            ]),u_min=0,u_max=PI,v_min=0,v_max=2*PI, color = BLUE_C, fill_color = BLUE_C, fill_opacity = 0.1,
            resolution=(15, 32)).scale(1)

        function_x = ParametricSurface(
            lambda u, v: np.array([
                3.5*np.sin(u)*np.cos(v),
                3.5*np.sin(u)*np.sin(v),
                -4*3.5*3.5*3.5*np.sin(u)*np.sin(u)*np.sin(u)*(2*np.sin(v)*np.sin(v))*np.exp(1 - 3.5*3.5*np.sin(u)*np.sin(u)) 
            ]),u_min=0,u_max=PI,v_min=0,v_max=2*PI, color = BLUE_C, fill_color = BLUE_C, fill_opacity = 0.1,
            resolution=(15, 32)).scale(1)
        
        func_x =ParametricFunction(
                lambda u : np.array([
                u,
                -1,
                (u*u )*np.exp(1-u*u)
            ]),color=RED_E,t_min=-3.5,t_max=3.5,
            )
    
        func_y =ParametricFunction(
                lambda u : np.array([
                0,
                u,
                (3*u*u)*np.exp(1-u*u)
            ]),color=PINK,t_min=-3.5,t_max=3.5,
            )
       
        plane_x = Polygon(np.array([-3.5,-1,-3]),np.array([3.5,-1,-3]),np.array([3.5,-1,3]),np.array([-3.5,-1,3]),np.array([-3.5,-1,-3]), color = YELLOW_E, fill_color = YELLOW_B, fill_opacity = 0.1)
        plane_text_x = TextMobject(r"$y = -1$", color = YELLOW_C).move_to(np.array([5,0,2.7])).scale(0.7)

        plane_y = Polygon(np.array([0,-3.5,-3]),np.array([0,3.5,-3]),np.array([0,3.5,3]),np.array([0,-3.5,3]),np.array([0,-3.5,-3]), color = GREEN_E, fill_color = GREEN_B, fill_opacity = 0.1)
        plane_text_y = TextMobject(r"$x = 0$", color = GREEN_C).move_to(np.array([0,4,2.7])).scale(0.7)
        
        surface_eqn = TextMobject("Surface", r"$z = f(x,y) = (x^2 + 3y^2)e^{(1 - x^2 - y^2)}$", color = YELLOW_C).scale(0.6).move_to(np.array([4.1*LEFT+3.8*UP]))
        surface_eqn[0].set_color(BLUE_C)
        number_plane = NumberPlane()

        line = Line(np.array([0,-1,3]), np.array([0,-1,-3]), color = PURPLE)

        self.set_camera_orientation(phi=60 * DEGREES, theta = 45*DEGREES)

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
        self.play(ShowCreation(number_plane))

        self.add_fixed_in_frame_mobjects(surface_eqn)

        self.play(ShowCreation(plane_x), ShowCreation(plane_y), ShowCreation(line))
        self.add_fixed_orientation_mobjects(plane_text_x, plane_text_y)

        self.move_camera(phi=0* DEGREES,theta=45*DEGREES)
        self.wait(3)
        self.move_camera(phi=60* DEGREES,theta=45*DEGREES)
        #self.play(ShowCreation(func_x), ShowCreation(func_y))
        
        dot_x = Dot().rotate(PI/2).set_color(YELLOW_C)
        alpha_x = ValueTracker(0)
        vector_x = self.get_tangent_vector(alpha_x.get_value(),func_x,scale=1.5)
        dot_x.add_updater(lambda m: m.move_to(vector_x.get_center()))
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
        dot_y = Dot().rotate(PI/2).set_color(GREEN_E)
        alpha_y = ValueTracker(0)
        vector_y = self.get_tangent_vector(alpha_y.get_value(),func_y,scale=1.5)
        dot_y.add_updater(lambda m: m.move_to(vector_y.get_center()))
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
        self.add(vector_x,dot_x)
        
        self.play(alpha_x.increment_value, 1, run_time=5, rate_func=linear)

        self.add(vector_y,dot_y)
        self.play(alpha_y.increment_value, 1, run_time=5, rate_func=linear)

        self.wait(2)
        

    def get_tangent_vector(self, proportion, curve, dx=0.001, scale=1):
        coord_i = curve.point_from_proportion(proportion)
        coord_f = curve.point_from_proportion(proportion + dx)
        reference_line = Line(coord_i,coord_f)
        unit_vector = reference_line.get_unit_vector() * scale
        vector = Line(coord_i - unit_vector, coord_i + unit_vector, color = ORANGE, buff=0)
        return vector
        


