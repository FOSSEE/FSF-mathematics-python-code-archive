from manimlib.imports import *
VECTORS = [[3,1],
           [1,3],
           [1.96,0.65]]
class Projection(LinearTransformationScene):
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": False,
        "show_coordinates": False,
        "show_basis_vectors": False,
        "basis_vector_stroke_width": 3,
    }
    def construct(self):
      v1 = self.add_vector(VECTORS[0],color = YELLOW, stroke_width = 3.5)
      u = TextMobject(r"$\vec{u}$",color=YELLOW).scale(0.65).shift(3.2*RIGHT,1*UP)
      self.play(ShowCreation(u))
      self.wait(0.7)
      v2 = self.add_vector(VECTORS[1],color = RED, stroke_width = 3.5)
      v = TextMobject(r"$\vec{v}$",color=RED).scale(0.65).shift(1.2*RIGHT,3*UP)
      self.play(ShowCreation(v))
      self.wait(0.7)
      angle = Arc(radius=0.6).scale(0.5)
      theta = TextMobject(r"$\theta$").scale(0.65).shift(0.5*UP+0.5*RIGHT).rotate(np.pi/6)
      self.play(ShowCreation(angle),ShowCreation(theta))
      self.wait(1)
      line1 = Line().scale(1.25).rotate(np.pi/(2)).shift(1.8*UP+1.47*RIGHT)
      line1.rotate(np.pi/8)     
      self.play(ShowCreation(line1))
      self.wait(1.3)
      v3 = self.add_vector(VECTORS[2],color = BLUE, stroke_width = 3.5)
      text1 = TextMobject(r"$\vec{v}$cos$\theta$",color=BLUE).scale(0.55).shift(1.25*RIGHT+0.26*UP).rotate(np.pi/9)
      self.play(ShowCreation(text1))
      self.wait(2)
      text2 = TextMobject(r"\text{Projection on }",r"\text{$\vec{v}$}",r"\text{ onto }",r"\text{$\vec{u}$}",r"\text{ = }",r"\text{$ |\vec{v}|cos\theta$}").scale(0.6).shift(4*RIGHT+3*UP)
      text2[1].set_color(RED)
      text2[3].set_color(YELLOW)
      text2[5].set_color(BLUE)
      text2.add_background_rectangle()
      self.play(ShowCreation(text2))
      self.wait(4)
      

      