from manimlib.imports import *
class ThreeDExplanation(ThreeDScene):
    
    def construct(self):

        basis = TextMobject(r"Set of Orthonormal Basis - $\left(\begin{array}{c}\frac{1}{\sqrt{2}}\\\frac{1}{\sqrt{2}}\\0\end{array}\right),\left(\begin{array}{c}\frac{-1}{\sqrt{2}}\\\frac{1}{\sqrt{2}}\\0\end{array}\right),\left(\begin{array}{c}0\\0\\1\end{array}\right)$")
        basis.scale(0.75)
        basis.move_to(UP*1.5)
        self.play(Write(basis))
        v = TextMobject(r"$v_1$",r"$v_2$",r"$v_3$")
        v[0].move_to(UP*0.5+RIGHT*0.75)
        v[1].move_to(UP*0.5+RIGHT*2.5)
        v[2].move_to(UP*0.5+RIGHT*4)
        eq = TextMobject(r"$v = \left(\begin{array}{c}3\\4\\5\end{array}\right)$")
        eq1 = TextMobject(r"$<v,v_1> = \frac{3}{\sqrt{2}} + \frac{4}{\sqrt{2}} + 0 = \frac{7}{\sqrt{2}}$")
        eq2 = TextMobject(r"$<v,v_2> = \frac{-3}{\sqrt{2}} + \frac{4}{\sqrt{2}} + 0 =\frac{1}{\sqrt{2}}$")
        eq3 = TextMobject(r"$<v,v_3> =  0 + 0 + 5 =5$")
        eq.move_to(4*LEFT+DOWN)
        eq1.move_to(0.5*DOWN+2*RIGHT)
        eq2.move_to(1.5*DOWN+2*RIGHT)
        eq3.move_to(2.5*DOWN+2*RIGHT)
        self.play(Write(v))
        self.play(Write(eq))
        self.play(Write(eq1))
        self.play(Write(eq2))
        self.play(Write(eq3))
        self.wait()
        self.play(FadeOut(basis), FadeOut(eq), FadeOut(v), FadeOut(eq1), FadeOut(eq2), FadeOut(eq3))
        self.wait()
        
        text = TextMobject("These are the 3 mutually orthonormal basis of the set(", r"$v_1$, ", r"$v_2$, ", r"$v_3$",")")
        text[1].set_color(DARK_BLUE)
        text[2].set_color(RED)
        text[3].set_color(YELLOW)
        text.scale(0.75)
        self.add_fixed_in_frame_mobjects(text)
        text.move_to(3*DOWN)
        self.play(Write(text))
        self.wait()

        axes = ThreeDAxes(x_min = -6,x_max=6,y_min=-6,y_max=6,z_min=-6,z_max=6)
        self.play(ShowCreation(axes))
        self.move_camera(distance = 100, phi=45*DEGREES,theta=45*DEGREES,run_time=5)
        self.begin_ambient_camera_rotation(rate=0.1)

        xy_plane = Polygon(6*RIGHT+6*UP,-6*RIGHT+6*UP,-6*RIGHT-6*UP,6*RIGHT-6*UP)
        xy_plane.set_color("#333333")
        xy_plane.set_fill("#333333")
        xy_plane.set_opacity(1)
        xy_plane.fade(0.7)
        self.play(ShowCreation(xy_plane))

        dashedline1 = DashedLine(start = -6*(UP+RIGHT), end = 6*(UP+RIGHT))
        dashedline2 = DashedLine(start = -6*(UP+LEFT), end = 6*(UP+LEFT))
        dashedline3 = DashedLine(start = 4*UP+3*RIGHT+[0,0,5], end = 3.5*UP+3.5*RIGHT)
        dashedline4 = DashedLine(start = 4*UP+3*RIGHT+[0,0,5], end = 0.5*UP+0.5*LEFT)
        dashedline5 = DashedLine(start = 4*UP+3*RIGHT+[0,0,5], end = [0,0,5])

        self.play(ShowCreation(dashedline1), ShowCreation(dashedline2))

        line1 = Line(start = ORIGIN,end = 0.707*RIGHT + 0.707*UP)
        line1.set_color(DARK_BLUE)
        tip1 = Polygon(0.707*RIGHT + 0.707*UP, 0.707*RIGHT + 0.607*UP, 0.607*RIGHT + 0.707*UP)
        tip1.set_opacity(1)
        tip1.set_fill(DARK_BLUE)
        tip1.set_color(DARK_BLUE)
        self.play(ShowCreation(line1), ShowCreation(tip1))

        line2 = Line(start = ORIGIN,end = 0.707*LEFT + 0.707*UP)
        line2.set_color(RED)
        tip2 = Polygon(0.707*LEFT + 0.707*UP, 0.707*LEFT + 0.607*UP, 0.607*LEFT + 0.707*UP)
        tip2.set_opacity(1)
        tip2.set_fill(RED)
        tip2.set_color(RED)

        self.play(ShowCreation(line2), ShowCreation(tip2))

        line3 = Line(start = ORIGIN,end = [0,0,1])
        line3.set_color(YELLOW)
        tip3 = Polygon([0,0,1],[0,0,0.8]-0.2*RIGHT,[0,0,0.8]-0.2*LEFT)
        tip3.set_opacity(1)
        tip3.set_fill(YELLOW)
        tip3.set_color(YELLOW)
        self.play(ShowCreation(line3), ShowCreation(tip3))
        self.wait()

        self.play(FadeOut(text))

        text = TextMobject("Take the projection of ", r"$v$", " on the mutually orthonormal vectors")
        text[1].set_color(GOLD_E)
        text.scale(0.75)
        self.add_fixed_in_frame_mobjects(text)
        text.move_to(3*DOWN)
        self.play(Write(text))
        self.wait(2)
        
        a_line = Line(start = ORIGIN,end = 4*UP+3*RIGHT+[0,0,5])
        a_line.set_color(GOLD_E)
        a_tip = Polygon(3.92*UP+2.94*RIGHT+[0,0,4.9],3.6*UP+2.7*RIGHT+[0,0,4.5]+0.1*UP+0.1*LEFT,3.6*UP+2.7*RIGHT+[0,0,4.5]+0.1*DOWN+0.1*RIGHT)
        a_tip.set_opacity(1)
        a_tip.set_fill(GOLD_E)
        a_tip.set_color(GOLD_E)

        self.play(ShowCreation(a_line), ShowCreation(a_tip))
        self.stop_ambient_camera_rotation()
        self.move_camera(distance = 100, phi=45*DEGREES,theta=135*DEGREES,run_time=5)

        self.play(ShowCreation(dashedline3),ShowCreation(dashedline4),ShowCreation(dashedline5))
        self.wait()

        pv1 = Line(start = ORIGIN,end = 4*UP+3*RIGHT+[0,0,5])
        pv1.set_color(GOLD_E)
        pv1tip = Polygon(4*UP+3*RIGHT+[0,0,5],3.6*UP+2.7*RIGHT+[0,0,4.5]+0.1*UP+0.1*LEFT,3.6*UP+2.7*RIGHT+[0,0,4.5]+0.1*DOWN+0.1*RIGHT)
        pv1tip.set_opacity(1)
        pv1tip.set_fill(GOLD_E)
        pv1tip.set_color(GOLD_E)

        v1_p = Line(start = ORIGIN,end = 3.5*RIGHT + 3.5*UP)
        v1_p.set_color(BLUE_E)
        v1_p_tip = Polygon(3.5*RIGHT + 3.5*UP, 3.5*RIGHT + 3.4*UP, 3.4*RIGHT + 3.5*UP)
        v1_p_tip.set_opacity(1)
        v1_p_tip.set_fill(BLUE_E)
        v1_p_tip.set_color(BLUE_E)

        pv2 = Line(start = ORIGIN,end = 4*UP+3*RIGHT+[0,0,5])
        pv2.set_color(GOLD_E)
        pv2tip = Polygon(4*UP+3*RIGHT+[0,0,5],3.6*UP+2.7*RIGHT+[0,0,4.5]+0.1*UP+0.1*LEFT,3.6*UP+2.7*RIGHT+[0,0,4.5]+0.1*DOWN+0.1*RIGHT)
        pv2tip.set_opacity(1)
        pv2tip.set_fill(GOLD_E)
        pv2tip.set_color(GOLD_E)

        v2_p = Line(start = ORIGIN,end = 0.5*LEFT + 0.5*UP)
        v2_p.set_color(RED_E)
        v2_p_tip = Polygon(0.5*LEFT + 0.5*UP, 0.5*LEFT + 0.4*UP, 0.4*LEFT + 0.5*UP)
        v2_p_tip.set_opacity(1)
        v2_p_tip.set_fill(RED_E)
        v2_p_tip.set_color(RED_E)

        pv3 = Line(start = ORIGIN,end = 4*UP+3*RIGHT+[0,0,5])
        pv3.set_color(GOLD_E)
        pv3tip = Polygon(4*UP+3*RIGHT+[0,0,5],3.6*UP+2.7*RIGHT+[0,0,4.5]+0.1*UP+0.1*LEFT,3.6*UP+2.7*RIGHT+[0,0,4.5]+0.1*DOWN+0.1*RIGHT)
        pv3tip.set_opacity(1)
        pv3tip.set_fill(GOLD_E)
        pv3tip.set_color(GOLD_E)

        v3_p = Line(start = ORIGIN,end = [0,0,5])
        v3_p.set_color(YELLOW_E)
        v3_p_tip = Polygon([0,0,5.15],[0,0,4.8]+0.2*RIGHT,[0,0,4.8]+0.2*LEFT)
        v3_p_tip.set_opacity(1)
        v3_p_tip.set_fill(YELLOW_E)
        v3_p_tip.set_color(YELLOW_E)

        #self.stop_ambient_camera_rotation()
        self.play(Transform(pv1,v1_p), 
        Transform(pv1tip,v1_p_tip), 
        Transform(pv2,v2_p), 
        Transform(pv2tip,v2_p_tip), 
        Transform(pv3,v3_p), 
        Transform(pv3tip,v3_p_tip))
        self.play(FadeOut(dashedline1),
        FadeOut(dashedline2),
        FadeOut(dashedline3),
        FadeOut(dashedline4),
        FadeOut(dashedline5),
        FadeOut(line1),
        FadeOut(tip1),
        FadeOut(line2),
        FadeOut(tip2),
        FadeOut(line3),
        FadeOut(tip3),
        FadeOut(text))

        text = TextMobject(r"$v$ is the sum of projections on the orthonormal vectors")
        text.set_color(GOLD_E)
        text.scale(0.75)
        self.add_fixed_in_frame_mobjects(text)
        text.move_to(3*DOWN)
        self.play(Write(text), ApplyMethod(pv2.move_to,(3.5*RIGHT + 3.5*UP+3*RIGHT+4*UP)/2), ApplyMethod(pv2tip.move_to,(3.1*RIGHT + 3.9*UP)))
        self.play(ApplyMethod(pv3.move_to,3*RIGHT + 4*UP + [0,0,2.5]), ApplyMethod(pv3tip.move_to,(3*RIGHT + 4*UP + [0,0,4.8])))

        self.wait(3)