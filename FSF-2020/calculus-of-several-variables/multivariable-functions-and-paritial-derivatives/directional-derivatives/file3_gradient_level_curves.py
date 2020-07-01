from manimlib.imports import *

class GradientLevelCurves(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                -u*u+2
            ]),u_min=-1.414,u_max=1.414,v_min=0,v_max=2*PI, color = BLUE_C, fill_color = BLUE_C, fill_opacity = 0.1,
            resolution=(15, 32)).scale(1)
        
        plane_0 = Polygon(np.array([2,-2,0]),np.array([2,2,0]),np.array([-2,2,0]),np.array([-2,-2,0]),np.array([2,-2,0]), color = BLUE_E, fill_color = BLUE_E, fill_opacity = 0.3)
        plane_0_lab = TextMobject("C = 0").move_to(0.4*UP+3.2*RIGHT).set_color(BLUE_E).scale(0.6)
        circle_0 = Circle(radius = 1.414 , color = BLUE_E)
        circle_0_lab = TextMobject("0").move_to(1.1*DOWN+1.1*RIGHT).set_color(BLUE_E).scale(0.6)

        plane_0_5 = Polygon(np.array([2,-2,0.5]),np.array([2,2,0.5]),np.array([-2,2,0.5]),np.array([-2,-2,0.5]),np.array([2,-2,0.5]), color = GREEN_C, fill_color = GREEN_C, fill_opacity = 0.3)
        plane_0_5_lab = TextMobject("C = 0.5").move_to(0.8*UP+3.4*RIGHT).set_color(GREEN_C).scale(0.6)
        circle_0_5 = Circle(radius = 1.224 , color = GREEN_C)
        circle_0_5_lab = TextMobject("0.5").move_to(0.9*DOWN+0.9*RIGHT).set_color(GREEN_C).scale(0.6)
        circle_0_5_copy = circle_0_5.copy().move_to(np.array([0,0,0.5]))

        plane_1 = Polygon(np.array([2,-2,1]),np.array([2,2,1]),np.array([-2,2,1]),np.array([-2,-2,1]),np.array([2,-2,1]), color = YELLOW_C, fill_color = YELLOW_C, fill_opacity = 0.3)
        plane_1_lab = TextMobject("C = 1").move_to(1.2*UP+3.3*RIGHT).set_color(YELLOW_C).scale(0.6)
        circle_1 = Circle(radius = 1 , color = YELLOW_C)
        circle_1_lab = TextMobject("1").move_to(0.7*DOWN+0.7*RIGHT).set_color(YELLOW_C).scale(0.6)
        circle_1_copy = circle_1.copy().move_to(np.array([0,0,1]))

        plane_1_5 = Polygon(np.array([2,-2,1.5]),np.array([2,2,1.5]),np.array([-2,2,1.5]),np.array([-2,-2,1.5]),np.array([2,-2,1.5]), color = ORANGE, fill_color = ORANGE, fill_opacity = 0.3)
        plane_1_5_lab = TextMobject("C = 1.5").move_to(1.7*UP+3.4*RIGHT).set_color(ORANGE).scale(0.6)
        circle_1_5 = Circle(radius = 0.707 , color = ORANGE)
        circle_1_5_lab = TextMobject("1.5").move_to(0.5*DOWN+0.5*RIGHT).set_color(ORANGE).scale(0.6)
        circle_1_5_copy = circle_1_5.copy().move_to(np.array([0,0,1.5]))

        plane_2 = Polygon(np.array([2,-2,2]),np.array([2,2,2]),np.array([-2,2,2]),np.array([-2,-2,2]),np.array([2,-2,2]), color = RED_C, fill_color = RED_C, fill_opacity = 0.3)
        plane_2_lab = TextMobject("C = 2").move_to(2.1*UP+3.3*RIGHT).set_color(RED_C).scale(0.6)
        dot_2 = Dot().set_fill(RED_C)
        circle_2_lab = TextMobject("2").move_to(0.2*DOWN+0.2*RIGHT).set_color(RED_C).scale(0.6)
        dot_2_copy = dot_2.copy().move_to(np.array([0,0,2]))

        vector1 = Arrow(np.array([0.99,-0.99,0]), np.array([0.865,-0.865,0.5]), buff=0.01, color = RED_C).set_stroke(width=3)
        gradient1 = Arrow(np.array([0.99,-0.99,0]), np.array([0.865,-0.865,0]), buff=0.01, color = RED_C).set_stroke(width=3)

        vector2 = Arrow(np.array([0.865,-0.865,0.5]), np.array([0.707,-0.707,1]), buff=0.01, color = RED_C).set_stroke(width=3)
        gradient2 = Arrow(np.array([0.865,-0.865,0]), np.array([0.707,-0.707,0]), buff=0.01, color = RED_C).set_stroke(width=3)

        vector3 = Arrow(np.array([0.707,-0.707,1]), np.array([0.499,-0.499,1.5]), buff=0.01, color = RED_C).set_stroke(width=3)
        gradient3 = Arrow(np.array([0.707,-0.707,0]), np.array([0.499,-0.499,0]), buff=0.01, color = RED_C).set_stroke(width=3)

        vector4 = Arrow(np.array([0.499,-0.499,1.5]), np.array([0,0,2]), buff=0.01, color = RED_C).set_stroke(width=3)
        gradient4 = Arrow(np.array([0.499,-0.499,0]), np.array([0,0,0]), buff=0.01, color = RED_C).set_stroke(width=3)


        self.set_camera_orientation(phi=80 * DEGREES, theta = 0*DEGREES)
        #self.set_camera_orientation(phi=45 * DEGREES, theta = -20*DEGREES)

        self.add(axes)

        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(np.array([0,0,3.7]))

        self.add_fixed_orientation_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1]) 
        
        self.play(Write(paraboloid))
        self.wait()
        self.play(ShowCreation(plane_0), ShowCreation(circle_0))
        self.add_fixed_in_frame_mobjects(plane_0_lab)
        self.wait()
        self.play(ShowCreation(plane_0_5), ShowCreation(circle_0_5_copy), ShowCreation(circle_0_5))
        self.add_fixed_in_frame_mobjects(plane_0_5_lab)
        self.wait()
        self.play(ShowCreation(plane_1), ShowCreation(circle_1_copy), ShowCreation(circle_1))
        self.add_fixed_in_frame_mobjects(plane_1_lab)
        self.wait()
        self.play(ShowCreation(plane_1_5), ShowCreation(circle_1_5_copy), ShowCreation(circle_1_5))
        self.add_fixed_in_frame_mobjects(plane_1_5_lab)
        self.wait()
        self.play(ShowCreation(plane_2), ShowCreation(dot_2_copy), ShowCreation(dot_2))
        self.add_fixed_in_frame_mobjects(plane_2_lab)
        self.wait()
        self.move_camera(phi=60 * DEGREES, theta = 30*DEGREES,run_time=3)
        self.play(FadeOut(plane_0), FadeOut(plane_0_lab), FadeOut(plane_0_5), FadeOut(plane_0_5_lab), FadeOut(plane_1), FadeOut(plane_1_lab), FadeOut(plane_1_5), FadeOut(plane_1_5_lab), FadeOut(plane_2), FadeOut(plane_2_lab))
        self.play(FadeOut(circle_0_5_copy), FadeOut(circle_1_copy), FadeOut(circle_1_5_copy), FadeOut(dot_2_copy))

        self.move_camera(phi=45 * DEGREES, theta = -20*DEGREES,run_time=3)
        self.play(Write(vector1), Write(gradient1))
        self.wait()
        self.play(Write(vector2), Write(gradient2))
        self.wait()
        self.play(Write(vector3), Write(gradient3))
        self.wait()
        self.play(Write(vector4), Write(gradient4))
        self.wait()
        self.move_camera(phi=0 * DEGREES, theta = 0*DEGREES,run_time=3)
        self.play(FadeOut(paraboloid))
        self.play(FadeOut(vector1), FadeOut(vector2), FadeOut(vector3), FadeOut(vector4))
        self.wait()
        self.add_fixed_in_frame_mobjects(circle_0_lab, circle_0_5_lab, circle_1_lab, circle_1_5_lab,circle_2_lab)
        self.wait(4)
        