from manimlib.imports import*

#---- visualization of total differential dz between two points lying on the surface of the function
class differentialdz(ThreeDScene):
    
    def construct(self):
    
        axes = ThreeDAxes()
        label_x = TextMobject("$x$").shift([5.5,-0.5,0]).fade(0.4)  #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5).fade(0.4)  #---- y axis
        
        #---- surface of the funtion f(x,y)
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2
            ]),u_min=-1,u_max=1, v_min=-1,v_max=1).set_color("#FF69B4").fade(0.6).scale(2).shift(3*UP+1*LEFT)
        
        d = Dot([1.4,1.75,1],color = '#00FFFF').rotate(1.571,UP) #---- point on the surface
        d2 = Dot([2,2,1],color = '#00FFFF').rotate(1.571,UP) #---- point on the surface

        p1 = TextMobject("$P_1$",color ='#ADFF2F').scale(0.6).shift(2*RIGHT+1*UP)
        p2 = TextMobject("$P_2$",color = '#ADFF2F').scale(0.6).shift(2.6*RIGHT+0.9*UP)

        l = DashedLine(color = '#800000').rotate(1.571,UP).scale(1).shift(1.7*UP+1.6*RIGHT)
        l2 = DashedLine(color = '#800000').rotate(1.571,UP).scale(0.8).shift(2.26*UP+1.2*RIGHT)

        l_text = TextMobject("$(x_1,y_1)$",color = '#ADFF2F').scale(0.6).shift(2*RIGHT+1.6*DOWN)
        l2_text = TextMobject("$(x_2,y_2)$",color = '#ADFF2F').scale(0.6).shift(2.7*RIGHT+1.2*DOWN)

        a = Arrow(color = '#FFFACD').scale(0.7).rotate(1.38,RIGHT).shift(2.5*LEFT+3.1*UP)

        a_text = TextMobject("$dz$",color='#800000').scale(0.5).shift(2.3*RIGHT+0.5*UP)

        plane = Rectangle(color = '#E6E6FA',fill_opacity = 1).scale(3).shift(1*RIGHT+3*UP).fade(0.9)

        label = TextMobject("$z = f(x,y)$").scale(0.6).shift(3.5*RIGHT+1.8*UP)
        
        self.set_camera_orientation(phi=75*DEGREES,theta=-10*DEGREES)
        self.add(axes)
        self.add(label_x)
        self.add(label_y)
        self.wait(1)
        self.play(Write(plane))
        self.play(Write(surface))
        self.add_fixed_in_frame_mobjects(label)
        self.wait(1)
        self.play(ShowCreation(l),ShowCreation(l2),Write(d),Write(d2))                
        self.wait(1)
        self.add_fixed_in_frame_mobjects(p1)
        self.add_fixed_in_frame_mobjects(p2)
        self.wait(1)
        self.add_fixed_in_frame_mobjects(l_text)
        self.add_fixed_in_frame_mobjects(l2_text)
        self.play(ShowCreation(a))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(a_text)
        self.wait(2)
