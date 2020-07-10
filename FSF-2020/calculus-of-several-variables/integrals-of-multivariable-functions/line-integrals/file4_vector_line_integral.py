from manimlib.imports import *

class LineIntegrationProcess(GraphScene):

    CONFIG = {
        "x_min" : -0,
        "x_max" : 1,
        "y_min" : -0,
        "y_max" : 1,
        "axes_color":WHITE,
        "graph_origin": ORIGIN+6.3*LEFT+3*DOWN,
        "x_axis_width": 5.5,
        "y_axis_height": 5.5,
        "x_tick_frequency": 1,
        "y_tick_frequency": 1,
        "default_vector_field_config": {
            "delta_x": .5,
            "delta_y": .5,
            "min_magnitude": 0,
            "max_magnitude": 15,
            "colors": [BLUE],
            "length_func": lambda norm : norm/35,
            "opacity": 1.0,
            "vector_config": {
                "stroke_width":2
            },
        },
        "default_graph_style": {
            "stroke_width": 2,
            "stroke_color": WHITE,
        },
    }


    def construct(self):
        X = RIGHT*self.x_axis_width/(self.x_max- self.x_min)
        Y = UP*self.y_axis_height/(self.y_max- self.y_min)
        self.X=X ;self.Y=Y
        
        self.setup_axes(animate=False)
    
        fn_text=TexMobject(
            r"\vec F = x^2\hat i-xy\hat j",
            stroke_width=2.5
        ).set_color_by_gradient(
            *self.default_vector_field_config["colors"]
        )
        fn_text.to_edge(TOP,buff=.1).shift(2*LEFT)
        
        origin=self.graph_origin
        v_field=self.get_vector_field(
            lambda v: np.array([
            (v[0]-origin[0])**2,
            -(v[0]-origin[0])*(v[1]-origin[1]),  
            0,
            ]),
            x_min= -.001+origin[0],
            x_max= 5.4+origin[0],
            y_min= -0+origin[1],
            y_max= 5.5+origin[1],
        )
         
        self.add(v_field, fn_text)
        self.play(Write(fn_text))
        self.wait(2)
        self.get_line_of_int()
        self.get_dot_product_values()
        self.wait(2)
        self.remove(v_field,fn_text)
        self.write_area_as_intgral_value()
        self.wait(2)
            
            
    def get_vector_field(self,func,**kwargs):
        config = dict()
        config.update(self.default_vector_field_config)
        config.update(kwargs)
        vector_field= VectorField(func,**config)
        self.vector_field=vector_field
        
        return vector_field
        
    def get_line_of_int(self): 
        line_of_int_text=TextMobject(
            r"Line of integration is\\",
            "$\\vec r(t)=\cos(t)\hat i+\sin(t)\hat j$"
        )
        line_of_int_text[1].set_color(PINK)
        line_of_int_text.to_corner(UR,buff=.8)
        
        
        line_of_int= self.get_graph(
            lambda x : np.sqrt(1-x**2),
            x_min=1,
            x_max=0,
        )
        line_of_int.set_style(
            stroke_width=3,
            stroke_color=PINK,
        )
        
        self.play(Write(line_of_int_text))
        self.wait(.5)
        self.play(ShowCreation(line_of_int),run_time=2)
     #   self.add(line_of_int)
        
        self.line_of_int=line_of_int
        self.line_of_int_text=line_of_int_text
        
        
    def get_dot_product_values(self):
        t_tracker = ValueTracker(0)
        self.t_tracker = t_tracker  
        self.get_vector_and_tangent()
        self.get_dot_product_graph()
        self.wait(1.5)
        self.play(ApplyMethod(
            self.t_tracker.set_value, PI/6,
                rate_func=linear,
                run_time=2.5,
            ) 
        )
        self.wait(1)
        self.play(ApplyMethod(
            self.t_tracker.set_value, PI/2,
                rate_func=linear,
                run_time=4,
            ) 
        )
        self.dot_prod_graph.suspend_updating()
        
    def get_vector_and_tangent(self):
        vect_tangent_text=TextMobject(
            "Get the"," vector",r" and\\"," tangent",
            " on the"," line"
        )
        vect_tangent_text.set_color_by_tex_to_color_map({
            "tangent": ORANGE, "vector": YELLOW, "line":PINK
        })
        vect_tangent_text.to_corner(UR,buff=.8)
        self.vect_tangent_text= vect_tangent_text
        
        self.play(FadeOut(self.axes))
        self.remove(self.line_of_int_text)
        self.play(Write(vect_tangent_text))
        self.show_vector()
        self.show_tangent()
        self.wait(1.3)
        
    def show_vector(self):
        t = self.t_tracker.get_value
        vect_label=TextMobject(
            "$\\vec F(x_i,y_i)$",
            color=YELLOW,
            stroke_width=2
        ).scale(.8)
        
        vector = always_redraw( lambda: 
            self.vector_field.get_vector(
                self.coords_to_point(
                np.cos(t()), np.sin(t())
                ),
                stroke_width=6,
                max_stroke_width_to_length_ratio= 8,
            ).set_color(YELLOW),
        )
        
        vect_label.next_to(vector,RIGHT,buff=.1)
        vector_group= VGroup(vector,vect_label)
        
    #    self.add(vector_group)
        self.play(Write(vector_group),run_time=1)
        self.wait(.4)
        
        self.vect_label = vect_label
        self.vector_group= vector_group
        
    def show_tangent(self):
        tangent_label=TextMobject(
            "$\\vec T(x_i,y_i)$",
            color=ORANGE,
            stroke_width=2
        ).scale(.8)
        
        t = self.t_tracker.get_value
        
        tangent = always_redraw(lambda: 
            Vector(
                color=ORANGE,
                stroke_width=6,
                ).scale(1).next_to(
                self.coords_to_point(
                    np.cos(t()), np.sin(t())
                ),DR,buff=-.1
            ).rotate(
                self.angle_of_tangent(
                    np.cos(t()),
                    self.line_of_int, 
                    dx=-0.00001
                ),
                about_point=self.coords_to_point(
                    np.cos(t()), np.sin(t())
                )
            )
        )
        tangent_label.next_to(tangent,UP,buff=.1)
        tangent_group=VGroup(tangent,tangent_label)
        
    #    self.add(tangent_group)
        self.play(Write(tangent_group))
        self.wait(.6)
        
        self.tangent_label=tangent_label
        self.tangent_group=tangent_group
        
    def get_dot_product_graph(self):
        t = self.t_tracker.get_value
        
        self.start_x= 1.3 ; self.end_x=2.3
        
        t_axis= self.get_graph(
            lambda x : 2.0/5,
            x_min= self.start_x,
            x_max= self.end_x,
        ).set_style(
            stroke_width=4,
        )
        
        dot_prod_axis= Vector(3*UP).next_to(
            t_axis,LEFT,buff=-.1
        ).set_color(GREEN)
        dot_prod_label=TexMobject(
            "\\vec F","\\cdot","\\vec T",
            stroke_width= 1.5,
        ).next_to(dot_prod_axis,UP).scale(.8)
        dot_prod_label[0].set_color(YELLOW)
        dot_prod_label[2].set_color(ORANGE)
        
        dot_prod_graph_axes= VGroup(t_axis,dot_prod_axis)
        
        self.write_about_graph()
        self.wait(1)
     #   self.add(dot_prod_graph_axes)
        self.play(Write(dot_prod_graph_axes))
        self.show_the_parameter(t,t_axis)
        self.wait(.6)
        self.play(ReplacementTransform(
            self.vect_label,dot_prod_label[0]
        ))
        self.play(ReplacementTransform(
            self.tangent_label,dot_prod_label[1:3]
        ))
        self.show_graph_area(t_axis)
        
        self.dot_prod_graph_axes= dot_prod_graph_axes 
        self.dot_prod_label= dot_prod_label
        
    def write_about_graph(self):
        graph_text=TextMobject(
            "Graph",r" of the "," vector",r" $-$\\ ",
            r"tangent",r" dot product\\",
            " with the parameter ","$t$"
        )
        graph_text.set_color_by_tex_to_color_map({
            "Graph":GREEN, "vector": YELLOW,
            "tangent":ORANGE, "$t$":RED
        })
        graph_text.to_corner(UR,buff=.5)
        self.graph_text=graph_text
        
        self.remove(self.vect_tangent_text)
        self.play(Write(graph_text),run_time=4)
        
    def show_the_parameter(self,t,t_axis):
        t_dot=Dot(color=RED).next_to(t_axis,LEFT,buff=0)
        t_dot.add_updater(lambda obj : 
            obj.move_to(self.c2g([t(),0])
        ))
        t_text=TextMobject("$t$=").next_to(t_dot,UP,buff=.25)
        t_val=always_redraw(
            lambda: DecimalNumber(
                t()/PI,
                color=GOLD
                ).next_to(t_text,RIGHT,buff=0).scale(.8)
        )
        t_label=VGroup(
            t_text,t_val
        ).set_color(RED)
        
        
        pi = TexMobject(
            "\\pi ",
            color=GOLD,
        ).next_to(t_val,RIGHT,buff=0.05)
        t_label.add(pi)
        
        t_label.add_updater(lambda label : 
            label.next_to(t_dot,UP)
        )
        
        t_group=VGroup(t_dot,t_label)
        
      #  self.add(t_group)
        self.play(Write(t_group))
        
        self.t_group= t_group
    
        
    def show_graph_area(self,t_axis):
        t = self.t_tracker.get_value
        dot_prod_graph= always_redraw(lambda: Polygon(
            *[
            self.c2g([t,-2*np.cos(t)**2*np.sin(t)]) 
                for t in np.arange(0,t(),0.01)
            ],
            *[
             self.c2g([t,0])
                for t in [ t(),0 ] 
            ],
            stroke_width=2.5,
            fill_color=TEAL_D,
            fill_opacity=.6,
        ))
        
        self.add(dot_prod_graph)
        
        self.dot_prod_graph=dot_prod_graph
        
    def c2g(self,coord):
        """ get points for the dot product graph 
                from its coordinates"""
                
        return self.coords_to_point(
            self.start_x+coord[0]/(PI/2),
            2.0/5+coord[1]/2,
        )

    
    def write_area_as_intgral_value(self):
        area_text=TextMobject(
            "Value of the "," line"," integral in the",
            r"Vector field\\",
            "is equal to this ","area"
        )
        area_text.set_color_by_tex_to_color_map({
            "Vector field": BLUE, "line":PINK, "area":TEAL_C
        })
        area_text.to_edge(TOP,buff=MED_SMALL_BUFF)
        
        
        self.play(FadeOut(VGroup(
            self.line_of_int,
            self.vector_group,
            self.tangent_group,
            self.t_group,
            self.dot_prod_graph_axes,
            self.dot_prod_label,
            self.graph_text
            )
        ))
        area= self.dot_prod_graph.copy().scale(1.3)
        area.next_to(area_text,DOWN,buff=1.5)
        
      #  self.add(area_text)
        self.play(Write(area_text),run_time=4)
        self.play(ReplacementTransform(
            self.dot_prod_graph,
            area
        ))
        self.wait(.5)        
                    
  #uploaded by Somnath Pandit.FSF2020_Line_Integrals
  
  
