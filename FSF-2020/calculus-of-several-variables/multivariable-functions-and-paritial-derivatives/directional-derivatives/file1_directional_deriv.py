from manimlib.imports import *

class GeomRepresen(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                3*np.sin(u)*np.cos(v),
                3*np.sin(u)*np.sin(v),
                -0.25*3*3*np.sin(u)*np.sin(u)+2
            ]),u_min=0,u_max=PI/4,v_min=0,v_max=2*PI, color = BLUE_C, fill_color = BLUE_C, fill_opacity = 0.7,
            resolution=(15, 32)).scale(1)

        parabola_curve = ParametricFunction(
                lambda u : np.array([
                u,
                -u,
                -0.5*(u*u)+2
            ]),color=PINK,t_min=-1.5,t_max=1.5,
            )

        circle = Circle(radius = 2.22 , color = BLACK, fill_color = BLUE_C, fill_opacity= 0.3, stroke_width=0.1)

        plane = Polygon(np.array([2.5,-2.5,0]),np.array([-2.5,2.5,0]),np.array([-2.5,2.5,2.5]),np.array([2.5,-2.5,2.5]),np.array([2.5,-2.5,0]), color = BLACK, fill_color = PINK, fill_opacity= 0.2, stroke_width=0.1)

        line = DashedLine(np.array([1,-1,0]), np.array([1,-1,1.5]), color = YELLOW_C) 

        tangent_line = Line(np.array([1.5,-1.5,1]), np.array([0.5,-0.5,2]), color = RED_C)

        vector = Arrow(np.array([1,-1,0]), np.array([0.5,-0.5,0]), buff=0.01, color = GREEN_C)

        dot1 =Sphere(radius=0.08).move_to(np.array([1,-1,0])).set_fill(YELLOW_C)
        dot2 =Sphere(radius=0.08).move_to(np.array([1,-1,1.5])).set_fill(YELLOW_C)

        dot1_lab = TextMobject(r"$P_0$").scale(0.6).move_to(np.array([1,-1,1.8])).set_color(RED_C)
        dot2_lab = TextMobject(r"$(x_0,y_0)$").scale(0.6).move_to(np.array([1.6,-1,0])).set_color(PURPLE)
        vector_lab = TextMobject(r"$\hat{u}$").scale(0.8).move_to(np.array([1.2,-0.5,0])).set_color(GREEN_C)
        domain_lab = TextMobject(r"$D$").scale(0.6).move_to(np.array([1,1,0])).set_color(GREEN_C)
        func_lab = TextMobject(r"$z = f(x,y)$").scale(0.6).move_to(1*UP + 2.8*RIGHT).set_color(BLUE_C)
        directional_deriv_lab = TextMobject(r"Slope = $D_{\hat{u}}f(x_0,y_0)$").scale(0.6).move_to(2.2*UP + 1.5*RIGHT).set_color(YELLOW_C)

        self.add(axes)

        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(np.array([0,0,3.7]))

        self.add_fixed_orientation_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1]) 

        self.set_camera_orientation(phi=65 * DEGREES, theta = 20*DEGREES)

        self.play(ShowCreation(paraboloid))
        self.add_fixed_in_frame_mobjects(func_lab)
        self.wait()

        #self.play(ShowCreation(circle))
        self.bring_to_front(circle)
        self.wait()
        self.add_fixed_orientation_mobjects(domain_lab)
        self.wait()

        self.play(ShowCreation(plane), ShowCreation(parabola_curve))
        self.play(ShowCreation(dot1), GrowArrow(line), ShowCreation(dot2))
        self.add_fixed_orientation_mobjects(dot1_lab)
        self.wait()
        self.add_fixed_orientation_mobjects(dot2_lab)
        self.wait()

        self.play(ShowCreation(tangent_line))
        self.add_fixed_in_frame_mobjects(directional_deriv_lab)
        self.wait()

        self.play(GrowArrow(vector))
        self.add_fixed_orientation_mobjects(vector_lab)
        self.wait()

        
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(3)

    
