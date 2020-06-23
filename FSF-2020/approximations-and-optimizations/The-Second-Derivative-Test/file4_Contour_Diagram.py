from manimlib.imports import*

#---- contour diagram animation
class ContourDiagram(ThreeDScene):
    def construct(self):

        heading = TextMobject("CONTOUR DIAGRAM", color = YELLOW).scale(1) 

        axes = ThreeDAxes()  
        label_x = TextMobject("$x$").shift([5.5,-0.5,0]) #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5) #---- y axis    

        #---- surface of a paraboloid 
        surface = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v)*u,
                np.sin(v)*u,
                u**2
            ]),v_min = -2, v_max = 2, u_min = -2, u_max = 2, checkerboard_colors = [GREEN_B,GREEN_C,GREEN_D,GREEN_E]).shift([0,0,0]).scale(0.5)
        
        #---- first contour projection
        contour1 = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2*(1 - 2.5*u)
            ])).fade(0.5).scale(0.21).shift([0,0,1.01])
        
        #---- first contour line
        c_1 = Circle(color = BLUE).scale(0.21).shift([0,0,0]).rotate(0.1,DOWN)

        #-------------------------------------------------

        #---- second contour projection
        contour2 = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2*(1 - 1.6*u)
            ])).fade(0.5).scale(0.41).shift([0,0,0.3]).set_color(RED)

        #---- second contour line
        c_2 = Circle(color = RED).scale(0.41).shift([0,0,0]).rotate(0.1,DOWN)

        #-------------------------------------------------
        
        #---- third contour projection
        contour3 = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2*(1 - 1.5*u)
            ])).fade(0.5).scale(0.61).shift([0,0,0.4]).set_color(YELLOW)
        
        #---- third contour line
        c_3 = Circle(color = YELLOW).scale(0.61).shift([0,0,0])

        #-------------------------------------------------

        #---- fourth contour projection
        contour4 = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2*(1 - 1.5*u)
            ])).fade(0.7).scale(0.81).shift([0,0,0.7]).set_color(PINK)

        #---- fourth contour line
        c_4 = Circle(color = PINK).scale(0.81).shift([0,0,0])

        #-------------------------------------------------
        
        #---- fifth contour projection
        contour5 = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2*(1 - 1.5*u)
            ])).fade(0.7).scale(1.01).shift([0,0,1]).set_color(PURPLE)
        
        #---- fifth contour line
        c_5 = Circle(color = PURPLE).scale(1.01).shift([0,0,0])

        c_text= TextMobject("Contour Lines").scale(0.5).shift(2*DOWN)
        s = Square().scale(1.3)
        
        self.set_camera_orientation(phi = 75 * DEGREES, theta = 10 * DEGREES)  
        self.add_fixed_in_frame_mobjects(heading)
        self.wait(1)
        self.play(FadeOut(heading))
        self.wait(1)
        self.add(axes)
        self.add(label_x)
        self.add(label_y)
        self.play(Write(surface))
        self.wait(1)
        self.add(contour1)
        self.wait(1)
        self.play(Write(c_1))
        self.play(ReplacementTransform(contour1,contour2))
        self.wait(1)
        self.play(Write(c_2))
        self.play(ReplacementTransform(contour2,contour3))
        self.wait(1)
        self.play(Write(c_3))
        self.play(ReplacementTransform(contour3,contour4))
        self.wait(1)
        self.play(Write(c_4))
        self.play(ReplacementTransform(contour4,contour5))
        self.wait(1)
        self.play(Write(c_5))
        self.wait(1)
        self.play(FadeOut(contour5),FadeOut(axes),FadeOut(label_x),FadeOut(label_y),FadeOut(surface),FadeOut(contour5),FadeOut(contour4),FadeOut(contour3),FadeOut(contour2),FadeOut(contour1))
        self.wait(1)
        self.move_camera(phi=0 * DEGREES,theta= 90*DEGREES)
        self.wait(1)
        self.add_fixed_in_frame_mobjects(c_text)  
        self.wait(1)
        self.play(ShowCreation(s),FadeOut(c_text))      
        self.wait(1)
