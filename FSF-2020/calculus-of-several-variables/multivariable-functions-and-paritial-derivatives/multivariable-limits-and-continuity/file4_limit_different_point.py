from manimlib.imports import *

class DifferentPoint(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 
        
        text3d = TextMobject(r"$f(x,y) = \frac{x^2 - y^2}{x^2 + y^2}$")
        self.add_fixed_in_frame_mobjects(text3d)
       
        text3d.to_corner(UL)
      
        text3d.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        self.play(Write(text3d))
        self.wait(1)
        
        limit_func = ParametricSurface(
            lambda u, v: np.array([
                3*np.sin(u)*np.cos(v),
                3*np.sin(u)*np.sin(v),
                (np.cos(v)*np.cos(v) - np.sin(v)*np.sin(v))
            ]),u_min=0,u_max=PI,v_min=0,v_max=2*PI,checkerboard_colors=[YELLOW_C, YELLOW_E],
            resolution=(15, 32)).scale(1)

        limit_func_copy1 = limit_func.copy()
        limit_func_copy2 = limit_func.copy()

        limit_func_x = ParametricSurface(
            lambda u, v: np.array([
                3*np.sin(u)*np.cos(v),
                3*np.sin(u)*np.sin(v),
                (np.cos(v)*np.cos(v) - np.sin(v)*np.sin(v))
            ]),u_min=0,u_max=PI,v_min=PI,v_max=2*PI,checkerboard_colors=[YELLOW_C, YELLOW_E],
            resolution=(15, 32)).scale(1)

        limit_func_y = ParametricSurface(
            lambda u, v: np.array([
                3*np.sin(u)*np.cos(v),
                3*np.sin(u)*np.sin(v),
                (np.cos(v)*np.cos(v) - np.sin(v)*np.sin(v))
            ]),u_min=0,u_max=PI,v_min=PI/2,v_max=3*PI/2,checkerboard_colors=[YELLOW_C, YELLOW_E],
            resolution=(15, 32)).scale(1)

        limit_x =ParametricFunction(
                lambda u : np.array([
                u,
                0,
                1
            ]),color="#006400",t_min=-3,t_max=3,
            )

        limit_y =ParametricFunction(
                lambda u : np.array([
                0,
                u,
                -1
            ]),color="#000080",t_min=-3,t_max=3,
            )

        plane_x = Polygon(np.array([-3,0,-2]),np.array([3,0,-2]),np.array([3,0,2]),np.array([-3,0,2]),np.array([-3,0,-2]), color = GREEN, fill_color = GREEN, fill_opacity = 0.2)
        plane_x_text = TextMobject(r"$y = 0$", color = GREEN_C).move_to(1.7*UP + 3.8*RIGHT)

        plane_y = Polygon(np.array([0,-3,-2]),np.array([0,3,-2]),np.array([0,3,2]),np.array([0,-3,2]),np.array([0,-3,-2]), color = BLUE, fill_color = BLUE, fill_opacity = 0.2)
        plane_y_text = TextMobject(r"$x = 0$", color = BLUE_C).move_to(1.7*UP + 3.8*RIGHT)

        origin_x = Polygon(*[np.array([0.05*np.cos(i*DEGREES),0,0.05*np.sin(i*DEGREES)]) for i in range(361)], color = "#000080", fill_color = "#000080", fill_opacity = 1).move_to(np.array([0,0,0]))
        origin_x_text = TextMobject(r"$(0,0,0)$", color = RED_C).scale(0.7).move_to(np.array([-0.6,0,-0.5]))

        origin_y = Polygon(*[np.array([0,0.05*np.cos(i*DEGREES),0.05*np.sin(i*DEGREES)]) for i in range(361)], color = "#000080", fill_color = "#000080", fill_opacity = 1).move_to(np.array([0,0,0]))
        origin_y_text = TextMobject(r"$(0,0,0)$", color = RED_C).scale(0.7).move_to(np.array([0,-0.6,-0.5]))

        self.set_camera_orientation(phi=80 * DEGREES, theta = 0*DEGREES)
        

        self.add(axes)

        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(3.7*UP)

        self.add_fixed_in_frame_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1])

        self.play(ShowCreation(limit_func))

        self.move_camera(phi=80* DEGREES,theta=105*DEGREES)

        self.play(ShowCreation(plane_x))
        self.add_fixed_in_frame_mobjects(plane_x_text)
        self.wait()
        self.play(ReplacementTransform(limit_func, limit_func_x))
        self.play(FadeOut(plane_x), FadeOut(plane_x_text), ShowCreation(origin_x))
        self.add_fixed_orientation_mobjects(origin_x_text)
        self.play(ShowCreation(limit_x))

        self.move_camera(phi=80* DEGREES,theta=15*DEGREES)
        self.wait(3)

        self.play(FadeOut(origin_x), FadeOut(origin_x_text), FadeOut(limit_x), ReplacementTransform(limit_func_x, limit_func_copy1))
        self.play(ShowCreation(plane_y))
        self.add_fixed_in_frame_mobjects(plane_y_text)
        self.wait()
        self.play(ReplacementTransform(limit_func_copy1, limit_func_y))
        self.play(FadeOut(plane_y), FadeOut(plane_y_text), ShowCreation(origin_y))
        self.add_fixed_orientation_mobjects(origin_y_text)
        self.play(ShowCreation(limit_y))

        self.move_camera(phi=80* DEGREES,theta=75*DEGREES)
        self.wait(3)

        self.play(FadeOut(origin_y), FadeOut(origin_y_text), FadeOut(limit_y), ReplacementTransform(limit_func_y, limit_func_copy2))
        self.wait(2)
        