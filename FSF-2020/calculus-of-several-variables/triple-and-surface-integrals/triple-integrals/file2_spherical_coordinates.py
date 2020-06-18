from manimlib.imports import*
class Sp(ThreeDScene):

    def construct(self):

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






        
        x1=TextMobject("$x_{1}$")
        y1=TextMobject("$y_{1}$")
        z1=TextMobject("$z_{1}$")
        



        x1.rotate(PI/2, axis=RIGHT)
        x1.rotate(PI/2, axis=OUT)
        x1.shift(2*DOWN+0.3*OUT+0.3*LEFT)
        
        y1.rotate(PI/2, axis=RIGHT)
        y1.shift(2*RIGHT+0.3*OUT)
        
        z1.rotate(PI/2, axis=RIGHT)
        z1.rotate(PI/4, axis=OUT)
        z1.shift(2*OUT+0.3*DOWN+0.2*LEFT)


        d1=Dot(color=RED,radius=0.05)
        d2=Dot(color=RED,radius=0.05)
        d3=Dot(color=RED,radius=0.05)


        d1.shift(2*DOWN)
        d1.rotate(PI/2,axis=UP)

        d2.rotate(PI/2, axis=RIGHT)
        d2.shift(2*RIGHT)

        d3.rotate(PI/2, axis=RIGHT)
        d3.rotate(PI/4, axis=OUT)
        d3.shift(2*OUT)



        l1=DashedLine(color=RED)
        l1.scale(5)
        l1.shift(2*DOWN+5*RIGHT)

        l2=DashedLine(color=RED)
        l2.scale(5)
        l2.rotate(PI/2, axis=IN)
        l2.shift(2*RIGHT+5*DOWN)

        l3=DashedLine(color=RED)
        l3.scale(5)
        l3.rotate(PI/4,axis=IN)
        l3.shift(2*OUT+4*RIGHT+4*DOWN)

        point=Sphere(radius=0.02, checkerboard_colors=[RED,RED])
        

        proj=DashedLine(color=RED_C)
        proj.scale(1.414)
        proj.rotate(PI/4,axis=IN)
        proj.shift(1*RIGHT+1*DOWN)


        projl=DashedLine()
        projl.rotate(PI/2, axis=UP)
        projl.shift(1*OUT+2*RIGHT+2*DOWN)

        p=TextMobject("$P(x,y,z)$")
        p.scale(0.6)
        p.rotate(PI/2, axis=RIGHT)
        p.rotate(PI/9, axis=OUT)
        p.shift(2.65*RIGHT+2.5*DOWN+2.3*OUT)

        rho=TextMobject(r"$\rho$",tex_to_color_map={r"$\rho$": YELLOW})
        rho.rotate(PI/2, axis=RIGHT)
        rho.shift(1.45*RIGHT+1.9*DOWN+1.94*OUT)

        



        carrow=ArcBetweenPoints(start=1*DOWN, end=0.5*RIGHT+0.5*DOWN)
        carrow2=ArcBetweenPoints(start=0.5*RIGHT+0.5*DOWN+0.5*OUT, end=0.4*OUT)
        # carrow2.rotate(PI/2, axis=LEFT)
        # carrow2.rotate(PI/2, axis=UP)

        theta=TextMobject(r"$\theta$",tex_to_color_map={r"$\theta$": YELLOW})
        theta.shift((0.75*OUT+0.2*RIGHT))
        theta.rotate(PI/2,axis=RIGHT)
        theta.scale(0.9)


         

        phi=TextMobject(r"$\phi$",tex_to_color_map={"$\phi$": YELLOW})
        phi.scale(0.93)
        phi.rotate(PI/2, axis=RIGHT)
        phi.shift(0.42*RIGHT+1.3*DOWN)










        self.set_camera_orientation(phi=70 * DEGREES,theta=-85*DEGREES)
        self.play(ShowCreation(axes),ShowCreation(axis_label))
        self.begin_ambient_camera_rotation(rate=0.009)
        self.wait(1)
        self.add(point)
        self.play(ApplyMethod(point.shift, 2*RIGHT+2*DOWN+2*OUT))
        self.wait(0.5)
        self.play(ShowCreation(p))
        self.wait(0.5)
        self.play(ShowCreation(vec),ShowCreation(rho))
        self.wait(1.5)
        self.play(ApplyMethod(point.shift,2*IN), ShowCreation(projl))
        self.wait(1)
        self.play(ShowCreation(proj))
        self.wait(1.2)
        self.play(ShowCreation(carrow))
        self.wait(0.64)
        self.play(ShowCreation(phi))
        self.wait(1.3)
        self.play(ShowCreation(carrow2))
        self.wait(0.5)
        self.play(ShowCreation(theta))
        self.wait(3)
        


