from manimlib.imports import *
class LinearTrans(LinearTransformationScene,MovingCameraScene):
        CONFIG = {
        "basis_vector_stroke_width": 1,
        "leave_ghost_vectors": True,
        }

        def setup(self):
            LinearTransformationScene.setup(self)
            MovingCameraScene.setup(self)
        
        def construct(self):
            self.setup()
            self.camera_frame.save_state()
            self.play(self.camera_frame.set_width, 7)
            matrix = [[0.866,-0.5],[0.5,0.866]]
            self.apply_matrix(matrix)
            arc1 = Arc(radius = 0.25,angle=TAU/12)
            arc2 = Arc(radius = 0.25,angle=TAU/12,start_angle=TAU/4)
            text1 = TextMobject(r"$\theta$")
            text1.scale(0.5)
            text1.move_to(0.5*UP+0.125*LEFT)
            text2 = TextMobject(r"$\theta$")
            text2.scale(0.5)
            text2.move_to(0.5*RIGHT+0.125*UP)
            self.play(ShowCreation(arc1),ShowCreation(arc2),Write(text1),Write(text2),run_time=1)
            self.wait()
