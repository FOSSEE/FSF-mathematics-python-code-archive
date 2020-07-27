from manimlib.imports import *
class limitfin1(GraphScene):
    CONFIG = {
        "x_min" : -8,
        "x_max" : 8,
        "x_labeled_nums" : list(range(-8, 10, 3)),
        "x_axis_width" : FRAME_WIDTH - LARGE_BUFF,
        "y_min" : -4,
        "y_max" : 4,
        "y_labeled_nums" : None,
        "y_axis_height" : FRAME_HEIGHT+2*LARGE_BUFF,
        "graph_origin" : DOWN,
        "graph_color" : BLUE,
        "x_axis_width":20,
        "y_axis_height":10,
    }
    def construct(self):
        self.setup_axes()
        XTD = 10/(8 - (-8))
        YTD = 10/(4 - (-4))
        graph1 = self.get_graph(lambda x: x**3 +1.5, x_min = self.x_min, x_max = -0.1)
        graph2 = self.get_graph(lambda x: x**3 +1.5, x_min = 0.1, x_max = self.x_max, color = self.graph_color)
        dot2 = Circle(radius = 0.1).move_to(self.graph_origin+1.5*UP*YTD)
        text0 = TextMobject("Let L be the value of f(x) at point denoted by circle").move_to(self.graph_origin+2*DOWN)
        text1 = TexMobject(r"\text{As }", r"\delta",r"\text{ tends to zero }" ,r"\epsilon" r"\text{ tends to zero}").move_to(self.graph_origin+2*DOWN)
        text2 = TexMobject(r"\text{For all values in }", r"(-\delta, +\delta)",r"\text{ you will always find a real and finite value of f(x) in }",r"(L-\epsilon, L+\epsilon)").move_to(self.graph_origin+2*DOWN).scale(0.6)
        self.play(ShowCreation(graph1), ShowCreation(graph2), ShowCreation(text0), FadeIn(dot2))
        line1 = DashedVMobject(Line(self.graph_origin+1*DOWN*YTD+1*LEFT*XTD, self.graph_origin+4*UP*YTD+1*LEFT*XTD), num_dashes = 50).set_color(PINK)
        line2 = DashedVMobject(Line(self.graph_origin+1*DOWN*YTD+1*RIGHT*XTD, self.graph_origin+4*UP*YTD+1*RIGHT*XTD), num_dashes = 50).set_color(PINK)
        line3 = DashedVMobject(Line(self.graph_origin+1.5*UP*YTD+5*LEFT*XTD, self.graph_origin+1.5*UP*YTD+4*RIGHT*XTD), num_dashes = 50).set_color(GOLD)
        line4 = DashedVMobject(Line(self.graph_origin+0.5*UP*YTD+5*LEFT*XTD, self.graph_origin+0.5*UP*YTD+4*RIGHT*XTD), num_dashes = 50).set_color(GOLD)
        line5 = DashedVMobject(Line(self.graph_origin+2.5*UP*YTD+5*LEFT*XTD, self.graph_origin+2.5*UP*YTD+4*RIGHT*XTD), num_dashes = 50).set_color(GOLD)
        self.play(ShowCreation(line1), ShowCreation(line2))
        vec1 = Line(self.graph_origin, self.graph_origin+1*RIGHT*XTD)
        vec2 = Line(self.graph_origin, self.graph_origin+1*LEFT*XTD)
        vec5 = Line(self.graph_origin+2.5*UP*YTD+4*RIGHT*XTD, self.graph_origin+1.5*UP*YTD+4*RIGHT*XTD)
        vec6 = Line(self.graph_origin+0.5*UP*YTD+4*RIGHT*XTD, self.graph_origin+1.5*UP*YTD+4*RIGHT*XTD)
        brace1 = Brace(vec1, DOWN)
        brace2 = Brace(vec2, DOWN)
        br1text = brace1.get_text(r"$\delta$").next_to(brace1, DOWN)
        br2text = brace2.get_text(r"$\delta$").next_to(brace2, DOWN)
        brace5 = Brace(vec5, RIGHT)
        brace6 = Brace(vec6, RIGHT)
        br5text = brace5.get_text(r"$\epsilon$").next_to(brace5, RIGHT)
        br6text = brace6.get_text(r"$\epsilon$").next_to(brace6, RIGHT)
        self.wait(3)
        self.play(ShowCreation(brace1), ShowCreation(brace2), ShowCreation(br1text), ShowCreation(br2text))
        self.wait(3)
        self.play(ReplacementTransform(text0, text1))
        self.play(ShowCreation(line3), ShowCreation(line4), ShowCreation(line5), ShowCreation(brace5), ShowCreation(brace6), ShowCreation(br5text), ShowCreation(br6text))
        vec3 = Line(self.graph_origin, self.graph_origin+0.1*RIGHT*XTD)
        vec4 = Line(self.graph_origin, self.graph_origin+0.11*LEFT*XTD)
        brace3 = Brace(vec3, DOWN)
        brace4 = Brace(vec4, DOWN)
        vec7 = Line(self.graph_origin+1.6*UP*YTD+4*RIGHT*XTD, self.graph_origin+1.5*UP*YTD+4*RIGHT*XTD)
        vec8 = Line(self.graph_origin+1.4*UP*YTD+4*RIGHT*XTD, self.graph_origin+1.5*UP*YTD+4*RIGHT*XTD)
        brace7 = Brace(vec7, RIGHT)
        brace8 = Brace(vec8, RIGHT)
        self.play(Transform(brace1, brace3), Transform(brace2, brace4), ApplyMethod(line2.shift, 0.8*LEFT*XTD), 
            ApplyMethod(line1.shift, 0.8*RIGHT*XTD), ApplyMethod(br1text.scale, 0.3), ApplyMethod(br2text.scale, 0.3),
            Transform(brace5, brace7), Transform(brace6, brace8), ApplyMethod(line4.shift, 1.8*UP*XTD), 
            ApplyMethod(line5.shift, 1.8*DOWN*XTD))
        self.wait(3)
        self.play(ReplacementTransform(text1, text2))
        self.play(FadeOut(brace5), FadeOut(brace6), FadeOut(brace1), FadeOut(brace2))
        self.play(ApplyMethod(line2.shift, 0.8*RIGHT*XTD), ApplyMethod(line1.shift, 0.8*LEFT*XTD), ApplyMethod(br1text.scale, 10/3), ApplyMethod(br2text.scale, 10/3),
            ApplyMethod(line5.shift, 1.8*UP*XTD), ApplyMethod(line4.shift, 1.8*DOWN*XTD))
        for i in range(0,3):
            self.play(ApplyMethod(line2.shift, 0.8*LEFT*XTD), ApplyMethod(line1.shift, 0.8*RIGHT*XTD), ApplyMethod(br1text.scale, 0.3), ApplyMethod(br2text.scale, 0.3),
            ApplyMethod(line5.shift, 1.8*DOWN*XTD), ApplyMethod(line4.shift, 1.8*UP*XTD), ApplyMethod(br5text.scale, 0.3), ApplyMethod(br6text.scale, 0.3), run_time = 0.5)
            self.play(ApplyMethod(line2.shift, 0.8*RIGHT*XTD), ApplyMethod(line1.shift, 0.8*LEFT*XTD), ApplyMethod(br1text.scale, 10/3), ApplyMethod(br2text.scale, 10/3),
            ApplyMethod(line5.shift, 1.8*UP*XTD), ApplyMethod(line4.shift, 1.8*DOWN*XTD), ApplyMethod(br5text.scale, 10/3), ApplyMethod(br6text.scale ,10/3), run_time = 0.5)
        self.play(ApplyMethod(line2.shift, 0.8*LEFT*XTD), ApplyMethod(line1.shift, 0.8*RIGHT*XTD), ApplyMethod(br1text.scale, 0.3), ApplyMethod(br2text.scale, 0.3),
            ApplyMethod(line5.shift, 1.8*DOWN*XTD), ApplyMethod(line4.shift, 1.8*UP*XTD),ApplyMethod(br5text.scale, 0.3), ApplyMethod(br6text.scale, 0.3), run_time = 0.5)

        self.wait(5)