from manimlib.imports import *

class TypescpAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        
        r_text = TextMobject("Relative Maxima at ORIGIN",color ='#87CEFA')
        f_text = TextMobject("$f(x,y) = -x^2-y^2$").to_corner(UL)

        #----graph of first function f(x,y) = -x**2-y**2
        f = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [YELLOW_D, YELLOW_E],
            resolution = (20, 20)).scale(1) 
        
        r2_text = TextMobject("Saddle Point at ORIGIN",color ='#87CEFA')
        f2_text = TextMobject("$f(x,y) = -x^2+y^2$").to_corner(UL)

        #----graph of second function f(x,y) = -x**2+y**2   
        f2 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2+v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [RED_D, RED_E],
            resolution = (20, 20)).scale(1)
        
        r3_text = TextMobject("Relative Minima at ORIGIN",color ='#87CEFA')
        f3_text = TextMobject("$f(x,y) = x^2+y^2$").to_corner(UL)         
        
        #----graph of third function f(x,y) = x**2+y**2   
        f3 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [GREEN_D, GREEN_E],
            resolution = (20, 20)).scale(1) 
        
        self.set_camera_orientation(phi = 75 * DEGREES, theta = -45 * DEGREES )

        self.add_fixed_in_frame_mobjects(r_text)
        self.wait(1)
        self.play(FadeOut(r_text))
        self.add(axes)
        self.play(Write(f))
        self.add_fixed_in_frame_mobjects(f_text)
        self.wait(2)
        self.play(FadeOut(axes),FadeOut(f),FadeOut(f_text))

        self.add_fixed_in_frame_mobjects(r2_text)
        self.wait(1)
        self.play(FadeOut(r2_text))
        self.add(axes)
        self.play(Write(f2))
        self.add_fixed_in_frame_mobjects(f2_text)
        self.wait(2)
        self.play(FadeOut(axes),FadeOut(f2),FadeOut(f2_text))

        self.add_fixed_in_frame_mobjects(r3_text)
        self.wait(1)
        self.play(FadeOut(r3_text))
        self.add(axes)
        self.play(Write(f3))
        self.add_fixed_in_frame_mobjects(f3_text)
        self.wait(2)
