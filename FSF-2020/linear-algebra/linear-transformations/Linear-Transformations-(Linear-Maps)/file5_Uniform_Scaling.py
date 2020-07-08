from manimlib.imports import *

class Scaling(GraphScene):
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

        introText = TextMobject("Scaling")
        self.play(Write(introText))
        self.wait(1)
        self.play(FadeOut(introText))

        introText = TextMobject("Uniform Scaling")
        self.play(Write(introText))
        self.wait(1)
        self.play(FadeOut(introText))

        Text1 = TextMobject("Let $\overrightarrow{v}$ be $3\hat{i}+3\hat{j}$")
        Text2 = TextMobject("$\overrightarrow{v} = 3\hat{i}+3\hat{j}$")

        Text1.move_to(4*RIGHT+2*UP)
        Text2.move_to(4*RIGHT+1*UP)
        self.play(Write(Text1))
        self.wait()
        self.play(Transform(Text1,Text2))
        
        self.setup_axes(animate=True)
        arrow_v = Arrow(stroke_width = 4, start = self.graph_origin + 0.15*LEFT + 0.15*DOWN, end = self.graph_origin+3*XTD*RIGHT+3*YTD*UP+ 0.15*RIGHT + 0.15*UP)
        vector_v = TextMobject(r"$\vec{v}$")
        vector_v.move_to(self.graph_origin + 1*XTD*RIGHT + 2*YTD*UP )
        self.play(ShowCreation(arrow_v),Write(vector_v))
        scaling_factor = TextMobject(r"Scaling Factor = $\frac{4}{3}$")
        scaling_factor.scale(0.75)
        scaled_vector = TextMobject(r"$T(\vec{v}) = \frac{4}{3} \left[ \begin{array} {c} 3 \\ 3 \end{array} \right] = \left[ \begin{array} {c} 4 \\ 4 \end{array} \right]$")
        scaled_vector.set_color(DARK_BLUE)
        scaled_vector.scale(0.75)
        scaling_factor.move_to(4*RIGHT)
        scaled_vector.move_to(4*RIGHT+DOWN)
        self.play(Write(scaling_factor))
        self.wait()
        self.play(Write(scaled_vector))

        transformed_arrow_v = Arrow(stroke_width = 2, start = self.graph_origin + 0.15*LEFT + 0.15*DOWN, end = self.graph_origin+4*XTD*RIGHT+4*YTD*UP+ 0.15*RIGHT + 0.15*UP)
        transformed_arrow_v.set_color(DARK_BLUE)
        transformed_vector_v = TextMobject(r"$T(\vec{v})$")
        transformed_vector_v.move_to(self.graph_origin + 4.5*XTD*RIGHT + 4.5*YTD*UP )
        transformed_vector_v.set_color(DARK_BLUE)
        self.play(ShowCreation(transformed_arrow_v), Write(transformed_vector_v))

        self.wait()

        represent_text1 = TextMobject("Representation of scaling")
        represent_text2 = TextMobject("of vectors in point form")
        represent_text1.move_to(4*RIGHT+3*UP)
        represent_text2.move_to(4*RIGHT+2*UP)
        self.play(Write(represent_text1), Write(represent_text2))

        dot_init = Dot(self.graph_origin+3*XTD*RIGHT+3*YTD*UP)
        dot_trans = Dot(self.graph_origin+4*XTD*RIGHT+4*YTD*UP)
        
        self.play(ApplyMethod(vector_v.move_to,self.graph_origin+2.5*XTD*RIGHT+2.5*YTD*UP),
        ApplyMethod(transformed_vector_v.move_to,self.graph_origin+4.5*XTD*RIGHT+4.5*YTD*UP),
        ShowCreation(dot_init), 
        Transform(arrow_v,dot_init),
        Transform(transformed_arrow_v,dot_trans))

        self.wait(2)

        self.play(FadeOut(dot_init), 
        FadeOut(arrow_v), 
        FadeOut(transformed_arrow_v), 
        FadeOut(represent_text1), 
        FadeOut(represent_text2),  
        FadeOut(self.axes), 
        FadeOut(scaling_factor),
        FadeOut(scaled_vector),
        FadeOut(transformed_vector_v),
        FadeOut(vector_v),
        FadeOut(Text1))