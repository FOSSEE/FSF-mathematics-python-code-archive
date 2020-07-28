from manimlib.imports import *

class ScalarFunction(Scene):
    def construct(self):
        circle = Circle(radius = 1.5, color = BLUE_E, fill_color = BLUE_C, fill_opacity = 0.1).move_to(2*LEFT)
        dot_circle = Dot().shift(np.array([-1.5,0,0])).set_color(BLUE_E)
        dot_circle_lab = TextMobject(r"$a$", color = BLUE_E).next_to(dot_circle, DOWN)

        arrow = Arrow(np.array([3,-3,0]),np.array([3,3,0]))
        line = Line(np.array([3,-1.5,0]),np.array([3,1.5,0]), color = RED_C)

        dot0 = Dot().shift(np.array([3,0,0])).set_color("#8b000c")
        dot0_lab = TextMobject(r"$f(a)$", color = "#8b000c").scale(0.8).next_to(dot0, RIGHT)

        dot1 = Dot().shift(np.array([3,-1.5,0])).set_color(RED_C)

        dot2 = Dot().shift(np.array([3,1.5,0])).set_color(RED_C)
        dot2_lab = TextMobject(r"$f(A)$", color = RED_C).scale(0.8).next_to(dot2, RIGHT)

        arrow_f = Arrow(np.array([-1.5,0,0]),np.array([3,0,0]), color = YELLOW_C, buff = 0.1)

        R = TextMobject(r"$\mathbb{R}$", color = WHITE).move_to(np.array([3,-3.3,0]))

        A = TextMobject(r"$A$", color = BLUE_E).move_to(np.array([-2.5,-3.3,0]))

        F = TextMobject(r"$f$", color = GREY).move_to(np.array([0,-2.9,0]))

        F_center = TextMobject(r"$f$", color = YELLOW_C).move_to(np.array([0.8,0.5,0]))

        arrow_R_A = Arrow(np.array([-2.3,-3.3,0]),np.array([2.7,-3.3,0]), color = GREY, buff = 0.1)

        scalar_function = TextMobject(r"Scalar Valued Function", r"$f: A \rightarrow \mathbb{R}$", color = PURPLE).move_to(np.array([0,3.5,0]))
        scalar_function[1].set_color(GREEN_C)



        self.play(ShowCreation(circle))
        self.play(ShowCreation(arrow))

        
        self.play(ShowCreation(dot1), ShowCreation(dot2), ShowCreation(line))
        self.play(ShowCreation(dot_circle))
        self.play(ShowCreation(dot_circle_lab),  ShowCreation(dot2_lab))
        self.play(ShowCreation(A), ShowCreation(R))
        self.play(GrowArrow(arrow_f), ShowCreation(dot0), ShowCreation(dot0_lab), ShowCreation(F_center), GrowArrow(arrow_R_A), ShowCreation(F), Transform(circle.copy(), line.copy()))
        self.bring_to_front(dot0)
        self.play(Write(scalar_function))


        self.wait(2)