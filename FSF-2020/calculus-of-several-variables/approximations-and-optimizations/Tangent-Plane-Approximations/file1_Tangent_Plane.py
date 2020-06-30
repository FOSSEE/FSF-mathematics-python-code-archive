from manimlib.imports import*

#---- tangent plane is parallel to the surface of the funtion at a point
class tangentplane(ThreeDScene):
    def construct(self):

        s1_text=TextMobject("Suppose, the point $(x,y)$ lies on the surface of the function.").scale(0.5).shift(2*UP)
        s2_text=TextMobject("When zooming on that point, the surface would appear more and more like a plane.").scale(0.5).shift(1*UP)
        s3_text=TextMobject("This plane is called the tangent plane.").scale(0.5)

        #---- graph of function f(x,y) = -x^2-y^2 

        f = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [YELLOW_B,YELLOW_C,YELLOW_D, YELLOW_E]).shift([0,0,0]).scale(1)

        
        d = Dot([0,0,0],color = '#800000')  #---- critical point

        r = Rectangle(color = PURPLE,fill_opacity=0.2).shift([0.1,0,0]).scale(0.3)  #---- tangent plane 

        s = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-v**2
            ]),v_min = -1, v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [YELLOW_B,YELLOW_C,YELLOW_D, YELLOW_E]).shift([0,0,0]).scale(3.5)

        d2 = Dot([0,0,2.5],color = '#800000') #---- changing position of critical point 

        r2 = Rectangle(color = PURPLE,fill_opacity=0.5).shift([0.1,0,2.5]).scale(0.3) #---- changing position of tangent plane 
        
        self.set_camera_orientation(phi = 50 * DEGREES, theta = 45 * DEGREES)
        self.add_fixed_in_frame_mobjects(s1_text)
        self.add_fixed_in_frame_mobjects(s2_text)
        self.add_fixed_in_frame_mobjects(s3_text)
        self.wait(2)
        self.play(FadeOut(s1_text))
        self.play(FadeOut(s2_text))
        self.play(FadeOut(s3_text))
        self.wait(1)
        self.play(Write(f))
        self.play(Write(d))
        self.play(Write(r))
        self.wait(2)
        self.play(ReplacementTransform(f,s),ReplacementTransform(d,d2),ReplacementTransform(r,r2))
        self.wait(2)
