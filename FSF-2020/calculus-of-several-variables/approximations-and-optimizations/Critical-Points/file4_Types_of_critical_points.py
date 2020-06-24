from manimlib.imports import*
 

#---- Relative Maxima 
class firstScene(ThreeDScene):
    def construct(self):

        r_text = TextMobject("Relative Maximum at ORIGIN",color ='#87CEFA')

        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.5,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5) #---- y axis

        #----graph of the function f(x,y) = -x**2-y**2
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [YELLOW_B,YELLOW_C,YELLOW_D, YELLOW_E]).scale(1.5).shift([0,0,-0.51]).fade(0.3)

        f_text = TextMobject("$f(x,y) = -x^2-y^2$").to_corner(UL)

        d = Dot(color = "#800000").shift([0,0,0]) #---- critical point

        self.set_camera_orientation(phi = 75 * DEGREES, theta = 45 * DEGREES)
        self.add_fixed_in_frame_mobjects(r_text)
        self.wait(1)
        self.play(FadeOut(r_text))
        self.begin_ambient_camera_rotation(rate = 0.1) 
        self.add(axes)
        self.add(label_x)
        self.add(label_y)
        self.play(Write(surface),Write(d))
        self.add_fixed_in_frame_mobjects(f_text)
        self.wait(2)
        self.play(FadeOut(axes),FadeOut(surface),FadeOut(f_text),FadeOut(d),FadeOut(label_x),FadeOut(label_y))


#---- Relative Minima 
class secondScene(ThreeDScene):
    def construct(self):

        r2_text = TextMobject("Relative Minimum at ORIGIN",color ='#87CEFA')

        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.5,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5) #---- y axis

        #----graph of the function g(x,y) = x**2+y**2
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors =[TEAL_B,TEAL_C,TEAL_D,TEAL_E]).scale(1.5).shift([0,0,0.55]).fade(0.1)

        d = Dot(color = "#800000").shift([0,0,0]) #---- critical point
        
        g_text = TextMobject("$f(x,y) = x^2+y^2$").to_corner(UL)   

        self.set_camera_orientation(phi = 75 * DEGREES, theta = 45 * DEGREES)
        self.add_fixed_in_frame_mobjects(r2_text)
        self.wait(1)
        self.play(FadeOut(r2_text))
        self.begin_ambient_camera_rotation(rate = 0.1) 
        self.add(axes)
        self.add(label_x)
        self.add(label_y)
        self.play(Write(surface),Write(d))
        self.add_fixed_in_frame_mobjects(g_text)
        self.wait(2)
        self.play(FadeOut(axes),FadeOut(surface),FadeOut(g_text),FadeOut(d),FadeOut(label_x),FadeOut(label_y))



#---- Saddle Point
class thirdScene(ThreeDScene):
    def construct(self):

        r3_text = TextMobject("Saddle Point", color = '#87CEFA')
    
        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.5,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5) #---- y axis     

        #---- graph of function h(x,y) = -x^2 + y^2   
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2+v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1,checkerboard_colors = [PURPLE_B,PURPLE_C,PURPLE_D,PURPLE_E]).scale(1.5).shift([0,0,0])
        
        #---- curve(trace) along x axis
        curve_x = ParametricSurface(
            lambda u, v: np.array([
                u*0.4,
                v,
                v**2
            ]),v_min = -1, v_max = 1, u_min = -0.2, u_max = 0.2).shift([0,0,0.34]).scale(1.5).set_color("#800000")

        #---- curve(trace) along y axis
        curve_y = ParametricSurface(
            lambda u, v: np.array([
                u,
                v*0.4,
                -u**2
            ]),v_min = -0.2, v_max = 0.2, u_min = -1, u_max = 1).scale(1.6).shift([0,0,-0.1]).set_color("#800000")
        
        d = Dot(color = GREEN).shift([0,0,0.1]) #---- critical point

        h_text = TextMobject("$f(x,y) = -x^2+y^2$").to_corner(UL)

        self.add_fixed_in_frame_mobjects(r3_text)
        self.wait(1)
        self.set_camera_orientation(phi = 50 * DEGREES,theta = 45 * DEGREES)
        self.play(FadeOut(r3_text))
        self.add(axes)    
        self.add(label_x)
        self.add(label_y)    
        self.begin_ambient_camera_rotation(rate = 0.3) 
        self.add_fixed_in_frame_mobjects(h_text)
        self.play(Write(surface))
        self.wait(1)               
        self.add(curve_y)
        self.add(d)
        self.wait(1)
        self.play(FadeOut(curve_y))
        self.wait(1)
        self.add(curve_x)
        self.wait(1)
        self.add(d)  
        self.wait(1)    
