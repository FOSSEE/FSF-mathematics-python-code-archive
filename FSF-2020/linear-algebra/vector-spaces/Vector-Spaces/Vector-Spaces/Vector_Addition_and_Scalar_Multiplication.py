from manimlib.imports import *
VECTORS = [[1, 2],
           [1, 1],
           [2, 2],
           [3, 4]]
class Scene1(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": False,
        "show_coordinates": True,
        "show_basis_vectors": False,
        "basis_vector_stroke_width": 3,
    }
    def construct(self):
    	self.write_stuff()
    	v1 = self.add_vector(VECTORS[0],color = YELLOW, stroke_width = 3.5)
    	line1 = Line(start = ORIGIN, end = VECTORS[0][0]*RIGHT)
    	line1.set_color(RED_B)
    	line2 = Line(start = line1.get_end(), end = line1.get_end() + VECTORS[0][1]*UP)
    	line2.set_color(GREEN_D)
    	self.play(ShowCreation(line1))
    	self.play(ShowCreation(line2))
    	self.wait(0.5)
    	text1 = TextMobject("(1, 2)",color=YELLOW).scale(0.6).shift(2*UP + 1.5*RIGHT)
    	self.play(ShowCreation(text1))
    	text2 = TextMobject(r"$\vec{a}$",color = YELLOW).scale(0.8).shift(2*UP + 1.2*RIGHT)
    	text3 = TextMobject(r"\text{$\vec{a}$}",r"\text{=}",r"\text{(1, 2)}").scale(0.7).shift(5.1*LEFT + 2.5*UP)
    	text3[0].set_color(YELLOW)
    	text3[2].set_color(YELLOW)    	
    	self.wait(1)
    	self.play(Transform(text1,text2),FadeOut(line1),FadeOut(line2))
    	self.wait(0.5)
    	self.play(ShowCreation(text3))
    	self.wait(1)


    	v2 = self.add_vector(VECTORS[1],color = BLUE, stroke_width = 3.5)
    	line3 = Line(start = ORIGIN, end = VECTORS[1][0]*RIGHT)
    	line3.set_color(RED_B)
    	line4 = Line(start = line3.get_end(), end = line3.get_end() + VECTORS[1][1]*UP)
    	line4.set_color(GREEN_D)
    	self.play(ShowCreation(line3))
    	self.play(ShowCreation(line4))
    	self.wait(0.5)
    	text4 = TextMobject("(2, 2)",color=BLUE).scale(0.6).shift(1*UP + 1.5*RIGHT)
    	self.play(ShowCreation(text4))
    	text5 = TextMobject(r"$\vec{b}$",color = BLUE).scale(0.8).shift(1*UP + 1.2*RIGHT)
    	text6 = TextMobject(r"\text{$\vec{b}$}",r"\text{=}",r"\text{(1, 1)}").scale(0.7).shift(5.1*LEFT + 1.8*UP)
    	text6[0].set_color(BLUE)
    	text6[2].set_color(BLUE)
    	self.wait(1)
    	self.play(Transform(text4,text5),FadeOut(line3),FadeOut(line4))
    	self.wait(0.5)
    	self.play(ShowCreation(text6))
    	self.wait(2)


    	
    	text7 = TextMobject(r"\text{Scaling}",r"\text{ $\vec{b}$ }",r"\text{by 2 units}",color = GOLD).scale(0.7).shift(2.8*UP+4*RIGHT)
    	text7[1].set_color(BLUE)
    	self.play(ShowCreation(text7))
    	self.play(FadeOut(text4))
    	v3 = self.add_vector(VECTORS[2],color = BLUE, stroke_width = 3.5)
    	line7 = Line(start = ORIGIN, end = VECTORS[2][0]*RIGHT)
    	line7.set_color(RED_B)
    	line8 = Line(start = line7.get_end(), end = line7.get_end() + VECTORS[2][1]*UP)
    	line8.set_color(GREEN_D)
    	self.play(FadeOut(v2))
    	self.play(ShowCreation(line7))
    	self.play(ShowCreation(line8))
    	

    	self.wait(0.5)
    	
    	text8 = TextMobject("(2, 2)",color=BLUE).scale(0.6).shift(2.5*RIGHT + 2*UP)
    	text9 = TextMobject(r"$2\vec{b}$",color = BLUE).scale(0.8).shift(2*UP + 2.3*RIGHT)
    	self.play(ShowCreation(text8))
    	self.wait(1)
    	self.play(Transform(text8,text9),FadeOut(line7),FadeOut(line8))
    	self.wait(1)
    	text10 = TextMobject(r"\text{$2\vec{b}$}",r"\text{=}",r"\text{(2, 2)}").scale(0.7).shift(5.1*LEFT + 1.8*UP)
    	text10[0].set_color(BLUE)
    	text10[2].set_color(BLUE)
    	self.play(Transform(text6,text10))
    	self.wait(1)
    	self.play(FadeOut(text7))
    	self.wait(1.5)



    	text11 = TextMobject(r"Addition of vectors",color = GOLD).scale(0.7).shift(2.8*UP+5*RIGHT)
    	self.play(ShowCreation(text11))
    	v1.move_to(3*UP+2.5*RIGHT)
    	self.play(ShowCreation(v1),FadeOut(text8),FadeOut(text1))
    	v4 = self.add_vector(VECTORS[3],color = ORANGE, stroke_width = 3.5)
    	line7 = Line(start = ORIGIN, end = VECTORS[3][0]*RIGHT)
    	line7.set_color(RED_B)
    	line8 = Line(start = line7.get_end(), end = line7.get_end() + VECTORS[3][1]*UP)
    	line8.set_color(GREEN_D)
    	self.play(ShowCreation(line7))
    	self.play(ShowCreation(line8))
    	text12 = TextMobject("(3, 4)",color=ORANGE).scale(0.6).shift(3.5*RIGHT + 3.8*UP)
    	text13 = TextMobject(r"$\vec{c}$",color = ORANGE).scale(0.8).shift(3.7*UP + 3.3*RIGHT)
    	self.play(ShowCreation(text12))
    	self.wait(1)
    	self.play(Transform(text12,text13),FadeOut(line7),FadeOut(line8))
    	self.wait(1)
    	add = TextMobject("+").scale(0.8).shift(6.2*LEFT + 1.8*UP)
    	line_1= Line().shift(1.5*UP+5.1*LEFT).scale(1.5)
    	line_2= Line().shift(0.8*UP+5.1*LEFT).scale(1.5)

    	text14=TextMobject(r"\text{$\vec{c}$}",r"\text{=}",r"\text{$\vec{a}$}",r"\text{+}",r"\text{$2\vec{b}$}",r"\text{=}",r"\text{(3, 4)}").scale(0.7).shift(1.2*UP+5.1*LEFT)
    	text14[0].set_color(ORANGE)
    	text14[2].set_color(YELLOW)
    	text14[4].set_color(BLUE)
    	text14[6].set_color(ORANGE)
       	
       
    	self.play(ShowCreation(add),ShowCreation(line_1))
    	self.play(ShowCreation(text14),ShowCreation(line_2))
    	self.wait(3)


    	
    	





    	



















    def write_stuff(self):
        self.text = []
        text = self.text

        text.append(TexMobject(r"\text{Consider the Vector Space }",
                               r"{\mathbb{R}^2}")) 
        self.add_title(text[0], 0.7, animate = True)
        text.append(TexMobject(r"{\mathbb{R}^2}",
                               tex_to_color_map = {r"{\mathbb{R}^2}": BLUE_E}))
        text[1].shift(6.5*LEFT+3.5*UP)
        self.wait(0.5)
        self.play(Transform(text[0], text[1]))
   
  











        

