from manimlib.imports import *

class MultivariableFunc(Scene):
    def construct(self):

        topic = TextMobject("Multivariable Functions")
        topic.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        topic.scale(1.5)

        self.play(Write(topic))
        self.wait()
        self.play(FadeOut(topic))


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
        output2.set_color(BLUE_C)
        output2.move_to(3*RIGHT)

    

        self.play(Write(eqn2))

        self.wait()
        self.play(ApplyMethod(number2.move_to, 3*LEFT))
        self.play(FadeOut(number2))

        self.play(ApplyMethod(output2.move_to, 2.5*DOWN+4*RIGHT))
        self.wait()
        self.play(Write(vector_function))
        self.play(FadeOut(output2),FadeOut(eqn2), FadeOut(vector_function), FadeOut(rectangle))
        self.wait()



class VectorValuedFunc(Scene):
    def construct(self):
        numberplane = NumberPlane()
       
        rectangle = Rectangle(height = 1, width = 2, color = PURPLE).move_to(2.5*UP+5*RIGHT)

        eqn = TextMobject(r"f(x,y) = $ \begin{bmatrix} xy \\ \frac{y}{x}  \end{bmatrix}$").scale(0.6).move_to(2.5*UP+5*RIGHT).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)

        dot1 = Dot().set_color(PINK).move_to(np.array([2,2,0]))

        number1 = TextMobject("(2,2)").scale(0.6).next_to(dot1, RIGHT).set_color(PINK)

        output1 = TextMobject(r"$ \begin{bmatrix} 4 \\ 1 \end{bmatrix}$").scale(0.6).set_color(YELLOW_C).move_to(2.5*UP+6.5*RIGHT)

        vector1 = Arrow(np.array([2,2,0]), np.array([4,1,0]), color = RED_C, buff = 0.01, tip_length = 0.25)

        dot2 = Dot().set_color(PINK).move_to(np.array([-1,2,0]))

        number2 = TextMobject("(-1,2)").scale(0.6).next_to(dot2, RIGHT).set_color(PINK)

        output2 = TextMobject(r"$ \begin{bmatrix} -2 \\ -2 \end{bmatrix}$").scale(0.6).set_color(YELLOW_C).move_to(2.5*UP+6.5*RIGHT)

        vector2 = Arrow(np.array([-1,2,0]), np.array([-2,-2,0]), color = RED_C, buff = 0.01, tip_length = 0.25)
        

        vector_valued_function = TextMobject("Vector Valued Function").move_to(2.5*UP+3*LEFT).set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)


        self.play(ShowCreation(numberplane))
        self.wait()
        self.play(ShowCreation(rectangle), ShowCreation(eqn))
        self.wait()
        self.play(ShowCreation(dot1), ShowCreation(number1))
        self.wait(0.5)
        self.play(ApplyMethod(number1.move_to, 2.5*UP+ 3.5*RIGHT))
        self.wait(0.5)
        self.play(FadeOut(number1))
        self.wait(0.5)
        self.play(ShowCreation(output1))
        self.wait(0.5)
        self.play(ShowCreation(vector1))
        self.wait(0.5)
        self.play(ApplyMethod(output1.move_to, 1*UP+ 4.5*RIGHT))
        self.wait()
        

        self.play(ShowCreation(dot2), ShowCreation(number2))
        self.wait(0.5)
        self.play(ApplyMethod(number2.move_to, 2.5*UP+ 3.5*RIGHT))
        self.wait(0.5)
        self.play(FadeOut(number2))
        self.wait(0.5)
        self.play(ShowCreation(output2))
        self.wait(0.5)
        self.play(ShowCreation(vector2))
        self.wait(0.5)
        self.play(ApplyMethod(output2.move_to, 2*DOWN+ 2.5*LEFT))
        self.wait()
        self.play(Write(vector_valued_function))
        self.wait(2)

