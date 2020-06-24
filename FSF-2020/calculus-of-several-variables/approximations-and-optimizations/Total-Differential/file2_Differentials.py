from manimlib.imports import*


class firstScene(ThreeDScene):
    
    def construct(self):

        axes = ThreeDAxes()

        s = Rectangle(color = '#00FF7F',fill_opacity=0.3).shift(2.3*UP+3.9*LEFT).scale(1).rotate(0.2,UP) #----surface z = f(x,y)

        label_y = TextMobject("$y$").shift(5*RIGHT+0.4*DOWN).rotate(1.571)
        label_x = TextMobject("$x$").shift(-0.1*UP+5.6*RIGHT).scale(0.5)

        plane = Rectangle(color = '#E6E6FA',fill_opacity = 1).scale(3).shift(-1*RIGHT+3*UP).fade(0.9)

        d = Dot([1,2,1],color = '#9400D3').rotate(1.571,UP)
        d2 = Dot([2,2.9,1],color = '#9400D3').rotate(1.571,UP)

        p1 = TextMobject("$P_1$",color ='#ADFF2F').scale(0.6).shift(2*RIGHT+1*UP)
        p2 = TextMobject("$P_2$",color = '#ADFF2F').scale(0.6).shift(2.6*RIGHT+0.4*UP)


        l1 = DashedLine(color = '#00BFFF').scale(1.6).shift(3.5*UP+3.25*LEFT).rotate(1.571)
        l2 = DashedLine(color = '#00BFFF').scale(1).shift(4*UP+2*LEFT).rotate(1.571)

        label_dz= TextMobject("$dz$").scale(0.4).shift(5.3*RIGHT+0.4*UP)


        l3 = Line(color = '#FFDAB9').scale(0.8).shift(1.95*UP+0.7*RIGHT).rotate(1.571,DOWN).fade(0.7)
        l4 = Line(color = '#FFDAB9').scale(0.6).shift(2.86*UP+0.9*RIGHT).rotate(1.571,DOWN).fade(0.7)

        line_y1 = DashedLine(color = '#00BFFF').scale(1.3).shift(0.82*UP+3.25*RIGHT).rotate(1.571)
        line_y2 = DashedLine(color = '#00BFFF').scale(1.7).shift(1.2*UP+2.8*RIGHT).rotate(1.571)

        label_dy= TextMobject("$dy$").scale(0.6).shift(3*RIGHT+0.8*DOWN).rotate(math.radians(90))

        line_x1 = DashedLine(color = '#00BFFF').scale(1.5).shift(2.2*UP+1.6*RIGHT).rotate(1.571,RIGHT)
        line_x2 = DashedLine(color = '#00BFFF').scale(1.2).shift(2.9*UP+1.6*RIGHT).rotate(1.571,RIGHT)

        label_dx= TextMobject("$dx$").scale(0.4).shift(-0.4*UP+2.5*RIGHT)

        label = TextMobject("$f(x,y)$").scale(0.6).shift(4*RIGHT+3*UP)
    

        self.add(axes)
        self.set_camera_orientation(phi=75*DEGREES,theta=10*DEGREES)
        self.play(Write(plane))
        self.play(ShowCreation(label_y))
        self.add_fixed_in_frame_mobjects(label_x)
        self.play(Write(s)) 
        self.add_fixed_in_frame_mobjects(label)
        self.wait(1)
        self.play(Write(d),Write(d2))        
        self.add_fixed_in_frame_mobjects(p1)
        self.add_fixed_in_frame_mobjects(p2)
        self.wait(1)
        self.play(Write(l1))   
        self.play(Write(l2))
        self.add_fixed_in_frame_mobjects(label_dz)
        self.wait(1)
        self.play(Write(l3))   
        self.play(Write(l4))   
        self.wait(1)
        self.play(Write(line_y1))   
        self.play(Write(line_y2))  
        self.play(ShowCreation(label_dy))
        self.wait(1)
        self.play(Write(line_x1))   
        self.play(Write(line_x2))
        self.add_fixed_in_frame_mobjects(label_dx)
        self.wait(1)
