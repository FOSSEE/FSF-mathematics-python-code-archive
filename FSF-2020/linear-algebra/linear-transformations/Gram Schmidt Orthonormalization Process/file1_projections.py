from manimlib.imports import *

class Projections(GraphScene):
    CONFIG = {
        "x_min": -6,
        "x_max": 6,
        "y_min": -4,
        "y_max": 4,
        "graph_origin" : ORIGIN ,
    }    
    def construct(self):
       
        self.setup_axes(animate=True)

        XTD = self.x_axis_width/(self.x_max-self.x_min)
        YTD = self.y_axis_height/(self.y_max-self.y_min)

        arrow_a = Arrow(start = ORIGIN, end = 4*XTD*RIGHT)
        arrow_a.scale(1.2)
        arrow_a.set_color(DARK_BLUE)
        arrow_b = Arrow(start = ORIGIN, end = 2*YTD*UP+2*XTD*RIGHT)
        arrow_b.scale(1.3)
        arrow_b.set_color(DARK_BLUE)
        self.play(ShowCreation(arrow_a), ShowCreation(arrow_b))

        text = TextMobject(r"Let there be 2 vectors $a$ and $b$")
        text.set_color(DARK_BLUE)
        text.scale(0.75)
        text.move_to(2*YTD*DOWN+4*XTD*LEFT)
        text_a = TextMobject("a")
        text_a.move_to(0.4*YTD*DOWN+3*XTD*RIGHT)
        text_a.set_color(DARK_BLUE)
        text_b = TextMobject("b")
        text_b.move_to(1.5*YTD*UP+RIGHT*XTD)
        text_b.set_color(DARK_BLUE)
 
        self.play(Write(text),Write(text_a), Write(text_b))
        self.wait()

        arrow_b_copy = Arrow(start = ORIGIN, end = 2*YTD*UP+2*XTD*RIGHT)
        arrow_b_copy.scale(1.25)

        arrow_p = Arrow(start = ORIGIN, end = 2*XTD*RIGHT)
        arrow_p.scale(1.5)
        arrow_p.set_color(GOLD_E)

        text_p = TextMobject("p")
        text_p.move_to(0.25*DOWN+RIGHT)
        text_p.set_color(GOLD_E)

        self.play(FadeOut(text), Transform(arrow_b_copy,arrow_p), FadeOut(text_a), FadeOut(text_b))
        text = TextMobject(r"$p$ is the projection of $b$ on $a$")
        text.set_color(GOLD_E)
        text.move_to(2*DOWN+3*LEFT)
        text.scale(0.8)
        self.play(Write(text),Write(text_p))
        self.wait()
        
        self.play(FadeIn(text_a), FadeIn(text_b))

        arrow_o = Arrow(start = 2*XTD*RIGHT, end = 2*YTD*UP+2*XTD*RIGHT)
        arrow_o.scale(1.5)
        arrow_o.set_color(GREEN_E)

        text_o = TextMobject("b-p")
        text_o.move_to(UP*YTD+2.7*XTD*RIGHT)
        text_o.set_color(GREEN_E)

        self.play(ShowCreation(arrow_o))
        self.play(FadeOut(text),Write(text_o))
        
        text = TextMobject(r"Observe, ($b-p$) is orthogonal to $a$")
        text.set_color(GREEN_E)
        text.move_to(2*DOWN+4*LEFT)
        text.scale(0.8)
        self.play(Write(text))
        self.wait(2)

        self.play(FadeOut(self.axes), FadeOut(arrow_a), FadeOut(arrow_b), FadeOut(arrow_b_copy), FadeOut(arrow_o), FadeOut(text_a), FadeOut(text_b), FadeOut(text_o), FadeOut(text_p), FadeOut(text))
        
        text = TextMobject(r"Therefore, unit vectors of $b-p$ and $a$ are orthonormal to each other")
        text.scale(0.75)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))