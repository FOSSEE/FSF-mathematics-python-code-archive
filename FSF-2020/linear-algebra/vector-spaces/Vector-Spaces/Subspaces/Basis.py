from manimlib.imports import *


VECTORS = [[1, 2],
           [-4, 2],
           [-3, -3],
           [3,-2],
           [3,3],
           [-2,1],
           [-1,-3]]

class Scene1(LinearTransformationScene):
    
    CONFIG = {
        "include_background_plane": True,
        "include_foreground_plane": False,
        "show_coordinates": False,
        "show_basis_vectors": True,
        "basis_vector_stroke_width": 3,
        
    }
    def construct(self):
        self.setup()
        ihat, jhat = self.get_basis_vectors()
        labels = self.get_basis_vector_labels()
        self.add(ihat, jhat)
        self.add(*labels)
        
        self.show_vector_as_basis_sum()
        self.wait(2)

    def show_vector_as_basis_sum(self):
        text1 = TextMobject(r"Vector Space $\mathbb{R}^2$}").scale(0.8).shift(3*UP)
        text1.add_background_rectangle()
        self.play(ShowCreation(text1))
        text2 = TextMobject(r"$\mathbb{R}^2$",color=BLUE_E).scale(0.8).shift(6.5*LEFT+3.5*UP)
        text3 = TextMobject(r"\text{Basis Vectors:}",r"\text{$\hat{i}$}",r"\text{,}",r"\text{$\hat{j}$}").scale(0.7).shift(2*UP+2.5*RIGHT)
        text3[1].set_color(GREEN_C)
        text3[3].set_color(RED_C)

        self.wait(2)
        self.play(Transform(text1,text2))
        self.wait(1)
        self.play(ShowCreation(text3))
        self.wait(1.7)
        self.play(FadeOut(text3))

        for i in range(len(VECTORS)):
            v = self.add_vector(VECTORS[i], stroke_width = 3,color=YELLOW_D)

            linei = Line(start = ORIGIN, end = VECTORS[i][0]*RIGHT)
            linei.set_color(GREEN_C)
            linej = Line(start = linei.get_end(),
                         end = linei.get_end() + VECTORS[i][1]*UP)
            linej.set_color(RED_C)
            self.play(ShowCreation(linei))
            self.play(ShowCreation(linej))
            vlabel = self.get_vector_label(v, str(VECTORS[i][0]) +
                                           r"\imath" + "+" +
                                           str(VECTORS[i][1]) +
                                           r"\jmath", at_tip = True)
            self.play(ShowCreation(vlabel))
            
            self.play(FadeOut(linei),FadeOut(linej))
            self.wait(1)
            dot = Dot(v.get_end(), fill_color = v.get_stroke_color())
            self.play(ShowCreation(dot),FadeOut(v),FadeOut(vlabel))
            self.wait(0.3)

class Scene2(LinearTransformationScene):
    CONFIG = {
        "num_vectors" : 16,
        "start_color" : GREY,
        "end_color" : YELLOW_D,
        "include_background_plane": True,
        "include_foreground_plane": False,
    }

    def get_vectors(self):
        return [
            Vector([x, y], stroke_width = 3.5)
            for x in np.arange(-int(FRAME_X_RADIUS), int(FRAME_X_RADIUS)+0.5, 0.5)
            for y in np.arange(-int(FRAME_Y_RADIUS), int(FRAME_Y_RADIUS)+0.5, 0.5)
        ]

    def lock_in_faded_grid(self, dimness=0.7, axes_dimness=0.5):
        plane = self.add_plane()
        axes = plane.get_axes()
        plane.fade(dimness)
        axes.set_color(WHITE)
        axes.fade(axes_dimness)
        self.add(axes)

    def construct(self):
        self.lock_in_faded_grid()

        vectors = self.get_vectors()
        colors = Color(self.start_color).range_to(
            self.end_color, len(vectors)
        )
        for vect, color in zip(vectors, colors):
            vect.set_color(color)

        vector_group = VGroup(*vectors)
        self.play(
            ShowCreation(
                vector_group,
                run_time = 3
            )
        )

        self.wait(1)

        vectors.sort(key=lambda v: v.get_length())
        def v_to_dot(vector):
            return Dot(vector.get_end(), fill_color = vector.get_stroke_color())
        self.wait()
        rate_functions = [
            squish_rate_func(smooth, float(x)/(len(vectors)+2), 1)
            for x in range(len(vectors))
        ]
        self.play(*[
            Transform(v, v_to_dot(v), rate_func = rf, run_time = 3)
            for v, rf in zip(vectors, rate_functions)
        ])
        self.wait(2)
        self.play_final_animation(vectors, rate_functions)
        self.wait(2)

        text1 = TextMobject(" Basis is the minimum information required to ").shift(3.1*UP).scale(0.8)
        text2 = TextMobject("generate the whole space.").scale(0.8).shift(2.6*UP)
        
        text1.add_background_rectangle()
        text2.add_background_rectangle()
        
        

        self.play(ShowCreation(text1),ShowCreation(text2))
        
        self.play(ShowCreation(self.get_basis_vectors()))
        self.wait(3)

    def play_final_animation(self, vectors, rate_functions):

        h_line = Line(
            FRAME_X_RADIUS*RIGHT, FRAME_X_RADIUS*LEFT,
            stroke_width = 0.5,
            color = BLUE_E
        )
        v_line = Line(
            FRAME_Y_RADIUS*UP, FRAME_Y_RADIUS*DOWN,
            stroke_width = 0.5,
            color = BLUE_E
        )
        line_pairs = [
            VGroup(h_line.copy().shift(y), v_line.copy().shift(x))
            for v in vectors
            for x, y, z in [v.get_center()]
        ]
        plane = NumberPlane()
        
        self.play(
            ShowCreation(plane),
            *[
                Transform(v, p, rate_func = rf)
                for v, p, rf in zip(vectors, line_pairs, rate_functions)
            ]
        )
        self.remove(*vectors)

        
        

    