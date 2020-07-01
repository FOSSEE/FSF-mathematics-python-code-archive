from manimlib.imports import *

class Gradient(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() # creates a 3D Axis
        

        quadrant = ParametricSurface(
            lambda u, v: np.array([
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v),
                2*np.cos(u)
            ]),u_min=0,u_max=PI/3,v_min=0,v_max=PI/2,checkerboard_colors=[GREEN_C, GREEN_E],
            resolution=(15, 32)).scale(1)

        quadrant_curve = ParametricSurface(
            lambda u, v: np.array([
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v),
                2*np.cos(u)
            ]),u_min=34*DEGREES,u_max=38*DEGREES,v_min=0,v_max=PI/2,checkerboard_colors=[YELLOW_C, YELLOW_E],
            resolution=(15, 32)).scale(1)



        dot1 =Sphere(radius=0.05).move_to(np.array([1,1,0])).set_fill(YELLOW_C)
        dot2 =Sphere(radius=0.05).move_to(np.array([1,1,1.732])).set_fill(YELLOW_C)

        dot1_line = DashedLine(np.array([1,1,1.732]), np.array([0,2,2]), color = WHITE)
        dot1_lab = TextMobject(r"$P_0(x_0,y_0,z_0)$").move_to(np.array([0,2.1,2.2])).set_color(YELLOW_C).scale(0.6)
        #dot2_line = Line(np.array([0.8,0.8,0]), np.array([1,0.6,0]), color = PINK)

        positive_vector = Arrow(np.array([1,1,0]), np.array([0.5,0.5,0]), buff=0.001, color = BLUE_C)
        positive_gradient = Arrow(np.array([1,1,1.732]), np.array([0.5,0.5,1.9362]), buff=0.001, color = BLUE_C)
        positive_gradient_lab = TextMobject(r"$\nabla f$").move_to(np.array([0.5,0.3,0])).set_color(BLUE_C).scale(0.5)

        negative_vector = Arrow(np.array([1,1,0]), np.array([1.5,1.5,0]), buff=0.001, color = RED_C)
        negative_gradient = Arrow(np.array([1,1,1.732]), np.array([1.5,1.5,1.322]), buff=0.001, color = RED_C)
        negative_gradient_lab = TextMobject(r"$-\nabla f$").move_to(np.array([1.6,1.6,0])).set_color(RED_C).scale(0.5)

        positive_vector_line = DashedLine(np.array([0.8,0.8,0]), np.array([1,-2,0]), color = WHITE)
        positive_vector_lab = TextMobject(r"Most Rapid increase in $f$").move_to(np.array([1.6,-3.6,0])).set_color(BLUE_C).scale(0.6)
        negative_vector_line = DashedLine(np.array([1.2,1.2,0]), np.array([3,-1.5,0]), color = WHITE)
        negative_vector_lab = TextMobject(r"Most Rapid decrease in $f$").move_to(np.array([3.6,-3,0])).set_color(RED_C).scale(0.6)



        line1 = DashedLine(np.array([0.5,0.5,0]), np.array([0.5,0.5,1.9362]), color = BLUE_C)
        line2 = DashedLine(np.array([1,1,0]), np.array([1,1,1.732]), color = YELLOW_C)
        line3 = DashedLine(np.array([1.5,1.5,0]), np.array([1.5,1.5,1.322]), color = RED_C)

        curve_vector1 = Arrow(np.array([1,1,0]), np.array([1.5,0.5,0]), buff=0.001, color = YELLOW_C)
        curve_vector2 = Arrow(np.array([1,1,0]), np.array([0.5,1.5,0]), buff=0.001, color = YELLOW_C)

        curve_vector1_line = DashedLine(np.array([1.2,0.8,0]), np.array([1,2.5,0]), color = WHITE)
        curve_vector2_line = DashedLine(np.array([0.8,1.2,0]), np.array([1,2.5,0]), color = WHITE)
        curve_vector_lab = TextMobject(r"Zero Change in $f$").move_to(np.array([0.7,3.6,0])).set_color(PINK).scale(0.6)

        #square = Square(side_length = 0.5).rotate(45*DEGREES).move_to(np.array([1.025,0.975,0]))
        line_x = Line(np.array([0.8,0.8,0]), np.array([1,0.6,0]), color = PINK)
        line_y = Line(np.array([1.2,0.8,0]), np.array([1,0.6,0]), color = PINK)

        ninety_degree = VGroup(line_x, line_y)
        
        self.set_camera_orientation(phi=60* DEGREES, theta = 20*DEGREES)

        self.add(axes)

        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(np.array([0,0,3.7]))

        self.add_fixed_orientation_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1]) 

        self.play(ShowCreation(quadrant))
        self.wait()
        self.play(ShowCreation(dot1),  ShowCreation(dot2))
        self.wait()
        self.play(GrowArrow(positive_vector), GrowArrow(positive_gradient))
        self.wait()
        self.play(GrowArrow(negative_vector), GrowArrow(negative_gradient))
        self.wait()
        self.play(GrowArrow(line1), GrowArrow(line2), GrowArrow(line3))
        self.wait()
        self.play(ShowCreation(quadrant_curve))
        self.wait()
        self.play(GrowArrow(curve_vector1), GrowArrow(curve_vector2), ShowCreation(ninety_degree))
        self.wait()
        self.play(GrowArrow(dot1_line))
        self.add_fixed_orientation_mobjects(dot1_lab)
        self.wait()
        self.play(GrowArrow(curve_vector1_line), GrowArrow(curve_vector2_line))
        self.add_fixed_orientation_mobjects(curve_vector_lab)
        self.wait()
        self.add_fixed_orientation_mobjects(positive_gradient_lab, negative_gradient_lab)
        self.wait()
        self.play(GrowArrow(positive_vector_line), GrowArrow(negative_vector_line))
        self.add_fixed_orientation_mobjects(positive_vector_lab, negative_vector_lab)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(3)