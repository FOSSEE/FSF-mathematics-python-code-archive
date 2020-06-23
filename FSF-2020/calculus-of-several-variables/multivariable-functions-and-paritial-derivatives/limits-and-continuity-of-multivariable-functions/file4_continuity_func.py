from manimlib.imports import *

class ContinuityFunc(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 

        text3d = TextMobject(r"$f(x,y) = \frac{3x^2y}{x^2 + y^2}$")
        self.add_fixed_in_frame_mobjects(text3d)
       
        text3d.to_corner(UL)
      
        text3d.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        self.play(Write(text3d))
        self.wait(1)

        continuity_func = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                3*u*np.cos(v)*np.cos(v)*np.sin(v)
            ]),u_min=-1.5,u_max=1.5,v_min=0,v_max=2*PI,checkerboard_colors=[YELLOW_C, YELLOW_E],
            resolution=(15, 32)).scale(2)

    

        self.set_camera_orientation(phi=80 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.3)

        self.add(axes)
        self.play(Write(continuity_func))
        self.wait(8)