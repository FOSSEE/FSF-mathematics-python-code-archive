from manimlib.imports import *


class MaximaScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        
        r_text = TextMobject("Relative Maximum at ORIGIN",color ='#87CEFA')
        f_text = TextMobject("$f(x,y) = -x^2-y^2$").to_corner(UL)

        #----graph of first function f(x,y) = -x**2-y**2
        f = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [YELLOW_B,YELLOW_C,YELLOW_D, YELLOW_E],
            resolution = (20, 20)).scale(1.5).shift([0,0,-0.51]).fade(0.3)
        
        d = Dot(np.array([0,0,0]), color = '#800000')        #---- critical point 
        
        self.set_camera_orientation(phi = 75 * DEGREES, theta = -45 * DEGREES )
        self.add_fixed_in_frame_mobjects(r_text)
        self.wait(1)
        self.play(FadeOut(r_text))
        self.add(axes)
        self.play(Write(f),Write(d))
        self.add_fixed_in_frame_mobjects(f_text)
        self.wait(2)
        self.play(FadeOut(axes),FadeOut(f),FadeOut(f_text),FadeOut(d))
        
class SaddlePoint(ThreeDScene):
    def construct(self):

        r2_text = TextMobject("Saddle Point",color ='#87CEFA')    
        axes = ThreeDAxes()
        
        #----graph of third function f(x,y) = -x**2+y**2   
        f2 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2+v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1,checkerboard_colors = [PURPLE_B,PURPLE_C,PURPLE_D,PURPLE_E]).scale(1.5).shift([0,0,0])
        
        #---- trace along y axis
        a = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                v**2
            ]),v_min = -1, v_max = 1, u_min = -0.2, u_max = 0.2).shift([0,0,0.36]).scale(1.5).set_color(GREEN)
        
        #---- trace along x axis
        b = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2
            ]),v_min = -0.2, v_max = 0.2, u_min = -1, u_max = 1).scale(1.6).shift([0,0,-0.1]).set_color(GREEN)
        
        d = Dot(color = '#800000').shift([0,0,0.1]) #---- critical point
        
        f2_text = TextMobject("$f(x,y) = -x^2+y^2$").to_corner(UL)
        
        self.add_fixed_in_frame_mobjects(r2_text)
        self.wait(1)
        self.set_camera_orientation(phi=75*DEGREES,theta=10*DEGREES)
        self.play(FadeOut(r2_text))
        self.add(axes)        
        self.begin_ambient_camera_rotation(rate=0.4) 
        self.add_fixed_in_frame_mobjects(f2_text)
        self.play(Write(f2))         
        self.add(b)
        self.wait(1)
        self.add(a)
        self.wait(3)
        self.add(d)          
        self.wait(2)
      
    
class MinimaScene(ThreeDScene):
    def construct(self):
        
        r3_text = TextMobject("Relative Minimum at ORIGIN",color ='#87CEFA')
        axes = ThreeDAxes()
        
        f3_text = TextMobject("$f(x,y) = x^2+y^2$").to_corner(UL)         
        
        #----graph of third function f(x,y) = x**2+y**2   
        f3 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors =[TEAL_B,TEAL_C,TEAL_D,TEAL_E],
            resolution = (20, 20)).scale(1.5).shift([0,0,0.55]).fade(0.1) 
        
        self.set_camera_orientation(phi = 75 * DEGREES, theta = -45 * DEGREES )
        d = Dot(np.array([0,0,0]), color = '#800000')        #---- critical point  
        
        self.add_fixed_in_frame_mobjects(r3_text)
        self.wait(1)
        self.play(FadeOut(r3_text))
        self.add(axes)
        self.play(Write(f3),Write(d))
        self.add_fixed_in_frame_mobjects(f3_text)
        self.wait(2)
