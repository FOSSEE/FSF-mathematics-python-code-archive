from manimlib.imports import*



class TripleBox(ThreeDScene):

    def construct(self):

        axes=ThreeDAxes()
        cube=Cube(fill_color=RED,fill_opacity=0.5)
        cube.scale(0.5)
        cube.shift(0.5*RIGHT+0.5*DOWN+0.5*OUT)
        cube.shift(2*RIGHT+2*DOWN+1*OUT)



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



        
        a=TextMobject("a")
        b=TextMobject("b")
        c=TextMobject("c")
        d=TextMobject("d")
        e=TextMobject("e")
        f=TextMobject("f")



        a.rotate(PI/2, axis=RIGHT)
        a.rotate(PI/2, axis=OUT)
        a.shift(2*DOWN+0.3*OUT+0.3*LEFT)

        b.rotate(PI/2, axis=RIGHT)
        b.rotate(PI/2, axis=OUT)
        b.shift(3*DOWN+0.3*OUT+0.3*LEFT)
        

        c.rotate(PI/2, axis=RIGHT)
        c.shift(2*RIGHT+0.3*OUT)
        
        d.rotate(PI/2, axis=RIGHT)
        d.shift(3*RIGHT+0.3*OUT)


        e.rotate(PI/2, axis=RIGHT)
        e.rotate(PI/4, axis=OUT)
        e.shift(1*OUT+0.3*DOWN+0.2*LEFT)


        f.rotate(PI/2, axis=RIGHT)
        f.rotate(PI/4, axis=OUT)
        f.shift(2*OUT+0.3*DOWN+0.2*LEFT)



        rec1=Rectangle(height=1, width=8,color=RED, fill_color=RED_C, fill_opacity=0.40)
        rec1.shift(2.5*DOWN+4*RIGHT)

        rec2=Rectangle(height=1, width=14,color=RED, fill_color=RED_C, fill_opacity=0.40)
        rec2.rotate(PI/2, axis=OUT)
        rec2.shift(7*DOWN+2.5*RIGHT)


        sq=Square(color=RED,fill_opacity=60,side_length=1)
        sq.shift(2.5*RIGHT+2.5*DOWN)



        self.set_camera_orientation(phi=70 * DEGREES,theta=-70*DEGREES)
        self.play(ShowCreation(axes),ShowCreation(axis_label))
        self.begin_ambient_camera_rotation(rate=0.04)
        self.play(ShowCreation(a),ShowCreation(b))
        self.wait(0.5)
        self.play(ShowCreation(rec1))
        self.play(ShowCreation(c),ShowCreation(d))
        self.play(ShowCreation(rec2))
        self.add(sq)
        self.wait(0.5)

        self.play(FadeOut(rec1),FadeOut(rec2))
        self.wait(1)

        self.play(ShowCreation(e),ShowCreation(f))
        self.wait(0.5)
        self.play(ApplyMethod(sq.shift, 1*OUT))
        self.wait(0.5)
        self.play(Transform(sq,cube))

   
        self.wait(0.5)


      
        self.wait(0.5)

       


        self.wait(3)
        self.stop_ambient_camera_rotation()  
        self.wait(1.5)
        
     
