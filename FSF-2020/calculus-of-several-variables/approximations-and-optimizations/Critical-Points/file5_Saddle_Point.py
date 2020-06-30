from manimlib.imports import*
import math as m

#---- saddle point of a function
class SaddlePoint(ThreeDScene):
    def construct(self):

        h_text = TextMobject("Saddle Point",color = GREEN)
    
        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.3,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.3,5.5,0]).rotate(-4.5) #---- y axis
        
        #---- f(x,y) = -x^2-y^2
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]),u_min = -1, u_max = 1, v_min = -1, v_max = 1,checkerboard_colors = [BLUE_B,BLUE_C,BLUE_D,BLUE_E]).shift([0,0,0]).scale(3)
        
        #---- curve(trace) along y axis
        curve_x = ParametricSurface(
            lambda u, v: np.array([
                u*0.1,
                v,
                v**2
            ]),v_min = -1, v_max = 1, u_min = -0.2, u_max = 0.2).shift([0,0,-2]).scale(3.1).set_color("#800000").rotate(m.radians(180),UP)
        
        x_text = TextMobject("A dip at critical point along x axis").scale(0.5).to_corner(UL)

        #---- curve(trace) along x axis
        curve_y = ParametricSurface(
            lambda u, v: np.array([
                u,
                v*0.1,
                -u**2
            ]),v_min = -0.2, v_max = 0.2, u_min = -1, u_max = 1).scale(3).shift([0.1,0,2.2]).set_color("#800000").rotate(m.radians(182),DOWN)
        
        y_text = TextMobject("A peak at critical point along y axis").scale(0.5).to_corner(UL)
        
        d = Dot(color = YELLOW).shift([0,-0.22,0]) #---- critical point(saddle point)
        
        self.add_fixed_in_frame_mobjects(h_text)
        self.wait(1)
        self.play(FadeOut(h_text))
        self.wait(1)
        self.set_camera_orientation(phi = 75*DEGREES, theta = 40*DEGREES) 
        self.add(axes)     
        self.add(label_x)
        self.add(label_y)     
        self.play(Write(surface))
        self.wait(1)
        self.move_camera(phi = 45*DEGREES, theta = 70*DEGREES) 
        self.add(curve_y)
        self.play(Write(d))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(x_text)
        self.wait(1)
        self.wait(1)
        self.play(FadeOut(curve_y),FadeOut(d),FadeOut(x_text))
        self.wait(1)
        self.move_camera(phi = 40*DEGREES, theta = 30*DEGREES)
        self.add(curve_x)
        self.play(Write(d))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(y_text)
        self.begin_ambient_camera_rotation(rate = 0.3)  
        self.wait(3)
        self.play(FadeOut(curve_x),FadeOut(d),FadeOut(y_text))          
        self.wait(1)
