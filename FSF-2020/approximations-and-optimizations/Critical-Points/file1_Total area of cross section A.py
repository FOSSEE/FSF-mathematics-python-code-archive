from manimlib.imports import*

class MotivationAnimation(Scene):
    def construct(self):
        
        r = Rectangle(height = 7,breadth = 2,color = BLUE, fill_opacity = 0.3).scale(0.6) #----metal strip
        b = Brace(r,UP)
        r_text = TextMobject("$x$ metres",color = YELLOW).shift(3*UP)
        m_text = TextMobject("Metal Strip").shift(3*DOWN)
        a = Arc(radius=2).rotate(1).shift(LEFT+0.5*UP)
        a2 = Arc(radius=2).rotate(5).shift(0.7*LEFT+0.9*UP).scale(0.2)
        START = [1,0,0]
        END = [0,3,0]
        l = Line(START,END,color = RED).shift(0.9*DOWN)
        a2_text = TextMobject("$\\theta$",color = PINK).shift(1.6*UP+0.4*RIGHT)

        group1 = VGroup(r_text,b,a,l,a2,a2_text)
        f_text = TextMobject("$A = f(x,\\theta)$").shift(2*DOWN)

        ring = Annulus(inner_radius = 0.7, outer_radius = 1, color = BLUE)  #--bent metal strip

        self.play(Write(r))
        self.wait(1)
        self.play(ShowCreation(m_text))
        self.wait(1)
        self.play(Write(group1))
        self.wait(2)
        self.play(FadeOut(group1))
        self.wait(1)
        self.play(ReplacementTransform(r,ring),ShowCreation(f_text))
        
