from manimlib.imports import*
import math as m

#---- tangent plane approximation visualization
class ApproximationScene(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes().scale(1.2).fade(0.7)
        label_x= TextMobject("$x$").shift([5.4,-0.5,0]).fade(0.7) #---- x axis
        label_y= TextMobject("$y$").shift([-0.5,5.2,0]).rotate(-4.5).fade(0.7) #---- y axis

        #---- graph of the function 
        s = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),u_min=0,u_max=PI,v_min=PI,v_max=2*PI,checkerboard_colors=[BLUE_B,BLUE_C,BLUE_D,BLUE_E]).shift([0,1,2.4]).scale(1.3)
        
        d1 = Dot([0.2,2.01,2.24],color = '#800000').rotate(1.1,LEFT) #---- point(x_0,y_0)
        d1_copy = Dot([0.2,2.01,0],color = '#800000') #---- projection of point(x_0,y_0) on x-y plane

        d1_text = TextMobject("$f(x_0,y_0)$",color=ORANGE).scale(0.5).shift([0.2,2.01,2.3])
        d1_copy_text = TextMobject("$(x_0,y_0)$",color=ORANGE).scale(0.5).shift([0.2,2.01,0],4.1*DOWN)

        d2 = Dot([2,2.6,3.5],color = '#800000').rotate(1,LEFT) #---- point(x,y)
        d2_copy = Dot([2,2.6,0],color = '#800000') #---- projection of point(x,y) on x-y plane

        d2_text = TextMobject("$f(x,y)$",color=ORANGE).scale(0.5).shift([0.8,1.4,1.5])
        d2_copy_text = TextMobject("$(x,y)$",color=ORANGE).scale(0.5).shift([0.8,1.4,0],2.4*DOWN)

        l1 = Line([0.2,2.01,2.21],[0.2,2.01,0],color= YELLOW).fade(0.2)
        l2 = Line([2,2.6,3.4],[2,2.6,0],color= YELLOW).fade(0.2)

        t_plane = Rectangle(color = PURPLE, fill_opacity=0.3).scale(0.6).rotate(m.radians(45),LEFT).shift([1.1,2.5,3.1]) #---- tangent plane
        t_text= TextMobject("Tangent Plane",color = PINK).scale(0.5).shift(0.3*RIGHT+2.6*UP).rotate(math.radians(5),LEFT)

        a1 = Line([0.2,2.01,0],[2,2.6,0],color ="#00FF7F")
        a_x = Line([0.2,2.01,0],[2,2.01,0],color ="#9400D3")
        a_y = Line([0.2,2.01,0],[0.2,2.6,0],color ="#8B4513")
        a2 = Line([2,2.01,0],[2,2.6,0])
        a3 = Line([0.2,2.6,0],[2,2.6,0])

        ax_text = TextMobject("$f_x (x_0 , y_0 )(x – x_0 ) $").scale(0.5).shift(DOWN+0.8*LEFT).rotate(0.4)
        ay_text = TextMobject("$ f_y (x_0 , y_0 )(y – y_0 ) $").scale(0.5).shift(0.8*DOWN+2.7*RIGHT).rotate(-0.6)
        a1_text = TextMobject("$f_x (x_0 , y_0 )(x – x_0 ) + f_y (x_0 , y_0 )(y – y_0 )$ ").scale(0.4).rotate(0.7).shift(1.7*DOWN+0.6*RIGHT)

        lines = VGroup(a1,a_y,a_x,a2,a3,d1_copy,d2_copy)


        self.set_camera_orientation(phi = 60 * DEGREES, theta = 55 * DEGREES)
        self.wait(1)
        self.add(axes)
        self.add(label_x)
        self.add(label_y)
        self.play(Write(s))
        self.wait(1)
        self.play(Write(d2))
        self.add_fixed_in_frame_mobjects(d1_text)
        self.wait(1)
        self.play(Write(t_plane))
        self.add_fixed_in_frame_mobjects(t_text)
        self.wait(1)
        self.play(Write(d1))
        self.add_fixed_in_frame_mobjects(d2_text)
        self.wait(1)
        self.play(Write(l1),Write(d1_copy))
        self.add_fixed_in_frame_mobjects(d2_copy_text)
        self.wait(1)
        self.play(Write(l2),Write(d2_copy))
        self.add_fixed_in_frame_mobjects(d1_copy_text)
        self.wait(2)
        self.play(FadeOut(d1_text),FadeOut(d1_copy_text),FadeOut(d2_text),FadeOut(d2_copy_text),FadeOut(t_text))
        self.wait(1)
        self.play(Write(a1),Write(a_x),Write(a_y),Write(a2),Write(a3))
        self.wait(1)
        self.play(FadeOut(s),FadeOut(d1),FadeOut(d2),FadeOut(l1),FadeOut(l2),FadeOut(t_plane),FadeOut(label_x),FadeOut(label_y))
        self.wait(1)
        lines.scale(2)
        axes.scale(1.5)
        self.wait(1)
        self.add_fixed_in_frame_mobjects(ax_text)
        self.add_fixed_in_frame_mobjects(ay_text)
        self.add_fixed_in_frame_mobjects(a1_text)
        self.wait(1)
