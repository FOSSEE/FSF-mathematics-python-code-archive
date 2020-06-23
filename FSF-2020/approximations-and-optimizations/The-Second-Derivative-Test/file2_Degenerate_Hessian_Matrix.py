from manimlib.imports import*

class firstscene(Scene):
    def construct(self):

        h_text = TextMobject("Degenerate Hessian Matrix", color = RED).scale(1).shift(UP)
        

        f_text = TextMobject("$f(x,y) = 2x^3+y^3$", color = TEAL).scale(1).to_corner(UL) 
        c_text = TextMobject("Critical Point: $(0,0)$", color = TEAL).scale(1).next_to(f_text).shift(DOWN+4.3*LEFT)
        m_text = TextMobject("\\begin{equation*} D_2(x,y)= \\begin{vmatrix} 12x\\space & 0\\space \\\\ 0 & 6y \\end{vmatrix} \\end{equation*}",color = YELLOW)
        d_text = TextMobject("\\begin{equation*} D_2(0,0)= \\begin{vmatrix} 0 \\space & 0\\space \\\\ 0 & 0 \\end{vmatrix} \\end{equation*}",color = PURPLE)


        t_text = TextMobject("$D_2 = 0$(Inconclusive)", color = TEAL).scale(1).shift(2*DOWN)

        self.play(ShowCreation(h_text))
        self.wait(1)
        self.play(FadeOut(h_text))
        self.wait(1)
        self.play(ShowCreation(f_text))
        self.wait(1)
        self.play(ShowCreation(c_text))
        self.wait(1)
        self.play(ShowCreation(m_text))
        self.wait(2)
        self.play(ReplacementTransform(m_text,d_text))
        self.wait(1)
        self.play(ShowCreation(t_text))
        self.wait(2)


class SecondScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        
        f = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                (2*u**3)+v**3
            ]),v_min=-1,v_max=1,u_min=-1,u_max=1,checkerboard_colors=[TEAL_C,YELLOW_D,BLUE_E],
            resolution=(20, 20)).scale(1)        

        self.set_camera_orientation(phi=25 * DEGREES,theta = 80*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        f_text = TextMobject("$f(x,y) = 2x^3+y^3$",color = ORANGE).shift(2*DOWN+2*RIGHT).scale(0.8)
        self.add_fixed_in_frame_mobjects(f_text)
        self.add(axes)
        self.play(Write(f))
        self.wait(2)
