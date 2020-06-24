from manimlib.imports import*
import math

#---- tangent plane does not exists for f(x,y): sqrt(x**2+y**2) at origin

class TangenttoSurface(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().rotate(2.3)
        axes2 = ThreeDAxes().scale(2).rotate(2.3).shift([0,0,1.3])
        
        #----f(x,y): sqrt(x**2+y**2)
        p = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -math.sqrt(u**2+v**2)
            ]),v_min = -1,v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [RED_C,TEAL_D],
            resolution = (20, 20)).scale(1)
        
        #----size increased of f(x,y): sqrt(x**2+y**2)
        p2 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -math.sqrt(u**2+v**2)
            ]),v_min = -1,v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [RED_C,TEAL_D],
            resolution = (20, 20)).scale(3).shift([0,0,0])

        self.set_camera_orientation(phi = 75 * DEGREES,theta = 40*DEGREES)  

        d = Dot([0,0,0],color = '#800000')  #---- critical point
        d2 = Dot([0,0,1.5],color = '#800000').scale(2) #---- size increased of critical point      

        f_text = TextMobject("$f$ is not differentiable at origin,because the surface").scale(0.5).to_corner(UL)
        f2_text = TextMobject("is not flat when zoomed in at the origin.").scale(0.5).to_corner(UL).shift(0.5*DOWN)

        self.add(axes)
        self.wait(1)
        self.play(Write(p),Write(d)) 
        self.wait(1)    
        self.move_camera(phi = 50 * DEGREES,theta = 40*DEGREES) 
        self.wait(1)
        self.play(ReplacementTransform(axes,axes2),ReplacementTransform(p,p2),ReplacementTransform(d,d2)) 
        self.wait(1)
        self.add_fixed_in_frame_mobjects(f_text)
        self.add_fixed_in_frame_mobjects(f2_text)
        self.wait(2)
