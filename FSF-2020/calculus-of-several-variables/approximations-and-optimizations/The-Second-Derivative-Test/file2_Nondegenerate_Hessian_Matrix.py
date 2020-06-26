from manimlib.imports import*
import math as m
 
class Minima(ThreeDScene):
    def construct(self):

        heading = TextMobject("Nondegenerate Hessian Matrix",color = BLUE)

        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.3,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.3,5.5,0]).rotate(-4.5) #---- y axis

        h_text = TextMobject("Case 1: $\\frac{\\partial^2 f}{\\partial x^2}>0$ and $\\frac{\\partial^2 f}{\\partial y^2}>0$").scale(1)

        #---- determiniant of Hessian Matrix
        hessian_surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -0.5*m.exp(-u**2-v**2)
            ]),u_min = -PI, u_max = PI, v_min = -PI, v_max =PI).set_color(TEAL).shift([0,0,0]).scale(1).fade(0.2)
        
        det_text= TextMobject("$det \\hspace{1mm} H = (\\frac{\\partial^2 f}{\\partial x^2})(\\frac{\\partial^2 f}{\\partial y^2})-(\\frac{\\partial^2 f}{\\partial x \\partial y})^2 $").to_corner(UL).scale(0.7)

        #---- function f(x,y)
        f_surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2
            ]),u_min = -1.3, u_max = 1.3, v_min = -1.3, v_max = 1.3).set_color(TEAL).shift([0,0,-0.5])
        
        f_text= TextMobject("surface of the function").to_corner(UL).scale(0.8)
        
        d = Dot(color = "#800000").shift([0,0,-0.52]) #---- critical point 
        
        self.set_camera_orientation(phi = 75*DEGREES, theta = 40*DEGREES) 
        self.add_fixed_in_frame_mobjects(heading)
        self.wait(1)
        self.play(FadeOut(heading))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(h_text)
        self.wait(1)
        self.play(FadeOut(h_text))
        self.wait(1)
        self.add(axes)     
        self.add(label_x)
        self.add(label_y)
        self.play(Write(hessian_surface))   
        self.wait(1)
        self.add_fixed_in_frame_mobjects(det_text)
        self.move_camera(phi = 90*DEGREES, theta= 60*DEGREES)
        self.play(Write(d))
        self.wait(1)
        self.play(FadeOut(det_text),ReplacementTransform(hessian_surface,f_surface))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(f_text)
        self.wait(1)
        self.play(FadeOut(f_text),FadeOut(f_surface),FadeOut(axes),FadeOut(label_x),FadeOut(label_y),FadeOut(d))
        
class Maxima(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.3,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.3,5.5,0]).rotate(-4.5) #---- y axis

        h_text = TextMobject("Case  2: $\\frac{\\partial^2 f}{\\partial x^2}<0$ and $\\frac{\\partial^2 f}{\\partial y^2}<0$").scale(1)

        #---- determiniant of Hessian Matrix
        hessian_surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                0.5*m.exp(-u**2-v**2)
            ]),u_min = -PI, u_max = PI, v_min = -PI, v_max =PI).set_color(TEAL).shift([0,0,0]).scale(1).fade(0.2)
        
        det_text= TextMobject("$det \\hspace{1mm} H = (\\frac{\\partial^2 f}{\\partial x^2})(\\frac{\\partial^2 f}{\\partial y^2})-(\\frac{\\partial^2 f}{\\partial x \\partial y})^2 $").to_corner(UL).scale(0.7)

        #---- function g(x,y)
        g_surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-v**2
            ]),u_min = -1.3, u_max = 1.3, v_min = -1.3, v_max = 1.3).set_color(TEAL).shift([0,0,0.5])
        
        g_text= TextMobject("surface of the function").to_corner(UL).scale(0.8)
        
        d = Dot(color = "#800000").shift([0,0,0.5]) #---- critical point 
        
        self.set_camera_orientation(phi = 75*DEGREES, theta = 40*DEGREES) 
        self.add_fixed_in_frame_mobjects(h_text)
        self.wait(1)
        self.play(FadeOut(h_text))
        self.wait(1)
        self.add(axes)     
        self.add(label_x)
        self.add(label_y)
        self.play(Write(hessian_surface))   
        self.wait(1)
        self.add_fixed_in_frame_mobjects(det_text)
        self.play(Write(d))
        self.wait(1)
        self.play(FadeOut(det_text),ReplacementTransform(hessian_surface,g_surface))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(g_text)
        self.wait(1)
        self.play(FadeOut(g_text),FadeOut(g_surface),FadeOut(axes),FadeOut(label_x),FadeOut(label_y),FadeOut(d))

class SaddlePoint(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.3,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.3,5.5,0]).rotate(-4.5) #---- y axis

        h_text = TextMobject("Case 3: $\\frac{\\partial^2 f}{\\partial x^2}$ and $\\frac{\\partial^2 f}{\\partial y^2}$ have opposite signs").scale(1)

        #---- determiniant of Hessian Matrix
        hessian_surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                m.exp(0.5*u**2-0.5*v**2)
            ]),u_min = -1.2, u_max = 1.2, v_min = -2.5, v_max = 2.5).set_color(TEAL).shift([0,0,-1]).scale(1).fade(0.2)
        
        det_text= TextMobject("$det \\hspace{1mm} H = (\\frac{\\partial^2 f}{\\partial x^2})(\\frac{\\partial^2 f}{\\partial y^2})-(\\frac{\\partial^2 f}{\\partial x \\partial y})^2 $").to_corner(UL).scale(0.7)

        #---- function p(x,y)
        p_surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]),u_min = -1, u_max = 1, v_min = -1, v_max =1).set_color(TEAL).shift([0,0,0]).scale(2)
        
        p_text= TextMobject("surface of the function").to_corner(UL).scale(0.8)
        
        d = Dot(color = "#800000").shift([0,0,0]) #---- critical point 
        
        self.set_camera_orientation(phi = 80*DEGREES, theta = 60*DEGREES) 
        self.add_fixed_in_frame_mobjects(h_text)
        self.wait(1)
        self.play(FadeOut(h_text))
        self.wait(1)
        self.add(axes)     
        self.add(label_x)
        self.add(label_y)  
        self.wait(1)
        self.play(Write(hessian_surface)) 
        self.play(Write(d))    
        self.wait(1)
        self.add_fixed_in_frame_mobjects(det_text)
        self.wait(2)
        self.play(FadeOut(det_text),ReplacementTransform(hessian_surface,p_surface))
        self.add_fixed_in_frame_mobjects(p_text)
        self.wait(2)
