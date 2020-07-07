from manimlib.imports import *

class Linear(GraphScene):
    CONFIG = {
    "x_min": -5,
    "x_max": 5,
    "y_min": -5,
    "y_max": 5,
    "graph_origin": ORIGIN,
    "x_labeled_nums": list(range(-5, 6)),
    "y_labeled_nums": list(range(-5, 6)),
    "x_axis_width": 7,
    "y_axis_height": 7,
    }
    def construct(self):
        
        text = TextMobject("T(x,y) = T(x+y,y)")
        text.scale(0.75)
        text.set_color(PURPLE)
        text.move_to(3*UP+5*LEFT)
        self.play(Write(text))

        XTD = self.x_axis_width/(self.x_max- self.x_min)
        YTD = self.y_axis_height/(self.y_max- self.y_min)

        self.setup_axes(animate = True)

        text1 = TextMobject("Before Linear Transformation")
        text1.scale(0.6)
        text1.move_to(UP*3+3*RIGHT)

        a = TextMobject("(1,1)")
        b = TextMobject("(3,1)")
        c = TextMobject("(3,2)")
        d = TextMobject("(1,2)")
        a.scale(0.5)
        b.scale(0.5)
        c.scale(0.5)
        d.scale(0.5)
        a.move_to(self.graph_origin+0.6*UP+0.6*RIGHT)
        b.move_to(self.graph_origin+0.6*UP+3.4*RIGHT)
        c.move_to(self.graph_origin+2.4*UP+3.4*RIGHT)
        d.move_to(self.graph_origin+2.6*UP+0.6*RIGHT)

        square = Polygon(self.graph_origin+UP+RIGHT,self.graph_origin+UP+3*RIGHT,self.graph_origin+2*UP+3*RIGHT,self.graph_origin+2*UP+RIGHT)
        
        self.play(Write(text1), Write(a), Write(b), Write(c), Write(d), ShowCreation(square))
        self.wait(2)
        self.play(FadeOut(text1), FadeOut(a), FadeOut(b), FadeOut(c), FadeOut(d), ApplyMethod(square.apply_matrix,[[1,1],[0,1]]))

        a = TextMobject("(2,1)")
        b = TextMobject("(4,1)")
        c = TextMobject("(3,2)")
        d = TextMobject("(5,2)")
        a.scale(0.5)
        b.scale(0.5)
        c.scale(0.5)
        d.scale(0.5)
        a.move_to(self.graph_origin+0.6*UP+1.6*RIGHT)
        b.move_to(self.graph_origin+0.6*UP+4.4*RIGHT)
        d.move_to(self.graph_origin+2.4*UP+5.4*RIGHT)
        c.move_to(self.graph_origin+2.4*UP+2.6*RIGHT)

        text1 = TextMobject("After Linear Transformation")
        text1.scale(0.6)
        text1.move_to(UP*3+3*RIGHT)

        self.play(Write(text1), Write(a), Write(b), Write(c), Write(d))
        
        self.wait(2)

class grid(LinearTransformationScene):
    def construct(self):

        text = TextMobject("Now, consider all the vectors.")
        text.scale(0.75)
        text.set_color(PURPLE)
        text.move_to(2.5*UP+3*LEFT)
        self.play(Write(text))

        text1 = TextMobject("Before Linear Transformation")
        text1.scale(0.6)
        text1.move_to(UP*3.5+3.5*RIGHT)

        square = Polygon(UP+RIGHT,UP+3*RIGHT,2*UP+3*RIGHT,2*UP+RIGHT)
        square.set_color(YELLOW)
        
        self.play(Write(text1), ShowCreation(square))
        self.wait(2)
        self.play(FadeOut(text1))
        self.add_transformable_mobject(square)

        text1 = TextMobject("After Linear Transformation")
        text1.scale(0.6)
        text1.move_to(UP*3.5+3.5*RIGHT)

        matrix = [[1,1],[0,1]]

        self.apply_matrix(matrix)
        self.play(Write(text1))
        
        self.wait()

