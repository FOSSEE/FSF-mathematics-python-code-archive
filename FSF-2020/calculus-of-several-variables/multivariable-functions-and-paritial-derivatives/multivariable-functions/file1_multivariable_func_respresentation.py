from manimlib.imports import *

class MultivariableFunc(Scene):
    def construct(self):

        topic = TextMobject("Multivariable Functions")
        topic.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        topic.scale(2)

        self.play(Write(topic))
        self.wait(1)
        self.play(FadeOut(topic))


        circle = Circle()
        circle.scale(3)

        eqn1 = TextMobject(r"f(x,y) = $x^2y$")
        eqn1.set_color(YELLOW)
        


        number1 = TextMobject("(2,1)")
        number1.move_to(3*UP+ 3*LEFT)
        number1.scale(1.2)
        number1.set_color(GREEN)

        output1 = TextMobject("4")
        output1.scale(1.5)
        output1.set_color(BLUE)

        eqn1_1 = TextMobject(r"f(2,1) = $2^2(1)$")
        eqn1_1.set_color(YELLOW)


        self.play(ShowCreation(circle),Write(eqn1))
        self.wait(1)
        self.play(ApplyMethod(number1.move_to, 0.6*LEFT))
        self.play(FadeOut(number1))
        self.play(Transform(eqn1, eqn1_1))
        self.wait(1)
        self.play(ApplyMethod(output1.move_to, 3*DOWN+4*RIGHT))
        self.wait(1)
        self.play(FadeOut(output1))


        eqn2 = TextMobject(r"f(x,y,z) = $x^2y+2yz$")
        eqn2.set_color(YELLOW)

        number2 = TextMobject("(2,1,3)")
        number2.move_to(3*UP+ 3*LEFT)
        number2.scale(1.2)
        number2.set_color(GREEN)

        output2 = TextMobject("8")
        output2.scale(1.5)
        output2.set_color(BLUE)

        eqn2_1 = TextMobject(r"f(2,1,3) = $2^2(1) + 2(1)(3)$")
        eqn2_1.set_color(YELLOW)

        eqn2_2 = TextMobject(r"f(2,1,3) = $2 + 6$")
        eqn2_2.set_color(YELLOW)


        
        self.play(FadeOut(eqn1))
        self.play(Write(eqn2))

        self.wait(1)
        self.play(ApplyMethod(number2.move_to, 1.2*LEFT))
        self.play(FadeOut(number2))
        self.play(Transform(eqn2, eqn2_1))
        self.wait(1)
        self.play(Transform(eqn2, eqn2_2))
        self.wait(1)
        self.play(ApplyMethod(output2.move_to, 3*DOWN+4*RIGHT))
        self.wait(1)
        self.play(FadeOut(output2),FadeOut(eqn2),FadeOut(circle))
        self.wait(2)