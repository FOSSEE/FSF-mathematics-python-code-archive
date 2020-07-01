from manimlib.imports import*
import math as m

class firstScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.5,0]).fade(0.4)  #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5).fade(0.4)  #---- y axis
        
        #---- constraint g(x,y)
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * u),
                np.sin(TAU * u),
                2 * (v)
            ]),checkerboard_colors=[YELLOW_C,YELLOW_D,YELLOW_E]).rotate(m.radians(-40),RIGHT).shift([0.5,0.5,0]).scale(0.8)
        
        #---- constraint h(x,y)
        plane =  ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u+v
            ]),checkerboard_colors=[TEAL_C,TEAL_D,TEAL_E]).shift([0,0,0]).rotate(m.radians(-40),RIGHT).scale(2).fade(0.3)
        
        figure = VGroup(cylinder,plane).rotate(m.radians(-45),DOWN).scale(1.5)

        self.set_camera_orientation(phi=65*DEGREES,theta=45*DEGREES)
        self.add(axes)        
        self.add(label_x) 
        self.add(label_y)
        self.wait(1)       
        self.play(Write(cylinder)) 
        self.play(Write(plane)) 
        self.wait(1)
        self.begin_ambient_camera_rotation(rate=0.4)    
        self.wait(1)
        self.wait(1)
        self.play(FadeOut(label_x),FadeOut(label_y))
        self.wait(1)           
        self.wait(1)
