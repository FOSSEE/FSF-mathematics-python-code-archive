from manimlib.imports import*

#---- visualization of geometric proof of Lagrange multiplier
class firstScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().scale(0.7).rotate(math.radians(180))       
        label_x = TextMobject("$x$").shift(4*RIGHT).fade(0.4)  #---- x axis
        label_y = TextMobject("$y$").shift(3.2*DOWN+0.2*RIGHT).rotate(math.radians(180)).fade(0.4)  #---- y axis

        surface = ParametricSurface(
            lambda u, v: np.array([
                1*np.sin(u)*np.cos(v),
                1*np.sin(u)*np.sin(v),
                -1*np.sin(u)*np.sin(u)+2
            ]),u_min=0,u_max=PI/2,v_min=0,v_max=2*PI).set_color(GREEN).scale(1).shift([-1.5,-1.5,0])
         
        d = Dot([-2,-2.55,0],color = '#800000')
        a_df = Arrow(color = '#00FFFF').rotate(-2).shift(3.2*DOWN+2.3*LEFT) #---- f parallel to g
        a_dg = Arrow(color = '#FF00FF').scale(0.8).shift(3.2*DOWN+2.3*LEFT).rotate(-2) #---- f parallel to g

        b_dg = Arrow(color = '#00FFFF').rotate(1.1).shift(0.82*LEFT+0.15*UP) #---- f parallel to g
        b_df = Arrow(color = '#FF00FF').scale(0.6).rotate(-2).shift(1.43*LEFT+1.1*DOWN) #---- f parallel to g


        qd = Dot(color = '#800000').shift(1.2*LEFT+0.6*DOWN)

        l1 = Line([-1,-3.1,0],[-4,-3.1,0],color = PINK).rotate(-0.3).fade(0.6)
        l2 = Line([-0.9,-2.9,0],[-4,-2.9,0],color = PINK).rotate(-0.3).fade(0.6)
        l3= Line([-0.8,-2.7,0],[-4,-2.7,0],color = PINK).rotate(-0.3).fade(0.6)
        l4= Line([-0.7,-2.45,0],[-4,-2.45,0],color = PINK).rotate(-0.3).fade(0.6)
        l5= Line([-0.6,-2.2,0],[-4,-2.25,0],color = PINK).rotate(-0.3).fade(0.6)
        l6 = Line([-0.5,-2,0],[-4,-2,0],color = PINK).rotate(-0.3).fade(0.6)
        l7 = Line([-0.4,-1.8,0],[-4,-1.8,0],color = PINK).rotate(-0.3).fade(0.6)
        l8 = Line([-0.3,-1.6,0],[-4,-1.6,0],color = PINK).rotate(-0.3).fade(0.6)
        l9= Line([-0.2,-1.4,0],[-4,-1.4,0],color = PINK).rotate(-0.3).fade(0.6)
        l10= Line([-0.1,-1.2,0],[-4,-1.2,0],color = PINK).rotate(-0.3).fade(0.6)
        l11 = Line([-0,-1,0],[-4,-1,0],color = PINK).rotate(-0.3).fade(0.6)
        l12 = Line([-0,-0.8,0],[-4,-0.8,0],color = PINK).rotate(-0.3).fade(0.6)
        l13= Line([-0,-0.55,0],[-4,-0.55,0],color = PINK).rotate(-0.3).fade(0.6)
        l14= Line([-0,-0.35,0],[-4,-0.35,0],color = PINK).rotate(-0.3).fade(0.6)
        l15= Line([-0.,-0.15,0],[-4,-0.15,0],color = PINK).rotate(-0.3).fade(0.6)

        rel_text = TextMobject("$\\nabla f = \\lambda \\nabla g$",color = TEAL).shift([3,3.2,0]).scale(0.5)

        f_text = TextMobject("$\\nabla f$",color = '#800000').shift([1,1,0]).scale(0.5)
        g_text = TextMobject("$\\nabla g$").shift([1.2,-0.8,0]).scale(0.5)

        p_text= TextMobject("$P$").shift([1.8,2.6,0]).scale(0.5)

        l1_text = TextMobject("$w=$ 17").rotate(math.radians(180)).scale(0.4).shift(2.7*DOWN+4.36*LEFT)
        l2_text = TextMobject("$w=$ 16").rotate(math.radians(180)).scale(0.4).shift(2.46*DOWN+4.36*LEFT)
        l3_text = TextMobject("$w=$ 15").rotate(math.radians(180)).scale(0.4).shift(2.2*DOWN+4.36*LEFT)
        l4_text = TextMobject("$w=$ 14").rotate(math.radians(180)).scale(0.4).shift(1.97*DOWN+4.36*LEFT)
        l5_text = TextMobject("$w=$ 13").rotate(math.radians(180)).scale(0.4).shift(1.74*DOWN+4.36*LEFT)
        l6_text = TextMobject("$w=$ 12").rotate(math.radians(180)).scale(0.4).shift(1.5*DOWN+4.36*LEFT)
        l7_text = TextMobject("$w=$ 11").rotate(math.radians(180)).scale(0.4).shift(1.26*DOWN+4.36*LEFT)
        l8_text = TextMobject("$w=$ 10").rotate(math.radians(180)).scale(0.4).shift(1.05*DOWN+4.36*LEFT)
        l9_text = TextMobject("$w=$ 9").rotate(math.radians(180)).scale(0.4).shift(0.8*DOWN+4.32*LEFT)
        l10_text = TextMobject("$w=$ 8").rotate(math.radians(180)).scale(0.4).shift(0.6*DOWN+4.32*LEFT)
        l11_text = TextMobject("$w=$ 7").rotate(math.radians(180)).scale(0.4).shift(0.4*DOWN+4.32*LEFT)
        l12_text = TextMobject("$w=$ 6").rotate(math.radians(180)).scale(0.4).shift(0.2*DOWN+4.32*LEFT)
        l13_text = TextMobject("$w=$ 5").rotate(math.radians(180)).scale(0.4).shift(-0.02*DOWN+4.32*LEFT)
        l14_text = TextMobject("$w=$ 4").rotate(math.radians(180)).scale(0.4).shift(-0.23*DOWN+4.32*LEFT)
        l15_text = TextMobject("$w=$ 3").rotate(math.radians(180)).scale(0.4).shift(-0.44*DOWN+4.32*LEFT)

        level_Curve = VGroup(l1,l1_text,l2,l2_text,l3,l3_text,l4,l4_text,l5,l5_text,l6,l6_text,l7,l7_text,l8,l8_text,l9,l9_text,l10,l10_text,l11,l11_text,l12,l12_text,l13,l13_text,l14,l14_text,l15,l15_text)

        self.set_camera_orientation(phi=0 * DEGREES, theta = 90*DEGREES)
        self.add(axes)
        self.add(label_x)
        self.add(label_y) 
        self.wait(1)     
        self.add(surface)
        self.wait(1)
        self.play(ShowCreation(level_Curve))
        self.wait(1)
        self.play(ShowCreation(a_df),ShowCreation(a_dg),Write(d))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(rel_text)
        self.add_fixed_in_frame_mobjects(p_text)
        self.wait(1)
        self.play(Write(qd)) 
        self.wait(1)        
        self.play(ShowCreation(b_df))
        self.add_fixed_in_frame_mobjects(f_text)
        self.wait(1)
        self.play(ShowCreation(b_dg))              
        self.add_fixed_in_frame_mobjects(g_text)
        self.wait(1)
