from manimlib.imports import *

class Limit(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 
        
        text3d = TextMobject(r"$f(x,y) = \frac{x - y}{x - 1}$")
        self.add_fixed_in_frame_mobjects(text3d)
       
        text3d.to_corner(UL)
      
        text3d.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        self.play(Write(text3d))
        self.wait(1)
        
        limit_func = ParametricSurface(
            lambda u, v: np.array([
                3*np.sin(u)*np.cos(v),
                3*np.sin(u)*np.sin(v),
                (3*np.sin(u)*np.cos(v) - 3*np.sin(u)*np.sin(v))/2*(3*np.sin(u)*np.cos(v) - 1)
            ]),u_min=0,u_max=PI,v_min=0,v_max=2*PI, color = BLUE_C, fill_color = BLUE_C, fill_opacity = 0.1,
            resolution=(15, 32)).scale(1)

        limit_y_x =ParametricFunction(
                lambda u : np.array([
                u,
                u,
                0
            ]),color=GREEN_D,t_min=-3,t_max=3,
            )

        limit_y_1 =ParametricFunction(
                lambda u : np.array([
                u,
                1,
                1/2
            ]),color=BLUE_D,t_min=-3,t_max=3,
            )

        limit_y_x_2 =ParametricFunction(
                lambda u : np.array([
                u,
                u*u,
                (u - u*u)/2*(u - 1)
            ]),color=RED_D,t_min=-3,t_max=3,
            )

        limit_y_2_x =ParametricFunction(
                lambda u : np.array([
                u,
                2 - u,
                1
            ]),color=YELLOW_D,t_min=-3,t_max=3,
            )

        plane_y_x = Polygon(np.array([-3,-3,-3]),np.array([3,3,-3]),np.array([3,3,3]),np.array([-3,-3,3]),np.array([-3,-3,-3]), color = GREEN_C, fill_color = GREEN_C, fill_opacity = 0.1)
        plane_y_x_text = TextMobject(r"$y = x$", color = GREEN_C).move_to(np.array([5,0,3]))

        plane_y_1 = Polygon(np.array([-3,1,-3]),np.array([3,1,-3]),np.array([3,1,3]),np.array([-3,1,3]),np.array([-3,1,-3]), color = BLUE_C, fill_color = BLUE_C, fill_opacity = 0.1)
        plane_y_1_text = TextMobject(r"$y = 1$", color = BLUE_C).move_to(np.array([5,0,2.5]))


        #Creating plane y = x^2
        ######
        y_x_2 = []
        y_x_2.append(np.array([2, 4, -3])) 
        y_x_2.append(np.array([2, 4, 3])) 
        y_x_2_1 = [np.array([i, i*i, 3]) for i in np.arange(1.9,-2.1, -0.1)]
        
        y_x_2 = y_x_2 + y_x_2_1

        y_x_2.append(np.array([-2, 4, 3]))
        y_x_2.append(np.array([-2, 4, -3])) 

        y_x_2_2 = [np.array([i, i*i, -3]) for i in np.arange(-2,2.1, 0.1)]
        
        y_x_2 = y_x_2 + y_x_2_2
        #y_x_2.append(np.array([-3, 9, 0]))

        plane_y_x_2 = Polygon(*y_x_2, color = RED_C, fill_color = RED_C, fill_opacity = 0.1)
        plane_y_x_2_text = TextMobject(r"$y = x^2$", color = RED_C).move_to(np.array([5,0,2]))

        ######

        plane_y_2_x = Polygon(np.array([-3,5,-3]),np.array([3,-1,-3]),np.array([3,-1,3]),np.array([-3,5,3]),np.array([-3,5,-3]), color = YELLOW_C, fill_color = YELLOW_C, fill_opacity = 0.1)
        plane_y_2_x_text = TextMobject(r"$y = 2 - x$", color = YELLOW_C).move_to(np.array([5,0,1.5]))

        line_1_1 = Line(np.array([1,1,-3]), np.array([1,1,3]), color = PINK)

        point = Polygon(*[np.array([0.05*np.cos(i*DEGREES),0,0.05*np.sin(i*DEGREES)]) for i in range(361)], color = "#000080", fill_color = "#000080", fill_opacity = 1).move_to(np.array([1,1,0]))
        point_text = TextMobject(r"$(1,1,0)$", color = WHITE).scale(0.7).move_to(np.array([1.8,1,0]))




        self.set_camera_orientation(phi=70 * DEGREES, theta = -95*DEGREES)
        

        self.add(axes)
        
        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(3.7*UP)

        self.add_fixed_in_frame_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1])

        self.play(ShowCreation(limit_func))
        self.wait(2)

        self.play(ShowCreation(plane_y_x))
        self.add_fixed_orientation_mobjects(plane_y_x_text)
        self.play(ShowCreation(limit_y_x))
        self.wait()
 
        self.play(ShowCreation(plane_y_1))
        self.add_fixed_orientation_mobjects(plane_y_1_text)
        self.play(ShowCreation(limit_y_1))
        self.wait()
        
        self.play(ShowCreation(plane_y_x_2))
        self.add_fixed_orientation_mobjects(plane_y_x_2_text)
        self.play(ShowCreation(limit_y_x_2))
        self.wait()
       
        self.play(ShowCreation(plane_y_2_x))
        self.add_fixed_orientation_mobjects(plane_y_2_x_text)
        self.play(ShowCreation(limit_y_2_x))
        self.wait()

        self.play(ShowCreation(line_1_1))
        self.wait()

        self.play(ShowCreation(point))
        self.add_fixed_orientation_mobjects(point_text)
        self.wait()

        self.play(FadeOut(plane_y_x_text), FadeOut(plane_y_1_text), FadeOut(plane_y_x_2_text), FadeOut(plane_y_2_x_text))

        self.move_camera(phi=0* DEGREES,theta=-95*DEGREES)
        self.wait(2)
        self.play(FadeOut(plane_y_x), FadeOut(plane_y_1), FadeOut(plane_y_x_2), FadeOut(plane_y_2_x))
        self.wait(3)

        self.move_camera(phi=75* DEGREES,theta=-95*DEGREES)
        self.wait(3)


    