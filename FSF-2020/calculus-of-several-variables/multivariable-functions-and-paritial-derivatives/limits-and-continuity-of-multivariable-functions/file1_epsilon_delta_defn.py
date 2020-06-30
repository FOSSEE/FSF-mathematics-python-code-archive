from manimlib.imports import *

class EpsilonDelta(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() # creates a 3D Axis
        

        sphere = ParametricSurface(
            lambda u, v: np.array([
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v),
                2*np.cos(u)
            ]),u_min=0,u_max=PI/4,v_min=0,v_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)
        #sphere.shift(0.5*RIGHT+0.5*UP)

        #self.set_camera_orientation(phi=0*DEGREES,theta=270*DEGREES)
        self.set_camera_orientation(phi=75 * DEGREES)
        


        circle = Circle(radius= 0.4,color = GREEN)
        circle.shift(0.5*RIGHT+0.5*UP)

        line1 = DashedLine(np.array([0.5, 0.1,0]), np.array([0.5, 0.1,2.1]), color = BLUE_E)
        line2 = DashedLine(np.array([0.5, 0.9,0]), np.array([0.5, 0.9,1.7]), color = BLUE_E)
        line3 = DashedLine(np.array([0, 0,2.1]), np.array([0.5, 0.1,2.1]), color = YELLOW_C)
        line4 = DashedLine(np.array([0, 0,1.7]), np.array([0.5, 0.9,1.7]), color = YELLOW_C)

        dot1 = Sphere()
        dot1.scale(0.01)
        dot1.move_to(np.array([0,0,1.9]))
        dot1.set_fill(BLUE_E)

        temp_func1 = TextMobject(r"$L$")
        temp_func1.scale(0.6)
        temp_func1.set_color(BLUE_E)

        dot2 = Sphere()
        dot2.scale(0.01)
        dot2.move_to(np.array([0,0,1.7]))
        dot2.set_fill(PURPLE)

        temp_func2 = TextMobject(r"$L - \epsilon$")
        temp_func2.scale(0.6)
        temp_func2.set_color(PURPLE)

        dot3 = Sphere()
        dot3.scale(0.01)
        dot3.move_to(np.array([0,0,2.1]))
        dot3.set_fill(PURPLE)

        temp_func3 = TextMobject(r"$L + \epsilon$")
        temp_func3.scale(0.6)
        temp_func3.set_color(PURPLE)

        self.add(axes)

        self.play(ShowCreation(dot1))
        self.add_fixed_in_frame_mobjects(temp_func1)
        temp_func1.move_to(1.9*UP)
        self.play(Write(temp_func1))

        self.play(ShowCreation(dot2))
        self.add_fixed_in_frame_mobjects(temp_func2)
        temp_func2.move_to(1.7*UP)
        self.play(Write(temp_func2))

        self.play(ShowCreation(dot3))
        self.add_fixed_in_frame_mobjects(temp_func3)
        temp_func3.move_to(2.1*UP)
        self.play(Write(temp_func3))


        circle_center = Sphere()
        circle_center.scale(0.05)
        circle_center.move_to(np.array([0.5,0.5,0]))
        circle_center.set_fill(GREEN)

        temp_circle_center = TextMobject(r"$(a,b,0)$")
        temp_circle_center.scale(0.5)
        temp_circle_center.set_color(GREEN)

        curve_circle_center = Sphere()
        curve_circle_center.scale(0.05)
        curve_circle_center.move_to(np.array([0.5,0.5,1.9]))
        curve_circle_center.set_fill(BLUE_E)

        temp_curve_circle_center = TextMobject(r"$(a,b,L)$")
        temp_curve_circle_center.scale(0.5)
        temp_curve_circle_center.set_color(BLUE)

        delta_lab = TextMobject(r"$\delta - disk$")
        delta_lab.scale(0.5)
        delta_lab.set_color(PINK)   

        self.play(ShowCreation(circle_center))
        self.add_fixed_in_frame_mobjects(temp_circle_center)
        temp_circle_center.move_to(1.5*RIGHT)
        self.play(Write(temp_circle_center))

        self.play(ShowCreation(curve_circle_center))
        self.add_fixed_in_frame_mobjects(temp_curve_circle_center)
        temp_curve_circle_center.move_to(1.9*UP+1*RIGHT)
        self.play(Write(temp_curve_circle_center))


        self.add_fixed_in_frame_mobjects(delta_lab)
        delta_lab.move_to(0.4*DOWN+1.7*RIGHT)
        self.play(Write(delta_lab))





        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(Write(sphere))
        self.play(ShowCreation(circle), ShowCreation(line1), ShowCreation(line2))
        self.play(ShowCreation(line3), ShowCreation(line4))
        self.wait(8)
