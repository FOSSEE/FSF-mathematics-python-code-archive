from manimlib.imports import *

class TypescpAnimation(ThreeDScene):
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
        
        r2_text = TextMobject("Saddle Point at ORIGIN",color ='#87CEFA')
        f2_text = TextMobject("$f(x,y) = -x^2+y^2$").to_corner(UL)

        #----graph of second function f(x,y) = -x**2+y**2   
        f2 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2+v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [RED_B,RED_C,RED_D, RED_E],
            resolution = (20, 20)).scale(1.5).shift([0,0.2,0]).fade(0.3)
        
        r3_text = TextMobject("Relative Minimum at ORIGIN",color ='#87CEFA')
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

        self.add_fixed_in_frame_mobjects(r_text)
        self.wait(1)
        self.play(FadeOut(r_text))
        self.add(axes)
        self.play(Write(f),Write(d))
        self.add_fixed_in_frame_mobjects(f_text)
        self.wait(2)
        self.play(FadeOut(axes),FadeOut(f),FadeOut(f_text),FadeOut(d))

        self.add_fixed_in_frame_mobjects(r2_text)
        self.wait(1)
        self.play(FadeOut(r2_text))
        self.add(axes)
        self.play(Write(f2),Write(d))
        self.add_fixed_in_frame_mobjects(f2_text)
        self.wait(2)
        self.play(FadeOut(axes),FadeOut(f2),FadeOut(f2_text),FadeOut(d))

        self.add_fixed_in_frame_mobjects(r3_text)
        self.wait(1)
        self.play(FadeOut(r3_text))
        self.add(axes)
        self.play(Write(f3),Write(d))
        self.add_fixed_in_frame_mobjects(f3_text)
        self.wait(2)
