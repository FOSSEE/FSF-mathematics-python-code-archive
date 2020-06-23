from manimlib.imports import*
import math as m

#---- tangent to the trace with x constant
class firstScene(ThreeDScene):
    def construct(self):
    
        axes = ThreeDAxes().scale(1)
        label_x = TextMobject("$x$").shift([5.8,-0.5,0])
        label_y = TextMobject("$y$").shift([-0.5,-5.6,0]).rotate(-4.5)
        
        #---- graph of f(x,y) = -x^2-y^2
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-v**2
            ]),u_min=-1,u_max=1, v_min=-1,v_max=1,checkerboard_colors=[PURPLE_C,PURPLE_D,PURPLE_E,PURPLE_B]).scale(1.5).shift([0,0,2]).rotate(0.2)
        
        #---- curve(trace) along y axis
        curve = ParametricSurface(
            lambda u, v: np.array([
                u*0.4,
                v,
                -v**2
            ]),v_min =-1 , v_max =1 , u_min = -0.1, u_max = 0.1).scale(1.6).shift([0.02,0.1,2.3]).set_color("#800000").rotate(0.1)

        d = Dot(color =YELLOW).shift([-0.05,-0.2,2.3]) #---- critical point

        x_text = TextMobject("Tangent to the trace with $x$ constant at critical point").shift(3*RIGHT+2*UP).scale(0.5).to_corner(UL)

        tangent_line = Line([-0.05,-1.5,2.3],[-0.05,1.5,2.3],color = '#228B22')

        self.add(axes)
        self.set_camera_orientation(phi = 40 * DEGREES, theta = 55 * DEGREES)
        self.begin_ambient_camera_rotation(rate = 0.1) 
        self.add(label_x)
        self.add(label_y)
        self.play(Write(surface))  
        self.add_fixed_in_frame_mobjects(x_text)
        self.add(curve)
        self.wait(1)
        self.play(Write(tangent_line),Write(d))
        self.wait(1)  



#---- tangent to the trace with y constant
class secondScene(ThreeDScene):
    def construct(self):
    
        axes = ThreeDAxes().scale(1)
        label_x = TextMobject("$x$").shift([5.8,-0.5,0])
        label_y = TextMobject("$y$").shift([-0.5,-5.6,0]).rotate(-4.5)
        
        #---- graph of f(x,y) = -x^2-y^2
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-v**2
            ]),u_min = -1, u_max = 1, v_min = -1, v_max = 1, checkerboard_colors = [PURPLE_B,PURPLE_C,PURPLE_D,PURPLE_E]).scale(1.5).shift([0,0,2]).rotate(0.2)

        #---- curve(trace) along x axis
        curve = ParametricSurface(
            lambda u, v: np.array([
                u,
                v*0.4,
                -u**2
            ]),v_min = -0.1, v_max = 0.1, u_min = -1, u_max = 1).scale(1.6).shift([0.07,0.1,2.3]).set_color("#800000")
        
        d = Dot(color = YELLOW).shift([0,-0.2,2.3]) #---- critical point
        
        tangent_line = Line(color = '#228B22').scale(1).shift([0,-0.2,2.3]).rotate(m.radians(190),LEFT)
        
        y_text = TextMobject("Tangent to the trace with $y$ constant at critical point").shift(3*RIGHT+2*UP).scale(0.5).to_corner(UL)

        self.add(axes)
        self.set_camera_orientation(phi = 40 * DEGREES, theta = 55 * DEGREES)
        self.add(label_x)
        self.add(label_y)
        self.begin_ambient_camera_rotation(rate = 0.1) 
        self.play(Write(surface))  
        self.add_fixed_in_frame_mobjects(y_text)
        self.add(curve)
        self.wait(1.5)
        self.play(Write(tangent_line),Write(d))
        self.wait(0.5)
