from manimlib.imports import *
import numpy as np


class Hills(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            number_line_config={
                "color": GREEN,
                "include_tip": False,
                "exclude_zero_from_default_numbers": True,
            }
        )
        self.add(axes)

        self.set_camera_orientation(phi=45*DEGREES,theta=45*DEGREES,distance=40)
        #self.begin_ambient_camera_rotation(rate=0.5)
        self.wait()

        cylinder_1 = ParametricSurface(
            lambda u, v: np.array([
            u,
            v,
            7*u*v/np.exp(u**2+v**2)
            ]),u_min=-3,u_max=3, v_min=-1,v_max=-0.95).set_color(YELLOW_E).rotate(PI/2).shift(LEFT).fade(0.5)
        cylinder = ParametricSurface(
            lambda u, v: np.array([
            u,
            v,
            7*u*v/np.exp(u**2+v**2)
            ]),u_min=-3,u_max=3, v_min=-3,v_max=3).set_color(YELLOW_E).rotate(PI/2).shift(LEFT).fade(0.5)     
        text_one = TexMobject(r"\textrm{Single variable functions slope up and down}")
        #name = TexMobject(r"\textrm{PROBE}").next_to(text_one, DOWN, buff = SMALL_BUFF).scale(0.7)
        text_one_a = TexMobject(r"\textrm{Position }", r" \rightarrow ").next_to(text_one, DOWN, buff = SMALL_BUFF)
        probe = Sphere(radius = 0.2).next_to(text_one_a, RIGHT).set_color(BLUE_E)
        text_one_b = TexMobject(r" \rightarrow ", r"\textrm{ slope }").next_to(probe, RIGHT, buff = SMALL_BUFF)
        name = TextMobject("PROBE").next_to(probe, DOWN, buff = SMALL_BUFF).scale(0.5)
        text = VGroup(text_one, text_one_a, probe, text_one_b, name).to_edge(UP+1.5*LEFT).scale(0.5)

        text_two = TexMobject(r"\textrm{Multivariable functions slope in infinitely many directions!}")
        #name_two = TexMobject(r"\textrm{PROBE2.0}").next_to(text_two, DOWN, buff = SMALL_BUFF).scale(0.7)
        text_two_a = TexMobject(r"\textrm{Position, Direction }", r" \rightarrow ").next_to(text_two, DOWN, buff = SMALL_BUFF)
        probe_two = Sphere(radius = 0.2).next_to(text_two_a, RIGHT).set_color(PURPLE_E)
        text_two_b = TexMobject(r" \rightarrow ", r"\textrm{ slope }").next_to(probe_two, RIGHT, buff = SMALL_BUFF)
        name_two = TextMobject("PROBE2.0").next_to(probe_two, DOWN, buff = SMALL_BUFF).scale(0.5)
        two = VGroup(text_two, text_two_a, probe_two, text_two_b, name_two).to_edge(UP+LEFT).scale(0.5).shift(3.5*LEFT)






        self.play(ShowCreation(cylinder_1))
        self.wait()
        self.add_fixed_in_frame_mobjects(text)
        self.wait(3.5)
        self.play(FadeOut(text))
        self.play(ReplacementTransform(cylinder_1, cylinder))
        self.wait()
        self.add_fixed_in_frame_mobjects(two)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(4)

class OneMore(ThreeDScene, GraphScene):
    def setup(self):
        GraphScene.setup(self)
        ThreeDScene.setup(self)

    def construct(self):
        axes = ThreeDAxes(
            number_line_config={
                "color": GREEN,
                "include_tip": False,
                "exclude_zero_from_default_numbers": True,
            }
        )
        self.add(axes)

        self.set_camera_orientation(phi=90*DEGREES,theta=90*DEGREES,distance=40)
        #self.begin_ambient_camera_rotation(rate=0.5)
        self.wait()

        shape = ParametricSurface(
            lambda u, v: np.array([
            u,
            v,
            2 - u**2 - v**2,
            ]),u_min=0,u_max =0.01, v_min=-2,v_max=2).set_color(GREEN_C)

        shape_A = ParametricSurface(
            lambda u, v: np.array([
            0*u,
            0,
            v,
            ]),u_min=-2,u_max = 2, v_min=-2,v_max=2).set_color(GREEN_C)


        '''
        path = self.get_graph(lambda u,v: np.array([
            u,
            2 - u**2 - v**2]), u_min=-2,u_max=2, v_min=-2,v_max=2)
        location = np.array([-2,-2, -2]) #location: Point
        dot = Dot(location)
        '''

        self.play(ShowCreation(shape))
        self.add(shape_A)
        #self.play(ShowCreation(path), ShowCreation(dot))
        #self.play(MoveAlongPath(dot, path))
        #self.wait(3)
        self.play(ApplyMethod(shape.fade, 0.5))
        self.begin_ambient_camera_rotation(rate = 0.5)
        self.wait(3)
