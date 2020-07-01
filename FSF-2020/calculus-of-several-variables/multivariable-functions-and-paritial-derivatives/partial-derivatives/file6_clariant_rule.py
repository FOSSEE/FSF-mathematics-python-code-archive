from manimlib.imports import *

class ClariantRule(Scene):
    def construct(self):
        derivatives = TextMobject(r"$cos(x)y^3$",r"$-sin(x)y^3$", r"$3cos(x)y^2$", r"$-cos(x)y^3$", r"$-3sin(x)y^2$", r"$-3sin(x)y^2$", r"$6cos(x)y$")

        partial_derivatives = TextMobject(r"$\frac{\partial}{\partial x}$", r"$\frac{\partial}{\partial y}$")

        
        derivatives[0].move_to(2*UP).set_color(PURPLE)
        derivatives[1].move_to(3*LEFT).set_color(YELLOW_C)
        derivatives[2].move_to(3*RIGHT).set_color(BLUE_C)
        
        arrrow_1 = Arrow(derivatives[0].get_bottom(), derivatives[1].get_top())
        arrrow_1_lab = partial_derivatives[0].copy().scale(0.7)  
        arrrow_1_lab.move_to(2.5*LEFT+ 1.3*UP)

        arrrow_2 = Arrow(derivatives[0].get_bottom(), derivatives[2].get_top())
        arrrow_2_lab = partial_derivatives[1].copy().scale(0.7)  
        arrrow_2_lab.move_to(2.5*RIGHT+ 1.3*UP)

        self.play(Write(derivatives[0]))
        self.play(GrowArrow(arrrow_1), GrowArrow(arrrow_2), Write(arrrow_1_lab), Write(arrrow_2_lab))

        self.play(Write(derivatives[1]))
        self.play(Write(derivatives[2]))

        derivatives[3].move_to(2*DOWN + 4.5*LEFT).set_color(GREEN_C)
        derivatives[4].move_to(2*DOWN + 1.5*LEFT).set_color(PINK)
        derivatives[5].move_to(2*DOWN + 1.5*RIGHT).set_color(PINK)
        derivatives[6].move_to(2*DOWN + 4.5*RIGHT).set_color(ORANGE)

        arrrow_3 = Arrow(derivatives[1].get_bottom(), derivatives[3].get_top())
        arrrow_3_lab = partial_derivatives[0].copy().scale(0.7) 
        arrrow_3_lab.move_to(4.3*LEFT+ 0.8*DOWN)

        arrrow_4 = Arrow(derivatives[1].get_bottom(), derivatives[4].get_top())
        arrrow_4_lab = partial_derivatives[1].copy().scale(0.7)  
        arrrow_4_lab.move_to(1.6*LEFT+ 0.8*DOWN)

        arrrow_5 = Arrow(derivatives[2].get_bottom(), derivatives[5].get_top())
        arrrow_5_lab = partial_derivatives[0].copy().scale(0.7)  
        arrrow_5_lab.move_to(1.6*RIGHT+ 0.8*DOWN)

        arrrow_6 = Arrow(derivatives[2].get_bottom(), derivatives[6].get_top())
        arrrow_6_lab = partial_derivatives[1].copy().scale(0.7)  
        arrrow_6_lab.move_to(4.3*RIGHT+ 0.8*DOWN)

        self.play(GrowArrow(arrrow_3), GrowArrow(arrrow_4), Write(arrrow_3_lab), Write(arrrow_4_lab))
        self.play(Write(derivatives[3]), Write(derivatives[4]))

        self.play(GrowArrow(arrrow_5), GrowArrow(arrrow_6), Write(arrrow_5_lab), Write(arrrow_6_lab))
        self.play(Write(derivatives[5]), Write(derivatives[6]))
        
        brace1 = Brace(derivatives[4:6], DOWN, buff = SMALL_BUFF, color = RED_C)
        brace_t1 = brace1.get_text("Mixed partial derivatives are the same!")
        brace_t1.set_color(RED_C)

        self.play(GrowFromCenter(brace1), FadeIn(brace_t1))
        
        self.wait()



