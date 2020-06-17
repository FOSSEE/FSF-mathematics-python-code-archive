from manimlib.imports import*
import math as m


class CriticalPoint(ThreeDScene):
    def construct(self):
    
        axes = ThreeDAxes()
        
        surface = ParametricSurface( #---- partial derivatives of the funtion exists
            lambda u, v: np.array([
                u,
                v,
                m.exp(-10*u**2-10*v**2)]),u_min=-1,u_max=1, v_min=-1,v_max=1,checkerboard_colors=[TEAL_E,TEAL_D,TEAL_C]).fade(0.6).scale(3.5).shift([0,0,1.5])
        
        surface2 = ParametricSurface( #---- partial derivatives of the funtion does not exists
            lambda u, v: np.array([
                u,
                v,
                abs(u)+abs(v)]),u_min=-1.5,u_max=1.5, v_min=-1.5,v_max=1.5,checkerboard_colors=[TEAL_E,TEAL_D,TEAL_C,TEAL_B])
        
        l1 = Line([0,0,3.75],[0,0,0],color = '#800000')
        
        d = Dot([0,0,3.75],color = '#800000') #---- critical point of surface
        
        d2 = Dot([0,0,0],color = '#800000') #---- critical point of surface2
        
        d_text = TextMobject("$\\frac{\\partial f}{\\partial x}=\\frac{\\partial f}{\\partial y} = 0$").scale(1).to_corner(UL)
        
        d2_text = TextMobject("$\\frac{\\partial f}{\\partial x}$ and/or $\\frac{\\partial f}{\\partial y}$ does not exist").scale(0.8).to_corner(UL)
        
        f_text = TextMobject("Critical Point of a function",color = YELLOW).shift([3,0,3.7]).scale(0.7)

        g_text = TextMobject("Critical Point of a function",color = YELLOW).shift(1*DOWN).scale(0.5)
        
        self.set_camera_orientation(phi=75*DEGREES,theta=90*DEGREES) 
        self.add(axes)        
        self.begin_ambient_camera_rotation(rate=0.2)   
        self.play(Write(surface))
        self.add_fixed_in_frame_mobjects(d_text)
        self.wait(1)
        self.play(Write(l1))
        self.play(Write(d))
        self.wait(1)
        self.move_camera(phi=0 * DEGREES,theta = 90*DEGREES)
        self.wait(2)
        self.add_fixed_in_frame_mobjects(f_text)
        self.play(FadeOut(f_text),FadeOut(surface),FadeOut(axes),FadeOut(d_text),FadeOut(d),FadeOut(l1))
        self.wait(1)
        self.set_camera_orientation(phi=75*DEGREES,theta=60*DEGREES) 
        self.add(axes)        
        self.begin_ambient_camera_rotation(rate=0.3) 
        self.add_fixed_in_frame_mobjects(d2_text) 
        self.wait(1) 
        self.play(Write(surface2))
        l1.fade(0.4)
        self.play(Write(l1))
        self.play(Write(d2))        
        self.add_fixed_in_frame_mobjects(g_text)
        self.wait(2)
        
