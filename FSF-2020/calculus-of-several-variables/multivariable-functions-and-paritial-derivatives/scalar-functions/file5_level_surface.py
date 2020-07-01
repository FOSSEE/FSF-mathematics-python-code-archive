from manimlib.imports import *

class LevelSurface(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 

        surface_0 = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                (u*u*np.cos(v)*np.cos(v))-(u*np.sin(v)/5)+0
            ]),u_min=-1,u_max=1,v_min=0,v_max=2*PI,checkerboard_colors=[RED_C, RED_E],
            resolution=(15, 32)).scale(1)

        k_0 = TextMobject("K = 0", color = RED_C).scale(0.7)

        surface_1 = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                (u*u*np.cos(v)*np.cos(v))-(u*np.sin(v)/5)+1
            ]),u_min=-1,u_max=1,v_min=0,v_max=2*PI,checkerboard_colors=[GREEN_C, GREEN_E],
            resolution=(15, 32)).scale(1)
        
        k_1 = TextMobject("K = 1", color = GREEN_C).scale(0.7)

        surface_2 = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                (u*u*np.cos(v)*np.cos(v))-(u*np.sin(v)/5)+2
            ]),u_min=-1,u_max=1,v_min=0,v_max=2*PI,checkerboard_colors=[YELLOW_C, YELLOW_E],
            resolution=(15, 32)).scale(1)

        k_2 = TextMobject("K = 2", color = YELLOW_C).scale(0.7)

        func = TextMobject(r"$w = g(x,y,z)$", r"$= z - f(x,y)$", r"$z-x^2+y/5 = K$")
        func.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        self.set_camera_orientation(phi=90 * DEGREES, theta = 90*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.3)


        self.add(axes)
        
        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(3.7*UP)

        self.add_fixed_in_frame_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1])

        self.play(Write(surface_0))
        self.add_fixed_in_frame_mobjects(k_0)
        k_0.move_to(np.array([1.4*RIGHT ]))

        self.play(Write(surface_1))
        self.add_fixed_in_frame_mobjects(k_1)
        k_1.move_to(np.array([1.4*RIGHT + 1*UP]))
    
        self.play(Write(surface_2))
        self.add_fixed_in_frame_mobjects(k_2)
        k_2.move_to(np.array([1.4*RIGHT + 2*UP]))
        self.wait()

        self.add_fixed_in_frame_mobjects(func)
        func[0].move_to(np.array([4.5*LEFT + 3*UP]))
        func[1].move_to(np.array([4.5*LEFT + 2.5*UP]))
        func[2].move_to(np.array([4.5*LEFT + 2*UP]))

        self.wait(3)
        self.move_camera(phi=60 * DEGREES,run_time=3)
        self.wait(2)


     