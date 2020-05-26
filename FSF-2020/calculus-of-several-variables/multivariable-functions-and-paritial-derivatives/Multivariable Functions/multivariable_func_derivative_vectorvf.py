from manimlib.imports import *

class Derivative(GraphScene):
    CONFIG = {
    "x_min": 0,
    "x_max": 3,
    "y_min": 0,
    "y_max": 5,
    "graph_origin": ORIGIN+6*LEFT+3*DOWN,
    "x_axis_width": 6,
    "x_labeled_nums": list(range(0, 4)),
    "y_labeled_nums": list(range(0, 6)),
    }
    def construct(self):

        XTD = self.x_axis_width/(self.x_max - self.x_min)
        YTD = self.y_axis_height/(self.y_max - self.y_min)

        self.setup_axes(animate = True)

        graph = self.get_graph(lambda x :  x*x, x_min = 0.5, x_max = 2, color = GREEN)

        point1 = Dot().shift(self.graph_origin+0.25*YTD*UP + 0.5*XTD*RIGHT)
        point1_lab = TextMobject(r"$t = a$") 
        point1_lab.scale(0.7)
        point1_lab.next_to(point1, RIGHT)

        point2 = Dot().shift(self.graph_origin+2*XTD*RIGHT+4*YTD*UP)
        point2_lab = TextMobject(r"$t = b$") 
        point2_lab.scale(0.7)
        point2_lab.next_to(point2, RIGHT)


        vector1 = Arrow(self.graph_origin, self.graph_origin+1*YTD*UP + 1*XTD*RIGHT, buff=0.02, color = RED)
        vector1_lab = TextMobject(r"$\vec r(t)$", color = RED) 
        vector1_lab.move_to(self.graph_origin+1.2*XTD*RIGHT+ 0.75*YTD*UP)
        vector1_lab.scale(0.8)

        vector2 = Arrow(self.graph_origin, self.graph_origin+2.25*YTD*UP + 1.5*XTD*RIGHT, buff=0.02, color = YELLOW_C)
        vector2_lab = TextMobject(r"$\vec r(t + h)$", color = YELLOW_C) 
        vector2_lab.move_to(self.graph_origin+0.5*XTD*RIGHT+ 2*YTD*UP)
        vector2_lab.scale(0.8)

        vector3 = Arrow(self.graph_origin+1*YTD*UP + 1*XTD*RIGHT, self.graph_origin+2.25*YTD*UP + 1.5*XTD*RIGHT, buff=0.02, color = PINK)
        vector3_lab = TextMobject(r"$\vec r(t + h) - \vec r(t)$", color = PINK) 
        vector3_lab.move_to(self.graph_origin+2*XTD*RIGHT+ 1.5*YTD*UP)
        vector3_lab.scale(0.8)
        

        self.play(ShowCreation(graph))
        self.play(ShowCreation(point1), Write(point1_lab))
        self.play(ShowCreation(point2), Write(point2_lab))

        self.play(GrowArrow(vector1),Write(vector1_lab))
        self.play(GrowArrow(vector2),Write(vector2_lab))
        self.play(GrowArrow(vector3),Write(vector3_lab))
        self.wait(1)

        self.display_text()

        self.play(ApplyMethod(vector3_lab.move_to,(self.graph_origin+2.3*XTD*RIGHT+ 2.2*YTD*UP)))

        vector4 = Arrow(self.graph_origin+1*YTD*UP + 1*XTD*RIGHT, self.graph_origin+1*YTD*UP + 1.5*XTD*RIGHT, buff=0.02, color = PURPLE)
        vector4_lab = TextMobject(r"$dx$", color = PURPLE) 
        vector4_lab.move_to(self.graph_origin+1.7*XTD*RIGHT+ 0.8*YTD*UP)
        vector4_lab.scale(0.7)

        vector5 = Arrow(self.graph_origin+1*YTD*UP + 1.5*XTD*RIGHT, self.graph_origin+2.25*YTD*UP + 1.5*XTD*RIGHT, buff=0.02, color = ORANGE)
        vector5_lab = TextMobject(r"$dy$", color = ORANGE) 
        vector5_lab.move_to(self.graph_origin+1.7*XTD*RIGHT+ 1.4*YTD*UP)
        vector5_lab.scale(0.7)

        self.play(GrowArrow(vector4),Write(vector4_lab))
        self.play(GrowArrow(vector5),Write(vector5_lab))
        self.wait(2)

        

    def display_text(self):
        text1 = TextMobject(r"$\vec r(t)$",r"+", r"$\vec r(t + h) - \vec r(t)$")
        text1[0].set_color(RED)
        text1[2].set_color(PINK)
        text1.scale(0.7)

        text2 = TextMobject(r"$\vec r(t + h)$", color = YELLOW_C)
        text2.scale(0.7)

        text3 = TextMobject(r"$ \vec r(t + h) - \vec r(t)$", color = PINK)
        text3.scale(0.7)

        text4 = TextMobject(r"[", r"$x(t+h)$", r"$\vec i$", r"+", r"$y(t+h)$", r"$\vec j$", r"$]  - [$", r"$x(t)$", r"$\vec i$", r"+", r"y(t)", r"$\vec j$", r"]")
        text4.set_color_by_tex(r"\vec i", BLUE)
        text4.set_color_by_tex(r"\vec j", GREEN)
        text4[1].set_color(YELLOW_C)
        text4[4].set_color(YELLOW_C)
        text4[-6].set_color(RED)
        text4[-3].set_color(RED)
        text4.scale(0.7)

        text5 = TextMobject(r"$[x(t+h) - x(t)]$", r"$\vec i$", r"+", r"$[y(t+h) + y(t)]$", r"$\vec j$")
        text5.set_color_by_tex(r"\vec i", BLUE)
        text5.set_color_by_tex(r"\vec j", GREEN)
        text5[0].set_color(PURPLE)
        text5[3].set_color(ORANGE)
        text5.scale(0.7)

        text6 = TextMobject(r"$\frac{[\vec r(t + h) - \vec r(t)]}{h}$", r"=", r"$\frac{[x(t+h) - x(t)]}{h}$", r"$\vec i$", r"+", r"$\frac{[y(t+h) + y(t)]}{h}$", r"$\vec j$")
        text6.set_color_by_tex(r"\vec i", BLUE)
        text6.set_color_by_tex(r"\vec j", GREEN)
        text6[0].set_color(PINK)
        text6[2].set_color(PURPLE)
        text6[-2].set_color(ORANGE)
        text6.scale(0.8)

        text7 = TextMobject(r"$\lim_{h \rightarrow 0}$", r"$\frac{[\vec r(t + h) - \vec r(t)]}{h}$", r"=", r"$\lim_{h \rightarrow 0}$", r"$\frac{[x(t+h) - x(t)]}{h}$", r"$\vec i$", r"+", r"$\lim_{h \rightarrow 0}$", r"$\frac{[y(t+h) + y(t)]}{h}$", r"$\vec j$")
        text7.set_color_by_tex(r"\vec i", BLUE)
        text7.set_color_by_tex(r"\vec j", GREEN)
        text7[1].set_color(PINK)
        text7[4].set_color(PURPLE)
        text7[-2].set_color(ORANGE)
        text7.scale(0.6)

        text8 = TextMobject(r"$\vec r'(t)$", r"=",r"$\vec x'(t)$", r"$\vec i$", r"+", r"$\vec y'(t)$", r"$\vec j$")
        text8.set_color_by_tex(r"\vec i", BLUE)
        text8.set_color_by_tex(r"\vec j", GREEN)
        text8[0].set_color(PINK)
        text8[2].set_color(PURPLE)
        text8[5].set_color(ORANGE)
        text8.scale(0.7)

        text9 = TextMobject(r"$\frac{d \vec r}{dt}$", r"=", r"$\frac{d \vec x}{dt}$", r"$\vec i$", r"+", r"$\frac{d \vec y}{dt}$", r"$\vec j$")
        text9.set_color_by_tex(r"\vec i", BLUE)
        text9.set_color_by_tex(r"\vec j", GREEN)
        text9[0].set_color(PINK)
        text9[2].set_color(PURPLE)
        text9[5].set_color(ORANGE)
        text9.scale(0.7)


        text10 = TextMobject(r"$d \vec r$", r"=", r"$\frac{d \vec x}{dt}dt$", r"$\vec i$", r"+", r"$\frac{d \vec y}{dt}dt$", r"$\vec j$")
        text10.set_color_by_tex(r"\vec i", BLUE)
        text10.set_color_by_tex(r"\vec j", GREEN)
        text10[0].set_color(PINK)
        text10[2].set_color(PURPLE)
        text10[5].set_color(ORANGE)
        text10.scale(0.7)

        text11 = TextMobject(r"$d \vec r$", r"=", r"$x'(t)dt$", r"$\vec i$", r"+", r"$y'(t)dt$", r"$\vec j$")
        text11.set_color_by_tex(r"\vec i", BLUE)
        text11.set_color_by_tex(r"\vec j", GREEN)
        text11[0].set_color(PINK)
        text11[2].set_color(PURPLE)
        text11[5].set_color(ORANGE)
        text11.scale(0.7)

        text12 = TextMobject(r"$d \vec r$", r"=", r"$dx$", r"$\vec i$", r"+", r"$dy$", r"$\vec j$")
        text12.set_color_by_tex(r"\vec i", BLUE)
        text12.set_color_by_tex(r"\vec j", GREEN)
        text12[0].set_color(PINK)
        text12[2].set_color(PURPLE)
        text12[5].set_color(ORANGE)
        text12.scale(0.7)


        text1.move_to(1*UP+2.7*RIGHT)
        text2.move_to(1*UP+2.7*RIGHT)
        text3.move_to(1*UP+2.7*RIGHT)
        text4.move_to(1*UP+2.7*RIGHT)
        text5.move_to(1*UP+2.7*RIGHT)
        text6.move_to(1*UP+2.7*RIGHT)
        text7.move_to(1*UP+2.5*RIGHT)
        text8.move_to(1*UP+2.7*RIGHT)
        text9.move_to(1*UP+2.7*RIGHT)
        text10.move_to(1*UP+2.7*RIGHT)
        text11.move_to(1*UP+2.7*RIGHT)
        text12.move_to(1*UP+2.7*RIGHT)

        brace1 = Brace(text7[0:2], DOWN, buff = SMALL_BUFF)
        brace2 = Brace(text7[3:6], UP, buff = SMALL_BUFF)
        brace3 = Brace(text7[7:], DOWN, buff = SMALL_BUFF)
        t1 = brace1.get_text(r"$\vec r'(t)$")
        t1.set_color(PINK)

        t2 = brace2.get_text(r"$\vec x'(t)$")
        t2.set_color(PURPLE)

        t3 = brace3.get_text(r"$\vec y'(t)$")
        t3.set_color(ORANGE)


        self.play(Write(text1))
        self.play(Transform(text1, text2))
        self.wait(1)

        self.play(Transform(text1, text3))
        self.wait(1)

        self.play(Transform(text1, text4))
        self.wait(1)

        self.play(Transform(text1, text5))
        self.wait(1)

        self.play(Transform(text1, text6))
        self.wait(1)

        self.play(Transform(text1, text7))
        self.wait(1)

        self.play(
            GrowFromCenter(brace1),
            FadeIn(t1),
            )
        self.wait()
        self.play(
            ReplacementTransform(brace1.copy(),brace2),
            ReplacementTransform(t1.copy(),t2)
            )
        self.wait()
        self.play(
            ReplacementTransform(brace2.copy(),brace3),
            ReplacementTransform(t2.copy(),t3)
            )
        self.wait()

        self.play(FadeOut(brace1), FadeOut(t1), FadeOut(brace2), FadeOut(t2), FadeOut(brace3), FadeOut(t3),)
        self.wait()

        self.play(Transform(text1, text8))
        self.wait(1)

        self.play(Transform(text1, text9))
        self.wait(1)

        self.play(Transform(text1, text10))
        self.wait(1)

        self.play(Transform(text1, text11))
        self.wait(1)

        self.play(Transform(text1, text12))
        self.wait(1)





