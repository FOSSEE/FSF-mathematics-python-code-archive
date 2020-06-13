from manimlib.imports import*
import math as m


class firstScene(ThreeDScene):
    def construct(self):
    
        axes = ThreeDAxes().scale(1.15)
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                m.exp(-10*u**2-10*v**2) #---- f(x,y) 
            ]),u_min=-2,u_max=1, v_min=-1,v_max=1,checkerboard_colors=[PURPLE_C,PURPLE_D,PURPLE_E,PURPLE_B]).scale(3).shift([1.1,0.48,1.731])

        trace = ParametricSurface(
            lambda u, v: np.array([
            m.exp(np.cos(v)+np.sin(v)),
            v,
            u/4
            ]), v_min = -1, v_max= 2).rotate(1.571,DOWN).shift(2.15*LEFT+[0.6,-0.4,1.54]).scale(1).set_color('#800000') 

         
        
        d = Dot(color =YELLOW).shift([1.9,0.7,4.1]) #---- critical point
        tangent_line = Line(color = '#228B22').scale(1).shift([1.9,0.7,4.1]).rotate(4.5) #---- tangent along y axis

        label_x = TextMobject("$x$").shift([5.8,-0.5,0])
        label_y = TextMobject("$y$").shift([-0.5,5.6,0]).rotate(-4.5)


        f_text = TextMobject("Tangent to the trace with $y$ constant at critical point").shift(3*RIGHT+2*UP).scale(0.5).to_corner(UL)
        
        self.add(axes)
        self.set_camera_orientation(phi=60*DEGREES,theta=15*DEGREES)
        self.add(label_x)
        self.add(label_y)
        self.play(Write(surface))  
        self.wait(1)
        self.add_fixed_in_frame_mobjects(s_text)
        self.add(trace)
        self.wait(1)
        self.play(Write(tangent_line),Write(d))
        self.wait(2)
        
        
class secondScene(ThreeDScene):
    def construct(self):
    
        axes = ThreeDAxes().scale(1.15)
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                m.exp(-10*u**2-10*v**2) #---- f(x,y) 
            ]),u_min=-2,u_max=1, v_min=-1,v_max=1,checkerboard_colors=[PURPLE_C,PURPLE_D,PURPLE_E,PURPLE_B]).scale(3).shift([1.1,0.48,1.731])

        trace = ParametricSurface(
            lambda u, v: np.array([
            m.exp(np.cos(v)+np.sin(v)),
            v,
            u/4
            ]), v_min = -1, v_max= 2).rotate(1.571,DOWN).shift(2.15*LEFT+[0.6,-0.4,1.54]).scale(1).set_color('#800000') 

         
        
        d = Dot(color =YELLOW).shift([1.9,0.7,4.1]) #---- critical point

        label_x = TextMobject("$x$").shift([5.8,-0.5,0])
        label_y = TextMobject("$y$").shift([-0.5,5.6,0]).rotate(-4.5)

        f_text = TextMobject("Tangent to the trace with $y$ constant at critical point").shift(3*RIGHT+2*UP).scale(0.5).to_corner(UL)
        
        tangent_line = Line(color = '#228B22').scale(1).shift([1.9,0.7,4.1]) #---- tangent along x axis


        self.add(axes)
        self.set_camera_orientation(phi=60*DEGREES,theta=15*DEGREES)
        self.add(label_x)
        self.add(label_y)
        self.play(Write(surface))  
        self.wait(1)       
        self.add_fixed_in_frame_mobjects(f_text)
        trace.rotate(-5).shift(0.2*RIGHT+0.8*UP+[0.6,-0.4,0.6])
        self.add(trace)
        self.play(Write(tangent_line),Write(d))
        self.wait(1)
        
        

        

        
