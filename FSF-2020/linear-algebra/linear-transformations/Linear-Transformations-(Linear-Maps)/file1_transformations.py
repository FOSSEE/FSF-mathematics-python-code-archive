from manimlib.imports import *

class text(Scene):
    def construct(self):
        text1 = TextMobject("For a grid, undergoing a linear transformation, all it's straight lines")
        text1.scale(0.9)
        text2 = TextMobject("must either remain straight lines or sends to a point in the grid formed")
        text2.scale(0.9)
        text3 = TextMobject("Origin must remains where it was before transformation.")
        text3.scale(0.9)
        text1.move_to(ORIGIN+UP)
        text2.move_to(ORIGIN)
        text3.move_to(ORIGIN+DOWN)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait()
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3))

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
        # I have taken reference from purusharth's code
        NonLinearTrans = lambda coordinates : coordinates + np.array([np.sin(coordinates[1]),np.sin(coordinates[0]),0,])
        grid.prepare_for_nonlinear_transform()
        self.play(grid.apply_function,NonLinearTrans)
        text = TextMobject("While, this is not a","Linear Trasformation")
        text[0].move_to(DOWN+4*LEFT)
        text[1].move_to(1.5*DOWN+4*LEFT)
        text.add_background_rectangle()
        self.play(Write(text))
        self.wait()
        
class MoveOrigin(LinearTransformationScene):

    CONFIG = {
        "show_basis_vectors": False,
    }
    def construct(self):
        self.wait()

        dot = Dot(ORIGIN, color = YELLOW)
        self.add_transformable_mobject(dot)
        self.apply_nonlinear_transformation(self.func)
        text = TextMobject("This is also not a linear transformation as the origin moves from its original position")
        text.move_to(2*DOWN)
        text.scale(0.5)
        text.set_color(YELLOW)
        text.add_background_rectangle()
        self.play(Write(text))
        self.wait()

    def func(self, point):
        matrix_transform = self.get_matrix_transformation([[1, -1], [1, 1]])
        return matrix_transform(point) + UP+ RIGHT
