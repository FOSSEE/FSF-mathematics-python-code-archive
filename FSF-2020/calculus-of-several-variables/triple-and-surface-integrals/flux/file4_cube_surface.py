from manimlib.imports import*



class cuber(ThreeDScene):
    def construct(self):

        axes=ThreeDAxes()
        cube=Cube()
        # cube.scale(1)
        cube.shift(RIGHT+DOWN+OUT)

        

        sq3=Square(color=RED, fill_opacity=0.85)
        sq3.rotate(PI/2, axis=UP)
        sq3.shift(DOWN+OUT+2*RIGHT)

        x=TextMobject("x")
        y=TextMobject("y")
        z=TextMobject("z")

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

        v1=Vector(color=YELLOW,buff=15)
        v1.rotate(PI/4,axis=RIGHT)
        v1.shift(2*RIGHT+1*DOWN+1*OUT)


        n1=TextMobject(r"$\vec{n}$",color=YELLOW)
        n1.scale(0.8)
        n1.rotate(PI/2,axis=RIGHT)
        n1.shift(3*RIGHT+1.3*OUT+DOWN)



        self.set_camera_orientation(phi=75 * DEGREES,theta=-15*DEGREES)
        self.play(ShowCreation(axes),ShowCreation(axis_label))
        self.play(ShowCreation(cube, run_time=3))
        self.begin_ambient_camera_rotation(rate=-0.2)
        # self.move_camera(phi=150*DEGREES,theta=-45*DEGREES, run_time=3)
        self.wait(1)
        self.play(ShowCreation(sq3))
        
        self.wait(1)
        self.play(ShowCreation(v1),ShowCreation(n1))
        self.wait(1)
        self.stop_ambient_camera_rotation() 
        self.wait(2)


        # self.play(Write(t1))
        # self.play(Transform(vg,t1))
        # self.wait(3)
        # self.play(ReplacementTransform(t1,t2))
        # self.wait(3)
        # # self.move_camera(phi=50*DEGREES,theta=-45*DEGREES,run_time=3)
        # self.wait(8)
        # self.move_camera(phi=75 * DEGREES, run_time=3)
        # self.wait(3)
