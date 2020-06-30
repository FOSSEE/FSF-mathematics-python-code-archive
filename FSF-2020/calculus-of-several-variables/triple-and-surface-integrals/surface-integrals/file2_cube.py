from manimlib.imports import*
class cuber(ThreeDScene):

    def construct(self):

        axes=ThreeDAxes()
        cube=Cube(color=RED)
        # cube.scale(1)
        cube.shift(RIGHT+DOWN+OUT)

        sq1=Square(side_length=2,color=RED, fill_opacity=0.5)
        sq1.shift(RIGHT+DOWN)
        # sq1.scale(1.2)
        sq2=Square(color=YELLOW, fill_opacity=0.5)
        sq2.rotate(PI/2,axis=RIGHT)
        sq2.shift(RIGHT+OUT)

        sq3=Square(color=GREEN , fill_opacity=0.5)
        sq3.rotate(PI/2, axis=UP)
        sq3.shift(DOWN+OUT)

        a=TextMobject("side A",tex_to_color_map={"side A": BLACK})
        b=TextMobject("side B",tex_to_color_map={"side B": BLACK})
        c=TextMobject("side C",tex_to_color_map={"side C": BLACK})
        a.rotate(PI/2, axis=RIGHT)
        a.shift(RIGHT+OUT+2*DOWN)
        b.rotate(PI/2, axis=OUT)
        b.rotate(PI/2, axis=UP)
        b.shift(2*RIGHT+DOWN+OUT)
        c.shift(RIGHT+DOWN+2*OUT)
        c.rotate(PI/4, axis=OUT)


        axes=ThreeDAxes()
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



     


        self.set_camera_orientation(phi=75 * DEGREES,theta=-67*DEGREES)
        self.play(ShowCreation(axes),ShowCreation(axis_label))
        self.play(ShowCreation(cube))
        self.begin_ambient_camera_rotation(rate=0.04)
        self.wait(0.7)
        self.play(ShowCreation(sq1))
        self.play(ShowCreation(sq2))
        
        self.play(ShowCreation(sq3))
        self.wait(0.6)
        self.play(ShowCreation(a))
        
        self.play(ShowCreation(b))
        self.move_camera(phi=60*DEGREES,run_time=1)
        self.play(ShowCreation(c))
        self.wait(1)
        self.wait(2)

        
