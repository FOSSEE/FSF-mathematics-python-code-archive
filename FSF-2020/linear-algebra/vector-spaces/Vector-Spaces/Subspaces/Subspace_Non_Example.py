from manimlib.imports import *
class ThreeDSpace(ThreeDScene):


    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi = 80*DEGREES,theta =110*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.09)
        plane1 = Polygon([-1.5,1.5,-1.5],[1.5,1.5,-1.5],[1.5,-1.5,1.5],[-1.5,-1.5,1.5])
        plane1.set_opacity(0.65)
        plane1.set_fill(GREEN)
        plane1.set_color(GREEN)
        
        
        plane2 = Polygon([-1.5,1.5,1.5],[1.5,1.5,1.5],[1.5,-1.5,-1.5],[-1.5,-1.5,-1.5])
        plane2.set_opacity(0.7)
        plane2.set_fill(MAROON_A)
        plane2.set_color(MAROON_A)
        line = Line(color=YELLOW,set_opacity=100,start=[1.5,1.2,1.2],end=[-1.5,1.2,1.2])
        
        
        self.play(ShowCreation(plane1),ShowCreation(plane2),ShowCreation(line))
        self.wait(10)

