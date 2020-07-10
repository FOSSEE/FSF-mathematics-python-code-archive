from manimlib.imports import *
def pendulum_vector_field_func(point):
    #theta, omega = point[:2]
    return np.array([
        point[0],
        point[1],
        point[2],
    ])
class F2D(Scene):
    CONFIG = {
        # "func": cylinder_flow_vec or_field,
        "flow_time": 5,
    }
    def initialize_vector_field(self):
        self.vector_field = VectorField(
            pendulum_vector_field_func,
        )
        self.vector_field.sort(get_norm)
    def construct(self):
        # plane = NumberPlane(color=RED)
        # plane.add(plane.get_axis_labels()) 
        # self.add(plane)  
        self.initialize_vector_field()

        field = self.vector_field
        c1=Circle(radius=3,color=BLUE)
        self.play(ShowCreation(field), run_time=7)
        self.play(ShowCreation(c1))
        self.wait(3)
        lines = StreamLines(
            pendulum_vector_field_func,
            virtual_time=3,
            min_magnitude=0,
            max_magnitude=2,
        )
        self.add(AnimatedStreamLines(
            lines,
            line_anim_class=ShowPassingFlash
        ))
        self.wait(2)
        phase_point = VectorizedPoint(1*UP+1*RIGHT)
        self.add(move_along_vector_field(phase_point, pendulum_vector_field_func))
        self.wait(2)
