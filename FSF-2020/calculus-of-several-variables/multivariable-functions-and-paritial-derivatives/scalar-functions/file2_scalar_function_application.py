from manimlib.imports import *

class ScalarApplication(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes() # creates a 3D Axis
        
        cube = Cube()
        cube.set_fill(YELLOW_E, opacity = 0.1)
        cube.scale(2)
        self.set_camera_orientation(phi=0 * DEGREES,theta=270*DEGREES)
        self.play(ShowCreation(cube),ShowCreation(axes))
        
        dot = Sphere()
        dot.scale(0.1)
        dot.move_to(np.array([1,0.5,1]))
        dot.set_fill(RED)

        #dot = Dot(np.array([1,0.5,1]), color = RED)
        temp_func = TextMobject("T(x,y,z)")
        temp_func.next_to(dot,RIGHT)
        temp_func.set_color(RED)
        temp_func_trans = TextMobject("T(1,0.5,1)")
        temp_func_trans.next_to(dot,RIGHT)
        temp_func_trans.set_color(RED)
        temp = TextMobject(r"$36 ^\circ$")
        temp.next_to(dot,RIGHT)
        temp.set_color(RED_E)


        self.play(ShowCreation(dot))
        self.play(ShowCreation(temp_func))
        self.play(Transform(temp_func, temp_func_trans))
        self.wait(1)
        self.play(Transform(temp_func, temp))




        dot1 = Sphere()
        dot1.scale(0.1)
        dot1.move_to(np.array([-1,-0.8,-1.5]))
        dot1.set_fill(BLUE_E)
        #dot1 = Dot(np.array([-1,-0.8,-1.5]), color = BLUE)
        temp_func1 = TextMobject("T(x,y,z)")
        temp_func1.next_to(dot1,LEFT)
        temp_func1.set_color(BLUE)
        temp_func_trans1 = TextMobject("T(-1,-0.8,-1.5)")
        temp_func_trans1.next_to(dot1,LEFT)
        temp_func_trans1.set_color(BLUE)
        temp1 = TextMobject(r"$24 ^\circ$")
        temp1.next_to(dot1,LEFT)
        temp1.set_color(BLUE)

        self.play(ShowCreation(dot1))
        self.play(ShowCreation(temp_func1))
        self.play(Transform(temp_func1, temp_func_trans1))
        self.wait(1)
        self.play(Transform(temp_func1, temp1))

        self.play(FadeOut(temp_func))
        self.play(FadeOut(temp_func1))


        self.move_camera(phi=80* DEGREES,theta=45*DEGREES,run_time=3)

        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        self.wait(2)
        



class AddTempScale(Scene):
    def construct(self):
        temp_scale = ImageMobject("tempscale.png")
        temp_scale.scale(4) 
        temp_scale.move_to(2*RIGHT) 
        self.play(ShowCreation(temp_scale))


        temp_func = TextMobject("T(x,y,z)")
        temp_func.move_to(3*UP +2*LEFT)
        temp_func.set_color(RED)
        temp_func_trans = TextMobject("T(1,0.5,1)")
        temp_func_trans.move_to(3*UP +2*LEFT)
        temp_func_trans.set_color(RED)
        temp = TextMobject(r"$36 ^\circ$")
        temp.set_color(RED)
        temp.move_to(3*UP +2*LEFT)
        temp.scale(0.7)

        self.play(ShowCreation(temp_func))
        self.play(Transform(temp_func, temp_func_trans))
        self.wait(1)
        self.play(Transform(temp_func, temp))
        self.play(ApplyMethod(temp_func.move_to, 1.8*UP +1.8*RIGHT))

        
        temp_func1 = TextMobject("T(x,y,z)")
        temp_func1.move_to(2*UP +2*LEFT)
        temp_func1.set_color(BLUE)
        temp_func_trans1 = TextMobject("T(-1,-0.8,-1.5)")
        temp_func_trans1.move_to(2*UP +2*LEFT)
        temp_func_trans1.set_color(BLUE)
        temp1 = TextMobject(r"$24 ^\circ$")
        temp1.set_color(BLUE)
        temp1.move_to(2*UP +2*LEFT)
        temp1.scale(0.7)
        
        self.play(ShowCreation(temp_func1))
        self.play(Transform(temp_func1, temp_func_trans1))
        self.wait(1)
        self.play(Transform(temp_func1, temp1))
        self.play(ApplyMethod(temp_func1.move_to, 0.6*UP +1.8*RIGHT))



        transtext = TextMobject("Scalar Function Transform:")
        transtext.set_color(GREEN)
        transtext1 = TextMobject(r"$\mathbb{R}^3 \rightarrow \mathbb{R}$")
        transtext1.set_color(YELLOW_E)
        transtext.move_to(3*UP +3*LEFT)
        transtext1.next_to(transtext,DOWN)
        self.play(Write(transtext))
        self.play(Write(transtext1))
        self.wait(2)   


