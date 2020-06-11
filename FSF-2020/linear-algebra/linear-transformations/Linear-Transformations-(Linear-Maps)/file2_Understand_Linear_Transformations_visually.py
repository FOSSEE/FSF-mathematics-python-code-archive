from manimlib.imports import *

class Rotation(GraphScene):
    CONFIG = {
        "x_min" : -5,
        "x_max" : 5,
        "y_min" : -5,
        "y_max" : 5,
        "graph_origin" : ORIGIN+3.5*LEFT,
        "x_axis_width" : 7,
        "y_axis_height" : 7
        #"x_labeled_nums" : list(range(-5,6)),
        #"y_labeled_nums" : list(range(-5,6)),
    }

    def construct(self):
        XTD = self.x_axis_width/(self.x_max-self.x_min)
        YTD = self.y_axis_height/(self.y_max-self.y_min)

        introText = TextMobject("Understanding Linear Transformations")
        self.play(Write(introText))
        self.wait(1)
        
        introText1 = TextMobject("Visually ... ")
        introText1.move_to(DOWN)
        self.play(Write(introText1))
        self.wait(1)
        self.play(FadeOut(introText), FadeOut(introText1))

        Text1 = TextMobject("Let $\overrightarrow{v}$ be $2\hat{i}+3\hat{j}$")
        Text2 = TextMobject("$\overrightarrow{v} = 2\hat{i}+3\hat{j}$")

        Text1.move_to(4*RIGHT+2*UP)
        Text2.move_to(4*RIGHT+1*UP)
        self.play(Write(Text1))
        self.wait()
        self.play(Transform(Text1,Text2))
        
        self.setup_axes(animate=True)
        arrow_v = Arrow(stroke_width = 3, start = self.graph_origin + 0.15*LEFT + 0.25*DOWN, end = self.graph_origin+2*XTD*RIGHT+3*YTD*UP+ 0.15*RIGHT + 0.25*UP)
        self.play(ShowCreation(arrow_v))
 
        Text_i = TextMobject("$\hat{i}$")
        Text_i.move_to(self.graph_origin+0.5*XTD*RIGHT+0.5*YTD*DOWN)
        Text_i.scale(0.75)
        Text_j = TextMobject("$\hat{j}$")
        Text_j.move_to(self.graph_origin+0.5*XTD*LEFT+0.5*YTD*UP)
        Text_j.scale(0.75)
 
        arrow_i = Arrow(stroke_width = 3, start = self.graph_origin + 0.25*LEFT, end = self.graph_origin+1*XTD*RIGHT+ 0.25*RIGHT)
        arrow_j = Arrow(stroke_width = 3, start = self.graph_origin + 0.25*DOWN, end = self.graph_origin+1*YTD*UP+0.25*UP)
        self.play(ShowCreation(arrow_i), ShowCreation(arrow_j), Write(Text_i), Write(Text_j))

        Text_2i = TextMobject("$2\hat{i}$")
        Text_2i.move_to(self.graph_origin+1*XTD*RIGHT+1*YTD*DOWN)
        Text_3j = TextMobject("$3\hat{j}$")
        Text_3j.move_to(self.graph_origin+1*XTD*LEFT+1.5*YTD*UP)

        arrow_2i = Arrow(stroke_width = 3, start = self.graph_origin + 0.25*LEFT, end = self.graph_origin+2*XTD*RIGHT+ 0.25*RIGHT)
        arrow_2i.set_color(YELLOW)
        arrow_3j = Arrow(stroke_width = 3, start = self.graph_origin + 0.25*DOWN, end = self.graph_origin+3*YTD*UP+0.25*UP)
        arrow_3j.set_color(RED)
        self.wait(0.5)
        self.play(Transform(arrow_i,arrow_2i), Transform(arrow_j,arrow_3j), Transform(Text_i,Text_2i), Transform(Text_j,Text_3j))
        self.play(ApplyMethod(arrow_j.move_to,self.graph_origin+2*XTD*RIGHT+1.5*YTD*UP) , ApplyMethod(Text_j.move_to,self.graph_origin+2.5*XTD*RIGHT+1.5*YTD*UP+ 0.15*RIGHT + 0.25*UP))

        new_Text_v = TextMobject("$\overrightarrow{v}$")
        new_Text_v.move_to(self.graph_origin+0.5*XTD*RIGHT+1.5*YTD*UP)
        self.play(Write(new_Text_v))

        new_arrow_i = Arrow(stroke_width = 3, start = self.graph_origin + 0.25*LEFT, end = self.graph_origin+1*XTD*RIGHT+ 0.25*RIGHT)
        new_arrow_i.set_color(YELLOW)
        new_arrow_j = Arrow(stroke_width = 3, start = self.graph_origin + 0.25*DOWN, end = self.graph_origin+1*YTD*UP+0.25*UP)
        new_arrow_j.set_color(RED)

        new_Text_i = TextMobject("$\hat{i}$")
        new_Text_i.move_to(self.graph_origin+0.5*XTD*RIGHT+0.5*YTD*DOWN)
        new_Text_i.scale(0.75)
        new_Text_j = TextMobject("$\hat{j}$")
        new_Text_j.move_to(self.graph_origin+0.5*XTD*LEFT+0.5*YTD*UP)
        new_Text_j.scale(0.75)
        
        self.wait(1)

        self.play(FadeOut(Text_i),
        FadeOut(Text_j),
        FadeOut(arrow_i),
        FadeOut(arrow_j),
        ShowCreation(new_arrow_i),
        ShowCreation(new_arrow_j),
        Write(new_Text_i),
        Write(new_Text_j))

        self.play(ApplyMethod(Text1.move_to,4*RIGHT))
        Text3 = TextMobject("Let the be a linear transformation function")
        Text3.scale(0.5)
        Text4 = TextMobject("$T$ which rotates the vectors by angle of $90^{\circ}$")
        Text4.scale(0.5)
        Text3.move_to(4*RIGHT+3*UP)
        Text4.move_to(4*RIGHT+2.5*UP)
        self.play(Write(Text3), Write(Text4))
        self.wait(2)
        
        Text6 = TextMobject(r"$\begin{pmatrix} 1 \\ 0 \end{pmatrix}$")
        Text6.scale(0.75)
        Text6.set_color(YELLOW)
        Text6.move_to(self.graph_origin+1*XTD*RIGHT+1*YTD*DOWN)
        Text7 = TextMobject(r"$\begin{pmatrix} 0 \\ 1 \end{pmatrix}$")
        Text7.scale(0.75)
        Text7.set_color(RED)
        Text7.move_to(self.graph_origin+1*XTD*LEFT+1*YTD*UP)

        self.play(Transform(new_Text_i,Text6))
        self.play(Transform(new_Text_j,Text7))

        Text5 = TextMobject(r"$\overrightarrow{v} = 2 $", r"$\begin{pmatrix} 1 \\ 0 \end{pmatrix}$", r"+3", r"$\begin{pmatrix} 0 \\ 1 \end{pmatrix}$")
        Text5[1].set_color(YELLOW)
        Text5[3].set_color(RED)
        Text5.move_to(4*RIGHT)
        
        self.play(Transform(Text1, Text5))
        self.wait()

        arrow_modified_i = Arrow(stroke_width = 3, start = self.graph_origin + 0.25*UP, end = self.graph_origin-(1*YTD*UP+0.25*UP))
        arrow_modified_i.set_color(YELLOW)
        arrow_modified_j = Arrow(stroke_width = 3, start = self.graph_origin + 0.25*LEFT, end = self.graph_origin+1*XTD*RIGHT+ 0.25*RIGHT)
        arrow_modified_j.set_color(RED)
        
        yellow_i = TextMobject(r"$\begin{pmatrix} 0 \\ -1 \end{pmatrix}$")
        yellow_i.set_color(YELLOW).scale(0.75)
        yellow_i.move_to(self.graph_origin + 1*XTD*DOWN + 1*YTD*LEFT)

        red_j = TextMobject(r"$\begin{pmatrix} 1 \\ 0 \end{pmatrix}$")
        red_j.set_color(RED).scale(0.75)
        red_j.move_to(self.graph_origin + 1*XTD*UP + 1*YTD*RIGHT)

        Text8 = TextMobject(r"$\overrightarrow{v}_{transformed} = 2 $", r"$\begin{pmatrix} 0 \\ -1 \end{pmatrix}$", r"+3", r"$\begin{pmatrix} 1 \\ 0 \end{pmatrix}$")
        Text8[1].set_color(YELLOW)
        Text8[3].set_color(RED)
        Text8.move_to(4*RIGHT+1.5*DOWN)
        Text8.scale(0.75)

        new_Text__v = TextMobject("$\overrightarrow{v}_{transformed}$")
        new_Text__v.scale(0.75)
        arrow_modified_v = Arrow(stroke_width = 3, start = self.graph_origin + 0.25*LEFT + 0.15*UP, end = self.graph_origin+2*XTD*DOWN+3*YTD*RIGHT+ 0.15*DOWN + 0.25*RIGHT)
        self.play(Transform(arrow_v, arrow_modified_v), 
        Transform(new_arrow_i, arrow_modified_i), 
        Transform(new_arrow_j, arrow_modified_j),
        Transform(new_Text_i,yellow_i),
        Transform(new_Text_j,red_j),
        FadeOut(new_Text_v),
        ApplyMethod(new_Text__v.move_to,self.graph_origin+3*XTD*RIGHT+0.5*YTD*DOWN),
        Write(Text8))

        self.play(FadeOut(Text1), FadeOut(Text3), FadeOut(Text4), ApplyMethod(Text8.move_to,4*RIGHT+3*UP))
        
        Text9 = TextMobject(r"$\overrightarrow{v}_{transformed} = 2 $", r"$\hat{i}_{transformed}$", r"+3", r"$\hat{j}_{transformed}$")
        Text9[1].set_color(YELLOW)
        Text9[3].set_color(RED)
        Text9.move_to(4*RIGHT+2*UP)
        Text9.scale(0.5)

        self.play(Write(Text9))

        v_transformed = TextMobject(r"$\overrightarrow{v}_{transformed} \equiv T(\overrightarrow{v})$")
        v_transformed.scale(0.75).move_to(4*RIGHT+UP)
        i_transformed = TextMobject(r"$\hat{i}_{transformed} \equiv T(\hat{i})$")
        i_transformed.set_color(YELLOW).scale(0.75).move_to(4*RIGHT)
        j_transformed = TextMobject(r"$\hat{v}_{transformed} \equiv T(\hat{j})$")
        j_transformed.set_color(RED).scale(0.75).move_to(4*RIGHT+DOWN)

        self.play(Write(v_transformed), Write(i_transformed), Write(j_transformed))
        self.wait(3)

        Text10 = TextMobject(r"$T(\overrightarrow{v}) = $", r"$\begin{pmatrix} 3 \\ -2 \end{pmatrix}$")
        Text10[1].set_color(BLUE_E)
        Text10.move_to(4*RIGHT+1*UP)
        Text10.scale(0.75)

        self.play(Write(Text10), ApplyMethod(v_transformed.move_to,4*RIGHT+2*UP), FadeOut(i_transformed), FadeOut(j_transformed), FadeOut(Text9))
        self.wait(1)

        self.play(FadeOut(self.axes), 
        FadeOut(arrow_v), 
        FadeOut(new_arrow_i), 
        FadeOut(new_arrow_j), 
        FadeOut(new_Text_i), 
        FadeOut(new_Text_i), 
        FadeOut(new_Text_j), 
        FadeOut(new_Text__v), 
        FadeOut(Text10), 
        FadeOut(v_transformed),
        FadeOut(Text8))
