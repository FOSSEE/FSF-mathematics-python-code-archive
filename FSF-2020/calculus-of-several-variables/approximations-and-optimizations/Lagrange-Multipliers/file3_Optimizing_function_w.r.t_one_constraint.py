from manimlib.imports import*

class firstScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (u)
            ]),checkerboard_colors=[YELLOW_C,YELLOW_D,YELLOW_E]
        ).fade(0.4) #Resolution of the surfaces

        plane =  ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u+v
            ]),checkerboard_colors=[TEAL_C,TEAL_D,TEAL_E]
        ).scale(2.5)
        self.add(axes)
        self.set_camera_orientation(phi=75*DEGREES,theta=45*DEGREES)
        self.play(Write(cylinder)) 
        self.play(Write(plane)) 
        self.wait(1)
        self.begin_ambient_camera_rotation(rate=0.7)          
        self.wait(5)
        self.move_camera(phi=35*DEGREES,theta=-45*DEGREES)
        self.wait(2)
