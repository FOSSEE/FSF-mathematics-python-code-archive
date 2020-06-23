from manimlib.imports import*

class TangenttoSurface(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 
        
        #----graph of first function f(x,y) = -x**2-y**2
        f = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [YELLOW_D, YELLOW_E],
            resolution = (20, 20)).scale(1) 
        f_text = TextMobject("Tangent plane at relative maxima").to_corner(UL).scale(0.5)

        #----graph of second function f(x,y) = -x**2+y**2   
        f2 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2+v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [RED_D, RED_E],
            resolution = (20, 20)).scale(1)
        f2_text = TextMobject("Tangent plane at saddle point").to_corner(UL).scale(0.5) 
        
        #----graph of third function f(x,y) = x**2+y**2   
        f3 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [GREEN_D, GREEN_E],
            resolution = (20, 20)).scale(1) 
        f3_text = TextMobject("Tangent plane at relative minima").to_corner(UL).scale(0.5)
        
        self.set_camera_orientation(phi = 75 * DEGREES, theta = -45 * DEGREES )
        d = Dot(np.array([0,0,0]), color = '#800000')        #---- critical point 

        r = Rectangle(height = 2,breadth = 1,color = PURPLE).scale(0.5)

        self.begin_ambient_camera_rotation(rate = 0.3) 
        self.add(axes)
        self.play(Write(f),Write(d))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(f_text)
        self.play(ShowCreation(r))
        self.wait(1)
        self.play(FadeOut(r),FadeOut(f),FadeOut(d),FadeOut(f_text))
        self.wait(1)
        self.play(Write(f2),Write(d))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(f2_text)
        self.play(ShowCreation(r))
        self.wait(1)
        self.play(FadeOut(r),FadeOut(f2),FadeOut(d),FadeOut(f2_text))
        self.wait(1)
        self.play(Write(f3),Write(d))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(f3_text)
        self.play(ShowCreation(r))
        self.wait(1)        
