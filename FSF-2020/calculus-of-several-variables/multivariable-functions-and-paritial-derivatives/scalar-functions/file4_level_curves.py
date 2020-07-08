from manimlib.imports import *

class LevelCurves(ThreeDScene):
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

        level_curves_line1 = DashedLine(np.array([0,-1.414,0]),np.array([0,-2,1]), color = WHITE)
        level_curves_line2 = DashedLine(np.array([0,-1.224,0.5]),np.array([0,-2,1]), color = WHITE)
        level_curves_line3 = DashedLine(np.array([0,-1,1]),np.array([0,-2,1]), color = WHITE)
        level_curves_line4 = DashedLine(np.array([0,-0.707,1.5]),np.array([0,-2,1]), color = WHITE)
        level_curves_line5 = DashedLine(np.array([0,0,2]),np.array([0,-2,1]), color = WHITE)

        level_curves = TextMobject("Level Curves").move_to(1.4*UP+3*LEFT).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE).scale(0.8)


        contour_line1 = DashedLine(np.array([0,-1.414,0]),np.array([0,-2,1]), color = WHITE)
        contour_line2 = DashedLine(np.array([0,-1.224,0]),np.array([0,-2,1]), color = WHITE)
        contour_line3 = DashedLine(np.array([0,-1,0]),np.array([0,-2,1]), color = WHITE)
        contour_line4 = DashedLine(np.array([0,-0.707,0]),np.array([0,-2,1]), color = WHITE)
        contour_line5 = DashedLine(np.array([0,0,0]),np.array([0,-2,1]), color = WHITE)

        contours = TextMobject("Contours").move_to(1.4*UP+2.7*LEFT).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE).scale(0.8)

        
        topic = TextMobject("Contour Plot").move_to(3*UP+3*LEFT).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE).scale(0.8)

        self.set_camera_orientation(phi=80 * DEGREES, theta = 0*DEGREES)
        #self.set_camera_orientation(phi=0 * DEGREES, theta = 0*DEGREES)

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
        
        self.play(GrowArrow(level_curves_line1), GrowArrow(level_curves_line2), GrowArrow(level_curves_line3), GrowArrow(level_curves_line4), GrowArrow(level_curves_line5))
        self.add_fixed_in_frame_mobjects(level_curves)
        self.wait()
        self.play(FadeOut(level_curves_line1), FadeOut(level_curves_line2), FadeOut(level_curves_line3), FadeOut(level_curves_line4), FadeOut(level_curves_line5), FadeOut(level_curves))
        self.play(FadeOut(circle_0_5_copy), FadeOut(circle_1_copy), FadeOut(circle_1_5_copy), FadeOut(dot_2_copy))
        self.wait()

        self.play(GrowArrow(contour_line1), GrowArrow(contour_line2), GrowArrow(contour_line3), GrowArrow(contour_line4), GrowArrow(contour_line5))
        self.add_fixed_in_frame_mobjects(contours)
        self.wait()
        self.play(FadeOut(contour_line1), FadeOut(contour_line2), FadeOut(contour_line3), FadeOut(contour_line4), FadeOut(contour_line5), FadeOut(contours))
        

        self.move_camera(phi=0 * DEGREES, theta = 0*DEGREES,run_time=3)
        self.play(FadeOut(paraboloid))
        self.wait()

        self.add_fixed_in_frame_mobjects(circle_0_lab, circle_0_5_lab, circle_1_lab, circle_1_5_lab,circle_2_lab)
        self.add_fixed_in_frame_mobjects(topic)
        self.wait(3)