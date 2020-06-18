from manimlib.imports import *
class fluxsphere(ThreeDScene):
    

    def construct(self):
        s = Sphere(checkerboard_colors=[BLUE_D,BLUE_D])
        s.scale(2.3)

        n = VGroup(
            *[self.n(*self.func(u, v))
              for u in np.arange(0, PI, 0.4)
              for v in np.arange(0, TAU, 0.8)]
        )

        

        self.move_camera(0.8 * PI / 2, -0.45 * PI)
        self.play(Write(s))
        # self.play(Write(f))
        self.play(ShowCreation(n), run_time=4)
        # self.add(n)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)


    def func(self, u, v):
        return [
            np.cos(v) * np.sin(u),
            np.sin(v) * np.sin(u),
            np.cos(u)
        ]

    def vect(self, x, y, z):
        return np.array([
            x, y, z
        ])

    def n(self, x, y, z):
        vect = np.array([
            x,
            y,
            z
        ])

        mag = math.sqrt(vect[0] ** 2 + vect[1] ** 2 + vect[2] ** 2)
        v = Vector(
            (1.5/mag) * vect,
            color=RED_B,
            stroke_width=4).shift(2*x * RIGHT + 2*y * UP + 2*z * OUT)
        return v
