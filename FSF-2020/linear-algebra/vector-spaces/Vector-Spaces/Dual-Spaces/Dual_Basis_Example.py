from manimlib.imports import *
import numpy as np

class Dual_Basis(GraphScene):
  CONFIG={
  "x_min": -7,
  "x_max": 7,
  "y_min": -7,
  "y_max": 7,
  "graph_origin": ORIGIN,
  "x_axis_label":"$X$",
  "y_axis_label":"$Y$",
  "x_labeled_nums": list(np.arange(-7, 8,1)),
  "y_labeled_nums": list(np.arange(-7, 8,1)),
  "x_axis_width": 10,
  "y_axis_height": 10,
  "x_tick_frequency":1,
  "axes_color": GREY,
  "area_opacity": 3,
  "num_rects": 10,
  } 
  def construct(self):
    self.setup_axes(animate = True)
    XD = self.x_axis_width/(self.x_max- self.x_min)
    YD = self.y_axis_height/(self.y_max- self.y_min)  
    a1=2*XD*RIGHT+1*YD*UP
    a2=3*XD*RIGHT+1*YD*UP
    vec1=Vector(direction=a1,stroke_width=2).set_color(RED_E)
    vec1.shift(self.graph_origin)    
    v1_label=TextMobject(r"$v_1$")
    v1_label=(v1_label.shift(self.graph_origin+a1+0.1)).scale(.6)
    self.play(ShowCreation(vec1),ShowCreation(v1_label))
    text1=TextMobject(r"\text{$v_1$}",r"\text{$= (2,1)$}").scale(.6)
    text1[0].set_color(RED_E)
    text1.shift(5*LEFT+3.5*UP)
    self.play(ShowCreation(text1))
    self.wait(1.5)
    vec2=Vector(direction=a2,stroke_width=2).set_color(YELLOW_E)
    vec2.shift(self.graph_origin)
    v2_label=TextMobject(r"$v_2$")
    v2_label=(v2_label.shift(self.graph_origin+a2+0.1)).scale(.6)
    self.play(ShowCreation(vec2),ShowCreation(v2_label))
    text2=TextMobject(r"\text{$v_2$}",r"\text{$= (3,1)$}").scale(.6)
    text2[0].set_color(YELLOW_E)
    text2.shift(5*LEFT+3*UP)
    self.play(ShowCreation(text2))
    self.wait(1.5)
    text3=TextMobject(r"\text{${T_2}$}",r"\text{$(v_1)$}",r"\text{$= 0$}").scale(.6)
    text3[0].set_color(BLUE)
    text3[1].set_color(RED_E)
    text3.shift(4.94*LEFT+2.5*UP)
    self.play(ShowCreation(text3))
    self.wait(1.5)
    text4=TextMobject(r"\text{${T_2}$}",r"\text{$= x - 2y$}").scale(.6)
    text4[0].set_color(BLUE)
    text4.shift(4.9*LEFT+2*UP)
    self.play(ShowCreation(text4))
    self.wait(1.5)
    line1 = self.get_graph(lambda x : x/2, x_min = -5,x_max=5,color=BLUE)
    v1_dual_label = TextMobject(r"${T_2}$").scale(.6).shift(3.9*RIGHT+1.85*UP)    
    self.play(ShowCreation(line1),ShowCreation(v1_dual_label))
    self.wait(1.5)    
    text5=TextMobject(r"\text{${T_1}$}",r"\text{$(v_2)$}",r"\text{$= 0$}").scale(.6)
    text5[1].set_color(YELLOW_E)
    text5[0].set_color(PINK)
    text5.shift(4.94*LEFT+1.5*UP)
    self.play(ShowCreation(text5))
    self.wait(1.5)
    line2 = self.get_graph(lambda x : x/3, x_min = -5,x_max=5,color=PINK)
    v2_dual_label = TextMobject(r"${T_1}$").scale(.6).shift(3.9*RIGHT+1.3*UP)
    self.play(ShowCreation(line2),ShowCreation(v2_dual_label))
    self.wait(1.5)
    text6=TextMobject(r"\text{${T_1}$}",r"\text{$= - x + 3y$}").scale(.6)
    text6[0].set_color(PINK)
    text6.shift(4.76*LEFT+1*UP)
    self.play(ShowCreation(text6))
    self.wait(3)
    text7 = TextMobject(r"\text{B =}",r"\text{$[$}",r"\text{$v_1,$}",r"\text{$v_2$}",r"\text{$]$}",r"\text{=}",r"\text{$[(2,1), (3,1)]$}").scale(0.6).shift(3*UP+4.5*LEFT)
    text7[2].set_color(RED_E)
    text7[3].set_color(YELLOW_E)
    self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3),FadeOut(text4),FadeOut(text5),FadeOut(text6))
    self.play(ShowCreation(text7))
    self.wait(0.7)
    text8 = TextMobject(r"\text{B$^* =$}",r"\text{$[$}",r"\text{${T_1}$,}",r"\text{${T_2} $}",r"\text{$]$}",r"\text{=}",r"\text{$[-x + 3y, x - 2y]$}").scale(0.6).shift(2.3*UP+4.1*LEFT)
    text8[3].set_color(BLUE)
    text8[2].set_color(PINK)
    self.play(ShowCreation(text8))
    self.wait(3)




 


   

