from manimlib.imports import *

class Helix(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() # creates a 3D Axis

        helix1=ParametricFunction(
                lambda u : np.array([
                1.5*np.cos(u),
                1.5*np.sin(u),
                u/4
            ]),color=PURPLE,t_min=-TAU,t_max=TAU,
            )

        helix2=ParametricFunction(
                lambda u : np.array([
                2*np.cos(u),
                2*np.sin(u),
                u/2
            ]),color=GREEN_C,t_min=-TAU,t_max=TAU,
            )

        function = TexMobject("f(", "r", ",", "\\theta", ")", "=", "[", "r", "\\cos", "\\theta", ",", "r", "\\sin" ,"\\theta", ",", "h" ,"\\theta", "]" ).scale(0.6).to_corner(UL)
        function.set_color_by_tex(r"\theta", BLUE_C)
        function.set_color_by_tex(r"r", RED_C)
        function.set_color_by_tex(r"\cos", GREEN_C)
        function.set_color_by_tex(r"\sin", YELLOW_C)
        function[0].set_color(ORANGE)
        function[4].set_color(ORANGE)


        self.add_fixed_in_frame_mobjects(function)

        self.set_camera_orientation(phi=60*DEGREES, theta = 45*DEGREES)

        self.add(axes)

        axis = TextMobject(r"X",r"Y",r"Z")
        axis[0].move_to(6*RIGHT)
        axis[1].move_to(6*UP)
        axis[2].move_to(np.array([0,0,3.7]))

        self.add_fixed_orientation_mobjects(axis[2])
        self.add_fixed_orientation_mobjects(axis[0])
        self.add_fixed_orientation_mobjects(axis[1])


        dot1 = Dot().rotate(PI/2).set_color(RED_C)
        alpha1 = ValueTracker(0)
        vector1 = self.get_vector(alpha1.get_value(),helix1)
        dot1.add_updater(lambda m: m.move_to(vector1.get_end()))
        self.play(
            ShowCreation(helix1),
            GrowFromCenter(dot1),
            GrowArrow(vector1)
            )
        vector1.add_updater(
            lambda m: m.become(
                    self.get_vector(alpha1.get_value()%1,helix1)
                )
            )
        self.add(vector1,dot1)
        self.play(alpha1.increment_value, 1, run_time=10, rate_func=linear)
        

        self.play(FadeOut(vector1), FadeOut(dot1))
        self.play(ReplacementTransform(helix1, helix2))


        dot2 = Dot().rotate(PI/2).set_color(RED_C)
        alpha2 = ValueTracker(0)
        vector2 = self.get_vector(alpha2.get_value(),helix2)
        dot2.add_updater(lambda m: m.move_to(vector2.get_end()))
        self.play(
            ShowCreation(helix2),
            GrowFromCenter(dot2),
            GrowArrow(vector2)
            )
        vector2.add_updater(
            lambda m: m.become(
                    self.get_vector(alpha2.get_value()%1,helix2)
                )
            )
        self.add(vector2,dot2)
        self.play(alpha2.increment_value, 1, run_time=10, rate_func=linear)
        self.wait()



    def get_vector(self, proportion, curve):
        vector = Line(np.array([0,0,0]), curve.point_from_proportion(proportion), color = YELLOW_C, buff=0)
        return vector