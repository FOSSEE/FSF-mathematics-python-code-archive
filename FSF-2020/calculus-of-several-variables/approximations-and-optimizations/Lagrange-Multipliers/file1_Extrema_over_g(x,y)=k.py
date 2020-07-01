from manimlib.imports import*
import math as m

#---- optimizing funtion f(x,y) w.r.t to g(x,y)
class ConstrainedExtrema(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().fade(0.4)        
        label_x = TextMobject("$x$").shift([5.5,-0.5,0])  #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5) #---- y axis

        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2+u**3-v**3
            ]),u_min=-0.5,u_max=0.5, v_min=-0.5,v_max=0.5).scale(5).shift([0,1,2.5]).set_color(TEAL).fade(0.2)
        
        c = Circle(color='#FF00FF',fill_opacity=0.3).shift([-0.4,0,1.5]).rotate(1.9,UP).scale(0.7)

        minima = Dot(color = '#4169E1').shift([-0.5,0.5,1]).rotate(1.571,UP)
        maxima  = Dot(color = '#4169E1').shift([0.1,0,2.2]).rotate(1.571,UP)    

        max_text = TextMobject("maximum over $g(x,y)=k$",color = '#FFA074').scale(0.6).shift(2.3*UP+2*LEFT)
        min_text = TextMobject("minimum over $g(x,y)=k$",color = '#FFA074').shift([2.5,0.5,1]).scale(0.6).shift(0.5*UP)
        label_f = TextMobject("$z=f(x,y)$",color=TEAL).scale(0.8).shift(3*UP+3*RIGHT)
        label_g = TextMobject("g(x,y)=k",color = PURPLE).scale(0.5).shift(1.5*UP+0.8*LEFT)
             

        self.add(axes)
        self.add(label_x)
        self.add(label_y)
        self.set_camera_orientation(phi=75*DEGREES,theta=45*DEGREES)
        self.play(Write(surface)) 
        self.add_fixed_in_frame_mobjects(label_f)
        self.wait(2)
        self.play(Write(c)) 
        self.wait(1)
        self.add_fixed_in_frame_mobjects(label_g)
        self.wait(1)
        self.play(Write(maxima))
        self.add_fixed_in_frame_mobjects(max_text)
        self.wait(1)
        self.play(Write(minima)) 
        self.add_fixed_in_frame_mobjects(min_text)
        self.wait(1) 
