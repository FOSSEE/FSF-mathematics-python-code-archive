from manimlib.imports import *
class S(ThreeDScene):
    def construct(self):
        axes=ThreeDAxes()

        sphere=Sphere(radius=2,checkerboard_colors=[BLUE_C,BLUE_B],fill_opacity=0.75)
        

        v1=Vector(color=YELLOW,buff=5)
        v1.rotate(PI/4,axis=DOWN)
        v1.shift(1.5*RIGHT+1.5*OUT)

        v2=Vector(color=RED,buff=5)
        v2.rotate(PI/4,axis=DOWN)
        v2.rotate(PI,axis=DOWN)
        v2.shift(0.77*RIGHT+0.77*OUT)

        

        
        n1=TextMobject(r"$\vec{n}$",color=YELLOW)
        n2=TextMobject(r"$-\vec{n}$",color= RED)
        n1.rotate(PI/2,axis=RIGHT)
        n1.shift(2*RIGHT+2*OUT)
        n2.rotate(PI/2,axis=RIGHT)
        n2.shift(0.42*RIGHT+0.42*OUT)



        self.set_camera_orientation(phi=75 * DEGREES,theta=-45*DEGREES)
        # self.add(mobius)
        # self.play(ShowCreation(axes))
        self.play(ShowCreation(axes))
        # self.play(ShowCreation(vg))
        self.play(ShowCreation(sphere))
        self.wait(0.7)
        self.play(ShowCreation(v1, run_time=2))
        self.play(ShowCreation(n1))
        self.wait(1)
        self.begin_ambient_camera_rotation(rate=0.65)
        self.wait(2)
        self.play(ShowCreation(v2, run_time=3))
        self.wait(3)
        self.play(ShowCreation(n2))

        self.stop_ambient_camera_rotation() 
        self.wait(1.2)
