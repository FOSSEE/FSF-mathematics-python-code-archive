from manimlib.imports import*

#---- visualization of the function 
class ExampleAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.5,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5) #---- y axis     

        #---- f(x,y) = (y-x)(1-2x-3y)
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (v-u)*(1-2*u-3*v)
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [PURPLE_B,PURPLE_C,PURPLE_D, PURPLE_E]).scale(1).fade(0.2).shift([0.2,0.2,0])   

        f_text = TextMobject("$f(x,y) = (y-x)(1-2x-3y)$").to_corner(UL)    
        
        self.set_camera_orientation(phi = 60 * DEGREES, theta = 75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.add_fixed_in_frame_mobjects(f_text)
        self.wait(1) 
        self.add(axes)
        self.add(label_x)
        self.add(label_y)
        self.wait(1)
        self.play(Write(f))
        self.wait(4)     
