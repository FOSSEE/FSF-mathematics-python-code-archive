from manimlib.imports import *
class Subspace(ThreeDScene):


    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi = 80*DEGREES,theta =110*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.09)
        cube = Cube(stroke_width=5,color=WHITE).shift([1.5,1.5,1.5]).scale(1.5)
        cube.set_fill(TEAL)
        
        cube.set_opacity(0.4) 
        line = Line(color=MAROON,set_opacity=100).shift([1.5,1.5,1.5]).scale(1.5)
        plane1 = Polygon([0,0,3],[3,0,3],[3,3,0],[0,3,0])
        plane1.set_opacity(0.8)
        plane1.set_fill(YELLOW)
        plane1.set_color(YELLOW)
        
        
        plane2 = Polygon([0,3,3],[3,3,3],[3,0,0],[0,0,0])
        plane2.set_opacity(0.7)
        plane2.set_fill(RED)
        plane2.set_color(RED)

        vgroup = VGroup(plane1,plane2,line,cube)
        vgroup.shift([-1,-1,-1])
        
        
        self.play(ShowCreation(cube))
        self.play(ShowCreation(plane1))
        self.play(ShowCreation(plane2))
        self.play(ShowCreation(line))
        self.wait(10)

        

  