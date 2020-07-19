from manimlib.imports import*
import math as m

#---- contour plot of the surface with constraint circle
class ContourScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().scale(0.7).rotate(m.radians(180)).fade(0.6)     
        label_x = TextMobject("$x$").shift(4*LEFT).fade(0.4)  #---- x axis
        label_y = TextMobject("$y$").shift(3.2*DOWN+0.2*RIGHT).rotate(m.radians(180)).fade(0.4)  #---- y axis

        #---- surface of the function f(x,y) = x^2+y^2+x^3-y^3
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2+u**3-v**3
            ]),u_min=-0.5,u_max=0.5, v_min=-0.5,v_max=0.5).scale(5).shift([0,-0.5,2.5]).set_color(TEAL).fade(0.5)

        
        #---- contour plots of the surface of the function
        
        c0 = Circle(color = '#800000').scale(0.5).shift([0,-0.5,0])
        c1 = Circle(color = '#800000').scale(1).shift([0,-0.5,0])
        c2 = Circle(color = '#800000').scale(1.5).shift([0,-0.5,0])
        c3 = Circle(color = '#800000').scale(2).shift([0,-0.5,0])
        c4 = Circle(color = '#800000').scale(2.5).shift([0,-0.5,0])
        
        #---- constraint circle
        circle = Circle(color='#FF00FF',fill_opacity=0.3).shift([-0.5,-1.2,1.5]).rotate(1.9,UP).scale(0.8)
        circle2 = Circle(color='#FF00FF',fill_opacity=0.3).shift([0.74,0.95,1.5]).rotate(1.9,UP).scale(0.8)

        maxima = Dot(color = '#4169E1').shift([0.7,0.15,1.5]) #---- point of maxima
        minima  = Dot(color = '#4169E1').shift([0.8,1.7,1.5]) #---- point of minima

        min_text = TextMobject("minimum over $g(x,y)=k$",color = '#FFA074').scale(0.6).shift([-2,0.16,1.5])
        max_text = TextMobject("maximum over $g(x,y)=k$",color = '#FFA074').shift([-2.3,-2.6,1.5]).scale(0.6).shift(0.5*UP)


        #---- labelling contour curves
        label_c0 = TextMobject("1",color = '#FFA074').shift([0.2,0.1,0.5]).scale(0.5)
        label_c1 = TextMobject("2",color = '#FFA074').shift([0.2,-0.6,0.5]).scale(0.5)
        label_c2 = TextMobject("3",color = '#FFA074').shift([0.2,-1.1,0.5]).scale(0.5)
        label_c3 = TextMobject("4",color = '#FFA074').shift([0.2,-1.6,0.5]).scale(0.5)
        label_c4 = TextMobject("5",color = '#FFA074').shift([0.2,-2.1,0.5]).scale(0.5)


        self.set_camera_orientation(phi=75 * DEGREES, theta = 45*DEGREES)
        self.add(axes)        
        self.add(label_x) 
        self.add(label_y)
        self.wait(1)
        self.play(Write(surface))
        self.play(Write(circle))
        self.wait(1)
        self.play(FadeOut(circle))
        self.wait(1)
        self.move_camera(phi=0 * DEGREES, theta = 90*DEGREES)
        self.wait(1)        
        self.play(Write(c0),Write(c1),Write(c2),Write(c3),Write(c4)) 
        self.play(FadeOut(surface))  
        self.add_fixed_in_frame_mobjects(label_c0) 
        self.add_fixed_in_frame_mobjects(label_c1)
        self.add_fixed_in_frame_mobjects(label_c2)
        self.add_fixed_in_frame_mobjects(label_c3)
        self.add_fixed_in_frame_mobjects(label_c4)
        self.wait(1)
        self.play(Write(circle2))  
        self.wait(1)
        self.play(Write(minima),Write(maxima)) 
        self.add_fixed_in_frame_mobjects(max_text) 
        self.add_fixed_in_frame_mobjects(min_text) 
        self.wait(1)
