from manimlib.imports import *

class Sphere(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() # creates a 3D Axis

        text3d = TextMobject(r"$f(x,y) \rightarrow Point(x,y,z)$")
        text3d1 = TextMobject(r"$f(x,y) \rightarrow Point(x,y, \sqrt{r^2 - x^2 - y^2})$")
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.scale(0.7)
        text3d1.scale(0.7)
        text3d.to_corner(UL)
        text3d1.to_corner(UL)
        text3d.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        text3d1.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE) 
        self.play(Write(text3d))
        self.wait(1)
        
        self.play(Transform(text3d,text3d1))
        self.add_fixed_in_frame_mobjects(text3d1)
        self.play(FadeOut(text3d))

        sphere = ParametricSurface(
            lambda u, v: np.array([
                2*np.sin(u)*np.cos(v),
                2*np.sin(u)*np.sin(v),
                2*np.cos(u)
            ]),u_min=0,u_max=PI,v_min=0,v_max=2*PI,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(1)


        #Experiment with circles by changing difference value of u and v
        '''
        sphere_points = [np.array([2*np.sin(u*DEGREES)*np.cos(v*DEGREES), 2*np.sin(u*DEGREES)*np.sin(v*DEGREES), 2*np.cos(u*DEGREES)]) for u in range(0, 185, 5) for v in range(0, 365, 5)]

        sphere_spheres = [Dot().move_to(pts) for pts in sphere_points]

        sphere = VGroup(*sphere_spheres)
        '''
        
        self.set_camera_orientation(phi=75 * DEGREES, theta = 45*DEGREES)

        self.add(axes)

        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(np.array([0,0,3.7]))

        self.add_fixed_orientation_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1]) 

        dot_x_y1 = Dot().scale(0.75).set_fill(RED_C).move_to(np.array([-1,1,0]))
        dot_x_y_z1 = Dot().scale(0.75).set_fill(RED_C).move_to(np.array([-1,1,1.414]))
        dot_x_y_z_1 = Dot().scale(0.75).set_fill(RED_C).move_to(np.array([-1,1,-1.414]))
        line1 = DashedLine(np.array([-1,1,-1.414]), np.array([-1,1,1.414]), color = YELLOW_C)

        point_x_y1 = TexMobject("(-1,1,0)").set_color(BLUE_C).move_to(np.array([-1.5,1.5,0])).scale(0.5)
        point_x_y_z1 = TexMobject("(-1,1,\\sqrt{r^2 - x^2 - y^2})").set_color(BLUE_C).move_to(np.array([-1.5,1.5,1.414])).scale(0.5)
        point_x_y_z1_2 = TexMobject("(-1,1,\\sqrt{4 - x^2 - y^2})").set_color(BLUE_C).move_to(np.array([-1.5,1.5,1.414])).scale(0.5)
        point_x_y_z1_3 = TexMobject("(-1,1,\\sqrt{4 - 1 - 1})").set_color(BLUE_C).move_to(np.array([-1.5,1.5,1.414])).scale(0.5)
        point_x_y_z1_4 = TexMobject("(-1,1,\\sqrt{2})").set_color(BLUE_C).move_to(np.array([-1.5,1.5,1.414])).scale(0.5)
        point_x_y_z1_5 = TexMobject("(-1,1,1.414)").set_color(BLUE_C).move_to(np.array([-1.5,1.5,1.414])).scale(0.5)

        point_x_y_z_1 = TexMobject("(-1,1,\\sqrt{r^2 - x^2 - y^2})").set_color(BLUE_C).move_to(np.array([-1.5,1.5,-1.414])).scale(0.5)
        point_x_y_z_1_2 = TexMobject("(-1,1,\\sqrt{4 - x^2 - y^2})").set_color(BLUE_C).move_to(np.array([-1.5,1.5,-1.414])).scale(0.5)
        point_x_y_z_1_3 = TexMobject("(-1,1,\\sqrt{4 - 1 - 1})").set_color(BLUE_C).move_to(np.array([-1.5,1.5,-1.414])).scale(0.5)
        point_x_y_z_1_4 = TexMobject("(-1,1,\\sqrt{2})").set_color(BLUE_C).move_to(np.array([-1.5,1.5,-1.414])).scale(0.5)
        point_x_y_z_1_5 = TexMobject("(-1,1,-1.414)").set_color(BLUE_C).move_to(np.array([-1.5,1.5,-1.414])).scale(0.5)

        
        self.play(ShowCreation(dot_x_y1))
        self.add_fixed_orientation_mobjects(point_x_y1)
        self.play(ShowCreation(dot_x_y_z1), ShowCreation(dot_x_y_z_1), ShowCreation(line1))
        self.add_fixed_orientation_mobjects(point_x_y_z1, point_x_y_z_1)
        self.wait(0.5)
        self.play(ReplacementTransform(point_x_y_z1,point_x_y_z1_2), ReplacementTransform(point_x_y_z_1,point_x_y_z_1_2))
        self.add_fixed_orientation_mobjects(point_x_y_z1_2, point_x_y_z_1_2)

        self.wait(0.5)
        self.play(ReplacementTransform(point_x_y_z1_2,point_x_y_z1_3), ReplacementTransform(point_x_y_z_1_2,point_x_y_z_1_3))
        self.add_fixed_orientation_mobjects(point_x_y_z1_3, point_x_y_z_1_3)
        self.wait(0.5)
        self.play(ReplacementTransform(point_x_y_z1_3,point_x_y_z1_4), ReplacementTransform(point_x_y_z_1_3,point_x_y_z_1_4))
        self.add_fixed_orientation_mobjects(point_x_y_z1_4, point_x_y_z_1_4)
        self.wait(0.5)
        self.play(ReplacementTransform(point_x_y_z1_4,point_x_y_z1_5), ReplacementTransform(point_x_y_z_1_4,point_x_y_z_1_5))
        self.add_fixed_orientation_mobjects(point_x_y_z1_5, point_x_y_z_1_5)
        


        dot_x_y2 = Dot().scale(0.75).set_fill(RED_C).move_to(np.array([0.5,-0.5,0]))
        dot_x_y_z2 = Dot().scale(0.75).set_fill(RED_C).move_to(np.array([0.5,-0.5,1.87]))
        dot_x_y_z_2 = Dot().scale(0.75).set_fill(RED_C).move_to(np.array([0.5,-0.5,-1.87]))
        line2 = DashedLine(np.array([0.5,-0.5,-1.87]), np.array([0.5,-0.5,1.87]), color = YELLOW_C)

        point_x_y2 = TexMobject("(0.5,-0.5,0)").set_color(BLUE_C).move_to(np.array([1.5,-1.5,0])).scale(0.5)
        point_x_y_z2 = TexMobject("(0.5,-0.5,\\sqrt{r^2 - x^2 - y^2})").set_color(BLUE_C).move_to(np.array([1.5,-1.5,1.87])).scale(0.5)
        point_x_y_z2_2 = TexMobject("(0.5,-0.5,\\sqrt{4 - x^2 - y^2})").set_color(BLUE_C).move_to(np.array([1.5,-1.5,1.87])).scale(0.5)
        point_x_y_z2_3 = TexMobject("(0.5,-0.5,\\sqrt{4 - 0.25 - 0.25})").set_color(BLUE_C).move_to(np.array([1.5,-1.5,1.87])).scale(0.5)
        point_x_y_z2_4 = TexMobject("(0.5,-0.5,\\sqrt{3.5})").set_color(BLUE_C).move_to(np.array([1.5,-1.5,1.87])).scale(0.5)
        point_x_y_z2_5 = TexMobject("(0.5,-0.5,1.87)").set_color(BLUE_C).move_to(np.array([1.5,-1.5,1.87])).scale(0.5)

        point_x_y_z_2 = TexMobject("(0.5,-0.5,\\sqrt{r^2 - x^2 - y^2})").set_color(BLUE_C).move_to(np.array([1.5,-1.5,-1.87])).scale(0.5)
        point_x_y_z_2_2 = TexMobject("(0.5,-0.5,\\sqrt{4 - x^2 - y^2})").set_color(BLUE_C).move_to(np.array([1.5,-1.5,-1.87])).scale(0.5)
        point_x_y_z_2_3 = TexMobject("(0.5,-0.5,\\sqrt{4 - 0.25 - 0.25})").set_color(BLUE_C).move_to(np.array([1.5,-1.5,-1.87])).scale(0.5)
        point_x_y_z_2_4 = TexMobject("(0.5,-0.5,\\sqrt{3.5})").set_color(BLUE_C).move_to(np.array([1.5,-1.5,-1.87])).scale(0.5)
        point_x_y_z_2_5 = TexMobject("(0.5,-0.5,-1.87)").set_color(BLUE_C).move_to(np.array([1.5,-1.5,-1.87])).scale(0.5)

        
        self.play(ShowCreation(dot_x_y2))
        self.add_fixed_orientation_mobjects(point_x_y2)
        self.play(ShowCreation(dot_x_y_z2), ShowCreation(dot_x_y_z_2), ShowCreation(line2))
        self.add_fixed_orientation_mobjects(point_x_y_z2, point_x_y_z_2)
        self.wait(0.5)
        self.play(ReplacementTransform(point_x_y_z2,point_x_y_z2_2), ReplacementTransform(point_x_y_z_2,point_x_y_z_2_2))
        self.add_fixed_orientation_mobjects(point_x_y_z2_2, point_x_y_z_2_2)

        self.wait(0.5)
        self.play(ReplacementTransform(point_x_y_z2_2,point_x_y_z2_3), ReplacementTransform(point_x_y_z_2_2,point_x_y_z_2_3))
        self.add_fixed_orientation_mobjects(point_x_y_z2_3, point_x_y_z_2_3)
        self.wait(0.5)
        self.play(ReplacementTransform(point_x_y_z2_3,point_x_y_z2_4), ReplacementTransform(point_x_y_z_2_3,point_x_y_z_2_4))
        self.add_fixed_orientation_mobjects(point_x_y_z2_4, point_x_y_z_2_4)
        self.wait(0.5)
        self.play(ReplacementTransform(point_x_y_z2_4,point_x_y_z2_5), ReplacementTransform(point_x_y_z_2_4,point_x_y_z_2_5))
        self.add_fixed_orientation_mobjects(point_x_y_z2_5, point_x_y_z_2_5)

        self.play(FadeOut(point_x_y1), FadeOut(point_x_y_z1_5), FadeOut(point_x_y_z_1_5), FadeOut(dot_x_y1), FadeOut(dot_x_y_z1), FadeOut(dot_x_y_z_1), FadeOut(line1))
        self.play(FadeOut(point_x_y2), FadeOut(point_x_y_z2_5), FadeOut(point_x_y_z_2_5), FadeOut(dot_x_y2), FadeOut(dot_x_y_z2), FadeOut(dot_x_y_z_2), FadeOut(line2))
        



        sphere_final = []
    
        for u in range(0, 180, 15): 
            sphere_points1 = [np.array([2*np.sin(u*DEGREES)*np.cos(v*DEGREES), 2*np.sin(u*DEGREES)*np.sin(v*DEGREES), 2*np.cos(u*DEGREES)]) for v in range(0, 370, 10)]
            sphere_dots1 = [Dot().scale(0.75).set_fill(RED_C).move_to(pts) for pts in sphere_points1]

            sphere_points2 = [np.array([2*np.sin((u+5)*DEGREES)*np.cos(v*DEGREES), 2*np.sin((u+5)*DEGREES)*np.sin(v*DEGREES), 2*np.cos((u+5)*DEGREES)]) for v in range(0, 370, 10)]
            sphere_dots2 = [Dot().scale(0.75).set_fill(RED_C).move_to(pts) for pts in sphere_points2]

            sphere_points3 = [np.array([2*np.sin((u+10)*DEGREES)*np.cos(v*DEGREES), 2*np.sin((u+10)*DEGREES)*np.sin(v*DEGREES), 2*np.cos((u+10)*DEGREES)]) for v in range(0, 370, 10)]
            sphere_dots3 = [Dot().scale(0.75).set_fill(RED_C).move_to(pts) for pts in sphere_points3]

            sphere_final = sphere_final + sphere_dots1 + sphere_dots2 + sphere_dots3

            sphere_dots = sphere_dots1 + sphere_dots2 + sphere_dots3
   
            sphere_with_dots = VGroup(*sphere_dots)
            self.play(ShowCreation(sphere_with_dots))

        sphere_final_with_dots = VGroup(*sphere_final)
        
        
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(3)
        self.play(ReplacementTransform(sphere_final_with_dots, sphere))
        self.wait(5)
        






        




        
        

        
