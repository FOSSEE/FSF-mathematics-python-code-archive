from manimlib.imports import*
import math as m
 
class DegenerateHessian(ThreeDScene):
    def construct(self):

        heading = TextMobject("Degenerate Hessian Matrix",color = BLUE)

        h_text = TextMobject("For $det \\hspace{1mm} H = 0$, the surface of the function at the critical point would be flat.").scale(0.7)

        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.3,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.3,5.5,0]).rotate(-4.5) #---- y axis

        #---- function f(x,y)
        f_surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**4-v**4
            ]),u_min = -0.8, u_max = 0.8, v_min = -0.8, v_max = 0.8).set_color(TEAL).shift([0,0,-0.5]).scale(2)
        
        f_text= TextMobject("surface of the function").to_corner(UL).scale(0.5)
        
        d = Dot(color = "#800000").shift([0,0,-0.5]) #---- critical point 
        plane = Square(color = YELLOW,fill_opacity= 0.2).shift([0,0,-0.5]).scale(1.3)
        
        self.set_camera_orientation(phi = 70*DEGREES, theta = 45*DEGREES) 
        self.add_fixed_in_frame_mobjects(heading)
        self.wait(1)
        self.play(FadeOut(heading))
        self.add_fixed_in_frame_mobjects(h_text)
        self.wait(2)
        self.play(FadeOut(h_text))
        self.wait(1)
        self.add(axes)     
        self.add(label_x)
        self.add(label_y)
        self.play(Write(f_surface)) 
        self.add_fixed_in_frame_mobjects(f_text)
        self.wait(1)
        self.play(Write(d))
        self.wait(1)
        self.play(Write(plane))
        self.wait(1)
