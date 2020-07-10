from manimlib.imports import *
import math

class uniformlyConvergent(Scene):
    def construct(self):
        introText2=TextMobject("Let","$g(x)=\\frac { 1 }{ 1+{ x }^{ 2 } }$","and","x=0.5 $\in$(-1,1)")
        introText3=TextMobject("Lets analyse..","!")
       
        introText2.scale(0.7)
        introText3.scale(0.9)
        introText3.shift(DOWN)
 
        introText2.set_color_by_tex_to_color_map({"$g(x)=\\frac { 1 }{ 1+{ x }^{ 2 } }$":BLUE,"x=0.5 $\in$(-1,1)":YELLOW})
        introText3.set_color_by_tex_to_color_map({"!":GREEN})
        self.play(Write(introText2))
        self.play(FadeIn(introText3))
        self.wait(2)


def gety(x,n):
    ans=0
    for i in range(0,n+1):
        if(i%2==0):
            ans+=(math.pow(x,2*i))
        else:
            ans-=(math.pow(x,2*i))
    return ans

def makeSeries(x,points,x_each_unit,y_each_unit):
    p=0
    for point in points:
        y=gety(x,p)
        point.shift(ORIGIN+RIGHT*x_each_unit*p+UP*y_each_unit*y)
        p+=1

def makeLines(x,numPoints,x_each_unit,y_each_unit):
    lines=[0]*numPoints
    for i in range(0,numPoints-1):
        y=gety(x,i)
        y_next=gety(x,i+1)
        lines[i]=Line(start=ORIGIN+RIGHT*x_each_unit*i+UP*y_each_unit*y,end=ORIGIN+RIGHT*x_each_unit*(i+1)+UP*y_each_unit*y_next,color=RED)
    return lines

class graphScene(GraphScene,ZoomedScene):
    CONFIG = {
        "x_min": -6,
        "x_max": 6,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_axis_label": "$k$",
        "y_axis_label": "$f(\\frac{1}{2})_k$",
        "exclude_zero_label": True,
        "x_axis_width":7,
        "y_axis_height":7,
        "zoomed_camera_frame_starting_position": 0.5*UP+0.5*RIGHT,
        "zoom_factor": 0.4,    
    }
    
    def setup(self):
        GraphScene.setup(self)
     
        ZoomedScene.setup(self)


    def construct(self):
        x_each_unit = self.x_axis_width / (self.x_max - self.x_min)
        y_each_unit = self.y_axis_height / (self.y_max - self.y_min)
        sequence=TextMobject("$1$ , $1-(0.5)^2$ , $1-(0.5)^2+(0.5)^4..$")
        sequence.set_color(RED)
        sequence.scale(0.35)
        sequence.to_edge(UP+RIGHT)
        formula=TextMobject("$f(x)_{ k }=\sum _{ i=0 }^{ k }{ (-1)^{ i }(x)^{ 2i } } $")
        formula.set_color(PURPLE_C)
        formula.scale(0.4)
        formula.shift(5.3*RIGHT+3*UP)
        fLine=Line(start=ORIGIN+x_each_unit*6*LEFT,end=ORIGIN+x_each_unit*6*RIGHT)
        fLine.shift(ORIGIN+(4/5)*y_each_unit*UP)
        fLineText=TextMobject("$g(0.5)=\\frac { 4 }{ 5 } $")
        fLineText.set_color(RED)
        fLineText.scale(0.3)
        fLineText.shift(UP*1.2*y_each_unit+RIGHT*x_each_unit+4*LEFT)
        points=[Dot(radius=0.03,color=BLUE) for i in range(0,6)]
        makeSeries(0.5,points,x_each_unit,y_each_unit)
        lines=makeLines(0.5,6,x_each_unit,y_each_unit)

        func1=TextMobject("$g(x)=\\frac { 1 }{ 1+{ x }^{ 2 } }$")
        func2=TextMobject("x=0.5 $\in$(-1,1)")
        func1.scale(0.4)
        func2.scale(0.4)
        func1.shift(5.3*LEFT+3.3*UP)        
        func2.shift(5.3*LEFT+2.9*UP)
        self.add(func1)
        self.add(func2)

        self.add(sequence)
        self.add(formula)
        self.setup_axes(animate=True)
        self.play(Write(fLine))
        self.add(fLineText)
        for p in points:
            self.add(p)
        self.setup()
        self.activate_zooming(animate=True)
        for p in range(0,5):
            self.play(Write(lines[p]))
       
        
        self.wait(1)
        self.get_zoomed_display_pop_out_animation()

        explanation1=TextMobject("Since the series","converges","to")
        explanation1.set_color_by_tex_to_color_map({"converges":YELLOW})
        explanation2=TextMobject("$\\frac {4}{5}$")
        explanation2.set_color(BLUE)
        explanation3=TextMobject("Hence","$\\forall \epsilon>0$,","$\exists k$","such that,")
        explanation3.set_color_by_tex_to_color_map({"$\\forall \epsilon>0$":BLUE,"$\exists k$":YELLOW})
        explanation4=TextMobject("$\left| { f\left( \\frac { 1 }{ 2 }  \\right)  }_{ k }-\\frac { 4 }{ 5 }  \\right| <$","$\epsilon$")
        explanation4.set_color_by_tex_to_color_map({"$\epsilon$":RED})
        explanation1.scale(0.5)
        explanation3.scale(0.5)
        explanation1.shift(1.8*DOWN+3.5*RIGHT)
        explanation2.shift(2.4*DOWN+3.5*RIGHT)
        explanation3.shift(1.8*DOWN+3.5*RIGHT)
        explanation4.shift(2.4*DOWN+3.5*RIGHT)

        self.play(Write(explanation1))
        self.play(FadeIn(explanation2))
        self.wait(1)
        self.play(FadeOut(explanation1),FadeOut(explanation2))
        self.play(Write(explanation3))
        self.play(Write(explanation4))
        self.wait(2)
