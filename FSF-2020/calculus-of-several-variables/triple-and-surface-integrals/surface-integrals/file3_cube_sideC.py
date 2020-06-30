from manimlib.imports import*



class cuber(ThreeDScene):

    def construct(self):

        axes=ThreeDAxes()
        cube=Cube(color=RED)
        # cube.scale(1)
        cube.shift(RIGHT+DOWN+OUT)

        sq1=Square(side_length=1.95,color=BLUE, fill_opacity=1)
        sq1.shift(RIGHT+DOWN+2*OUT)
        # sq1.scale(1.2)

        sq12=Square(side_length=1.95,color=BLUE, fill_opacity=1)
        sq12.shift(RIGHT+DOWN+2*OUT)

        sq2=Square(side_length=1.95,color=RED, fill_opacity=0.6)
        sq2.shift(RIGHT+DOWN)

        sq2w=Square(side_length=1.95,color=WHITE, fill_opacity=0.9)
        sq2w.shift(RIGHT+DOWN)
        

        c=TextMobject("side C",tex_to_color_map={"side C": BLACK})

        dxdy=TextMobject(r"$dxdy$",tex_to_color_map={r"$dxdy$": WHITE})
        dxdy.scale(0.7)
        dxdy.rotate(PI/2, axis=RIGHT)
        dxdy.rotate(PI/7, axis=OUT)
        dxdy.shift(0.85*RIGHT+0.65*DOWN)


        
        c.shift(RIGHT+DOWN+2*OUT)
        c.rotate(PI/4, axis=OUT)


        
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

        v=Vector(color=YELLOW)
        # v.scale(2)
        v.rotate(PI/2,axis=DOWN)
        v.shift(0.4*RIGHT+0.9*DOWN+2.5*OUT)



     


        self.set_camera_orientation(phi=60 * DEGREES,theta=-67*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.008)
        self.add(axes)
        self.add(axis_label)
        
        self.add(cube)
        # self.move_camera(phi=150*DEGREES,theta=-45*DEGREES, run_time=3)
        self.wait(1.2)
        self.add(sq1)
        self.add(sq12)
        self.play(ShowCreation(c))
        self.wait(0.7)
        self.play(FadeOut(cube))
        self.wait(0.7)
        # self.move_camera(phi=75*DEGREES,run_time=2)
        self.play(ShowCreation(v))
        self.wait(1)
        self.play(Transform(sq1,sq2))
        self.wait(0.7)
        self.play(ApplyMethod(sq2w.scale, 0.08))
        self.play(ShowCreation(dxdy))
        self.wait(2)
        
        
       

      
