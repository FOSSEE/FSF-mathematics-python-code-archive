from manimlib.imports import*

#---- graphs of second-order partial derivatives of a function
class SurfacesAnimation(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()
        x_label = TextMobject('$x$').shift([5,0.5,0]) #---- x axis
        y_label = TextMobject('$y$').shift([0.5,4,0]).rotate(-4.5) #---- y axis
        
        #---- surface of function: f(x,y) = (x^2+y^2)^2
        surface_f = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                ((u**2)+(v**2))**2
            ]),v_min=-1,v_max=1,u_min=-1,u_max=1,checkerboard_colors=[GREEN_D, GREEN_E]).scale(1)
 
        #---- surface of second-order partial derivative f_xx
        surface_fxx = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (3*u**2)+(v**2)
            ]),v_min=-1,v_max=1,u_min=-1,u_max=1,checkerboard_colors=[YELLOW_D, YELLOW_E]).shift([0,0,0]).scale(0.6)
        
        #---- surface of second-order partial derivative f_yy
        surface_fyy = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (u**2)+(3*v**2)
            ]),v_min=-1,v_max=1,u_min=-1,u_max=1,checkerboard_colors=[PURPLE_D, PURPLE_E]).scale(0.6).shift([0,0,0])
        
        #---- surface of second-order partial derivative f_xy = f_yx
        surface_fxy = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                8*u*v
            ]),v_min=-1,v_max=1,u_min=-1,u_max=1,checkerboard_colors=[TEAL_D, TEAL_E]).scale(0.6)

        f_text= TextMobject("$f(x,y) = (x^2+y^2)^2$",color = GREEN).scale(0.7).to_corner(UL)

        fxx_text= TextMobject("$f_{xx} = 12x^2+4y^2$ (Concavity along x axis)",color = YELLOW).scale(0.5).to_corner(UL)

        fyy_text= TextMobject("$f_{yy} = 4x^2+12y^2$(Concavity along y axis)",color = PURPLE).scale(0.5).to_corner(UL)

        fxy_text= TextMobject("$f_{xy} = f_{yx} = 8xy$ (Twisting of the function)",color = TEAL).scale(0.5).to_corner(UL)


        self.set_camera_orientation(phi = 40 * DEGREES, theta = 45 * DEGREES)
        self.begin_ambient_camera_rotation(rate = 0.1)
        self.add_fixed_in_frame_mobjects(f_text)
        self.add(axes)
        self.add(x_label)
        self.add(y_label)
        self.wait(1)
        self.play(Write(surface_f))
        self.wait(2)
        self.play(FadeOut(f_text))


        self.play(ReplacementTransform(surface_f,surface_fxx))
        
        self.add_fixed_in_frame_mobjects(fxx_text)
        self.wait(2)
        self.play(FadeOut(fxx_text))

        self.play(ReplacementTransform(surface_fxx,surface_fyy))
        self.add_fixed_in_frame_mobjects(fyy_text)
        self.wait(2)
        self.play(FadeOut(fyy_text))

        self.play(ReplacementTransform(surface_fyy,surface_fxy))      
        self.move_camera(phi = 35 * DEGREES, theta = 80 * DEGREES)
        self.add_fixed_in_frame_mobjects(fxy_text)
        self.wait(2)
