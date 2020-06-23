from manimlib.imports import *
class OrthonormalBasis(GraphScene):
    CONFIG = {
        "x_min" : -6,
        "x_max" : 6,
        "y_min" : -4,
        "y_max" : 4,
        "graph_origin" : ORIGIN ,
}

    def construct(self):
        self.setup_axes(animate=True)

        XTD = self.x_axis_width/(self.x_max-self.x_min)
        YTD = self.y_axis_height/(self.y_max-self.y_min)

        arrow1 = Arrow(start = ORIGIN,end = 0.707*YTD*UP+0.707*XTD*RIGHT)
        arrow1.scale(2.25)
        arrow1.set_color(DARK_BLUE)

        arrow2 = Arrow(start = ORIGIN,end = 0.707*YTD*UP+0.707*XTD*LEFT)
        arrow2.scale(2.25)
        arrow2.set_color(DARK_BLUE)

        square = Polygon(UP*0.4*YTD,0.2*(YTD*UP+XTD*RIGHT),ORIGIN,0.2*(YTD*UP+XTD*LEFT))
        square.set_color(DARK_BLUE)
        self.play(ShowCreation(arrow2), ShowCreation(arrow1), ShowCreation(square))

        ortho = TextMobject("Orthonormal Vectors")
        ortho.scale(0.75)
        ortho.move_to(DOWN+3*RIGHT)
        self.play(Write(ortho))
        self.wait()
        self.play(FadeOut(ortho))

        arrow3 = Arrow(start = ORIGIN,end = YTD*3*UP+XTD*LEFT)
        arrow3.scale(1.25)
        arrow3.set_color(GOLD_E)
        self.play(ShowCreation(arrow3))

        arrow4 = Arrow(start = ORIGIN,end = YTD*UP+XTD*RIGHT)
        arrow4.scale(1.8)
        arrow4.set_color(GOLD_A)
        
        arrow5 = Arrow(start = ORIGIN,end = 2*YTD*UP-2*XTD*RIGHT)
        arrow5.scale(1.3)
        arrow5.set_color(GOLD_A)
        
        self.play(ShowCreation(arrow5), ShowCreation(arrow4))
        
        self.wait()

        self.play(FadeOut(arrow1), FadeOut(arrow2), FadeOut(square))

        self.wait()

        text1 = TextMobject(r"$<v,v_1> v_1$")
        text1.move_to(UP+2*RIGHT)
        text1.scale(0.75)
        text2 = TextMobject(r"$<v,v_2> v_2$")
        text2.move_to(UP+3*LEFT)
        text2.scale(0.75)
        
        text3 = TextMobject("v")
        text3.move_to(YTD*3.5*UP+XTD*1.5*LEFT)

        self.play(Write(text1), Write(text2), Write(text3))
        self.wait()

        line1 = DashedLine(start = YTD*UP+XTD*RIGHT, end = YTD*3*UP+XTD*1*LEFT)
        line2 = DashedLine(start = YTD*2*UP+XTD*2*LEFT, end = YTD*3*UP+XTD*1*LEFT)
        self.play(ShowCreation(line1),ShowCreation(line2))

        self.wait()
        
        text = TextMobject(r"$v$ is the sum of projections","on the orthonormal vectors")
        text[0].move_to(DOWN+3.2*RIGHT)
        text[1].move_to(1.5*DOWN+3.2*RIGHT)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(arrow3), FadeOut(arrow4), FadeOut(arrow5), FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(self.axes), FadeOut(line1), FadeOut(line2))
        self.play(FadeOut(text))
