from manimlib.imports import*
import math as m


class CriticalPoint(ThreeDScene):
    def construct(self):
    
        axes = ThreeDAxes()
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                m.exp(-10*u**2-10*v**2) #---- function equation
            ]),u_min=-1,u_max=1, v_min=-1,v_max=1,checkerboard_colors=[TEAL_E,TEAL_D,TEAL_C]).fade(0.6).scale(3.5).shift([0,0,1.5])
        
        l1 = Line([0,0,3.75],[0,0,0],color = '#800000')
        
        d = Dot([0,0,3.75],color = '#800000')
        f_text = TextMobject("Critical Point of a function",color = YELLOW).shift([3,0,3.7]).scale(0.7)

        self.add(axes)
        self.set_camera_orientation(phi=75*DEGREES,theta=90*DEGREES) 
        self.begin_ambient_camera_rotation(rate=0.4)   
        self.play(Write(surface))
        self.wait(1)
        self.play(Write(l1))
        self.play(Write(d))
        self.wait(2)
        self.move_camera(phi=0 * DEGREES,theta = 90*DEGREES)
        self.add_fixed_in_frame_mobjects(f_text)
        self.wait(1)
        
