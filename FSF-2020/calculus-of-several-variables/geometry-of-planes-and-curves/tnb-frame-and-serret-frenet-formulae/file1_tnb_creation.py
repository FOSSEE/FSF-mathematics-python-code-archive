from manimlib.imports import *

class tnb(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 75*DEGREES, theta=45*DEGREES)

        helix1 = ParametricFunction(
                lambda t: np.array([
                np.cos(TAU*t),
                np.sin(TAU*t),
                0.4*t
                ]), t_min = -2*np.pi/3, t_max = -1.638*np.pi/3, color = WHITE
                )

        helix2 = ParametricFunction(
                lambda t: np.array([
                np.cos(TAU*t),
                np.sin(TAU*t),
                0.4*t
                ]), t_min = -1.638*np.pi/3, t_max = -1.33*np.pi/3, color = WHITE
                )

        pointText = TextMobject(r'Consider an arbitrary point \\ on the given curve.').scale(0.8).shift(1.5*UP)
        tgtText = TextMobject(r'Unit', ' tangent ', r'vector at \\ this point is given as:').scale(0.8).shift(1.5*UP)
        tgtText.set_color_by_tex_to_color_map({
            "tangent": YELLOW
        })
        normalText = TextMobject(r'Unit', ' normal ', r'vector at \\ this point is given as:').scale(0.8).shift(1.5*UP)
        normalText.set_color_by_tex_to_color_map({
            "normal": BLUE
        })
        planeText = TextMobject(r'$\overrightarrow{T}$ and $\overrightarrow{N}$ \\ prescribe a plane.').scale(0.8).shift(1.5*UP)
        bnmText = TextMobject(r'The vector normal to this plane \\ is called the', ' binormal ', 'vector.').scale(0.8).shift(1.5*UP)
        bnmText.set_color_by_tex_to_color_map({
            "binormal": GREEN_E
        })

        dot1 = Dot(np.array([np.cos(-np.pi/3), np.sin(-np.pi/3), -0.4*np.pi/3]) + np.array([0,0.2,0]), radius = 0.16, color=RED)
        tgt1 = Arrow((0,0,0), (-2,-0.55,0), color = YELLOW).shift(dot1.get_center() + np.array([0.18,0.04,0]))
        nm1 = Arrow((0,0,0), (0.4,-2,0), color = BLUE).shift(dot1.get_center() + np.array([0,0.26,0]))
        bnm1 = Arrow((0,0,0), (0,2,0), color=GREEN_E).shift(2.1*RIGHT+2*DOWN)
        plane1 = Square(color = DARK_BROWN, fill_color = WHITE, fill_opacity=0.3).shift(dot1.get_center() + np.array([-0.4, -0.6, 0])).rotate(13*DEGREES).scale(1.2)
        point1 = VGroup(*[dot1, tgt1, nm1, plane1]).scale(0.8).shift(np.array([1,4.86,0])).rotate(-15*DEGREES)



        helix = VGroup(*[helix1, helix2])
        self.play(FadeIn(helix))
        self.play(ApplyMethod(helix.scale, 4))
        self.add_fixed_in_frame_mobjects(pointText)
        self.play(FadeIn(dot1), FadeIn(pointText))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(tgtText)
        self.play(Write(tgt1), ReplacementTransform(pointText, tgtText))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(normalText)
        self.play(Write(nm1), ReplacementTransform(tgtText, normalText))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(planeText)
        self.play(FadeIn(plane1), ReplacementTransform(normalText, planeText))
        self.wait(2)
        self.add_fixed_in_frame_mobjects(bnmText)
        self.add_fixed_in_frame_mobjects(bnm1)
        self.play(ReplacementTransform(planeText, bnmText), Write(bnm1))
        self.wait(2)
        self.play(FadeOut(VGroup(*[helix, bnm1, bnmText, dot1, tgt1, nm1, plane1])))
