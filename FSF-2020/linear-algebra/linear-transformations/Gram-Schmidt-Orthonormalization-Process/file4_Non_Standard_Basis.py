from manimlib.imports import *

class NSB(ThreeDScene):
    def construct(self):

        line1 = Line(start = ORIGIN,end = 1*RIGHT)
        line1.set_color(DARK_BLUE)
        tip1 = Polygon(RIGHT,0.9*RIGHT-0.1*DOWN,0.9*RIGHT-0.1*UP)
        tip1.set_opacity(1)
        tip1.set_fill(DARK_BLUE)
        tip1.set_color(DARK_BLUE)

        arrow2 = Line(start = ORIGIN,end = 1*UP)
        arrow2.set_color(DARK_BLUE)
        tip2 = Polygon(UP,0.9*UP-0.1*RIGHT,0.9*UP-0.1*LEFT)
        tip2.set_opacity(1)
        tip2.set_fill(DARK_BLUE)
        tip2.set_color(DARK_BLUE)
        arrow2.set_color(DARK_BLUE)
        
        arrow3 = Line(start = ORIGIN,end = [0,0,1])
        arrow3.set_color(DARK_BLUE)
        tip3 = Polygon([0,0,1],[0,0,0.9]-0.1*RIGHT,[0,0,0.9]-0.1*LEFT)
        tip3.set_opacity(1)
        tip3.set_fill(DARK_BLUE)
        tip3.set_color(DARK_BLUE)

        axes = ThreeDAxes(x_min = -3,x_max=3,y_min=-3,y_max=3,z_min=-3,z_max=3)
        self.play(ShowCreation(axes))
        self.move_camera(phi=70*DEGREES,theta=0*DEGREES,run_time=3)
        self.begin_ambient_camera_rotation(rate=0.2)

        #matrix = [[1,0,0],[0,1,0],[0,0,1]]
        matrix = [[0.70710678118,-0.57735026919,-0.57735026919],[0.70710678118,0.57735026919,0.57735026919],[0,-0.57735026919,0.57735026919]]
        matrix1 = [[0.70710678118,0,0],[0.70710678118,1,0],[0,0,1]]
        
        matrix1 = [[0.70710678118,-0.70710678118,0],[0.70710678118,0.70710678118,0],[0,0,1]]
        matrix2 = [[1,0,0],[0,0.70710678118,0.70710678118],[0,-0.70710678118,0.70710678118]]
        

        line1.apply_matrix(matrix1)
        tip1.apply_matrix(matrix1)
        arrow2.apply_matrix(matrix1)
        tip2.apply_matrix(matrix1)
        arrow3.apply_matrix(matrix1)
        tip3.apply_matrix(matrix1)
        
        line1.apply_matrix(matrix2)
        tip1.apply_matrix(matrix2)
        arrow2.apply_matrix(matrix2)
        tip2.apply_matrix(matrix2)
        arrow3.apply_matrix(matrix2)
        tip3.apply_matrix(matrix2)
        
        self.play(ShowCreation(line1), 
        ShowCreation(tip1), 
        ShowCreation(arrow2), 
        ShowCreation(tip2), 
        ShowCreation(arrow3), 
        ShowCreation(tip3))
        
        text = TextMobject(r"This is also a set of Orthonormal Vectors")
        text.set_color(DARK_BLUE)
        self.add_fixed_in_frame_mobjects(text)
        text.scale(0.6)
        text.move_to(3*DOWN+3.5*RIGHT)
        self.play(Write(text))

        self.wait(22)
