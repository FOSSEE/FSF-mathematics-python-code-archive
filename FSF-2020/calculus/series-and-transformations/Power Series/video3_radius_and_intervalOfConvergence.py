from manimlib.imports import *
import math

class intro(Scene):
    def construct(self):
        introText1=TextMobject("Consider the example","above",)
        introText1.scale(0.8)
        introText1.set_color_by_tex_to_color_map({"above":YELLOW})
        self.play(Write(introText1))
        self.wait(1)

class graphScene(GraphScene,MovingCameraScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "exclude_zero_label": True,
        "x_labeled_nums": range(-1, 2, 1),
        "y_labeled_nums": range(0,2,1),
        "y_axis_height":7,
        "x_axis_width":7,
    }

    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)
       

    def construct(self):
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)

        function_expan=TextMobject("$1-{ x }^{ 2 }+{ x }^{ 4 }-{ x }^{ 6 }+{ x }^{ 8 }+..$")
        function_expan.scale(0.6)
        function_expan.set_color(RED)
        function_expan.to_edge(UP+RIGHT)
        self.add(function_expan)

        self.setup_axes()

        equation = self.get_graph(lambda x : 1-math.pow(x,2)+math.pow(x,4)-math.pow(x,6)+math.pow(x,8)-math.pow(x,10)+math.pow(x,12)-math.pow(x,14)+math.pow(x,16)-math.pow(x,18),color = RED,x_min = -1.1,x_max=1.1)
        self.play(ShowCreation(equation))
        self.wait(1)

        dashLineLeft=DashedLine(start=ORIGIN+y_each_unit*5*UP,end=ORIGIN+y_each_unit*5*DOWN)
        dashLineRight=DashedLine(start=ORIGIN+y_each_unit*5*UP,end=ORIGIN+y_each_unit*5*DOWN)
        dashLineLeft.shift(ORIGIN+LEFT*x_each_unit)
        dashLineRight.shift(ORIGIN+RIGHT*x_each_unit)
        radiusLine=Line(start=ORIGIN,end=ORIGIN+RIGHT*x_each_unit)
        rangeLine=Line(start=ORIGIN+LEFT*x_each_unit,end=ORIGIN+RIGHT*x_each_unit)
        circle=Circle(radius=x_each_unit)
        movingPoint=Circle(radius=0.025)
        movingPoint.shift(ORIGIN+RIGHT*x_each_unit)
        circleEq1=self.get_graph(lambda x:math.sqrt(1-x**2),color=BLUE,x_max=-1,x_min=1)
        circleEq2=self.get_graph(lambda x:-math.sqrt(1-x**2),color=BLUE,x_max=1,x_min=-1)

        self.play(Write(dashLineLeft),Write(dashLineRight))
        self.wait(1)

        equation_updated=self.get_graph(lambda x : 1-math.pow(x,2)+math.pow(x,4)-math.pow(x,6)+math.pow(x,8)-math.pow(x,10)+math.pow(x,12)-math.pow(x,14)+math.pow(x,16)-math.pow(x,18),color = GREEN,x_min = -1,x_max=1)
        self.play(FadeOut(self.axes),ReplacementTransform(equation,equation_updated))
        self.wait(0.5)
        self.play(Write(radiusLine))
        self.play(MoveAlongPath(movingPoint,circleEq1))
        self.play(MoveAlongPath(movingPoint,circleEq2))
        self.play(FadeIn(circle))
        self.wait(1)

        radiusText=TextMobject("Radius of convergence")
        radiusText.scale(0.14)
        radiusText.shift(ORIGIN+RIGHT*x_each_unit*0.45+DOWN*y_each_unit*0.2)
        #self.activate_zooming(animate=True)
        self.play(Write(radiusText))
        self.wait(0.6)

        self.camera_frame.save_state()
        self.play(self.camera_frame.set_width,5.5)
        self.wait(1)
        self.play(self.camera_frame.set_width,14)
        self.wait(1.3)

        self.play(FadeOut(radiusText),FadeOut(circle),FadeOut(movingPoint))
        extendLine=Line(start=ORIGIN,end=ORIGIN+x_each_unit*LEFT)
        self.play(Write(extendLine))
        doubleArrow=TextMobject("$\longleftrightarrow$")
        doubleArrow.scale(1.6)
        doubleArrow.set_color(BLUE)
        doubleArrow.shift(ORIGIN+DOWN*y_each_unit*0.5)
        self.play(FadeIn(doubleArrow))
        self.wait(1)
        rangeText=TextMobject("Interval of convergence")
        rangeText.scale(0.15)
        rangeText.shift(ORIGIN+y_each_unit*DOWN)
        self.play(Write(rangeText))
        self.wait(0.6)

        self.camera_frame.save_state()
        self.play(self.camera_frame.set_width,5.5)
        self.wait(1)
        self.play(self.camera_frame.set_width,14)
        self.wait(1.3)
        # self.camera_frame.save_state()
        # self.camera_frame.set_width(5.5)
        # self.play(self.camera_frame.move_to, ORIGIN)
        # self.wait(1)
        # self.camera_frame.set_width(14)
        # self.wait(1.5)
