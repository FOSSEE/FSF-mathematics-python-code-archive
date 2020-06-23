from manimlib.imports import *

class CurvyRegion(GraphScene):
    CONFIG = {
    "x_min": 0,
    "x_max": 8,
    "y_min": 0,
    "y_max": 6,
    "graph_origin": ORIGIN+4.5*LEFT+3*DOWN,
    "x_labeled_nums": np.arange(0, 9,2),
    "y_labeled_nums": np.arange(0, 7,2),
    "x_axis_width": 6,
    "y_axis_height": 6,
    }
	
    def construct(self):
        XD = self.x_axis_width/(self.x_max- self.x_min)
        YD = self.y_axis_height/(self.y_max- self.y_min)
        self.X=XD*RIGHT ;self.Y=YD*UP
                
        sin_curve_points=[self.graph_origin+(2+.5*np.sin(2*y),y,0) 
            for y in np.arange(1,5,.005)]
        
        cos_curve_points=[self.graph_origin+(
            5+.5*np.cos(2*y),y,0)  
            for y in np.arange(1,5,.005)]
        cos_curve_points.reverse()
        
        region=Polygon(
            *sin_curve_points+cos_curve_points,
            color=YELLOW,
            stroke_width=1,  
            fill_color=BLUE_E,
            fill_opacity=.75
        )
        
        line=Line((1,0,0),(1,6,0),color=RED)
        line.move_to(self.graph_origin+2.5*self.X,DOWN)
        self.line=line
        self.setup_axes(animate = False)
        
        self.add(region)
        self.wait()
        self.first_y_int_scene()
        self.try_x_first_scene()
        
        
    def first_y_int_scene(self):
        talk=TextMobject(r"For doing the $y$ integration\\ first we need to set\\ proper $y$ limts").to_corner(UR,buff=LARGE_BUFF)
        problem=TextMobject(r"But here we get\\ more than two $y$ values\\ for a single $x$ value" ).to_corner(UR,buff=LARGE_BUFF)
        int_y=TextMobject("$$\\int_?^? dy$$").next_to(problem,DOWN,buff=.5)
        
        self.play(Write(talk))
        self.play(FadeIn(self.line))
        self.wait(2)
        self.play(ReplacementTransform(talk,problem))
        self.play(
            ApplyMethod(self.line.shift,3.7*self.X),
            run_time=4
        )
        self.wait()
        self.play(Write(int_y))
        self.wait(3)
        self.play(FadeOut(VGroup(problem,int_y,self.line)))

    def try_x_first_scene(self):
        try_text=TextMobject(r"But if we try to integrate\\ along $x$ first ...." ).to_corner(UR,buff=LARGE_BUFF)
        good_limits=TextMobject(r"For one $y$ value we get\\ only \textbf{two} $x$ values $\dots$").to_corner(UR,buff=LARGE_BUFF)
        limit_values= TextMobject(r"one Lower limit\\ one Upper limit ").next_to(good_limits,DOWN,buff=.5)
        int_x=TextMobject("$$\\int_{f(y)}^{g(y)} dx$$").next_to(limit_values,DOWN)
        
        self.setup_line()
        self.play(Write(try_text))
        self.play(FadeIn(self.line))
        self.wait()
        self.play(ReplacementTransform(try_text,good_limits))
        self.wait()
        self.play(
            ApplyMethod(self.line.shift,3*self.Y),
            run_time=4
        )
        self.play(Write(limit_values))
        self.wait()
        self.show_functions()
        self.play(Write(int_x))
        self.wait(3)
        
    def setup_line(self):
        line=self.line.rotate(PI/2)
        line.move_to(self.graph_origin+.5*self.X+1.5*self.Y,LEFT)
        self.line=line
        
    def show_functions(self):
        fy=TextMobject("$$f(y)$$")
        gy=TextMobject("$$g(y)$$")
        fy.move_to(self.graph_origin+2*self.X+3.3*self.Y)
        gy.move_to(self.graph_origin+7*self.X+2*self.Y)
        self.play(FadeIn(VGroup(fy,gy)))
        
        
  #uploaded by Somnath Pandit.FSF2020_Fubini's_Theorem   

