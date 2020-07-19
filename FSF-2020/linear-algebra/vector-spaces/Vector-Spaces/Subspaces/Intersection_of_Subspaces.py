from manimlib.imports import *
class ThreeDSpace(ThreeDScene):


    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi = 80*DEGREES,theta =110*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.09)
        
       
        
        
        cube = Cube(stroke_width=5,color=WHITE).shift([1.5,1.5,1.5]).scale(1.5)
        cube.set_fill(TEAL)
        
        cube.set_opacity(0.4) 
        
        
        plane1 = Polygon([0,0,3],[3,0,3],[3,3,0],[0,3,0])
        plane1.set_opacity(0.65)
        plane1.set_fill(PURPLE)
        plane1.set_color(PURPLE)
        
        
        plane2 = Polygon([0,3,3],[3,3,3],[3,0,0],[0,0,0])
        plane2.set_opacity(0.7)
        plane2.set_fill(RED)
        plane2.set_color(RED)
        line = Line(color=YELLOW,set_opacity=100).shift([1.5,1.5,1.5]).scale(1.5)

        vgroup = VGroup(plane1,plane2,line,cube)
        vgroup.shift([-1,-1,-1])
        
        dot = Dot(color=BLACK).shift([0.5,0.5,0.5]).scale(1)
        text = TextMobject(r"\text{The}",r"\text{line}",r"\text{representing the intersection of the two planes is a Subspace.}",opacity = 0.6).scale(0.7).shift(3*UP)
        text[1].set_color(YELLOW)
        self.add_fixed_in_frame_mobjects(text)
        self.play(ShowCreation(text))
        
        
        self.play(ShowCreation(cube))
        self.play(ShowCreation(plane1))
        self.play(ShowCreation(plane2))

        self.play(ShowCreation(line),ShowCreation(dot))
        

        self.wait(15)

        

  