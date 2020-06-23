from manimlib.imports import *

class Surface(ThreeDScene):
    def construct(self):
        axes=ThreeDAxes()
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                v,
                u
            ]),
            resolution=(6, 32)).fade(0.5) #Resolution of the surfaces


        x=TextMobject("X")
        y=TextMobject("Y")
        z=TextMobject("Z")

        x.rotate(PI/2, axis=RIGHT)
        x.rotate(PI/4,axis=OUT)
        x.shift(5.8*DOWN)

        y.rotate(PI/2, axis=RIGHT)
        y.rotate(PI/8,axis=OUT)
        y.shift(5.8*RIGHT)

        z.rotate(PI/2, axis=RIGHT)
        z.rotate(PI/5,axis=OUT)
        z.shift(3.2*OUT+0.4*LEFT)
        axis_label=VGroup(x,y,z)



        cylinder.rotate(PI/2, axis=RIGHT)
        cylinder.shift(2*RIGHT+OUT+DOWN)
        cylinder.scale(1.5)

        self.set_camera_orientation(phi=75 * DEGREES,theta=-85*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(ShowCreation(axes),ShowCreation(axis_label))
        self.play(ShowCreation(cylinder))
        # self.wait(0.7)
    
        

        self.wait(2)
        self.stop_ambient_camera_rotation() 
        self.wait(0.7)


























        


