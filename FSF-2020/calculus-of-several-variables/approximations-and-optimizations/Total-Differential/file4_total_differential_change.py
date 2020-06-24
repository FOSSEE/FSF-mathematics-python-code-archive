from manimlib.imports import*


class firstScene(ThreeDScene):
    
    def construct(self):

        axes = ThreeDAxes()

        s = Rectangle(color = '#F08080',fill_opacity=1).fade(0.7).shift(1.9*UP+5*LEFT).scale(0.9)#----surface z = f(x,y)

        s2= Rectangle(color = '#F08080',fill_opacity=1).fade(0.7).shift(2.4*UP+3.1*RIGHT).scale(0.6) #----reflection of the surface on the x-y plane
        
        l1 = DashedLine(color = '#AFEEEE').rotate(1.571,UP).scale(1).shift(1.53*UP+1.5*RIGHT)
        l2 = DashedLine(color = '#AFEEEE').rotate(1.571,UP).scale(1).shift(2.9*UP+1.4*RIGHT)
        l3 = DashedLine(color = '#AFEEEE').rotate(1.571,UP).scale(1).shift(1.5*UP-1.6*RIGHT)
        l4 = DashedLine(color = '#AFEEEE').rotate(1.571,UP).scale(1).shift(2.9*UP-1.75*RIGHT)


        l1_text = TextMobject("$(x+\\triangle x,y)$").shift(RIGHT+1.7*DOWN).scale(0.4)
        l2_text = TextMobject("$(x+\\triangle x,y+\\triangle y)$").shift(3*RIGHT+1.8*DOWN).scale(0.4)
        l3_text = TextMobject("$f(x,y)$").shift(1.6*RIGHT+1.5*UP).scale(0.4)
        l4_text = TextMobject("$(x,y+\\triangle y)$").shift(3.5*RIGHT+0.7*DOWN).scale(0.4)

        label_x = TextMobject("$x$").shift(5*RIGHT+0.4*DOWN)
        label_y = TextMobject("$y$").shift(5*UP-0.6*RIGHT)
        
        self.add(axes)
        self.set_camera_orientation(phi=75*DEGREES,theta=10*DEGREES)
        self.wait(1)
        self.play(ShowCreation(label_x),ShowCreation(label_y))
        self.play(Write(s))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(l3_text)
        self.wait(1)
        self.play(Write(l3))        
        self.wait(1)
        self.play(Write(l1))
        self.add_fixed_in_frame_mobjects(l1_text)
        self.wait(1)
        self.play(Write(l2))
        self.add_fixed_in_frame_mobjects(l2_text)
        self.wait(1)
        self.play(Write(l4))
        self.add_fixed_in_frame_mobjects(l4_text)
        self.wait(1)
        self.play(Write(s2))
        self.wait(1)
        
        
        
        
        
        
