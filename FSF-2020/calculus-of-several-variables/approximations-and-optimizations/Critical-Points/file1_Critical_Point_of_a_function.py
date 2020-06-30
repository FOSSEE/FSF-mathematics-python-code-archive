from manimlib.imports import*
import math as m

#---- case 1:  parial derivatives exist at critical point of the function
class firstScene(ThreeDScene):
    def construct(self):
    
        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.5,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5) #---- y axis
        
        #---- f(x,y) = e^(-10x^2-10y^2)
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                m.exp(-10*u**2-10*v**2)
            ]),u_min = -1, u_max = 1, v_min = -1, v_max = 1, checkerboard_colors = [TEAL_E,TEAL_D,TEAL_C,TEAL_B]).fade(0.6).scale(3.5).shift([0,0,1.5])
        
        l1 = Line([0,0,3.75],[0,0,0],color = '#800000')
        
        d = Dot([0,0,3.75],color = '#800000') #---- critical point

        d_text = TextMobject("$\\frac{\\partial f}{\\partial x}=\\frac{\\partial f}{\\partial y} = 0$").scale(0.8).to_corner(UL)

        f_text = TextMobject("Critical Point ",color = YELLOW).shift(3.4*UP).scale(0.5)

        self.set_camera_orientation(phi = 45*DEGREES, theta = 40*DEGREES) 
        self.add(axes)     
        self.add(label_x)
        self.add(label_y) 
        self.add_fixed_in_frame_mobjects(d_text)
        self.begin_ambient_camera_rotation(rate = 0.2) 
        self.play(Write(surface))        
        self.wait(1)
        self.play(Write(l1))
        self.play(Write(d))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(f_text)
        self.wait(3)
        self.play(FadeOut(f_text),FadeOut(surface),FadeOut(axes),FadeOut(d_text),FadeOut(d),FadeOut(l1),FadeOut(label_x),FadeOut(label_y))      

        
#---- case 2:  parial derivatives do not exist at critical point of the function
class secondScene(ThreeDScene): 
    def construct(self):
        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.5,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5) #---- y axis

        #---- g(x,y)= |x|+|y|
        surface = ParametricSurface( 
            lambda u, v: np.array([
                u,
                v,
                abs(u)+abs(v)
            ]),u_min = -1.5, u_max = 1.5, v_min = -1.5, v_max = 1.5, checkerboard_colors = [TEAL_E,TEAL_D,TEAL_C,TEAL_B])

        d2 = Dot([0,0,0],color = '#800000') #---- critical point

        d2_text = TextMobject("$\\frac{\\partial f}{\\partial x}$ and/or $\\frac{\\partial f}{\\partial y}$ does not exist").scale(0.7).to_corner(UL)

        g_text = TextMobject("Critical Point",color = YELLOW).shift(1.2*RIGHT).scale(0.6)

        self.set_camera_orientation(phi = 60*DEGREES, theta = 40*DEGREES) 
        self.add(axes)    
        self.add(label_x)
        self.add(label_y) 
        self.add_fixed_in_frame_mobjects(d2_text)
        self.begin_ambient_camera_rotation(rate = 0.2) 
        self.wait(1)         
        self.play(Write(surface2))
        self.wait(1)
        self.play(Write(d2)) 
        self.wait(1)       
        self.add_fixed_in_frame_mobjects(g_text)
        self.wait(2)        
