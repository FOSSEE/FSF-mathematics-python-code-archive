from manimlib.imports import*
import math

#---- tangent plane does not exists for f(x,y): sqrt(x**2+y**2) at origin

class TangenttoSurface(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 
        
        #----f(x,y): sqrt(x**2+y**2)
        p = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                math.sqrt(u**2+v**2)
            ]),v_min = -1,v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [RED_C,TEAL_D],
            resolution = (20, 20)).scale(1)

        self.set_camera_orientation(phi = 75 * DEGREES)  
         
        d = Dot([0,0,0],color = '#800000') #----critical point
        d_text = TextMobject("$(0,0)$").scale(0.5).shift(0.2*DOWN)
        f_text = TextMobject("$f$ is not differentiable at origin").scale(0.5).to_corner(UL)

        self.begin_ambient_camera_rotation(rate=0.1) 
        self.add(axes)
        self.play(Write(p),Write(d))      
        self.add_fixed_in_frame_mobjects(d_text)
        self.add_fixed_in_frame_mobjects(f_text)
        self.wait(2)
