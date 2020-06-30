from manimlib.imports import*
import math as m

#---- optimizing funtion f(x,y) w.r.t to g(x,y)
class ConstrainedExtrema(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().fade(0.4)        
        label_x = TextMobject("$x$").shift([5.5,-0.5,0]).fade(0.4)  #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5).fade(0.4)  #---- y axis

        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2+u**3-v**3
            ]),u_min=-0.5,u_max=0.5, v_min=-0.5,v_max=0.5).scale(5).shift([0,1,2.5]).set_color(TEAL).fade(0.4)
        
        c = Circle().set_color('#FF00FF').shift([-0.4,0,1.5]).rotate(1.9,UP).scale(0.7)

        minima = Dot(color = '#4169E1').shift([-0.5,0.5,1]).rotate(1.571,UP)
        maxima  = Dot(color = '#4169E1').shift([0.1,0,2.2]).rotate(1.571,UP)

        l1 = DashedLine([-0.5,0.5,0.9],[-0.5,0.5,0],color = '#F08080')
        l2 = DashedLine([0.1,0,2.1],[0.1,0,0],color = '#F08080')

        c2 = Circle(fill_opacity= 0.5).shift([-0.3,0.2,0]).scale(0.4)

        minima_refl = Dot(color = '#4682B4').shift([-0.5,0.5,0]).rotate(1.571,UP)
        maxima_refl  = Dot(color = '#4682B4').shift([0.1,0,0]).rotate(1.571,UP)

        max_text = TextMobject("maximum over $g(x,y)=k$",color = '#FFA074').shift([-1.7,0,0]).scale(0.5).shift(2.2*UP)
        min_text = TextMobject("minimum over $g(x,y)=k$",color = '#FFA074').shift([2.5,0.5,1]).scale(0.5).shift(0.5*UP)
        label_f = TextMobject("$z=f(x,y)$",color = '#8A2BE2').scale(0.5).shift(3*UP+3*RIGHT)
        label_g = TextMobject("$g(x,y)=k$",color = '#8A2BE2').scale(0.5).shift(2*RIGHT)       

        self.add(axes)
        self.add(label_x)
        self.add(label_y)
        self.set_camera_orientation(phi=75*DEGREES,theta=45*DEGREES)
        self.play(Write(surface)) 
        self.add_fixed_in_frame_mobjects(label_f)
        self.wait(2)
        self.play(Write(c)) 
        self.wait(1)
        self.play(Write(maxima))
        self.add_fixed_in_frame_mobjects(max_text)
        self.wait(1)
        self.play(Write(minima)) 
        self.add_fixed_in_frame_mobjects(min_text)
        self.wait(1)
        self.play(ShowCreation(l1),ShowCreation(l2))
        self.play(Write(c2))                       
        self.add_fixed_in_frame_mobjects(label_g)
        self.wait(1)
        self.play(Write(maxima_refl))
        self.play(Write(minima_refl))
        self.wait(1)