class grid2(LinearTransformationScene):
    CONFIG = {
    "include_background_plane": True,
    "include_foreground_plane": False,
    "show_coordinates": True,
    "show_basis_vectors": True,
    "basis_vector_stroke_width": 3,
    "i_hat_color": X_COLOR,
    "j_hat_color": Y_COLOR,
    "leave_ghost_vectors": True,
    }

    def construct(self):

        text = TextMobject("Now, let us focus only on the standard basis")
        text.scale(0.7)
        text.set_color(PURPLE)
        text.move_to(2.5*UP+3.5*LEFT)
        self.play(Write(text))

        text1 = TextMobject("Before Linear Transformation")
        text1.scale(0.6)
        text1.move_to(UP*3.5+3.5*RIGHT)

        square = Polygon(UP+RIGHT,UP+3*RIGHT,2*UP+3*RIGHT,2*UP+RIGHT)
        square.set_color(YELLOW)
        
        self.play(Write(text1), ShowCreation(square))
        self.wait(2)
        self.play(FadeOut(text1))
        self.add_transformable_mobject(square)

        text1 = TextMobject("After Linear Transformation")
        text1.scale(0.6)
        text1.move_to(UP*3.5+3.5*RIGHT)

        matrix = [[1,1],[0,1]]

        self.apply_matrix(matrix)
        self.play(Write(text1))

        self.play(FadeOut(square), FadeOut(text1))
        
        cor_x = TextMobject("(1,0)")
        cor_y = TextMobject("(1,1)")
        cor_x.scale(0.65)
        cor_y.scale(0.65)
        cor_y.move_to(1.25*RIGHT+1.5*UP)
        cor_x.move_to(0.75*RIGHT-0.5*UP)
        cor_x.set_color(GREEN)
        cor_y.set_color(RED)
        
        x_cor = TextMobject(r"$\left[\begin{array}{c} 1\\0\end{array}\right]$")
        x_cor.set_color(GREEN)
        x_cor.scale(0.5)
        y_cor = TextMobject(r"$\left[\begin{array}{c} 1\\1\end{array}\right]$")
        x_cor.move_to(0.75*RIGHT-0.5*UP)
        y_cor.move_to(1.25*RIGHT+1.5*UP)
        y_cor.set_color(RED)
        y_cor.scale(0.5)

        text1 = TextMobject(r"$T(\left[\begin{array}{c} x\\y \end{array}\right]) = $",r"$\left[\begin{array}{c} x+y\\y \end{array}\right]$")
        text1.scale(0.7)
        text1.set_color(PURPLE)
        text1.move_to(1.5*UP+3*LEFT)

        text = TextMobject(r"$T(x,y) = (x+y,y)$")
        text.scale(0.6)
        text.set_color(PURPLE)
        text.move_to(1.5*UP+3*LEFT)

        self.play(FadeIn(text),FadeIn(cor_x), FadeIn(cor_y))
        self.wait()

        self.play(Transform(text,text1), Transform(cor_x,x_cor), Transform(cor_y,y_cor))

        text3 = TextMobject(r"$\left[\begin{array}{c} x+y\\y \end{array}\right]$")
        text3.scale(0.7)
        text3.set_color(PURPLE)
        text3.move_to(1.5*DOWN+5*LEFT)

        equal = TextMobject("=")
        equal.move_to(1.5*DOWN+3.5*LEFT)

        text3 = TextMobject("[")
        text4 = TextMobject(r"$\begin{array}{c} (1)x\\(0)x \end{array}$")
        text5 = TextMobject(r"$\begin{array}{c} + \\ + \end{array}$")
        text6 = TextMobject(r"$\begin{array}{c} (1)y\\(1)y \end{array}$")
        text7 = TextMobject("]")
        text3.scale(2)
        text4.scale(0.7)
        text5.scale(0.7)
        text6.scale(0.7)
        text7.scale(2)
        text4.set_color(GREEN)
        text5.set_color(PURPLE)
        text6.set_color(RED)
        text3.move_to(1.5*DOWN+3*LEFT)
        text4.move_to(1.5*DOWN+2.5*LEFT)
        text5.move_to(1.5*DOWN+2*LEFT)
        text6.move_to(1.5*DOWN+1.5*LEFT)
        text7.move_to(1.5*DOWN+1*LEFT)

        text1[1].scale(1.2)
        self.play(FadeOut(text1[0]), ApplyMethod(text1[1].move_to,1.5*DOWN+5*LEFT), FadeIn(text3), FadeIn(equal), FadeIn(text4), FadeIn(text5), FadeIn(text6), FadeIn(text7))

        self.wait()
        self.play(FadeOut(text1[1]))
        
        self.play(ApplyMethod(text3.move_to,1.5*DOWN+6*LEFT),
        ApplyMethod(text4.move_to,1.5*DOWN+5.5*LEFT),
        ApplyMethod(text5.move_to,1.5*DOWN+5*LEFT),
        ApplyMethod(text6.move_to,1.5*DOWN+4.5*LEFT),
        ApplyMethod(text7.move_to,1.5*DOWN+4*LEFT))
        
        text10 = TextMobject("[")
        text11 = TextMobject(r"$\begin{array}{c} 1\\0 \end{array}$")
        text13 = TextMobject(r"$\begin{array}{c} 1\\1 \end{array}$")
        text14 = TextMobject("]")
        text10.scale(2)
        text11.scale(0.7)
        text13.scale(0.7)
        text14.scale(2)
        text11.set_color(GREEN)
        text13.set_color(RED)
        text10.move_to(1.5*DOWN+3*LEFT)
        text11.move_to(1.5*DOWN+2.75*LEFT)
        text13.move_to(1.5*DOWN+2.25*LEFT)
        text14.move_to(1.5*DOWN+2*LEFT)

        self.play(FadeIn(text10), Transform(x_cor,text11), Transform(y_cor,text13), FadeIn(text14))

        text15 = TextMobject(r"$\left[\begin{array}{c} x\\y \end{array}\right]$")
        text15.scale(0.7)
        text15.set_color(PURPLE)
        text15.move_to(1.5*DOWN+1.5*LEFT)

        self.play(FadeIn(text15))
        self.play(FadeOut(text3), FadeOut(text4), FadeOut(text5), FadeOut(text7), FadeOut(text6))

        text1[0].scale(1.2)
        self.play(ApplyMethod(text1[0].move_to,1.5*DOWN+4.5*LEFT), FadeOut(equal))
        self.wait(2)