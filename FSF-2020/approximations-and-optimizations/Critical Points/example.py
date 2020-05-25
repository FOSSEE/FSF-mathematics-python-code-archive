from manimlib.imports import*

class ExampleAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        f_text = TextMobject("$f(x,y) = (y-x)(1-2x-3y)$").to_corner(UL)        
        d = Dot(np.array([0,0,0]), color = '#800000')  #---- Critical Point
        d_text = TextMobject("$(0.2,0.2)$",color = '#DC143C').scale(0.5).shift(0.2*UP)  #----x = 0.2, y = 0.2
        r_text=TextMobject("Critical Point",color = '#00FFFF').shift(0.3*DOWN).scale(0.6)

        #----f(x,y) = (y-x)(1-2x-3y)
        f = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (v-u)*(1-2*u-3*v)
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [PURPLE_D, PURPLE_E],
            resolution=(20, 20)).scale(1)       
        
        fx_text = TextMobject("$\\frac{\\partial f}{\\partial x} = 4x-1+y$").to_corner(UL)

        #----fx = 4x-1+y
        fx = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                4*u-1+v
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [BLUE_D, BLUE_E],
            resolution = (20, 20)).scale(1)

        fy_text = TextMobject("$\\frac{\\partial f}{\\partial y} = -6y+1+x$").to_corner(UL)

        #----fy = -6y+1+x
        fy = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -6*v+1+u
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [RED_D, RED_E],
            resolution = (20, 20)).scale(1)

        self.set_camera_orientation(phi = 75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        group1 = VGroup(axes,f,d,d_text,r_text,f_text)
        group2 = VGroup(axes,fx,fx_text)

        self.add_fixed_in_frame_mobjects(f_text)
        self.wait(1) 
        self.add(axes)
        self.play(Write(f),Write(d))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(d_text)
        self.wait(1)
        self.add_fixed_in_frame_mobjects(r_text)
        self.wait(2)
        self.play(FadeOut(group1))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(fx_text) 
        self.add(axes)
        self.play(Write(fx))
        self.wait(2)
        self.play(FadeOut(group2))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(fy_text) 
        self.add(axes)
        self.play(Write(fy))
        self.wait(2)
