from manimlib.imports import *

class MultivariableFunc(Scene):
    def construct(self):

        topic = TextMobject("Multivariable Functions")
        topic.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        topic.scale(1.5)

        self.play(Write(topic))
        self.wait()
        self.play(FadeOut(topic))


        #circle = Circle()
        #circle.scale(3)

        scalar_function = TextMobject("Scalar Valued Function")
        scalar_function.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        scalar_function.scale(1.5)
        scalar_function.move_to(2.5*UP)

        rectangle = Rectangle(height = 2, width = 4)
        rectangle.set_color(PURPLE)

        eqn1 = TextMobject(r"f(x,y) = $x^2y$")
        eqn1.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE)
        


        number1 = TextMobject("(2,1)")
        number1.move_to(2.5*UP+ 4*LEFT)
        number1.scale(1.2)
        number1.set_color(ORANGE)

        output1 = TextMobject("4")
        output1.scale(1.5)
        output1.set_color(BLUE_C)
        output1.move_to(3*RIGHT)

        eqn1_1 = TextMobject(r"f(2,1) = $2^2(1)$")
        eqn1_1.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE)


        self.play(Write(eqn1),ShowCreation(rectangle))
        self.wait()
        self.play(ApplyMethod(number1.move_to, 3*LEFT))
        self.play(FadeOut(number1))
        self.play(Transform(eqn1, eqn1_1))
        self.wait()
        self.play(ApplyMethod(output1.move_to, 2.5*DOWN+4*RIGHT))
        self.wait()
        self.play(Write(scalar_function))
        self.play(FadeOut(output1), FadeOut(scalar_function), FadeOut(eqn1))


        vector_function = TextMobject("Vector Valued Function")
        vector_function.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        vector_function.scale(1.5)
        vector_function.move_to(2.5*UP)


        eqn2 = TextMobject(r"f(x,y,z) = $ \begin{bmatrix} x^2y \\ 2yz  \end{bmatrix}$")
        eqn2.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        number2 = TextMobject("(2,1,3)")
        number2.move_to(2.5*UP+ 4*LEFT)
        number2.scale(1.2)
        number2.set_color(ORANGE)

        output2 = TextMobject(r"$ \begin{bmatrix} 4 \\ 6  \end{bmatrix}$")
        #output2.scale(1.5)
        output2.set_color(BLUE_C)
        output2.move_to(3*RIGHT)

        #eqn2_1 = TextMobject(r"f(2,1,3) = $2^2(1) + 2(1)(3)$")
        #eqn2_1.set_color(YELLOW)

        #eqn2_2 = TextMobject(r"f(2,1,3) = $2 + 6$")
        #eqn2_2.set_color(YELLOW)


        self.play(Write(eqn2))

        self.wait()
        self.play(ApplyMethod(number2.move_to, 3*LEFT))
        self.play(FadeOut(number2))

        #self.play(Transform(eqn2, eqn2_1))
        #self.wait(1)
        #self.play(Transform(eqn2, eqn2_2))
        #self.wait(1)

        self.play(ApplyMethod(output2.move_to, 2.5*DOWN+4*RIGHT))
        self.wait()
        self.play(Write(vector_function))
        self.play(FadeOut(output2),FadeOut(eqn2), FadeOut(vector_function), FadeOut(rectangle))
        self.wait()