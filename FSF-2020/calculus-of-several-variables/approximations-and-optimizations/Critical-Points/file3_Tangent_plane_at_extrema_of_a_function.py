from manimlib.imports import*  

#---- tangent plane to minima of the function
class firstScene(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.5,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5) #---- y axis

        #---- parabola: f(x,y) = x**2 + y**2
        parabola = ParametricSurface(  
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [GREEN_E,GREEN_D,GREEN_C,GREEN_B], resolution = (20, 20)).scale(1)     
        
        d = Dot(np.array([0,0,0]), color = '#800000') # ---- critical point     

        tangent_plane = Rectangle(fill_color = '#C0C0C0', fill_opacity = 0.3).move_to(ORIGIN).fade(0.7)  # ----tangent plane         
     
        parabola_text = TextMobject("Minimum with horizontal tangent plane").scale(0.7).to_corner(UL)  

        self.set_camera_orientation(phi = 75 * DEGREES, theta = 45 * DEGREES)  
        self.begin_ambient_camera_rotation(rate = 0.2) 
        self.add(axes)
        self.add(label_x)
        self.add(label_y)
        self.add_fixed_in_frame_mobjects(parabola_text)
        self.wait(1) 
        self.play(Write(parabola))
        self.play(ShowCreation(d))
        self.wait(1)
        self.play(ShowCreation(tangent_plane))     
        self.wait(2)
        self.play(FadeOut(parabola_text),FadeOut(parabola),FadeOut(tangent_plane),FadeOut(d),FadeOut(label_x),FadeOut(label_y),FadeOut(axes))  


#---- tangent plane to maxima of the function
class secondScene(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.5,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5) #---- y axis   
        
        #----parabola: g(x,y) = -x**2-y**2
        parabola = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [BLUE_E,BLUE_D,BLUE_C,BLUE_B], resolution = (20, 20)).scale(1)
        
        d = Dot(np.array([0,0,0]), color = '#800000') #---- critical point     

        tangent_plane = Rectangle(fill_color = '#C0C0C0',fill_opacity = 0.3).move_to(ORIGIN).fade(0.7) #---- tangent plane         

        parabola_text = TextMobject("Maximum with horizontal tangent plane").scale(0.7).to_corner(UL)        

        self.set_camera_orientation(phi = 75 * DEGREES, theta = 45 * DEGREES)  
        self.begin_ambient_camera_rotation(rate = 0.2) 
        self.add(axes)
        self.add(label_x)
        self.add(label_y)
        self.add_fixed_in_frame_mobjects(parabola_text)
        self.wait(1) 
        self.play(Write(parabola))
        self.play(ShowCreation(d))
        self.wait(1)
        self.play(ShowCreation(tangent_plane))     
        self.wait(2)    
