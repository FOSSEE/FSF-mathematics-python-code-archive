from manimlib.imports import*

#---- tangent plane is parallel to the x-y plane
class MaximaScene(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes().scale(1.2)
        label_x= TextMobject("$x$").shift([5.4,-0.5,0]) #---- x axis
        label_y= TextMobject("$y$").shift([-0.5,5.2,0]).rotate(-4.5) #---- y axis

        #---- graph of the function 
        s = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),u_min=0,u_max=PI,v_min=PI,v_max=2*PI,checkerboard_colors=[BLUE_B,BLUE_C,BLUE_D,BLUE_E]).scale(1.5).shift([-0.8,0.5,1.5])

        d1 = Dot([0.2,2.01,2.24],color = '#800000').rotate(1.1,LEFT) #---- point(x_0,y_0)
        d1_copy = Dot([1.1,2.2,-0.45],color = '#800000') #---- projection of point(x_0,y_0) on x-y plane
        d1_text = TextMobject("$(x_0,y_0)$",color = "#8B0000").scale(0.4).shift(1.3*RIGHT+1.1*UP)

        d2 = Dot([1.1,2.2,2.7],color = '#800000').rotate(1,LEFT) #---- point(x,y)
        d2_copy = Dot([0.1,1.95,0.4],color = '#800000') #---- projection of point(x,y) on x-y plane
        d2_text = TextMobject("$(x,y)$",color = "#8B0000").scale(0.4).shift(0.6*RIGHT+0.8*UP)

        t_plane = Rectangle(color = PURPLE, fill_opacity=0.3).scale(0.4).rotate(1,LEFT).shift([1.1,2.5,2.9]) #---- tangent plane

        t_text= TextMobject("Tangent Plane",color = RED).scale(0.5).shift(0.3*RIGHT+1.3*UP).rotate(math.radians(5),LEFT)

        l1 = Line([1.1,2.2,2.6],[1.1,2.2,-0.45]).fade(0.2)
        l2 = Line([0.1,1.95,2.05],[0.1,1.95,0.4]).fade(0.2)

        a1 = Line([0.1,1.95,0.4],[1.1,2.2,-0.45],color ="#00FF7F")
        a_x = Line([0.1,1.95,0.4],[1.7,1.95,0.4],color ="#9400D3")
        a_y = Line([0.1,1.95,0.4],[0.1,2.75,0.4],color ="#8B4513")
        a2 = Line([1.7,1.95,0.4],[1.7,2.75,0.4])
        a3 = Line([0.1,2.75,0.4],[1.7,2.75,0.4])
        
        #---- transition of tangent plane

        t2_plane = Rectangle(color = PURPLE, fill_opacity=0.3).scale(0.4).rotate(1,LEFT).shift([1.1,2.5,2]) 
        t3_plane = Rectangle(color = PURPLE, fill_opacity=0.3).scale(0.4).rotate(math.radians(180),LEFT).shift([1.1,2.5,2])
        t4_plane = Rectangle(color = PURPLE, fill_opacity=0.3).scale(0.4).rotate(math.radians(180),LEFT).shift([0.9,2.35,0.4])

        #-------------------------------------------
        self.set_camera_orientation(phi = 50 * DEGREES, theta = 45 * DEGREES)
        self.wait(1)
        self.add(axes)
        self.add(label_x)
        self.add(label_y)
        self.play(Write(s))
        self.wait(1)
        self.play(Write(d1))
        self.add_fixed_in_frame_mobjects(d1_text)
        self.play(ShowCreation(t_plane))
        self.add_fixed_in_frame_mobjects(t_text)
        self.wait(1)
        self.play(FadeOut(t_text),Write(d2))
        self.add_fixed_in_frame_mobjects(d2_text)        
        self.wait(1)
        self.play(Write(l1),Write(l2))
        self.play(Write(d2_copy),Write(d1_copy))
        self.wait(1)
        self.play(Write(a1),Write(a_x),Write(a_y))
        self.wait(1)
        self.play(Write(a2),Write(a3))
        self.wait(1)        
        self.play(ReplacementTransform(t_plane,t2_plane))
        self.wait(1)
        self.play(ReplacementTransform(t2_plane,t3_plane))
        self.wait(1)
        self.play(ReplacementTransform(t3_plane,t4_plane))
        self.wait(1)         
