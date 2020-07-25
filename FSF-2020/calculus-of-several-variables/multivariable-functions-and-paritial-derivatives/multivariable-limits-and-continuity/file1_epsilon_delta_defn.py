from manimlib.imports import *

class EpsilonDelta(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        sphere = ParametricSurface(
            lambda u, v: np.array([
                3*np.sin(u)*np.cos(v),
                3*np.sin(u)*np.sin(v),
                3*np.cos(u)
            ]),u_min=0,u_max=PI/4,v_min=PI/2,v_max=PI,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(1)

        delta_circle_boundary = Circle(radius= 0.3, color = GREEN_E).shift(1*LEFT+1*UP)

        circle = [np.array([0.3*np.cos(i*DEGREES)-1, 0.3*np.sin(i*DEGREES)+1, 0]) for i in range(361)]

        circle_above = [np.array([0.3*np.cos(i*DEGREES)-1, 0.3*np.sin(i*DEGREES)+1, np.sqrt(9 - (0.3*np.cos(i*DEGREES)-1)**2 - (0.3*np.sin(i*DEGREES)+1)**2)]) for i in range(361)]

        delta_circle = Polygon(*circle, color = BLACK, fill_color = GREEN_E, fill_opacity= 0.5, stroke_width=0.1)

        delta_circle_above = Polygon(*circle_above, color = BLACK, fill_color = GREEN_E, fill_opacity= 0.5, stroke_width=0.1)

        dot_circle = Dot().scale(0.6).move_to(np.array([-1,1,0])).set_fill(PINK)
        
        dot_surface = Dot().rotate(-PI/3).scale(0.7).move_to(np.array([-1.2,1.2,2.7])).set_fill(PINK)



        #Creating cylinder 
        ######
        '''
        cylinder = []
        cylinder.append(np.array([-0.7, 1, 0])) 
        cylinder.append(np.array([-0.7, 1, np.sqrt(9 - (0.7)**2 - 1)])) 
       

        #circle_above_reverse = [ele for ele in reversed(circle_above)]
        circle_above_reverse = [np.array([0.3*np.cos(i*DEGREES)-1, 0.3*np.sin(i*DEGREES)+1, np.sqrt(9 - (0.3*np.cos(i*DEGREES)-1)**2 - (0.3*np.sin(i*DEGREES)+1)**2)]) for i in range(181)]
        
        cylinder = cylinder + circle_above_reverse

        #cylinder.append(np.array([-0.7, 1, np.sqrt(9 - (0.7)**2 - 1)]))
        cylinder.append(np.array([0.3*np.cos(180)-1, 0.3*np.sin(180)+1, np.sqrt(9 - (0.3*np.cos(180)-1)**2 - (0.3*np.sin(180)+1)**2)]))
        #cylinder.append(np.array([-0.7, 1, 0]))  
        cylinder.append(np.array([0.3*np.cos(180)-1, 0.3*np.sin(180)+1, 0]))

        
        cylinder = cylinder + [np.array([0.3*np.cos(i*DEGREES)-1, 0.3*np.sin(i*DEGREES)+1, 0]) for i in range(180,-1,-1)]
        #y_x_2.append(np.array([-3, 9, 0]))
        #cylinder.append(np.array([-0.7, 1, 0]))

        cylinder_plane = Polygon(*cylinder, color = BLACK, fill_color = YELLOW_C, fill_opacity= 0.3, stroke_width=0.1)
        #plane_y_x_2_text = TextMobject(r"$y = x^2$", color = RED_C).move_to(np.array([5,0,2]))
        
        #cylinder_plane2 = cylinder_plane.copy().rotate(2*PI)

        cylinder = []
        cylinder.append(np.array([-0.7, 1, 0])) 
        cylinder.append(np.array([-0.7, 1, np.sqrt(9 - (0.7)**2 - 1)])) 
       

        #circle_above_reverse = [ele for ele in reversed(circle_above)]
        circle_above_reverse = [np.array([0.3*np.cos(i*DEGREES)-1, 0.3*np.sin(i*DEGREES)+1, np.sqrt(9 - (0.3*np.cos(i*DEGREES)-1)**2 - (0.3*np.sin(i*DEGREES)+1)**2)]) for i in range(360, 179, -1)]
        
        cylinder = cylinder + circle_above_reverse

        #cylinder.append(np.array([-0.7, 1, np.sqrt(9 - (0.7)**2 - 1)]))
        cylinder.append(np.array([0.3*np.cos(180)-1, 0.3*np.sin(180)+1, np.sqrt(9 - (0.3*np.cos(180)-1)**2 - (0.3*np.sin(180)+1)**2)]))
        #cylinder.append(np.array([-0.7, 1, 0]))  
        cylinder.append(np.array([0.3*np.cos(180)-1, 0.3*np.sin(180)+1, 0]))

        
        cylinder = cylinder + [np.array([0.3*np.cos(i*DEGREES)-1, 0.3*np.sin(i*DEGREES)+1, 0]) for i in range(180,360)]
        #y_x_2.append(np.array([-3, 9, 0]))
        #cylinder.append(np.array([-0.7, 1, 0]))

        cylinder_plane = Polygon(*cylinder, color = BLACK, fill_color = YELLOW_C, fill_opacity= 0.3, stroke_width=0.1)
        
        ######
        '''


        lines = [Line(circle[i], circle_above[i], color = BLUE_B, opacity=0.01, stroke_width=0.1) for i in range(0,len(circle),1)]
        lines_group = VGroup(*lines)

        line_epsilon_first = DashedLine(np.array([-1, 1, 0]), np.array([-1, 1, np.sqrt(7)]), color = YELLOW_C)




        self.add(axes)

        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(np.array([0,0,3.7]))

        self.add_fixed_orientation_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1]) 

        self.set_camera_orientation(distance=200,phi=70*DEGREES,theta=135*DEGREES)

        self.play(ShowCreation(sphere))
        self.wait()

        text1 = TexMobject("\\sqrt{(x-a)^2+(y-b)^2}", color = GREEN_E).scale(0.7).to_corner(UR)

        self.play(ShowCreation(delta_circle_boundary), ShowCreation(dot_circle))
        self.add_fixed_in_frame_mobjects(text1)
        self.wait(2)

        text2 = TexMobject("\\sqrt{(x-a)^2+(y-b)^2}", "<", "\\delta ", color = GREEN_E).scale(0.7).to_corner(UR)
        text2[1].set_color(YELLOW_C)
        text2[2].set_color(ORANGE)

        self.play(FadeOut(text1), FadeOut(delta_circle_boundary), ShowCreation(delta_circle))
        self.bring_to_front(dot_circle)
        self.add_fixed_in_frame_mobjects(text2)

        #self.play(ShowCreation(sphere), ShowCreation(delta_circle), ShowCreation(delta_circle_above)) 

        temp_circle_center = TextMobject(r"$(a,b,0)$").scale(0.6).set_color(PINK).move_to(1.7*LEFT+1.1*UP)
        self.add_fixed_orientation_mobjects(temp_circle_center)
        self.wait()

        delta_lab = TextMobject(r"$\delta$",  "disk").scale(0.5).move_to(0.6*LEFT+1.7*UP)
        delta_lab[0].set_color(ORANGE).scale(1.3)
        delta_lab[1].set_color(GREEN_E)

        self.add_fixed_orientation_mobjects(delta_lab)

        self.play(ShowCreation(lines_group), ShowCreation(line_epsilon_first))
        self.bring_to_front(delta_circle_above, dot_surface)
        temp_curve_circle_center = TextMobject(r"$(a,b,L)$").scale(0.6).set_color(PINK).move_to(np.array([-1.7,1.1,2.7]))
        self.add_fixed_orientation_mobjects(temp_curve_circle_center)

        self.move_camera(distance = 5, phi=50*DEGREES,theta=135*DEGREES)
        self.wait(3)
        
        
        self.play(FadeOut(dot_surface))

        self.move_camera(distance=200,phi=0* DEGREES,theta=135*DEGREES)
        self.wait()

        self.move_camera(distance=10,phi=80* DEGREES,theta=225*DEGREES)
        self.wait()
        
        self.play(FadeOut(delta_lab), FadeOut(temp_circle_center), FadeOut(temp_curve_circle_center), FadeOut(text2))
        self.wait()


        line_epsilon1 = DashedLine(np.array([0.3*np.cos(315*DEGREES)-1, 0.3*np.sin(315*DEGREES)+1, np.sqrt(9 - (0.3*np.cos(315*DEGREES)-1)**2 - (0.3*np.sin(315*DEGREES)+1)**2)]), 
                                   np.array([0, 0, np.sqrt(9 - (0.3*np.cos(315*DEGREES)-1)**2 - (0.3*np.sin(315*DEGREES)+1)**2)]), color = YELLOW_C)

        line_epsilon2 = DashedLine(np.array([0.3*np.cos(135*DEGREES)-1, 0.3*np.sin(135*DEGREES)+1, np.sqrt(9 - (0.3*np.cos(135*DEGREES)-1)**2 - (0.3*np.sin(135*DEGREES)+1)**2)]), 
                                   np.array([0, 0, np.sqrt(9 - (0.3*np.cos(135*DEGREES)-1)**2 - (0.3*np.sin(135*DEGREES)+1)**2)]), color = YELLOW_C)

        line_epsilon = DashedLine(np.array([-1, +1, np.sqrt(7)]), np.array([0, 0, np.sqrt(7)]), color = YELLOW_C)


        self.play(ShowCreation(line_epsilon1), ShowCreation(line_epsilon2), ShowCreation(line_epsilon))
        self.wait()    

        self.move_camera(distance=5,phi=75* DEGREES,theta=325*DEGREES)



        dot_L_epsilon1 = Polygon(*[np.array([0.05*np.cos(i*DEGREES),0,0.05*np.sin(i*DEGREES)]) for i in range(361)], color = "#000080", fill_color = "#000080", fill_opacity = 1).rotate(PI/4).move_to(np.array([0,0,np.sqrt(9 - (0.3*np.cos(315*DEGREES)-1)**2 - (0.3*np.sin(315*DEGREES)+1)**2)]))

        dot_L_epsilon2 = Polygon(*[np.array([0.05*np.cos(i*DEGREES),0,0.05*np.sin(i*DEGREES)]) for i in range(361)], color = "#000080", fill_color = "#000080", fill_opacity = 1).rotate(PI/4).move_to(np.array([0,0,np.sqrt(9 - (0.3*np.cos(135*DEGREES)-1)**2 - (0.3*np.sin(135*DEGREES)+1)**2)]))
        
        dot_L = Polygon(*[np.array([0.05*np.cos(i*DEGREES),0,0.05*np.sin(i*DEGREES)]) for i in range(361)], color = "#006400", fill_color = "#006400", fill_opacity = 1).rotate(PI/4).move_to(np.array([0,0,np.sqrt(7)]))

        dot_L_epsilon1_lab = TextMobject(r"$L$", r"$-$", r"$\epsilon$").scale(0.6).move_to(np.array([-0.4,-0.4,np.sqrt(9 - (0.3*np.cos(315*DEGREES)-1)**2 - (0.3*np.sin(315*DEGREES)+1)**2)]))
        dot_L_epsilon1_lab[0].set_color("#D4108A")
        dot_L_epsilon1_lab[1].set_color("#006400")
        dot_L_epsilon1_lab[2].set_color("#4DC8A1").scale(1.5)

        dot_L_epsilon2_lab = TextMobject(r"$L$", r"$+$", r"$\epsilon$").scale(0.6).move_to(np.array([-0.4,-0.4,np.sqrt(9 - (0.3*np.cos(135*DEGREES)-1)**2 - (0.3*np.sin(135*DEGREES)+1)**2)]))
        dot_L_epsilon2_lab[0].set_color("#D4108A")
        dot_L_epsilon2_lab[1].set_color("#006400")
        dot_L_epsilon2_lab[2].set_color("#4DC8A1").scale(1.5)
        
        dot_L_lab = TextMobject(r"$L$").scale(0.6).set_color("#D4108A").move_to(np.array([-0.4,-0.4,np.sqrt(7)]))

        epsilon_line = Line(np.array([0,0,np.sqrt(9 - (0.3*np.cos(315*DEGREES)-1)**2 - (0.3*np.sin(315*DEGREES)+1)**2)]), np.array([0,0,np.sqrt(9 - (0.3*np.cos(135*DEGREES)-1)**2 - (0.3*np.sin(135*DEGREES)+1)**2)]), color = "#4DC8A1")

        delta_line = Line(np.array([-1,1,0]), np.array([0.3*np.cos(0*DEGREES)-1, 0.3*np.sin(0*DEGREES)+1, 0]), color = "#000080")
        delta_line_lab = TexMobject("\\delta", color = ORANGE).scale(0.6).move_to(delta_line.get_center())

        self.play(ShowCreation(epsilon_line), ShowCreation(delta_line), ShowCreation(dot_L_epsilon1), ShowCreation(dot_L), ShowCreation(dot_L_epsilon2))
        self.bring_to_front(dot_L_epsilon1, dot_L, dot_L_epsilon2)
        self.add_fixed_orientation_mobjects(delta_line_lab, dot_L_epsilon1_lab, dot_L_epsilon2_lab, dot_L_lab)

        self.wait(2)


        circle_1 = [np.array([0.6*np.cos(i*DEGREES)-1, 0.6*np.sin(i*DEGREES)+1, 0]) for i in range(361)]

        circle_above_1 = [np.array([0.6*np.cos(i*DEGREES)-1, 0.6*np.sin(i*DEGREES)+1, np.sqrt(9 - (0.6*np.cos(i*DEGREES)-1)**2 - (0.6*np.sin(i*DEGREES)+1)**2)]) for i in range(361)]

        delta_circle_1 = Polygon(*circle_1, color = BLACK, fill_color = GREEN_E, fill_opacity= 0.5, stroke_width=0.1)

        delta_circle_above_1 = Polygon(*circle_above_1, color = BLACK, fill_color = GREEN_E, fill_opacity= 0.5, stroke_width=0.1)

        lines_1 = [Line(circle_1[i], circle_above_1[i], color = BLUE_B, opacity=0.01, stroke_width=0.1) for i in range(0,len(circle_1),1)]
        lines_group_1 = VGroup(*lines_1)


        line_epsilon1_1 = DashedLine(np.array([0.6*np.cos(315*DEGREES)-1, 0.6*np.sin(315*DEGREES)+1, np.sqrt(9 - (0.6*np.cos(315*DEGREES)-1)**2 - (0.6*np.sin(315*DEGREES)+1)**2)]), 
                                   np.array([0, 0, np.sqrt(9 - (0.6*np.cos(315*DEGREES)-1)**2 - (0.6*np.sin(315*DEGREES)+1)**2)]), color = YELLOW_C)

        line_epsilon2_1 = DashedLine(np.array([0.6*np.cos(135*DEGREES)-1, 0.6*np.sin(135*DEGREES)+1, np.sqrt(9 - (0.6*np.cos(135*DEGREES)-1)**2 - (0.6*np.sin(135*DEGREES)+1)**2)]), 
                                   np.array([0, 0, np.sqrt(9 - (0.6*np.cos(135*DEGREES)-1)**2 - (0.6*np.sin(135*DEGREES)+1)**2)]), color = YELLOW_C)

      
        epsilon_line_1 = Line(np.array([0,0,np.sqrt(9 - (0.6*np.cos(315*DEGREES)-1)**2 - (0.6*np.sin(315*DEGREES)+1)**2)]), np.array([0,0,np.sqrt(9 - (0.6*np.cos(135*DEGREES)-1)**2 - (0.6*np.sin(135*DEGREES)+1)**2)]), color = "#4DC8A1")
        
        delta_line1 = Line(np.array([-1,1,0]), np.array([0.6*np.cos(0*DEGREES)-1, 0.6*np.sin(0*DEGREES)+1, 0]), color = "#000080")
        delta_line_lab1 = TexMobject("\\delta", color = ORANGE).scale(0.6).move_to(delta_line1.get_center())




        epsilon_text1 = TextMobject(r"For every", r"$\epsilon$", " ,", color = YELLOW_C).scale(0.7).move_to(4.2*RIGHT+3.2*UP)
        epsilon_text1[1].set_color("#4DC8A1")

        epsilon_text2 = TextMobject("there exists a corresponding", r"$\delta$", r"disk", color = YELLOW_C).scale(0.7)
        epsilon_text2[1].set_color(ORANGE)
        epsilon_text2.next_to(epsilon_text1, DOWN)

        
        epsilon_text3 = TextMobject(r"So that for every value", color = YELLOW_C).scale(0.7).move_to(4*RIGHT+3.2*UP)
        
        epsilon_text4 = TextMobject("that lies within the", r"$\delta$", r"disk,", color = YELLOW_C).scale(0.7).next_to(epsilon_text3, DOWN)
        epsilon_text4[1].set_color(ORANGE)
        
        epsilon_text5 = TextMobject(r"the limit lies within the", r"$\epsilon$", r"band", color = YELLOW_C).scale(0.7)
        epsilon_text5[1].set_color("#4DC8A1")
        epsilon_text5.next_to(epsilon_text4, DOWN)
        
        self.add_fixed_in_frame_mobjects(epsilon_text1)

        self.play( ReplacementTransform(line_epsilon1, line_epsilon1_1), ReplacementTransform(line_epsilon2, line_epsilon2_1), ReplacementTransform(epsilon_line, epsilon_line_1),
            ApplyMethod(dot_L_epsilon1.move_to, np.array([0,0,np.sqrt(9 - (0.6*np.cos(315*DEGREES)-1)**2 - (0.6*np.sin(315*DEGREES)+1)**2)])), 
            ApplyMethod(dot_L_epsilon2.move_to, np.array([0,0,np.sqrt(9 - (0.6*np.cos(135*DEGREES)-1)**2 - (0.6*np.sin(135*DEGREES)+1)**2)])),
            ApplyMethod(dot_L_epsilon1_lab.move_to, np.array([-0.4,-0.4,np.sqrt(9 - (0.6*np.cos(315*DEGREES)-1)**2 - (0.6*np.sin(315*DEGREES)+1)**2)])), 
            ApplyMethod(dot_L_epsilon2_lab.move_to, np.array([-0.4,-0.4,np.sqrt(9 - (0.6*np.cos(135*DEGREES)-1)**2 - (0.6*np.sin(135*DEGREES)+1)**2)])))


        self.bring_to_front(dot_L_epsilon1, dot_L, dot_L_epsilon2)

        self.wait()

        self.add_fixed_in_frame_mobjects(epsilon_text2)



        self.play(ReplacementTransform(lines_group, lines_group_1), ReplacementTransform(delta_circle, delta_circle_1), ReplacementTransform(delta_circle_above, delta_circle_above_1), 
            ReplacementTransform(delta_line, delta_line1), ReplacementTransform(delta_line_lab, delta_line_lab1))

        self.bring_to_front(dot_L_epsilon1, dot_L, dot_L_epsilon2)

        self.add_fixed_orientation_mobjects(delta_line_lab1 ,dot_L_epsilon1_lab, dot_L_epsilon2_lab, dot_L_lab)

        

        self.wait(2)

        self.play(FadeOut(epsilon_text1), FadeOut(epsilon_text2))

        self.add_fixed_in_frame_mobjects(epsilon_text3, epsilon_text4)

        self.wait(2)

        self.add_fixed_in_frame_mobjects(epsilon_text5)

        self.wait(2)


        self.play(FadeOut(epsilon_text3), FadeOut(epsilon_text4), FadeOut(epsilon_text5))



        self.move_camera(distance=10,phi=80* DEGREES,theta=45*DEGREES)
        self.bring_to_front(dot_L_epsilon1_lab, dot_L_lab, dot_L_epsilon2_lab)
        self.wait(2)

        self.move_camera(distance=10,phi=75* DEGREES,theta=135*DEGREES)
        self.bring_to_front(dot_L_epsilon1_lab, dot_L_lab, dot_L_epsilon2_lab)
        self.wait(2)

        circle_2 = [np.array([0.5*np.cos(i*DEGREES)-1, 0.5*np.sin(i*DEGREES)+1, 0]) for i in range(361)]

        circle_above_2 = [np.array([0.5*np.cos(i*DEGREES)-1, 0.5*np.sin(i*DEGREES)+1, np.sqrt(9 - (0.5*np.cos(i*DEGREES)-1)**2 - (0.5*np.sin(i*DEGREES)+1)**2)]) for i in range(361)]

        delta_circle_2 = Polygon(*circle_2, color = BLACK, fill_color = GREEN_E, fill_opacity= 0.5, stroke_width=0.1)

        delta_circle_above_2 = Polygon(*circle_above_2, color = BLACK, fill_color = GREEN_E, fill_opacity= 0.5, stroke_width=0.1)

        lines_2 = [Line(circle_2[i], circle_above_2[i], color = BLUE_B, opacity=0.01, stroke_width=0.1) for i in range(0,len(circle_2),1)]
        lines_group_2 = VGroup(*lines_2)


        line_epsilon1_2 = DashedLine(np.array([0.5*np.cos(315*DEGREES)-1, 0.5*np.sin(315*DEGREES)+1, np.sqrt(9 - (0.5*np.cos(315*DEGREES)-1)**2 - (0.5*np.sin(315*DEGREES)+1)**2)]), 
                                   np.array([0, 0, np.sqrt(9 - (0.5*np.cos(315*DEGREES)-1)**2 - (0.5*np.sin(315*DEGREES)+1)**2)]), color = YELLOW_C)

        line_epsilon2_2 = DashedLine(np.array([0.5*np.cos(135*DEGREES)-1, 0.5*np.sin(135*DEGREES)+1, np.sqrt(9 - (0.5*np.cos(135*DEGREES)-1)**2 - (0.5*np.sin(135*DEGREES)+1)**2)]), 
                                   np.array([0, 0, np.sqrt(9 - (0.5*np.cos(135*DEGREES)-1)**2 - (0.5*np.sin(135*DEGREES)+1)**2)]), color = YELLOW_C)

      
        epsilon_line_2 = Line(np.array([0,0,np.sqrt(9 - (0.5*np.cos(315*DEGREES)-1)**2 - (0.5*np.sin(315*DEGREES)+1)**2)]), np.array([0,0,np.sqrt(9 - (0.5*np.cos(135*DEGREES)-1)**2 - (0.5*np.sin(135*DEGREES)+1)**2)]), color = "#4DC8A1")
        
        delta_line2 = Line(np.array([-1,1,0]), np.array([0.5*np.cos(0*DEGREES)-1, 0.5*np.sin(0*DEGREES)+1, 0]), color = "#000080")
        delta_line_lab2 = TexMobject("\\delta", color = ORANGE).scale(0.6).move_to(delta_line1.get_center())

        self.bring_to_front(dot_L_epsilon1, dot_L, dot_L_epsilon2)

        self.play(ReplacementTransform(lines_group_1, lines_group_2), ReplacementTransform(delta_circle_1, delta_circle_2), ReplacementTransform(delta_circle_above_1, delta_circle_above_2), 
            ReplacementTransform(line_epsilon1_1, line_epsilon1_2), ReplacementTransform(line_epsilon2_1, line_epsilon2_2), ReplacementTransform(epsilon_line_1, epsilon_line_2),
            ReplacementTransform(delta_line1, delta_line2), ReplacementTransform(delta_line_lab1, delta_line_lab2),
            ApplyMethod(dot_L_epsilon1.move_to, np.array([0,0,np.sqrt(9 - (0.5*np.cos(315*DEGREES)-1)**2 - (0.5*np.sin(315*DEGREES)+1)**2)])), 
            ApplyMethod(dot_L_epsilon2.move_to, np.array([0,0,np.sqrt(9 - (0.5*np.cos(135*DEGREES)-1)**2 - (0.5*np.sin(135*DEGREES)+1)**2)])),
            ApplyMethod(dot_L_epsilon1_lab.move_to, np.array([-0.4,-0.4,np.sqrt(9 - (0.5*np.cos(315*DEGREES)-1)**2 - (0.5*np.sin(315*DEGREES)+1)**2)])), 
            ApplyMethod(dot_L_epsilon2_lab.move_to, np.array([-0.4,-0.4,np.sqrt(9 - (0.5*np.cos(135*DEGREES)-1)**2 - (0.5*np.sin(135*DEGREES)+1)**2)])))

        self.bring_to_front(dot_L_epsilon1, dot_L, dot_L_epsilon2)
        self.add_fixed_orientation_mobjects(delta_line_lab2 ,dot_L_epsilon1_lab, dot_L_epsilon2_lab, dot_L_lab)

        self.wait(2)
        