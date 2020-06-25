from manimlib.imports import*
import math as m

#---- locating extrema of a funtion using critical points
class Extrema(ThreeDScene):
    def construct(self):

        h_text = TextMobject("Relative Maxima and Relative Minima",color = GREEN)
    
        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.3,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.3,5.5,0]).rotate(-4.5) #---- y axis
        
        #---- f(x,y) = 5(x+y)e^(-x^2-y^2)
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                5*(u+v)*m.exp(-u**2-v**2)
            ]),u_min = -PI, u_max = PI, v_min = -PI, v_max = PI).set_color(TEAL).shift([0,0,0]).fade(0.4)
        
        d1 = Dot(color = YELLOW).shift([0.5,0.5,3.02]) #---- critical point for maxima 
        l1 = Line([0.5,0.5,0.1],[0.5,0.5,3],color = YELLOW)

        d2 = Dot(color = YELLOW).shift([-1.15,0,-2.98]) #---- critical point for minima
        l2 = Line([-1.15,0,0],[-1.15,0,-2.98],color = YELLOW)

        max_text = TextMobject("Relative Maxima").shift(3.1*UP+1.5*RIGHT).scale(0.5)
        min_text = TextMobject("Relative Minima").shift(3.1*DOWN+1.5*LEFT).scale(0.5)

        self.add_fixed_in_frame_mobjects(h_text)
        self.wait(1)
        self.wait(1)
        self.play(FadeOut(h_text))
        self.wait(1)    
        self.set_camera_orientation(phi = 100*DEGREES, theta = -40*DEGREES) 
        self.add(axes)     
        self.add(label_x)
        self.add(label_y)       
        self.play(Write(surface))
        self.wait(1)
        self.play(Write(l1),Write(d1))
        self.add_fixed_in_frame_mobjects(max_text)
        self.wait(1)
        self.play(Write(l2),Write(d2))        
        self.add_fixed_in_frame_mobjects(min_text)
        self.wait(1)
        self.wait(1)
        self.play(FadeOut(l1),FadeOut(d1),FadeOut(l2),FadeOut(d2),FadeOut(max_text),FadeOut(min_text))
        self.begin_ambient_camera_rotation(rate = 0.3)        
        self.wait(3)     
