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
        "Func":lambda x :  1+x**1.3*np.exp(-.12*(x-2)**2)*np.sin(x/4),
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
        
        self.get_vector_field()
        
        
        self.play(ShowCreation(VGroup(curve,curve_label)))
        self.wait(.6)
        self.break_in_arcs()
        self.show_the_sum()
        
        self.wait(2)
        
        
    def get_vector_field(self):
        func = lambda v: np.array([
            v[0],  # x
            -v[1],  # y
            0        # z
        ])
        vector_field= VectorField(
            func,
            delta_x=1,
            delta_y=1,
            colors=[GREEN_A,GREEN_C],
            length_func= lambda norm: .8*sigmoid(norm),
            vector_config={
            "stroke_width": 2
            }
        )
        
        self.vector_field= vector_field
        
        
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
        
        evaluate_text=TextMobject("$\\vec F(x,y)$ ", "is evaluated").next_to(at_any_points_text,DOWN)
        evaluate_text.set_color_by_tex("$\\vec F(x,y)$",ORANGE)
        
        multiply_text=TextMobject("...is multiplied with ","$\\Delta s_i$") 
        multiply_text.set_color_by_tex("\\Delta s_i", BLUE)
        multiply_text.next_to(at_any_points_text,DOWN)
        
        
        
        self.at_any_points_text=at_any_points_text
        self.evaluate_text=evaluate_text
        self.multiply_text=multiply_text
        
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
        self.dots=dots
        
        self.wait()
        self.show_the_dot_product()
        self.multiply_with_ds()
        self.construct_equation()
        
            
    def show_the_dot_product(self):
        index=-(len(self.points)//3)
        self.index=index
        
        dot=self.dots[index]
        
        
        dot_prod_text=TextMobject("Dot Product of", "$\\vec F(x_i,y_i)$", "and","$\\vec T(x_i,y_i)$") 
        dot_prod_text.set_color_by_tex_to_color_map({
            "\\vec F(x_i,y_i)":ORANGE , 
            "\\vec T(x_i,y_i)":  "#DC75CD" ,
        })
        dot_prod_text.to_edge(TOP,buff=SMALL_BUFF)
        
        
        point_coord=TextMobject("$(x_i,y_i)$",color=YELLOW)
        point_coord.next_to(dot,DL,buff=.01).scale(.8)
        
        func_val=TextMobject("$\\vec F(x_i,y_i)$",color=ORANGE)
        func_val.next_to(dot,UR).scale(.8)
        
        self.dot_prod_text=dot_prod_text
        self.func_val=func_val
        
        dot.set_color(ORANGE).scale(1.2)
        
                
        self.play(FadeIn(VGroup(point_coord,dot)))
        self.play(Write(self.evaluate_text))
        self.wait(1)
        self.play(FadeOut(self.vector_field))
        self.get_vector_and_tangent()
        self.dot_product()
        
         
        self.wait(2)
        self.remove(point_coord)  
        
    
    def get_vector_and_tangent(self):
        dot=self.dots[self.index]
        self.show_specific_vectors(dot)
        self.play(Write(self.func_val))
        self.wait(1)
        self.show_tangent(dot)
        self.play(FadeIn(VGroup(*[
            dot.set_color(ORANGE).scale(1.4)
                for dot in self.dots ]
        )))
        
        
    def show_specific_vectors(self,dots):
        for dot in dots:
            vector=self.vector_field.get_vector(dot.get_center()) 
            vector.set_color(ORANGE)

            self.play(Write(vector),run_time=.2)

        
    def show_tangent(self,dot):
        tangent_sym=TextMobject("$\\vec T(x_i,y_i)$",color="#DC75CD").scale(.8)
        x=dot.get_center()
        angle=self.angle_of_tangent( 
             self.point_to_coords(x)[0],
             self.curve, 
             dx=0.01
        )
        vect = Vector().rotate(angle,about_point=x)
        vect.set_color("#DC75CD")
        tangent=vect.next_to(x,DR,buff=0)
        tangent_sym.next_to(tangent,DOWN,buff=.1)
        self.play(Write(VGroup(tangent,tangent_sym)))
        
        self.tangent_sym=tangent_sym
         
    def dot_product(self):
        
        dot_sym=Dot().next_to(self.func_val,RIGHT)
        
        self.play(FadeOut(VGroup(
            self.at_any_points_text,
            self.evaluate_text
        )))
        self.play(Write(self.dot_prod_text))
        self.play(
            FadeIn(dot_sym),
            ApplyMethod(
            self.tangent_sym.next_to,
            dot_sym, RIGHT
        ))

        self.dot_sym=dot_sym
        
    def multiply_with_ds(self):
        self.get_ds()
        
        self.play(GrowFromCenter(self.ds_brace_group))
        self.wait(2)
        self.play(Write(self.multiply_text))
        self.play(ApplyMethod(
            self.ds_brace_label.next_to,
            self.tangent_sym, RIGHT,buff=.15
        ))
    


    def get_ds(self):
        p1= self.dots[self.index]
        p2= self.dots[self.index+1]
        ds_brace=Brace(VGroup(p1,p2),DL)
        ds_brace.move_to(p1,UR)
        ds_brace_label=ds_brace.get_text("$\Delta s_i$", buff = .05)
        ds_brace_label.set_color(BLUE)
        self.ds_brace=ds_brace
        self.ds_brace_label=ds_brace_label
        self.ds_brace_group=VGroup(ds_brace,ds_brace_label)
        
        
    def construct_equation(self):
        sum_up_text=TextMobject("and"," summed ", "for all i' s")
        sum_up_text.set_color_by_tex("summed",PURPLE_A)
        sum_up_text.next_to(self.multiply_text,DOWN,buff=MED_SMALL_BUFF)
        sum_up_text.shift(LEFT)

        sum_eqn=TextMobject("$$\\sum_i^{ } $$").set_color(PURPLE_A)
        sum_eqn.move_to(self.graph_origin+6.5*self.X+4*self.Y)
        
        line_integral_text=TextMobject("The Value of the"," line ","integral is").to_edge(TOP,buff=MED_SMALL_BUFF)
        line_integral_text.set_color_by_tex("line",BLUE_C)
        approx=TextMobject("$\\approx$",color=RED).next_to(sum_eqn,LEFT)
        multipled=VGroup(
            self.func_val,
            self.dot_sym,
            self.tangent_sym,
            self.ds_brace_label
        )


        self.play(Write(sum_up_text))
        self.show_specific_vectors(self.dots)
        self.play(FadeIn(sum_eqn))
        self.play(ApplyMethod(
            multipled.next_to,sum_eqn,RIGHT
        ))
        self.wait()
        self.play(FadeOut(VGroup(
            self.dot_prod_text,
            self.multiply_text,
            sum_up_text
        )))
        self.play(Write(line_integral_text))
        self.play(FadeIn(approx))
        
        
        
#uploaded by Somnath Pandit.FSF2020_Line Integrals


       
