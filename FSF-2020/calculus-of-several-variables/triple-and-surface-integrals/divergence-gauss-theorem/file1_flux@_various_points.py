from manimlib.imports import *
def pendulum_vector_field_func(point):
    #theta, omega = point[:2]
    return np.array([
        5*point[2]+point[1],
        3*point[0]+3*point[1],
        0,
    ])
class SimpleField(Scene):
    CONFIG = {
        #"func": cylinder_flow_vector_field,
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
        # self.initialize_vector_field()

        c1=Circle(radius=3,color=RED)
        field = self.vector_field
        self.play(c1)
        self.play(ShowCreation(field), run_time=10)
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
