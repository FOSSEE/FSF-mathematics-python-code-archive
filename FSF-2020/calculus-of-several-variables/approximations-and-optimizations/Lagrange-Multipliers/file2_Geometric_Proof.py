from manimlib.imports import*

class firstScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().scale(0.7).rotate(math.radians(180))
        surface = ParametricSurface(
            lambda u, v: np.array([
                1*np.sin(u)*np.cos(v),
                1*np.sin(u)*np.sin(v),
                -1*np.sin(u)*np.sin(u)+2
            ]),u_min=0,u_max=PI/2,v_min=0,v_max=2*PI,checkerboard_colors=[GREEN_C, GREEN_E]).scale(1).shift([-1.5,-1.5,0])
         
        d = Dot([-2,-2.55,0],color = '#800000')
        a_df = Arrow(color = '#00FFFF').rotate(-2).shift(3.2*DOWN+2.3*LEFT) #---- f parallel to g
        a_dg = Arrow(color = '#FF00FF').scale(0.8).shift(3.2*DOWN+2.3*LEFT).rotate(-2) #---- f parallel to g

        b_df = Arrow(color = '#00FFFF').rotate(1.1).shift(0.82*LEFT+0.15*UP) #---- f parallel to g
        b_dg = Arrow(color = '#FF00FF').scale(0.6).rotate(-2).shift(1.43*LEFT+1.1*DOWN) #---- f parallel to g


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

        level_Curve = VGroup(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15)

        rel_text = TextMobject("$\\nabla f = \\lambda \\nabla g$",color = TEAL).shift([3,3.2,0]).scale(0.5)

        f_text = TextMobject("$\\nabla f$",color = '#800000').shift([1,1,0]).scale(0.5)
        g_text = TextMobject("$\\nabla g$").shift([1.2,-0.8,0]).scale(0.5)

        p_text= TextMobject("$P$").shift([1.8,2.6,0]).scale(0.5)
        

        
        self.add(axes)
        self.set_camera_orientation(phi=0 * DEGREES, theta = 90*DEGREES)
        self.play(Write(surface))
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
        self.play(ShowCreation(b_dg))        
        self.wait(1)
        self.add_fixed_in_frame_mobjects(f_text)
        self.add_fixed_in_frame_mobjects(g_text)
        self.wait(1)
