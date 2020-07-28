from manimlib.imports import*
import math as m

class Contourplots(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().scale(0.7).rotate(math.radians(180)).fade(0.6)     
        label_x = TextMobject("$x$").shift(4*LEFT).fade(0.4)  #---- x axis
        label_y = TextMobject("$y$").shift(3.5*DOWN+0.2*RIGHT).rotate(math.radians(180)).fade(0.4)  #---- y axis

        #---- surface of the function
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2+u**3-v**3
            ]),u_min=-0.5,u_max=0.5, v_min=-0.5,v_max=0.5).scale(6).shift([0,0,2.5]).set_color(TEAL).fade(0.5)
        
        #---- contour plots 
        curve1 = ParametricSurface(
            lambda u, v: np.array([
                u*0.4,
                m.exp(m.sin(v**2)),
                -v*2.2
            ]),v_min =-1.3 , v_max =1.3, u_min = -0.1, u_max = 0.1).scale(0.8).shift([0,-2.65,0]).set_color("#800000").rotate(1.2,DOWN)
        
        curve2 = ParametricSurface(
            lambda u, v: np.array([
                u*0.4,
                m.exp(m.sin(v**2)),
                -v*2.2
            ]),v_min =-1.3 , v_max =1.3, u_min = -0.1, u_max = 0.1).scale(0.9).shift([0,-3,0]).set_color("#800000").rotate(1.2,DOWN)
        
        curve3 = ParametricSurface(
            lambda u, v: np.array([
                u*0.4,
                m.exp(m.sin(v**2)),
                -v*2.2
            ]),v_min =-1.3 , v_max =1.3 , u_min = -0.1, u_max = 0.1).scale(1).shift([0,-3.5,0]).set_color("#800000").rotate(1.2,DOWN)
        
        curve4 = ParametricSurface(
            lambda u, v: np.array([
                u*0.4,
                m.exp(m.sin(v**2)),
                -v*2.2
            ]),v_min =-1.3 , v_max =1.3 , u_min = -0.1, u_max = 0.1).scale(1.1).shift([0,-4,0]).set_color("#800000").rotate(1.2,DOWN)

        curve5 = ParametricSurface(
            lambda u, v: np.array([
                u*0.4,
                -m.exp(m.sin(v**2)),
                v*2.2
            ]),v_min =-1.3 , v_max =1.3, u_min = -0.1, u_max = 0.1).scale(0.9).shift([0,3,0]).set_color("#800000").rotate(1.2,DOWN)
        
        curve6 = ParametricSurface(
            lambda u, v: np.array([
                u*0.4,
                -m.exp(m.sin(v**2)),
                v*2.2
            ]),v_min =-1.3 , v_max =1.3, u_min = -0.1, u_max = 0.1).scale(1).shift([0,3.5,0]).set_color("#800000").rotate(1.2,DOWN)

        curve7 = ParametricSurface(
            lambda u, v: np.array([
                u*0.4,
                -m.exp(m.sin(v**2)),
                v*2.2
            ]),v_min =-1.3 , v_max =1.3, u_min = -0.1, u_max = 0.1).scale(1.1).shift([0,4,0]).set_color("#800000").rotate(1.2,DOWN)

        curve8 = ParametricSurface(
            lambda u, v: np.array([
                u*0.4,
                -m.exp(m.sin(v**2)),
                v*2.2
            ]),v_min =-1.3 , v_max =1.3, u_min = -0.1, u_max = 0.1).scale(0.8).shift([0,2.65,0]).set_color("#800000").rotate(1.2,DOWN)

        #---------------
        
        #---- label contours
        label_c1 = TextMobject("4",color = '#FFA074').shift([0.2,3,0.5]).scale(0.5).rotate(m.radians(180))
        label_c2 = TextMobject("3",color = '#FFA074').shift([0.2,2.4,0.5]).scale(0.5).rotate(m.radians(180))
        label_c3 = TextMobject("2",color = '#FFA074').shift([0.2,1.9,0.5]).scale(0.5).rotate(m.radians(180))
        label_c4 = TextMobject("1",color = '#FFA074').shift([0.2,1.4,0.5]).scale(0.5).rotate(m.radians(180))
        label_c5 = TextMobject("1",color = '#FFA074').shift([0.2,-1.5,0.5]).scale(0.5).rotate(m.radians(180))
        label_c6 = TextMobject("2",color = '#FFA074').shift([0.2,-2,0.5]).scale(0.5).rotate(m.radians(180))
        label_c7 = TextMobject("3",color = '#FFA074').shift([0.2,-2.5,0.5]).scale(0.5).rotate(m.radians(180))
        label_c8 = TextMobject("4",color = '#FFA074').shift([0.2,-3,0.5]).scale(0.5).rotate(m.radians(180))

        contourplot = VGroup(curve1,curve2,curve3,curve4,curve5,curve6,curve7,curve8,label_c1,label_c2,label_c3,label_c4,label_c5,label_c6,label_c7,label_c8)
        

        circle = Circle(color='#FF00FF',fill_opacity=0.3).shift([-0.5,-1.2,1.5]).rotate(1.9,UP).scale(0.8)
        circle2 = ParametricSurface(
            lambda u, v: np.array([
                1*np.sin(u)*np.cos(v),
                1*np.sin(u)*np.sin(v),
                -1*np.sin(u)*np.sin(u)+2
            ]),u_min=0,u_max=PI/2,v_min=0,v_max=2*PI).set_color('#FF00FF').scale(0.6).shift([1.2,2,-3]).scale(1.24)

        maxima = Dot(color = '#4169E1').shift([0.7,1.2,1.5])
        minima  = Dot(color = '#4169E1').shift([1.4,2.2,1.5])

        min_text = TextMobject("minimum over $g(x,y)=k$",color = '#FFA074').scale(0.6).shift([-2.2,-1,1.5])
        max_text = TextMobject("maximum over $g(x,y)=k$",color = '#FFA074').shift([-2.3,-2.6,1.5]).scale(0.6)


        self.set_camera_orientation(phi=75 * DEGREES, theta = 45*DEGREES)
        self.add(axes)        
        self.add(label_x) 
        self.add(label_y)
        self.wait(1)
        self.play(Write(surface))
        self.play(Write(circle))
        self.wait(1)
        self.play(FadeOut(circle))
        self.wait(1)
        self.move_camera(phi=0 * DEGREES, theta = 90*DEGREES)
        self.wait(1)        
        self.add(contourplot)
        self.play(FadeOut(surface))
        self.wait(1)
        self.add(circle2)
        self.wait(1)
        self.play(Write(minima),Write(maxima)) 
        self.add_fixed_in_frame_mobjects(max_text) 
        self.add_fixed_in_frame_mobjects(min_text) 
        self.wait(1)
