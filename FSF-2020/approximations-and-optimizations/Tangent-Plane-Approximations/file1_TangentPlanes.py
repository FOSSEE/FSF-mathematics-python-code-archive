from manimlib.imports import*  

class TangenttoSurface(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() 
        
        #parabola: -x**2-y**2
        p = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-v**2
            ]),v_min=-1,v_max=1,u_min=-1,u_max=1,checkerboard_colors=[BLUE_C,TEAL_D],
            resolution=(20, 20)).scale(1).shift(1*RIGHT+2*UP)
        self.set_camera_orientation(phi = 35 * DEGREES,theta = -40 * DEGREES )            

        r = Rectangle(side_length=2,side_breadth= 1, fill_color=PURPLE, fill_opacity=0.2).shift(ORIGIN-1+3*UP+2*RIGHT).scale(0.7) #---tangent plane along x axis
        
        r_text = TextMobject("Tangent Plane along $x$ axis",color = '#FFE4E1').scale(0.6).to_corner(UL)
        r2_text = TextMobject("Tangent Plane along $y$ axis",color = '#FFE4E1').scale(0.6).to_corner(UL)  

        a = Arrow(color = '#FFFFF0').shift(ORIGIN-1+3*UP+4*RIGHT).scale(0.5) 
        a2 = Arrow(color = '#FFFFF0').shift(ORIGIN+0.5+3*UP+RIGHT).scale(0.5)
        a2.rotate(1.571) #----1.571 radian = 90 degrees
        
        self.add(axes)
        self.play(Write(p))
        self.begin_ambient_camera_rotation(rate = 0.1)
        self.add_fixed_in_frame_mobjects(r_text)
        self.play(ShowCreation(r))
        self.play(ShowCreation(a))
        self.wait(1)        
        self.play(FadeOut(r),FadeOut(a),FadeOut(r_text))

        r.rotate(1.571) #---tangent plane along y axis
        self.play(ShowCreation(r))
        self.play(ShowCreation(a2))
        self.add_fixed_in_frame_mobjects(r2_text)
        self.wait(2)
