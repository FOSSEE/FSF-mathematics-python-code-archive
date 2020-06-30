from manimlib.imports import*

#---- approximation value of function between two points using total differentials
class approximation(ThreeDScene):
    
    def construct(self):
    
        axes = ThreeDAxes()        
        label_x = TextMobject("$x$").shift([5.5,-0.3,0]).fade(0.4)  #---- x axis
        label_y = TextMobject("$y$").shift([-0.5,5.5,0]).rotate(-4.5).fade(0.4)  #---- y axis

        surface = ParametricSurface(
            lambda u, v: np.array([
                np.sin(u),
                v,
                -u**2-v
            ]),u_min=-1,u_max=1, v_min=-1,v_max=1).set_color("#00008B").scale(2).shift(3.8*UP+2*LEFT)
        
        d = Dot([1.4,1.75,1],color = '#00FFFF').rotate(1.571,UP)
        d2 = Dot([2,2,1],color = '#00FFFF').rotate(1.571,UP)

        l = DashedLine(color = '#800000').rotate(1.571,UP).scale(1).shift(1.7*UP+1.6*RIGHT)
        l2 = DashedLine(color = '#800000').rotate(1.571,UP).scale(0.8).shift(2.26*UP+1.2*RIGHT)

        l_text = TextMobject("$(x_1,y_1)$",color = '#ADFF2F').scale(0.6).shift(2*RIGHT+1.6*DOWN)
        l2_text = TextMobject("$(x_2,y_2)$",color = '#ADFF2F').scale(0.6).shift(2.7*RIGHT+1.2*DOWN)

        plane = Rectangle(color = '#E6E6FA',fill_opacity = 1).scale(3).shift(1*RIGHT+3*UP).fade(0.9)

        tangentplane = Rectangle(color = '#E6E6FA',fill_opacity = 1).scale(1.1).shift(2*LEFT+3.4*UP).fade(0.5).rotate(0.8,RIGHT)
        tangentplane_text = TextMobject("Tangent Plane").scale(0.4).shift(3*RIGHT+1*UP)

        label = TextMobject("$z = f(x,y)$").scale(0.6).shift(4*RIGHT+3*UP)

        self.set_camera_orientation(phi=75*DEGREES,theta=-10*DEGREES)
        self.add(axes)
        self.add(label_x)
        self.add(label_y)
        self.wait(1)
        self.play(Write(plane))
        self.wait(1)
        self.play(Write(surface))
        self.add_fixed_in_frame_mobjects(label)
        self.wait(1.5)
        self.play(ShowCreation(l),ShowCreation(l2),Write(d),Write(d2))           
        self.wait(1)
        self.add_fixed_in_frame_mobjects(l_text)
        self.add_fixed_in_frame_mobjects(l2_text)
        self.wait(1)
        self.play(Write(tangentplane))
        self.add_fixed_in_frame_mobjects(tangentplane_text)        
        self.wait(2)
