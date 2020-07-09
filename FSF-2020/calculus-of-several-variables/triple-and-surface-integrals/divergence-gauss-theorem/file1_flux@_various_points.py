from manimlib.imports import *
def pendulum_vector_field_func(point):
    #theta, omega = point[:2]
    return np.array([
        5*point[0]+point[1],
        3*point[1]+3*point[1],
        0,
    ])
class SF(Scene):
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

        A=TextMobject("The net flux through the green circular region is zero",tex_to_color_map={"green": GREEN})
        B=TextMobject("The net flux through the blue circular region is non-zero",tex_to_color_map={"blue": BLUE})

        c1=Circle(color=GREEN, radius=1.5)
        c1.shift(4*LEFT+2.2*UP)
        c2=Circle(color=BLUE, radius=1.5)
        



        self.play(ShowCreation(A))
        self.wait(0.5)
        self.play(ApplyMethod(A.shift, (0.8*UP+0.2*LEFT)))
        self.play(ShowCreation(B))
        # self.play(ApplyMethod(B.shift, (2*UP)))
        self.wait(2)
        self.play(FadeOut(A),FadeOut(B))
        self.initialize_vector_field()
        field = self.vector_field
        self.play(ShowCreation(field), run_time=4)
        self.play(ShowCreation(c1))
        self.play(ShowCreation(c2))
        self.wait(1)
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
