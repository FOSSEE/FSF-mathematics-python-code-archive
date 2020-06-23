from manimlib.imports import*

class TangenttoSurface(ThreeDScene):

    def construct(self):
        axes = ThreeDAxes() 
        
        #----f(x,y): x**2+y**2
        p = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2+v**2
            ]),v_min = -1,v_max = 1, u_min = -1, u_max = 1, checkerboard_colors = [GREEN_C,GREEN_D],
            resolution = (20, 20)).scale(1)
        self.set_camera_orientation(phi = 75*DEGREES) 

        h_text = TextMobject("The graph tends to coincide with its tangent plane").scale(0.5).to_corner(UL)
        d = Dot([0,0,0],color ='#800000')  #----critical point
        r = Rectangle(height = 2,breadth = 1,color = YELLOW).scale(0.5) #----tangent plane to critical point
        line1 = DashedLine(color=RED).shift(4*UP+1.3*RIGHT).rotate(1.571,UP).scale(1.2)
        line2 = DashedLine(color=RED).shift(4*UP-1.3*RIGHT).rotate(1.571,UP).scale(1.2) 

        r2 = Rectangle(height = 2, breadth = 1,color = GREEN, fill_opacity=0.3).scale(0.5)

        self.add(axes)
        self.play(Write(r))
        self.play(Write(p),Write(d))
        self.play(ShowCreation(line1),ShowCreation(line2))
        self.wait(2)
        
        self.play(FadeOut(line1),FadeOut(line2),ReplacementTransform(p,r2))
        self.add_fixed_in_frame_mobjects(h_text)
        self.wait(1)
