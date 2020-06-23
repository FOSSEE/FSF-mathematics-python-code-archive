from manimlib.imports import *

class Examples(GraphScene):
    def construct(self):
       
        rectangle = Rectangle(height = 3, width = 4, color = GREEN)
        square = Square(side_length = 5, color = PURPLE)
        circle = Circle(radius = 2, color = PINK)
        radius = Line(ORIGIN,2*RIGHT)
        
        radius.set_color(RED)

        rectangle_area_func = TextMobject(r"$Area = f(Length, Breadth)$")
        rectangle_area_func.scale(0.6)
        square_area_func = TextMobject(r"$Area = f(Length)$")
        circle_area_func = TextMobject(r"$Area = f(r)$")


        rectangle_area = TextMobject(r"$Area = Length \times Breadth$")
        rectangle_area.scale(0.6)
        square_area = TextMobject(r"$Area = Length^2$")
        circle_area = TextMobject(r"$Area = \pi r^2$")

        braces_rect1 = Brace(rectangle, LEFT)
        eq_text1 = braces_rect1.get_text("Length")
        braces_rect2 = Brace(rectangle, UP)
        eq_text2 = braces_rect2.get_text("Breadth")

        braces_square = Brace(square, LEFT)
        braces_square_text = braces_square.get_text("Length")

        radius_text = TextMobject("r")
        radius_text.next_to(radius,UP)

        

        self.play(ShowCreation(rectangle))
        self.wait(1)
        self.play(GrowFromCenter(braces_rect1),Write(eq_text1),GrowFromCenter(braces_rect2),Write(eq_text2))
        self.wait(1)
        self.play(Write(rectangle_area_func))
        self.wait(1)
        self.play(Transform(rectangle_area_func, rectangle_area))
        self.wait(1)
        self.play(FadeOut(braces_rect1),FadeOut(eq_text1),FadeOut(braces_rect2),FadeOut(eq_text2),FadeOut(rectangle_area_func))


        self.play(Transform(rectangle, square))
        self.wait(1)
        self.play(GrowFromCenter(braces_square),Write(braces_square_text))
        self.wait(1)
        self.play(Write(square_area_func))
        self.wait(1)
        self.play(Transform(square_area_func, square_area))
        self.wait(1)
        self.play(FadeOut(braces_square),FadeOut(braces_square_text),FadeOut(square_area_func))


        self.play(Transform(rectangle, circle))
        self.wait(1)
        self.play(ShowCreation(radius),Write(radius_text))
        self.wait(1)
        self.play(FadeOut(radius_text),FadeOut(radius))
        self.wait(1)
        self.play(Write(circle_area_func))
        self.wait(1)
        self.play(Transform(circle_area_func, circle_area))
        self.wait(1)
        self.play(FadeOut(circle_area_func))