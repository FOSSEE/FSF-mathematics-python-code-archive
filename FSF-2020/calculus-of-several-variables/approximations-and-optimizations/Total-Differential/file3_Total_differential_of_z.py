from manimlib.imports import*

#---- visualization of total differential definition
class totaldifferential(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().fade(0.5)
        surface = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2
            ]),u_min=-1,u_max=1, v_min=-1,v_max=1).set_color("#FF69B4").fade(0.6).shift([1,0.8,1.5]).scale(2)

        plane = Rectangle(color = '#E6E6FA',fill_opacity = 1).scale(3).shift(-1*RIGHT+3*UP).fade(0.9)
        label_x = TextMobject("$x$").shift(5*RIGHT+0.4*DOWN).rotate(1.571)
        label_y = TextMobject("$y$").shift(0.3*DOWN+5.6*RIGHT).scale(0.5)
        label_z = TextMobject("$z$").shift(3.5*UP+0.2*LEFT).scale(0.5)

        s1 = Square(color = '#00FF00',fill_opacity=0.4).shift([1,1,0])
        s2 = Square(color = '#00FF00',fill_opacity=0.4).shift([1,1,3]).scale(0.95)

        l1 = Line([2,0,3],[2,0,0],color = '#FFFACD')
        l2 = Line([0,2,3],[0,2,0],color = '#FFFACD')
        l3 = Line([2,1.95,3],[2,2,0],color = '#FFFACD')

        d1 = Dot([2,0,1.5],color = '#FFD700').rotate(1.571,UP)
        d1_text = TextMobject("$P1$").scale(0.4).shift(1.2*LEFT+1.1*UP)

        d2 = Dot([0,2,3],color = '#FFD700').rotate(1.571,UP)
        d2_text = TextMobject("$P2$").scale(0.4).shift(2.3*RIGHT+3.1*UP)

        d3 = Dot([2,2,2],color = '#FFD700').rotate(1.571,UP)
        d3_text = TextMobject("$Q$").scale(0.4).shift([1.6,-1,0]+2.5*UP)

        s3 = Square().shift([1,1,1.5]).scale(0.95)
        s4 = Square().shift([1,1,2]).scale(0.95)

        m1_line = DashedLine([2,0,1.5],[2,2,2],color = '#87CEEB')
        m2_line = DashedLine([2,2,2],[0,2,3],color = '#87CEEB')

        dx_line = Line([2,2,0],[4,2,0],color = '#00FF7F')
        dy_line = Line([2,2,0],[2,4,0],color = '#00FF7F')

        dx = DashedLine([3.5,0,0],[3.5,2,0],color = '#87CEEB')
        dy = DashedLine([0,3.5,0],[2,3.5,0],color = '#87CEEB')

        dx_text = TextMobject("$dx$").scale(0.8).shift([4,1,0]).rotate(1.571)
        dy_text = TextMobject("$dy$").scale(0.8).shift([1,3.8,0]).rotate(math.radians(180))

        parx_line = Line([0,2,1.5],[0,5,1.5],color = '#00FF7F')
        parm_line = Line([0,2,2],[0,5,2],color = '#00FF7F')
        pary_line = Line([0,2.1,3],[0,5,3],color = '#00FF7F')

        delx = DashedLine([0,4,2],[0,4,1.5],color = '#F0F8FF')
        dely = DashedLine([0,4,3],[0,4,2],color = '#FAEBD7')

        dely_text = TextMobject("$\\frac{\\partial z}{\\partial y}dy$").shift(4.6*RIGHT+2.3*UP).scale(0.4)
        delx_text = TextMobject("$\\frac{\\partial z}{\\partial x}dx$").shift(4.6*RIGHT+1.4*UP).scale(0.4)


        self.set_camera_orientation(phi=75*DEGREES,theta=20*DEGREES)
        self.add(axes)        
        self.play(Write(plane))
        self.play(ShowCreation(label_x))
        self.add_fixed_in_frame_mobjects(label_y)
        self.add_fixed_in_frame_mobjects(label_z)
        self.wait(1)
        self.play(Write(surface))
        self.play(ShowCreation(d1))
        self.add_fixed_in_frame_mobjects(d1_text)
        self.play(ShowCreation(d2))
        self.add_fixed_in_frame_mobjects(d2_text)
        self.wait(1) 
        self.play(Write(s2))
        self.wait(1)
        self.play(Write(l1),Write(l2),Write(l3))
        self.wait(1)
        self.play(Write(s1))
        self.wait(1)
        self.play(FadeOut(surface))      
        self.play(ShowCreation(d3))
        self.add_fixed_in_frame_mobjects(d3_text)
        self.play(ShowCreation(m1_line))
        self.play(ShowCreation(m2_line))
        self.wait(1)        
        self.play(ShowCreation(dx_line),ShowCreation(dx),ShowCreation(dx_text))
        self.wait(1)
        self.play(ShowCreation(dy_line),ShowCreation(dy),ShowCreation(dy_text))
        self.wait(2)
        self.play(Write(s3))
        self.play(Write(s4))
        self.wait(1)
        self.play(ShowCreation(parx_line),ShowCreation(parm_line),ShowCreation(pary_line))
        self.wait(1)
        self.play(ShowCreation(dely))
        self.add_fixed_in_frame_mobjects(dely_text)
        self.wait(1)
        self.play(ShowCreation(delx))
        self.add_fixed_in_frame_mobjects(delx_text)
        self.wait(1)
