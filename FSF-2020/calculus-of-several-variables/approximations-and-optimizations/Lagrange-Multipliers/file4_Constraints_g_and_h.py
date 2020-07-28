from manimlib.imports import*
import math as m

    class Constraints(ThreeDScene):
    def construct(self):
       axes = ThreeDAxes().rotate(m.radians(75))
        label_x = TextMobject("$x$").shift([-5.5,1,0]).fade(0.4)  #---- x axis
        label_y = TextMobject("$y$").shift([1,5.5,0]).rotate(-4.5).fade(0.4)  #---- y axis

        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * u),
                np.sin(TAU * u),
                2 * (1-1.5*v)
            ]),checkerboard_colors=[YELLOW_C,YELLOW_D,YELLOW_E]).shift([0.5,0.5,-0.13]).scale(1) 

        plane =  ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u+v
            ]),checkerboard_colors=[TEAL_C,TEAL_D,TEAL_E]).shift([0,0,0]).rotate(m.radians(-40),RIGHT).scale(4).fade(0.3)

        c = Circle(color='#FF00FF',fill_opacity=0.3).shift([0.7,-1.3,0.4]).rotate(2.5,UP).scale(1.32)

        f_text = TextMobject("$f(x,y)=x^2+y^2+z^2$",color = '#FFA074').scale(0.6).to_corner(UL)
        g_text = TextMobject("$g(x,y)=x^2+y^2+1$",color = '#FFA074').scale(0.6).to_corner(UL)
        h_text = TextMobject("$h(x,y)=x+y-z=1$",color = '#FFA074').scale(0.6).to_corner(UL)



        self.set_camera_orientation(phi=65*DEGREES,theta=95*DEGREES)

        self.add(axes)        
        self.add(label_x) 
        self.add(label_y)
        self.wait(1) 
        self.add_fixed_in_frame_mobjects(f_text)    
        self.play(Write(c))
        self.wait(1)
        self.play(FadeOut(f_text))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(g_text)
        self.play(Write(cylinder)) 
        self.wait(1)
        self.play(FadeOut(g_text))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(h_text)
        self.play(Write(plane))            
        self.wait(1)
        self.play(FadeOut(h_text))
        self.wait(1)
