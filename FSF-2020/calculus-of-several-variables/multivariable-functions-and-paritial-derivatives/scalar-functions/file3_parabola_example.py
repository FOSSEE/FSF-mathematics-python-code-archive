from manimlib.imports import *

class Parabola(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() # creates a 3D Axis

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                2*np.cosh(u)*np.cos(v),
                2*np.cosh(u)*np.sin(v),
                2*np.sinh(u)
            ]),v_min=0,v_max=TAU,u_min=0,u_max=2,checkerboard_colors=[YELLOW_D, YELLOW_E],#
            resolution=(15, 32))

        text3d = TextMobject(r"Plot of $f: \mathbb{R}^2 \rightarrow \mathbb{R}$", r"$z = f(x,y) = \sqrt{x^2 + y^2 - 4}$") 
        text3d[0].move_to(4*LEFT+2*DOWN)
        text3d[1].next_to(text3d[0], DOWN)
        text3d[0].set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        text3d[1].set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE)

        #self.set_camera_orientation(phi=0 * DEGREES,theta=270*DEGREES)
        self.move_camera(phi=110* DEGREES,theta=45*DEGREES)

        self.add(axes)

        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(np.array([0,0,3.7]))

        self.add_fixed_orientation_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1]) 


        self.play(ShowCreation(paraboloid))
        self.add_fixed_in_frame_mobjects(text3d)
        self.play(Write(text3d[0]))
        self.play(Write(text3d[1]))
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.move_camera(phi=0 * DEGREES,theta=180*DEGREES,run_time=3)
        self.wait(3)
        self.move_camera(phi=110* DEGREES,theta=90*DEGREES,run_time=3)
        self.wait(3)
        
        