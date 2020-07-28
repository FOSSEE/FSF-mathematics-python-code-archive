from manimlib.imports import *

class PartialDeriv(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v),
                -2*2*np.sin(u)*np.sin(u)+2
            ]),u_min=0,u_max=PI/2,v_min=0,v_max=2*PI,checkerboard_colors=[PINK, PURPLE],
            resolution=(15, 32)).scale(1)

        paraboloid_copy1 = paraboloid.copy()
        paraboloid_copy2 = paraboloid.copy()

        paraboloid_x = ParametricSurface(
            lambda u, v: np.array([
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v),
                -2*2*np.sin(u)*np.sin(u)+2
            ]),u_min=0,u_max=PI/2,v_min=PI,v_max=2*PI,checkerboard_colors=[PINK, PURPLE],
            resolution=(15, 32)).scale(1)

        paraboloid_x_copy = paraboloid_x.copy()

        paraboloid_y = ParametricSurface(
            lambda u, v: np.array([
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v),
                -2*2*np.sin(u)*np.sin(u)+2
            ]),u_min=0,u_max=PI/2,v_min=PI/2,v_max=3*PI/2,checkerboard_colors=[PINK, PURPLE],
            resolution=(15, 32)).scale(1)

        parabola1 =ParametricFunction(
                lambda u : np.array([
                u,
                0,
                -(u*u) + 2
            ]),color="#006400",t_min=-2,t_max=2,
            )
        parabola2 =ParametricFunction(
                lambda u : np.array([
                0,
                u,
                -(u*u) + 2
            ]),color=BLUE_C,t_min=-2,t_max=2,
            )

        plane1 = Polygon(np.array([-2.2,0,-2.5]),np.array([2.2,0,-2.5]),np.array([2.2,0,2.5]),np.array([-2.2,0,2.5]),np.array([-2.2,0,-2.5]), color = GREEN, fill_color = GREEN, fill_opacity = 0.2)
        plane1_text = TextMobject(r"$y = 0$", color = GREEN_C).move_to(2*UP + 3.3*RIGHT)

        plane2 = Polygon(np.array([0,-2.2,-2.5]),np.array([0,2.2,-2.5]),np.array([0,2.2,2.5]),np.array([0,-2.2,2.5]),np.array([0,-2.2,-2.5]), color = BLUE, fill_color = BLUE, fill_opacity = 0.2)
        plane2_text = TextMobject(r"$x = 0$", color = BLUE_C).move_to(2*UP + 3.2*RIGHT)

        surface_eqn = TextMobject("Surface", r"$z = f(x,y) = 2 - x^2 - y^2$", color = YELLOW_C).scale(0.6).move_to(np.array([3*LEFT +3*UP]))
        surface_eqn[0].set_color(PINK)

        dot1 =Sphere(radius=0.08).move_to(np.array([-1,0,1]))
        dot1.set_fill(RED)
        line1 = Line(np.array([-1.55, 0,0]), np.array([-0.4, 0,2.2]), color = RED)
        lab_x = TextMobject(r"$f(x_0,y_0)$", color = RED).scale(0.7)
        para_lab_x = TextMobject(r"$f(x,y_0)$", color = "#006400").scale(0.7)
        tangent_line_x = TextMobject("Tangent Line", color = RED_C, buff = 0.4).scale(0.6).move_to(np.array([1.7*RIGHT +1.8*UP]))


        text1 = TextMobject(r"$\frac{\partial f}{\partial x}\vert_{(x_0,y_0)} = \frac{d}{dx}$", r"$f(x,y_0)$", r"$\vert_{x=x_0}$").scale(0.6)
        brace1 = Brace(text1[1], DOWN, buff = SMALL_BUFF, color = GREEN)
        t1 = brace1.get_text("Just depends on x")
        t1.scale(0.6)
        t1.set_color(GREEN)
        

        dot2 =Sphere(radius=0.08).move_to(np.array([0,1,1]))
        dot2.set_fill(RED)
        line2 = Line(np.array([0, 1.55,0]), np.array([0, 0.4,2.2]), color = RED)
        lab_y = TextMobject(r"$f(x_0,y_0)$", color = RED).scale(0.7)
        para_lab_y = TextMobject(r"$f(x_0,y)$", color = BLUE_C).scale(0.7)
        tangent_line_y = TextMobject("Tangent Line", color = RED_C, buff = 0.4).scale(0.6).move_to(np.array([1.7*RIGHT +1.8*UP]))

        text2 = TextMobject(r"$\frac{\partial f}{\partial y}\vert_{(x_0,y_0)} = \frac{d}{dy}$", r"$f(x_0,y)$", r"$\vert_{y=y_0}$").scale(0.6)
        brace2 = Brace(text2[1], DOWN, buff = SMALL_BUFF, color = GREEN)
        t2 = brace2.get_text("Just depends on y")
        t2.scale(0.6)
        t2.set_color(GREEN)

        text3 = TextMobject(r"$= \lim_{h \to 0} \frac{f(x_0+h,y_0) - f(x_0,y_0)}{h}$").scale(0.6)

        dot3 =Sphere(radius=0.08).move_to(np.array([-1.22,0,0.5]))
        dot3.set_fill(YELLOW_C)
        line3 = Line(np.array([-1.44,0,0]), np.array([-0.6,0,2.2]), color = YELLOW_C)
        lab_line3 = TextMobject(r"$f(x_0+h,y_0)$", color = YELLOW_C).scale(0.7)
        

        self.set_camera_orientation(phi=80 * DEGREES, theta = 0*DEGREES)
        #self.set_camera_orientation(phi=80 * DEGREES, theta = 20*DEGREES)
        #self.begin_ambient_camera_rotation(rate=0.3)


        self.add(axes)

        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(3.7*UP)

        self.add_fixed_in_frame_mobjects(axis[2])
        #self.add_fixed_orientation_mobjects(axis[2])
        
        self.play(Write(paraboloid))

        self.add_fixed_in_frame_mobjects(surface_eqn)
        #self.move_camera(phi=80* DEGREES,theta=110*DEGREES)
        self.move_camera(phi=80* DEGREES,theta=45*DEGREES)
        
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1])
        self.play(ShowCreation(plane1))
        self.add_fixed_in_frame_mobjects(plane1_text)
        self.wait()
        self.play(ReplacementTransform(paraboloid, paraboloid_x))

        lab_x.move_to(np.array([1.8*RIGHT +1.15*UP]))
        para_lab_x.move_to(np.array([1.3*LEFT +1.6*UP]))
        self.wait()
        self.play(FadeOut(plane1), FadeOut(plane1_text))
        self.play(ShowCreation(parabola1))
        self.add_fixed_in_frame_mobjects(para_lab_x)
        self.play(ShowCreation(dot1))
        self.add_fixed_in_frame_mobjects(lab_x)
        #self.play(ShowCreation(dot1))
        self.wait()
        self.play(ShowCreation(line1))
        self.add_fixed_in_frame_mobjects(tangent_line_x)
        self.wait()
   
        self.add_fixed_in_frame_mobjects(text1, brace1, t1)
        grp1 = VGroup(text1, brace1, t1)
        grp1.move_to(3*UP+3*RIGHT)
        self.play(Write(text1),GrowFromCenter(brace1), FadeIn(t1))
        self.wait()
        self.play(FadeOut(parabola1), FadeOut(line1), FadeOut(lab_x), FadeOut(para_lab_x), FadeOut(dot1), FadeOut(tangent_line_x),FadeOut(grp1))
        
        

        
        #self.move_camera(phi=80* DEGREES,theta=20*DEGREES)
        
        self.play(ReplacementTransform(paraboloid_x, paraboloid_copy1))
        self.wait()
        self.play(ShowCreation(plane2))
        self.add_fixed_in_frame_mobjects(plane2_text)
        self.wait()
        self.play(ReplacementTransform(paraboloid_copy1, paraboloid_y))
        
        lab_y.move_to(np.array([1.8*RIGHT +1.15*UP]))
        para_lab_y.move_to(np.array([1.3*LEFT +1.6*UP]))
        self.wait()
        self.play(FadeOut(plane2), FadeOut(plane2_text))
        self.play(ShowCreation(parabola2))
        self.add_fixed_in_frame_mobjects(para_lab_y)
        self.play(ShowCreation(dot2))
        self.add_fixed_in_frame_mobjects(lab_y)
        self.wait()
        self.play(ShowCreation(line2))
        self.add_fixed_in_frame_mobjects(tangent_line_y)
        self.wait()
   
        self.add_fixed_in_frame_mobjects(text2, brace2, t2)
        grp2 = VGroup(text2, brace2, t2)
        grp2.move_to(3*UP+3*RIGHT)
        self.play(Write(text2),GrowFromCenter(brace2), FadeIn(t2))
        self.wait()
        self.play(FadeOut(parabola2), FadeOut(line2), FadeOut(lab_y), FadeOut(para_lab_y), FadeOut(dot2), FadeOut(tangent_line_y), FadeOut(grp2))
        self.wait()

        
        #self.move_camera(phi=80* DEGREES,theta=105*DEGREES)
        self.play(ReplacementTransform(paraboloid_y, paraboloid_copy2))
        self.wait()

        
        self.play(ShowCreation(plane1))
        self.add_fixed_in_frame_mobjects(plane1_text)
        self.wait()
        self.play(ReplacementTransform(paraboloid_copy2, paraboloid_x_copy))
        
        lab_x.move_to(np.array([1.8*RIGHT +1.15*UP]))
        para_lab_x.move_to(np.array([1.3*LEFT +1.6*UP]))
        lab_line3.move_to(np.array([2.4*RIGHT +0.5*UP]))
        self.wait()
        self.play(FadeOut(plane1), FadeOut(plane1_text))
        self.play(ShowCreation(parabola1))
        self.add_fixed_in_frame_mobjects(para_lab_x)
        self.play(ShowCreation(dot1))
        self.add_fixed_in_frame_mobjects(lab_x)
        self.play(ShowCreation(dot3))
        self.add_fixed_in_frame_mobjects(lab_line3)
        self.wait()
        self.play(ShowCreation(line1))
        self.add_fixed_in_frame_mobjects(tangent_line_x)
        self.play(ShowCreation(line3))
        self.wait()
        
        
        self.add_fixed_in_frame_mobjects(text1,text3)
        text1.move_to(3*UP+3*RIGHT)
        text3.next_to(text1, DOWN)
        self.play(Write(text1),Write(text3))
        self.wait()
        self.play(FadeOut(parabola1), FadeOut(line1), FadeOut(lab_x), FadeOut(line3), FadeOut(lab_line3), FadeOut(para_lab_x), FadeOut(dot1), FadeOut(dot3), FadeOut(tangent_line_x), FadeOut(text1), FadeOut(text3))
        self.wait()
        




