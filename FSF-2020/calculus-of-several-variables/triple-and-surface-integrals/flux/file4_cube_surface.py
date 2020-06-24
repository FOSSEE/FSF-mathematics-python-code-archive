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

        spaceloc = [[0,0,2],[1,0,2],[-1,0,2],[2,0,2],[-2,0,2],[3,0,2],[-3,0,2],
                    [0,1,2],[1,1,2],[-1,1,2],[2,1,2],[-2,1,2],[3,1,2],[-3,1,2],
                    [0,-1,2],[1,-1,2],[-1,-1,2],[2,-1,2],[-2,-1,2],[3,-1,2],[-3,-1,2],
                    [0,2,2],[1,2,2],[-1,2,2],[2,2,2],[-2,2,2],[3,2,2],[-3,2,2],
                    [0,-2,2],[1,-2,2],[-1,-2,2],[2,-2,2],[-2,-2,2],[3,-2,2],[-3,-2,2],
                    [0,3,2],[1,3,2],[-1,3,2],[2,3,2],[-2,3,2],[3,3,2],[-3,3,2],
                    [0,3,2],[1,3,2],[-1,3,2],[2,3,2],[-2,3,2],[3,3,2],[-3,3,2],
                    [0,4,2],[1,4,2],[-1,4,2],[2,4,2],[-2,4,2],[3,4,2],[-3,4,2],
                    [0,4,2],[1,4,2],[-1,4,2],[2,4,2],[-2,4,2],[3,4,2],[-3,4,2],
                    [0,5,2],[1,5,2],[-1,5,2],[2,5,2],[-2,5,2],[3,5,2],[-3,5,2],
                    [0,5,2],[1,5,2],[-1,5,2],[2,5,2],[-2,5,2],[3,5,2],[-3,5,2],
                    [0,6,2],[1,6,2],[-1,6,2],[2,6,2],[-2,6,2],[3,6,2],[-3,6,2],
                    [0,1.5,2],[1,1.5,2],[-1,1.5,2],[2,1.5,2],[-2,1.5,2],[3,1.5,2],[-3,1.5,2],
                    [0,3,2],[1,3,2],[-1,3,2],[2,3,2],[-2,3,2],[3,3,2],[-3,3,2]]


        veclist1=[Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E)]




    
        [veclist1[i].rotate(PI/4,axis=RIGHT) for i in range(10,30,1)]
        [veclist1[i].rotate(PI/4,axis=RIGHT) for i in range(40,80,2)]
        [veclist1[i].rotate(PI/6,axis=OUT) for i in range(98)]
        [veclist1[i].rotate(PI/8,axis=DOWN) for i in range(98)]
        vectorfield1=VGroup(*veclist1)
        [veclist1[i].shift(spaceloc[i]) for i in range(98)]     


        

        veclist2=[Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),
                  Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E),Vector(color=GOLD_E)]




    
        [veclist2[i].rotate(PI/4,axis=RIGHT) for i in range(10,30,1)]
        [veclist2[i].rotate(PI/4,axis=RIGHT) for i in range(40,80,2)]
        [veclist2[i].rotate(PI/6,axis=OUT) for i in range(98)]
        [veclist2[i].rotate(PI/8,axis=DOWN) for i in range(98)]
        vectorfield2=VGroup(*veclist2)
        [veclist2[i].shift(spaceloc[i]) for i in range(98)]



        veclist3=[Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector()]




    
        [veclist3[i].rotate(PI/4,axis=RIGHT) for i in range(10,30,1)]
        [veclist3[i].rotate(PI/4,axis=RIGHT) for i in range(40,80,2)]
        [veclist3[i].rotate(PI/6,axis=OUT) for i in range(98)]
        [veclist3[i].rotate(PI/8,axis=DOWN) for i in range(98)]
        vectorfield3=VGroup(*veclist3)
        [veclist3[i].shift(spaceloc[i]) for i in range(98)]




        veclist4=[Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector(),
                  Vector(color=RED),Vector(color=GREEN),Vector(color=BLUE),Vector(color=PINK),Vector(color=MAROON),Vector(color=GREEN),Vector()]




    
        [veclist4[i].rotate(PI/4,axis=RIGHT) for i in range(10,30,1)]
        [veclist4[i].rotate(PI/4,axis=RIGHT) for i in range(40,80,2)]
        [veclist4[i].rotate(PI/6,axis=OUT) for i in range(98)]
        [veclist4[i].rotate(PI/8,axis=DOWN) for i in range(98)]
        vectorfield4=VGroup(*veclist4)
        [veclist4[i].shift(spaceloc[i]) for i in range(98)]    

                    
        vectorfield1.shift(1.5*DOWN)
        vectorfield2.shift(IN+1.5*DOWN)
        vectorfield3.shift(2*IN+1.5*DOWN)
        vectorfield4.shift(3*IN+1.5*DOWN)           

        vectors=[vectorfield1,vectorfield2,vectorfield3,vectorfield4]
        vectorfield=VGroup(*vectors)
        vectorfield.scale(1.25)

        fv=[Vector(color=ORANGE),Vector(color=ORANGE),Vector(color=ORANGE),Vector(color=ORANGE),
            Vector(color=ORANGE),Vector(color=ORANGE),Vector(color=ORANGE),Vector(color=ORANGE),
            Vector(color=ORANGE),Vector(color=ORANGE),Vector(color=ORANGE),Vector(color=ORANGE),
            Vector(color=ORANGE),Vector(color=ORANGE),Vector(color=ORANGE),Vector(color=ORANGE),
            ]

        spaceloc2 = [[1.5,0.5,0.5],[1.5,1,0.5],[1.5,1.5,0.5],[1.5,2,0.5],
                     [1.5,0.5,1],[1.5,1,1],[1.5,1.5,1],[1.5,2,1],
                     [1.5,0.5,1.5],[1.5,1,1.5],[1.5,1.5,1.5],[1.5,2,1.5],
                     [1.5,0.5,2],[1.5,1,2],[1.5,1.5,2],[1.5,2,2]]

        [fv[i].rotate(PI/4,axis=RIGHT) for i in range(1)]
        [fv[i].rotate(PI/6,axis=OUT) for i in range(16)]
        [fv[i].rotate(PI/8,axis=DOWN) for i in range(16)]
        [fv[i].shift(spaceloc2[i]) for i in range(16)]     
        fvfield=VGroup(*fv)
        fvfield.shift(0.5*IN+2*DOWN)

        flux=TextMobject("Flux through one side of the cube").set_color(ORANGE)
        flux.shift(3*UP+1.5*LEFT)





        self.set_camera_orientation(phi=70 * DEGREES,theta=-75*DEGREES)
        self.play(ShowCreation(axes),ShowCreation(axis_label))
        self.play(ShowCreation(vectorfield))
        self.add(fvfield)
        self.begin_ambient_camera_rotation(rate=0.01)

        self.play(ShowCreation(cube, run_time=1))
        
        self.wait(1)
        self.play(ShowCreation(sq3))
        self.wait(1)
        self.play(FadeOut(cube))
        self.play(FadeOut(vectorfield))
        self.add_fixed_in_frame_mobjects(flux)
        # self.play(ShowCreation(flux)) 
        self.wait(1)
        self.play(ShowCreation(v1),ShowCreation(n1))
        self.wait(6)
        # self.stop_ambient_camera_rotation() 
        
