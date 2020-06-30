from manimlib.imports import *
import math

def func(x):
    return math.pow(x,3)-2*math.pow(x,2)-x+3

class graphScene(GraphScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 3,
        "y_min": -4,
        "y_max": 4,
        "x_tick_frequency": 0.2,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": BLUE,
        "x_axis_label": "$t$",
        "y_axis_label": "$f(t)$",
        "exclude_zero_label": True,
        "x_labeled_nums": range(-3, 4, 1),
        "y_axis_height": 5,
        "x_axis_width": 9,
    }

    def construct(self):
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)   

        fx=TextMobject("$f(t) = { t }^{ 3 }{ -2t }^{ 2 }-t+3$").set_color(RED).to_corner(UP+RIGHT).scale(0.4)
        self.setup_axes(animate=True,scalee=1)
        function=self.get_graph(lambda x:math.pow(x,3)-2*math.pow(x,2)-x+3,color=RED,x_min=-1,x_max=2)
        functionArea=self.get_riemann_rectangles(function,x_min=-1,x_max=2,dx=0.01,start_color=GREEN,end_color=YELLOW,stroke_color=GREEN,fill_opacity=0.8)
        functionDot=Dot(point=self.graph_origin,radius=0.065,color=WHITE)
        aboveText1=TextMobject("Continuous","Time Function").shift(4*RIGHT+2*UP).scale(0.4).set_color_by_tex_to_color_map({"Continuous":YELLOW,"Time Function":BLUE})
        aboveText2=TextMobject("Discrete","Time Function").shift(4*RIGHT+2*UP).scale(0.4).set_color_by_tex_to_color_map({"Time Function":BLUE,"Discrete":YELLOW})

        bottomText1=TextMobject("Instead of considering the","function","over the","entire $t$,").shift(4.5*RIGHT+3*DOWN).scale(0.4).set_color_by_tex_to_color_map({"entire $t$,":RED,"function":YELLOW})
        bottomText2=TextMobject("We consider only at","certain $t$").shift(4.5*RIGHT+3*DOWN).scale(0.4).set_color_by_tex_to_color_map({"certain $t$":RED})
        
        self.play(ShowCreation(function),Write(fx),FadeIn(aboveText1))
        self.wait(0.7)
        self.play(Write(bottomText1))
        self.play(ShowCreation(functionArea),MoveAlongPath(functionDot,function))
        self.wait(0.7)
        self.play(FadeOut(bottomText1))
        self.play(Write(bottomText2),FadeOut(aboveText1))
        
        dots=[Dot(radius=0.05) for i in range(10)]
        dotShifts=[-1,-0.7,-0.4,0,0.3,0.6,1,1.3,1.6,2]
        lines=[]
        for x in dotShifts:
            lines.append(Line(start=(x*x_each_unit,func(x)*y_each_unit,0),end=(x*x_each_unit,0,0),color=GREEN))
        for i in range(10):
            dots[i].shift(ORIGIN+RIGHT*x_each_unit*dotShifts[i]+y_each_unit*UP*func(dotShifts[i]))
        updatedGraph=VGroup(dots[0],
                            dots[1],
                            dots[2],
                            dots[3],
                            dots[4],
                            dots[5],
                            dots[6],
                            dots[7],
                            dots[8],
                            dots[9])
        updatedGraph1=VGroup(
                            lines[0],
                            lines[1],
                            lines[2],
                            lines[3],
                            lines[4],
                            lines[5],
                            lines[6],
                            lines[7],
                            lines[8],
                            lines[9])

        self.play(FadeOut(functionDot))
        self.play(FadeOut(function),FadeIn(updatedGraph))
        self.play(FadeOut(functionArea),FadeIn(updatedGraph1))
        self.play(FadeOut(bottomText2),FadeIn(aboveText2))
        self.wait(2)