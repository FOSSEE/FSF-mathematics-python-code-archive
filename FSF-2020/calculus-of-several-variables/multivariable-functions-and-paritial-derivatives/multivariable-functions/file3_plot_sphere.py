from manimlib.imports import *

class Sphere(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() # creates a 3D Axis

        sphere = ParametricSurface(
            lambda u, v: np.array([
                np.sin(u)*np.cos(v),
                np.sin(u)*np.sin(v),
                np.cos(u)
            ]),u_min=0,u_max=PI,v_min=0,v_max=2*PI,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)



        #self.set_camera_orientation(phi=0 * DEGREES,theta=270*DEGREES)

        text3d = TextMobject(r"$f(x,y) \rightarrow Point(x,y,z)$")
        text3d1 = TextMobject(r"$f(x,y) \rightarrow Point(x,y, 1 - x^2 - y^2)$")
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

        
        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.3)


        self.add(axes)
        self.play(Write(sphere))
        self.wait(5)