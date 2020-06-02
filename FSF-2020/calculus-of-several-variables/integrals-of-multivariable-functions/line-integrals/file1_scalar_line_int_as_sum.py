from manimlib.imports import *


class LineIntegrationAsSum(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 10,
        "y_min" : 0,
        "y_max" : 6,
        "graph_origin": ORIGIN+5*LEFT+3*DOWN,
        "x_axis_width": 10,
        "y_axis_height": 6 ,
        "x_tick_frequency": 2,
        "y_tick_frequency": 2,
        "Func":lambda x : 1+x**1.3*np.exp(-.12*(x-2)**2)*np.sin(x/4),
        "a": 1 ,"b": 9, "n": 15,
    }  

    def construct(self):
        X = RIGHT*self.x_axis_width/(self.x_max- self.x_min)
        Y = UP*self.y_axis_height/(self.y_max- self.y_min)
        self.X=X ;self.Y=Y
        
        self.setup_axes(animate=False)
        
        curve=self.get_graph(
            self.Func, 
            x_min=self.a,
            x_max=self.b,
        )
        curve.set_color([BLACK,BLUE,BLUE,BLUE,BLACK])
        curve_label= self.get_graph_label(
            curve,
            label="\\text{path of intgration}",
            x_val=4,
            direction=UR,
            buff=.6,
            color=BLUE
        )
        self.curve=curve
        self.curve_label=curve_label
        
        self.play(ShowCreation(VGroup(curve,curve_label)))
        self.wait(.6)
        self.break_in_arcs()
        self.show_the_sum()
        self.construct_equation()
        self.wait(2)
        
        
    
    def break_in_arcs(self):
        
        self.write_about_breaking()
        
        dl=0.8
        self.get_breakers(dl)
        self.wait(2)
        self.play(FadeOut(self.upto_break_text))
        self.dl=dl
    
    def write_about_breaking(self):
        breaking_text=TextMobject("\\texttt{..broken}"," into small", "subarcs")
        breaking_text.set_color_by_tex_to_color_map({
            "broken":RED,"subarcs": BLUE 
        })
        breaking_text.next_to(self.curve_label,DOWN)
        breaking_text.align_to(self.curve_label,LEFT)
        self.play(
            Write(breaking_text)
        )  
         
        self.upto_break_text=VGroup(
            self.curve_label,
            breaking_text,
        )
        
    def get_breakers(self,dl):
        point=self.a
        points=[]
        while point<(self.b-dl) :
            start=point
            end=point+dl
            points += [end]
            breaker=Line(
                self.input_to_graph_point(start,self.curve),
                self.input_to_graph_point(end,self.curve),
                stroke_width=2,
                color=RED,
            )
            breaker.rotate(PI/2).scale(.5)
         
            point=end
            self.play(FadeIn(breaker),run_time=.2)
          #  self.add(breaker)
           
        del points[-1]
        self.points=points
        
            
    def show_the_sum(self):
        at_any_points_text=TextMobject("At any ","point", "in each ", "subarc")
        at_any_points_text.set_color_by_tex_to_color_map({
            "point":YELLOW , "subarc": BLUE
        })  
        at_any_points_text.to_edge(TOP,buff=SMALL_BUFF)
        
        evaluate_text=TextMobject("$f(x,y)$ ", "is evaluated").next_to(at_any_points_text,DOWN)
        evaluate_text.set_color_by_tex("$f(x,y)$",ORANGE)
        
        self.at_any_points_text=at_any_points_text
        self.evaluate_text=evaluate_text
        
        
        dots=[]
        for point in self.points:
        
            dot=Dot(
              point=self.input_to_graph_point(point,self.curve),
              radius= .7*DEFAULT_DOT_RADIUS,
              stroke_width= 0,
              fill_opacity= 1.0,
              color= YELLOW,
            )
            dots+=[dot]
        
        self.play(
            Write(at_any_points_text),
            FadeIn(VGroup(*dots)),run_time=1.5
        )
        self.wait()
        self.position_of_point_irrelevent()
        self.multiply_with_function(dots)
        
        
            
    def multiply_with_function(self,dots):
        index=-(len(self.points)//3)
        dot=dots[index]
        
        
        multiply_text=TexMobject("f(x_i,y_i)", "\\text{ is multiplied with }","\\Delta s_i") 
        multiply_text.set_color_by_tex_to_color_map({
            "f(x_i,y_i)":ORANGE , "\\Delta s_i": BLUE
        })
        multiply_text.to_edge(TOP,buff=MED_SMALL_BUFF)
        
        point_coord=TextMobject("$(x_i,y_i)$",color=YELLOW)
        point_coord.next_to(dot,DL,buff=.01).scale(.8)
        
        func_val=TextMobject("$f(x_i,y_i)$",color=ORANGE)
        func_val.next_to(dot,UR)
        
        sum_up_text=TextMobject("and "," summed ", "for all i' s")
        sum_up_text.set_color_by_tex("summed",PURPLE)
        sum_up_text.next_to(multiply_text,DOWN)
        
        dot.set_color(ORANGE).scale(1.2)
        
        self.play(FadeIn(VGroup(
            point_coord,dot
        )))
        self.play(Write(self.evaluate_text))
        self.play(Write(func_val))
        self.play(FadeIn(VGroup(*[
            dot.set_color(ORANGE).scale(1.4)
                for dot in dots ]
        )))
        self.wait(2)
        self.remove(point_coord)
        self.get_ds(dots,index)
        self.play(GrowFromCenter(self.ds_brace_group))
        self.wait(2)
        self.play(FadeOut(VGroup(
            self.ds_brace,
            self.at_any_points_text,
            self.evaluate_text
        )))
        self.play(Write(multiply_text))
        self.play(ApplyMethod(
            self.ds_brace_label.next_to,
            func_val, RIGHT,buff=.2
        ))
        self.play(Write(sum_up_text))
        
        self.func_val=func_val
        self.sum_text_group=VGroup(multiply_text,sum_up_text)
        
    def position_of_point_irrelevent(self):
        pass  
        
        
        
    def get_ds(self,dots,index):
        p1= dots[index]
        p2= dots[index+1]
        ds_brace=Brace(VGroup(p1,p2),DL)
        ds_brace.move_to(p1,UR)
        ds_brace_label=ds_brace.get_text("$\Delta s_i$", buff = .05)
        ds_brace_label.set_color(BLUE)
        self.ds_brace=ds_brace
        self.ds_brace_label=ds_brace_label
        self.ds_brace_group=VGroup(ds_brace,ds_brace_label)
        
        
    def construct_equation(self):
        sum_eqn=TextMobject("$$\\sum_i^{ } $$").set_color(PURPLE)
        sum_eqn.move_to(self.graph_origin+7*self.X+4*self.Y)
        
        line_integral_text=TextMobject("The Value of the line integral is").next_to(self.sum_text_group,IN)
        approx=TextMobject("$\\approx$",color=RED).next_to(sum_eqn,LEFT)
        multipled=VGroup(self.func_val,self.ds_brace_label)
        self.play(FadeIn(sum_eqn))
        self.play(ApplyMethod(
            multipled.next_to,sum_eqn,RIGHT
        ))
        self.wait()
        self.play(FadeOut(self.sum_text_group))
        self.play(Write(line_integral_text))
        self.play(FadeIn(approx))
        
        
        
#uploaded by Somnath Pandit.FSF2020_Line Integrals


       
