from manimlib.imports import *

class ChainRule(Scene):
    def construct(self):

        chain_rule = TextMobject(r"$\frac{dw}{dt}$", r"=", r"$\frac{\partial w}{\partial x}$", r"$\frac{dx}{dt}$", r"+", r"$\frac{\partial w}{\partial y}$", r"$\frac{dy}{dt}$").move_to(4*RIGHT).scale(0.8)
        
        chain_rule[0].set_color(ORANGE)
        chain_rule[2].set_color(GREEN_C)
        chain_rule[3].set_color(RED_C)
        chain_rule[5].set_color(YELLOW_C)
        chain_rule[6].set_color(BLUE_C)
        
        functions = TextMobject(r"$w =f(x,y)$",r"$x$", r"$y$", r"$t$")

        functions[0].move_to(3.3*UP+1*LEFT).set_color(ORANGE)
        functions[1].move_to(3.3*LEFT).set_color(PURPLE)
        functions[2].move_to(1.3*RIGHT).set_color(PURPLE)
        functions[3].move_to(3.3*DOWN+1*LEFT).set_color(WHITE)

        partial_derivatives = TextMobject(r"$\frac{\partial w}{\partial x}$", r"$\frac{\partial w}{\partial y}$")

        partial_derivatives[0].move_to(1.5*UP+3*LEFT).set_color(GREEN_C)
        partial_derivatives[1].move_to(1.5*UP+1*RIGHT).set_color(YELLOW_C)

        derivatives = TextMobject(r"$\frac{dx}{dt}$", r"$\frac{dy}{dt}$")

        derivatives[0].move_to(1.5*DOWN+3*LEFT).set_color(RED_C)
        derivatives[1].move_to(1.5*DOWN+1*RIGHT).set_color(BLUE_C)

        line_f_x = Line(np.array([-1,3,0]), np.array([-3,0,0]), color = BLUE_C)
        line_f_y = Line(np.array([-1,3,0]), np.array([1,0,0]), color = BLUE_C)
        line_x_t = Line(np.array([-3,0,0]), np.array([-1,-3,0]), color = BLUE_C)
        line_y_t = Line(np.array([1,0,0]), np.array([-1,-3,0]), color = BLUE_C)

        dot_f = Dot().shift(np.array([-1,3,0])).set_color(BLUE_C)
        dot_x = Dot().shift(np.array([-3,0,0])).set_color(BLUE_C)
        dot_y = Dot().shift(np.array([1,0,0])).set_color(BLUE_C)
        dot_t = Dot().shift(np.array([-1,-3,0])).set_color(BLUE_C)

        variables = TextMobject("Dependent Variable","Intermediate Variables", "Dependent Variable").set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE).scale(0.7)
        variables[0].move_to(3.3*UP+3.5*RIGHT)
        variables[1].move_to(3.5*RIGHT)
        variables[2].move_to(3.3*DOWN+3.5*RIGHT)

        self.play(ShowCreation(dot_f), Write(functions[0]))
        self.play(ShowCreation(dot_x), ShowCreation(line_f_x), Write(functions[1]), ShowCreation(dot_y), ShowCreation(line_f_y), Write(functions[2]))
        self.play(Write(partial_derivatives[0]), Write(partial_derivatives[1]))
        self.wait()

        self.play(ShowCreation(dot_t), ShowCreation(line_x_t), ShowCreation(line_y_t), Write(functions[3]))
        self.play(Write(derivatives[0]), Write(derivatives[1]))
        self.wait()

        self.play(Write(variables[0]), Write(variables[1]), Write(variables[2]))

        self.play(FadeOut(variables))
        self.play(Write(chain_rule))
        self.wait()
 