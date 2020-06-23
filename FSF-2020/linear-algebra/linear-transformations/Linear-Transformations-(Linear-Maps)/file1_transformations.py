from manimlib.imports import *

class text(Scene):
    def construct(self):
        text1 = TextMobject("For a grid, undergoing a linear transformation, all it's straight lines")
        text1.scale(0.9)
        text2 = TextMobject("must either remain straight lines or sends to a point in the grid formed")
        text2.scale(0.9)
        text1.move_to(ORIGIN+UP)
        text2.move_to(ORIGIN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.wait()
        self.play(FadeOut(text1),FadeOut(text2))

class LinearTransformation(LinearTransformationScene):
    CONFIG = {
    "basis_vector_stroke_width": 3,
    "leave_ghost_vectors": True,
    }

    def construct(self):
        self.setup()
        matrix = [[0.866,-0.5],[0.5,0.866]]
        self.apply_matrix(matrix)
        text = TextMobject("This is a Linear","Trasformation")
        text[0].move_to(DOWN+4*LEFT)
        text[1].move_to(1.5*DOWN+4*LEFT)
        text.add_background_rectangle()
        self.play(Write(text))
        self.wait()

class NonLinearTransformation(Scene):
    def construct(self):
        grid = NumberPlane()
        self.play(ShowCreation(grid),run_time =2)
        NonLinearTrans = lambda coordinates : coordinates + np.array([np.sin(coordinates[1]),np.sin(coordinates[0]),0,])
        grid.prepare_for_nonlinear_transform()
        self.play(grid.apply_function,NonLinearTrans)
        text = TextMobject("While, this is not a","Linear Trasformation")
        text[0].move_to(DOWN+4*LEFT)
        text[1].move_to(1.5*DOWN+4*LEFT)
        text.add_background_rectangle()
        self.play(Write(text))
        self.wait()