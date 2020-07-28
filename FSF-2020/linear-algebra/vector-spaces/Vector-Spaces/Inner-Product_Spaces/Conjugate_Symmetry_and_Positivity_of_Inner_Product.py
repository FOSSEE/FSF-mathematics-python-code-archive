from manimlib.imports import *
VECTORS = [[0, 2],
           [1, 1],
           [0, -2],
           [1, -1],
           [2, -2],
           [2, 2],
           [2, 2],
           [-2, -1],
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
      text1 = TextMobject(r"\text{$u$}",r"\text{ = $0 + 2i$, }",r"\text{$v$}",r"\text{ = $1 + i$}").scale(0.6).shift(3.5*UP+4*LEFT)      
      text1[0].set_color(YELLOW)
      text1[2].set_color(RED)
      text1.add_background_rectangle()
      self.play(ShowCreation(text1))
      text2 = TextMobject(r"\text{$\overline{u}$}",r"\text{ = $0 - 2i$, }",r"\text{$\overline{v}$}",r"\text{ = $1 - i$}").scale(0.6).shift(3*UP+4*LEFT)      
      text2[0].set_color(YELLOW)
      text2[2].set_color(RED)
      text2.add_background_rectangle()
      self.play(ShowCreation(text2))
      self.wait(2)
      v1 = self.add_vector(VECTORS[0],color = YELLOW, stroke_width = 3.5)
      u = TextMobject(r"$u$",color=YELLOW).shift(0.3*LEFT+2*UP).scale(0.6)
      self.play(ShowCreation(u))
      v1b = self.add_vector(VECTORS[2],color = YELLOW, stroke_width = 3.5)
      ub = TextMobject(r"$\overline{u}$",color=YELLOW).shift(2*DOWN+0.3*LEFT).scale(0.6)
      self.play(ShowCreation(ub))
      self.wait(2)
      v2 = self.add_vector(VECTORS[1],color = RED, stroke_width = 3.5)
      v = TextMobject(r"$v$",color=RED).shift(1.2*RIGHT+1*UP).scale(0.6)
      self.play(ShowCreation(v))
      v2b = self.add_vector(VECTORS[3],color = RED, stroke_width = 3.5)
      vb = TextMobject(r"$\overline{v}$",color=RED).shift(1.2*RIGHT+1*DOWN).scale(0.6)
      self.play(ShowCreation(vb))
      text3 = TextMobject(r"\text{$<u, v>$}",r"\text{ = }",r"\text{$\overline{u}$",r"\text{$\cdot$}",r"\text{$v$}",r"\text{ = }",r"\text{$2 - 2i$}").shift(2.5*UP+3.7*LEFT).scale(0.6)
      text3[0].set_color(BLUE)
      text3[2].set_color(YELLOW)
      text3[4].set_color(RED)
      text3.add_background_rectangle()
      self.play(ShowCreation(text3))
      self.wait(2)
      text4 = TextMobject(r"\text{$<\overline{u, v}>$",r"\text{ = }",r"\text{$\overline{u}$",r"\text{$\cdot$}",r"\text{$v$}",r"\text{ = }",r"\text{$2 + 2i$}").shift(2*UP+3.7*LEFT).scale(0.6)
      text4[0].set_color(BLUE)
      text4[2].set_color(YELLOW)
      text4[4].set_color(RED)
      text4.add_background_rectangle()
      line = Line(stroke_width = 1.5).scale(0.33).shift(2.2*UP+3.54*LEFT)
      self.play(ShowCreation(text4),ShowCreation(line))
      self.wait(2)
      self.play(FadeOut(v1),FadeOut(v1b),FadeOut(v2),FadeOut(v2b),FadeOut(u),FadeOut(ub),FadeOut(v),FadeOut(vb))
      v3 = self.add_vector(VECTORS[4],color = BLUE, stroke_width = 3.5)
      uv = TextMobject(r"$\overline{u}\cdot v$",color=BLUE).shift(2.4*RIGHT+2.1*DOWN).scale(0.6)
      self.play(ShowCreation(uv))
      v3b = self.add_vector(VECTORS[5],color = BLUE, stroke_width = 3.5)
      uvb = TextMobject(r"$\overline{\overline{u}\cdot v}$",color=BLUE).shift(2.4*RIGHT+2.1*UP).scale(0.6)
      self.play(ShowCreation(uvb))
      self.wait(2)
      text5 = TextMobject(r"\text{$<v, u>$}",r"\text{ = }",r"\text{$\overline{v}$",r"\text{$\cdot$}",r"\text{$u$}",r"\text{ = }",r"\text{$2 + 2i$}").shift(1.5*UP+3.7*LEFT).scale(0.6)
      text5[0].set_color(MAROON_B)
      text5[2].set_color(RED)
      text5[4].set_color(YELLOW)
      text5.add_background_rectangle()
      self.play(ShowCreation(text5))
      self.wait(2)
      v4 = self.add_vector(VECTORS[5],color = MAROON_B, stroke_width = 3.5)
      vu = TextMobject(r"$\overline{v}\cdot u$",color=MAROON_B).shift(1.3*RIGHT+2.1*UP).scale(0.6)
      self.play(ShowCreation(vu))
      self.play(FadeOut(uvb))
      self.wait(2)
      text6 = TextMobject(r"\text{$<\overline{u, v}>$",r"\text{ = }",r"\text{$<v, u>$").scale(0.6).shift(0.8*UP+4.2*LEFT)
      text6[0].set_color(BLUE)
      text6[2].set_color(MAROON_B)
      text6.add_background_rectangle()
      self.play(ShowCreation(text6))
      rect = Rectangle(height = 0.7,width = 3.5)
      rect.surround(text6)
      self.play(ShowCreation(rect))
      self.wait(3)
      self.play(FadeOut(line),FadeOut(text1),FadeOut(text2),FadeOut(text3),FadeOut(text4),FadeOut(text5),FadeOut(text6),FadeOut(v4),FadeOut(vu),FadeOut(v3),FadeOut(uv),FadeOut(rect),FadeOut(v3b))

      text7 = TextMobject(r"\text{$u$}",r"\text{ = $(1 + i) > 0$}").scale(0.6).shift(3.5*UP+4.5*LEFT)
      text7[0].set_color(YELLOW)
      text7.add_background_rectangle()
      self.play(ShowCreation(text7))
      v5 = self.add_vector(VECTORS[1],color = YELLOW, stroke_width = 3.5)
      u = TextMobject(r"$u$",color=YELLOW).shift(1.2*RIGHT+1*UP).scale(0.6)
      self.play(ShowCreation(u))
      self.wait(1.5)
      text8 = TextMobject(r"\text{$<u, u>$}",r"\text{ = $(0 + 2i) > 0$ }").scale(0.6).shift(2.7*UP+4*LEFT)      
      text8[0].set_color(GREEN)
      text8.add_background_rectangle()
      rect1 = Rectangle(height = 0.55, width = 3.3)
      rect1.surround(text8)
      self.play(ShowCreation(text8),ShowCreation(rect1))
      self.wait(2)
      v6 = self.add_vector(VECTORS[0],color = GREEN, stroke_width = 3.5)
      uu = TextMobject(r"$<u, u>$",color=GREEN).shift(0.8*LEFT+1.9*UP).scale(0.6)
      self.play(ShowCreation(uu))
      text9 = TextMobject(r"\text{$v$}",r"\text{ = $(-2 - i) < 0$}").scale(0.6).shift(1.5*UP+4.4*LEFT)
      text9[0].set_color(RED)
      text9.add_background_rectangle()
      self.play(ShowCreation(text9))
      self.wait(1.5)
      v7 = self.add_vector(VECTORS[7],color = RED, stroke_width = 3.5)
      v = TextMobject(r"$v$",color=RED).shift(2.2*LEFT+1*DOWN).scale(0.6)
      self.play(ShowCreation(v))
      self.wait(1.5)
      text10 = TextMobject(r"\text{$<v, v>$}",r"\text{ = $(3 + 4i) > 0$ }").scale(0.6).shift(0.7*UP+4*LEFT)      
      text10[0].set_color(BLUE)
      text10.add_background_rectangle()
      rect2 = Rectangle(height=0.55,width=3.3)
      rect2.surround(text10)
      self.play(ShowCreation(text10),ShowCreation(rect2))
      self.wait(2)
      v8 = self.add_vector(VECTORS[8],color = BLUE, stroke_width = 3.5)
      vv = TextMobject(r"$<v, v>$",color=BLUE).shift(2.1*RIGHT+3.8*UP).scale(0.6)
      self.play(ShowCreation(vv))
      self.wait(4)






      







