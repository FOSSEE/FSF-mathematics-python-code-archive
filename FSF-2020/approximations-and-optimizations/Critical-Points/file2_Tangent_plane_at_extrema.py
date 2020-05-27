from manimlib.imports import*  

class TheoremAnimation(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()

        #----parabola: x**2+y**2
        parabola1 = ParametricSurface(  
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2
            ]),v_min=-1,v_max=1,u_min=-1,u_max=1,checkerboard_colors=[TEAL_E],
            resolution=(20, 20)).scale(1)     
        
        #----parabola: -x**2-y**2
        parabola2 = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-v**2
            ]),v_min=-1,v_max=1,u_min=-1,u_max=1,checkerboard_colors=[PURPLE_E,PURPLE_E],
            resolution=(20, 20)).scale(1)
               
        self.set_camera_orientation(phi=75 * DEGREES)  
        self.begin_ambient_camera_rotation(rate=0.4)  

        d = Dot(np.array([0,0,0]), color = '#800000')           #---- critical point     
        r = Rectangle(fill_color= '#C0C0C0',fill_opacity =0.3).move_to(ORIGIN)    #----tangent plane         

        parabola1_text = TextMobject("Maximum with horizontal tangent plane").scale(0.7).to_corner(UL)    
     
        parabola2_text = TextMobject("Minimum with horizontal tangent plane").scale(0.7).to_corner(UL)        

        self.add(axes)
        self.add_fixed_in_frame_mobjects(parabola2_text)
        self.wait(1) 
        self.play(Write(parabola1))
        self.wait(1)
        self.play(ShowCreation(d))
        self.wait(1)
        self.play(ShowCreation(r))     
        self.wait(2)
        self.play(FadeOut(parabola2_text),FadeOut(parabola1),FadeOut(r),FadeOut(d))  
        
        self.wait(1)
        self.add_fixed_in_frame_mobjects(parabola1_text)
        self.wait(1)
        self.play(Write(parabola2))
        self.wait(1)
        self.play(ShowCreation(d))
        self.wait(1)
        self.play(ShowCreation(r))     
        self.wait(2)
