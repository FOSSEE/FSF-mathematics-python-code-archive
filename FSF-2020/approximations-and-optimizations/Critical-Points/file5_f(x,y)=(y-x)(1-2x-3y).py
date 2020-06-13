from manimlib.imports import*

class ExampleAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        f_text = TextMobject("$f(x,y) = (y-x)(1-2x-3y)$").to_corner(UL)        

        #----f(x,y) = (y-x)(1-2x-3y)
        f = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (v-u)*(1-2*u-3*v)
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [PURPLE_B,PURPLE_C,PURPLE_D, PURPLE_E],
            resolution=(20, 20)).scale(1).fade(0.2).shift([0.2,0.2,0])     
        
        self.set_camera_orientation(phi = 75 * DEGREES,theta= 60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        self.add_fixed_in_frame_mobjects(f_text)
        self.wait(1) 
        self.add(axes)
        self.play(Write(f))
        self.wait(3)
