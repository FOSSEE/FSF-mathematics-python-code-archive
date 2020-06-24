from manimlib.imports import*

class firstScene(Scene):
    def construct(self):
        
        e_text = TextMobject("Case 3: One positive and one negative eigenvalue", color = YELLOW).scale(1).shift(3*UP+1*LEFT) 
        f_text = TextMobject("$f(x,y) = x^2-2y^2-2x$").scale(0.8).next_to(e_text).shift(6*LEFT+DOWN)
        c_text = TextMobject("Critical Point: $(1,0)$").scale(0.8).next_to(f_text).shift(DOWN+4*LEFT)
        d_text = TextMobject("\\begin{equation*} D_2(1,0)= \\begin{vmatrix} 2 \\space & 0\\space \\\\ 0 & -4 \\end{vmatrix} \\end{equation*}",color = GREEN).scale(0.9)

        t_text = TextMobject("$D_2 = -8<0$  (Saddle Point)", color = BLUE).scale(0.9).shift(2*DOWN)

        self.play(ShowCreation(e_text))
        self.wait(1)
        self.play(ShowCreation(f_text))
        self.wait(1)
        self.play(ShowCreation(c_text))
        self.wait(1)
        self.play(ShowCreation(d_text))
        self.wait(1)
        self.play(ShowCreation(t_text))
        self.wait(2)

class SaddlePoint(ThreeDScene):
     def construct(self):
        axes = ThreeDAxes()        
        f = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-2*v**2-2*u
            ]),v_min=-1,v_max=1,u_min=-1,u_max=1,checkerboard_colors=[RED_C,PURPLE_D,YELLOW_E],
            resolution=(20, 20)).scale(1)        

        self.set_camera_orientation(phi=35 * DEGREES,theta=80*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.4)

        f_text = TextMobject("$f(x,y) = x^2-2y^2-2x$",color = GREEN).shift(2*DOWN+2*RIGHT).scale(0.8)
        self.add_fixed_in_frame_mobjects(f_text)
        self.add(axes)
        self.play(Write(f))
        self.wait(3)


class secondScene(Scene):
    def construct(self):
        
        h_text = TextMobject("NonDegenerate Hessian Matrix", color = GREEN).scale(1).shift(UP)
        e_text = TextMobject("Case 1: Two positive eigenvalues", color = PINK).scale(1).shift(3*UP+2*LEFT) 
        f_text = TextMobject("$f(x,y) = 2x^2+3y^2-2yx$",color = TEAL).scale(0.8).next_to(e_text).shift(6*LEFT+DOWN)
        c_text = TextMobject("Critical Point: $(0,0)$",color = TEAL).scale(0.8).next_to(f_text).shift(DOWN+4.5*LEFT)
        d_text = TextMobject("\\begin{equation*} D_2(0,0)= \\begin{vmatrix} 4 \\space & -2\\space \\\\ -2 & 6 \\end{vmatrix} \\end{equation*}",color = PINK).scale(0.9)

        t_text = TextMobject("$D_2 = 20>0$  (Relative Maxima or Relative Minima)", color = YELLOW).scale(0.9).shift(1*DOWN)
        tm_text = TextMobject("$D_1 = \\frac{\\partial^2 f}{\\partial x^2} =4 >0$  (Relative Minima)", color = YELLOW).scale(0.9).shift(2*DOWN)


        self.play(ShowCreation(h_text))
        self.wait(1)
        self.play(FadeOut(h_text))
        self.wait(1)
        self.play(ShowCreation(e_text))
        self.wait(1)
        self.play(ShowCreation(f_text))
        self.wait(1)
        self.play(ShowCreation(c_text))
        self.wait(1)
        self.play(ShowCreation(d_text))
        self.wait(1)
        self.play(ShowCreation(t_text))
        self.wait(1)
        self.play(ShowCreation(tm_text))
        self.wait(2)
        self.play(FadeOut(e_text),FadeOut(f_text),FadeOut(c_text),FadeOut(d_text),FadeOut(t_text),FadeOut(tm_text))

class Minima(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()        
        f = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                2*u**2+3*v**2-2*v*u
            ]),v_min=-1,v_max=1,u_min=-1,u_max=1,checkerboard_colors=[BLUE_C,YELLOW_D,GREEN_E],
            resolution=(20, 20)).scale(1)        

        self.set_camera_orientation(phi=10 * DEGREES,theta=90*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)

        f_text = TextMobject("$f(x,y) = 2x^2+3y^2-2yx$",color = PURPLE).shift(2*DOWN+3*RIGHT).scale(0.8)
        self.add_fixed_in_frame_mobjects(f_text)
        self.add(axes)
        self.play(Write(f))
        self.wait(2)


class thirdScene(Scene):
    def construct(self):
        
        
        e_text = TextMobject("Case 2: Two negative eigenvalues", color = RED).scale(1).shift(3*UP+2*LEFT) 
        f_text = TextMobject("$f(x,y) = -x^2-4y^2$",color = BLUE).scale(0.8).next_to(e_text).shift(6*LEFT+DOWN)
        c_text = TextMobject("Critical Point: $(0,0)$",color = BLUE).scale(0.8).next_to(f_text).shift(DOWN+3.8*LEFT)
        d_text = TextMobject("\\begin{equation*} D_2(0,0)= \\begin{vmatrix} -2 \\space & 0\\space \\\\ 0 & -8 \\end{vmatrix} \\end{equation*}",color = TEAL).scale(0.9)

        t_text = TextMobject("$D_2 = 16>0$  (Relative Maxima or Relative Minima)" ).scale(0.9).shift(1*DOWN)
        tm_text = TextMobject("$D_1 = \\frac{\\partial^2 f}{\\partial x^2} =-2 <0$  (Relative Maxima)").scale(0.9).shift(2*DOWN)


        self.play(ShowCreation(e_text))
        self.wait(1)
        self.play(ShowCreation(f_text))
        self.wait(1)
        self.play(ShowCreation(c_text))
        self.wait(1)
        self.play(ShowCreation(d_text))
        self.wait(1)
        self.play(ShowCreation(t_text))
        self.wait(1)
        self.play(ShowCreation(tm_text))
        self.wait(2)
        self.play(FadeOut(e_text),FadeOut(f_text),FadeOut(c_text),FadeOut(d_text),FadeOut(t_text),FadeOut(tm_text))


class Maxima(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()        
        f = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                -u**2-4*v**2
            ]),v_min=-1,v_max=1,u_min=-1,u_max=1,checkerboard_colors=[BLUE_C,PURPLE_D,TEAL_E],
            resolution=(20, 20)).scale(1)        

        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.4)

        f_text = TextMobject("$f(x,y) = -x^2-4y^2$",color = YELLOW).shift(2*DOWN+3*RIGHT).scale(0.8)
        self.add_fixed_in_frame_mobjects(f_text)
        self.add(axes)
        self.play(Write(f))
        self.wait(1)
        self.move_camera(phi=30*DEGREES,theta=45*DEGREES,run_time=5)
        self.wait(2)
