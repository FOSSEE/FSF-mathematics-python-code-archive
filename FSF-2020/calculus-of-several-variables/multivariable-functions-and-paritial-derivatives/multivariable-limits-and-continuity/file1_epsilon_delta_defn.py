from manimlib.imports import *

class EpsilonDelta(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() # creates a 3D Axis
        

        sphere = ParametricSurface(
            lambda u, v: np.array([
                3*np.sin(u)*np.cos(v),
                3*np.sin(u)*np.sin(v),
                3*np.cos(u)
            ]),u_min=0,u_max=PI/4,v_min=PI/2,v_max=PI,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(1)
        

        cylinder_z = ParametricSurface(
            lambda u, v: np.array([
                0.25*np.cos(TAU * v),
                1.8* (1 - u),
                0.25*np.sin(TAU * v)
                
            ]),
            checkerboard_colors=[YELLOW_C, YELLOW_E], resolution=(6, 32)).fade(0.2).rotate(PI/4).move_to(np.array([-0.65,0.65,2.54]))


        cylinder_x = ParametricSurface(
            lambda u, v: np.array([
                0.3*np.cos(TAU * v)-1,
                0.3*np.sin(TAU * v)+1,
                2.6*(1 - u)
            ]),
            checkerboard_colors=[BLUE_C, BLUE_E], resolution=(6, 32)).fade(0.2)
        

        delta_circle = Circle(radius= 0.3, color = BLACK).shift(1*LEFT+1*UP).set_fill(GREEN_E, opacity = 0.5)

        epsilon_circle = [np.array([0.25*np.cos(i*DEGREES),0,0.25*np.sin(i*DEGREES)]) for i in range(361)]

        epsilon_circle_polygon = Polygon(*epsilon_circle, color = RED_E, fill_color = RED_E, fill_opacity = 0.5).rotate(PI/4).move_to(np.array([0,0,2.54]))


        dot_circle = Dot().move_to(np.array([-1,1,0])).set_fill("#000080")
        
        dot_surface = Dot().rotate(-PI/4).scale(1.5).move_to(np.array([-1.2,1.2,2.7])).set_fill("#000080")

        dot_L_epsilon1 = Polygon(*[np.array([0.05*np.cos(i*DEGREES),0,0.05*np.sin(i*DEGREES)]) for i in range(361)], color = "#000080", fill_color = "#000080", fill_opacity = 1).rotate(PI/4).move_to(np.array([0,0,2.3]))

        dot_L_epsilon2 = Polygon(*[np.array([0.05*np.cos(i*DEGREES),0,0.05*np.sin(i*DEGREES)]) for i in range(361)], color = "#000080", fill_color = "#000080", fill_opacity = 1).rotate(PI/4).move_to(np.array([0,0,2.8]))
        
        dot_L = Polygon(*[np.array([0.05*np.cos(i*DEGREES),0,0.05*np.sin(i*DEGREES)]) for i in range(361)], color = "#006400", fill_color = "#006400", fill_opacity = 1).rotate(PI/4).move_to(np.array([0,0,2.54]))

        
    
        self.add(axes)

        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(np.array([0,0,3.7]))

        self.add_fixed_orientation_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1]) 

        self.set_camera_orientation(phi=75*DEGREES,theta=135*DEGREES)
        #self.set_camera_orientation(phi=80*DEGREES,theta=45*DEGREES)


        self.play(ShowCreation(sphere),ShowCreation(delta_circle), ShowCreation(dot_circle)) 

        temp_circle_center = TextMobject(r"$(a,b,0)$").scale(0.6).set_color(BLUE_C).move_to(1.7*LEFT+1.1*UP)
        self.add_fixed_orientation_mobjects(temp_circle_center)
        self.wait()

        delta_lab = TextMobject(r"$\delta$", r"$-$", "disk").scale(0.5).move_to(0.6*LEFT+1.7*UP)
        delta_lab[0].set_color(PINK).scale(1.3)
        delta_lab[1].set_color(ORANGE)
        delta_lab[2].set_color(GREEN_E)

        self.add_fixed_orientation_mobjects(delta_lab)

        self.play(ShowCreation(dot_surface))

        temp_curve_circle_center = TextMobject(r"$(a,b,L)$").scale(0.6).set_color("#006400").move_to(np.array([-2,1,2.7]))
        self.add_fixed_orientation_mobjects(temp_curve_circle_center)


        self.wait()
        self.play(ShowCreation(cylinder_x), FadeOut(dot_surface))
        self.wait()
        
        self.move_camera(phi=0* DEGREES,theta=135*DEGREES)
        self.wait()

        self.move_camera(phi=80* DEGREES,theta=225*DEGREES)
        self.wait()
        
        self.play(FadeOut(delta_lab), ShowCreation(cylinder_z))
        self.wait()

        self.play(FadeOut(temp_circle_center), FadeOut(temp_curve_circle_center),ShowCreation(epsilon_circle_polygon))

        self.move_camera(phi=80* DEGREES,theta=325*DEGREES)

        dot_L_epsilon1_lab = TextMobject(r"$L$", r"$-$", r"$\epsilon$").scale(0.6).move_to(np.array([-0.4,-0.4,2.3]))
        dot_L_epsilon1_lab[0].set_color("#D4108A")
        dot_L_epsilon1_lab[1].set_color("#006400")
        dot_L_epsilon1_lab[2].set_color("#4DC8A1").scale(1.5)

        dot_L_epsilon2_lab = TextMobject(r"$L$", r"$+$", r"$\epsilon$").scale(0.6).move_to(np.array([-0.4,-0.4,2.8]))
        dot_L_epsilon2_lab[0].set_color("#D4108A")
        dot_L_epsilon2_lab[1].set_color("#006400")
        dot_L_epsilon2_lab[2].set_color("#4DC8A1").scale(1.5)
        
        dot_L_lab = TextMobject(r"$L$").scale(0.6).set_color("#D4108A").move_to(np.array([-0.4,-0.4,2.54]))


        self.play(ShowCreation(dot_L_epsilon1), ShowCreation(dot_L), ShowCreation(dot_L_epsilon2))
        self.add_fixed_orientation_mobjects(dot_L_epsilon1_lab, dot_L_epsilon2_lab, dot_L_lab)
        self.wait(4)

        self.move_camera(phi=80* DEGREES,theta=45*DEGREES)
        self.wait(2)


        

        

        

        
        

        
        

        '''
        


        
        




        

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
        
        self.play(ShowCreation(circle), ShowCreation(line1), ShowCreation(line2))
        self.play(ShowCreation(line3), ShowCreation(line4))
        self.wait(8)
        '''