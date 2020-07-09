from manimlib.imports import *

class LineIntegrationProcess(GraphScene):

    CONFIG = {
        "x_min" : -0,
        "x_max" : 1,
        "y_min" : -0,
        "y_max" : 1,
        "axes_color":WHITE,
        "graph_origin": ORIGIN+6.5*LEFT+3*DOWN,
        "x_axis_width": 6,
        "y_axis_height": 6,
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
        fn_text.to_corner(UR,buff=.8).shift(2*LEFT)
        
        origin=self.graph_origin
        v_field=self.get_vector_field(
            lambda v: np.array([
            (v[0]-origin[0])**2,
            -(v[0]-origin[0])*(v[1]-origin[1]),  
            0,
            ]),
            x_min= -.001+origin[0],
            x_max= 5.8+origin[0],
            y_min= -0+origin[1],
            y_max= 6.+origin[1],
        )
        
     #   self.play(Write(surface))  
     #   self.play(Write(v_field),Write(fn_text))
        self.add(v_field, fn_text)
        self.get_line_of_int()
        self.get_dot_product_values()
        '''self.get_field_values_on_line()
        self.wait(1.5)
   
        self.remove(surface)
        self.trasform_to_graphs()'''
        self.wait(2)
            
            
    def get_vector_field(self,func,**kwargs):
        config = dict()
        config.update(self.default_vector_field_config)
        config.update(kwargs)
        vector_field= VectorField(func,**config)
        self.vector_field=vector_field
        
        return vector_field
        
    def get_line_of_int(self): 
        line_of_int_text=TextMobject(r"Line of integration is\\","$\\vec r(t)=\cos(t)\hat i+\sin(t)\hat j$")
        line_of_int_text[1].set_color(PINK)
        line_of_int_text.to_edge(TOP,buff=SMALL_BUFF)
        
        
        line_of_int= self.get_graph(
            lambda x : np.sqrt(1-x**2),
            x_min=1,
            x_max=0,
        )
        line_of_int.set_style(
            stroke_width=3,
            stroke_color=PINK,
        )
        
      #  self.play(Write(line_of_int_text))
        self.wait(.5)
      #  self.play(ShowCreation(line_of_int),run_time=1.5)
        self.add(line_of_int)
        
        self.line_of_int=line_of_int
        self.line_of_int_text=line_of_int_text
    
    def get_dot_product_values(self):
        t_tracker = ValueTracker(0)
        self.t_tracker = t_tracker  
        self.get_vector_and_tangent()
        self.get_dot_product_graph()
        self.wait(1.5)
        self.play(ApplyMethod(
            self.t_tracker.set_value, PI/2,
                rate_func=linear,
                run_time=2,
            ) 
        )
        
    def get_dot_product_graph(self):
        pass
        
            
    def get_vector_and_tangent(self):
        self.play(FadeOut(self.axes))
        self.show_vector()
        self.show_tangent()
        
        
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
        vector.set_color(ORANGE)
        vect_label.next_to(vector,RIGHT,buff=.1)
        self.add(vector,vect_label)
       # self.play(Write(vector),run_time=.2)
        
        self.vect_label = vect_label
        
    def show_tangent(self):
        tangent_label=TextMobject("$\\vec T(x_i,y_i)$",color="#DC75CD",stroke_width=2).scale(.8)
        
        t = self.t_tracker.get_value
        
        tangent = always_redraw(lambda: 
            Vector(
                color="#DC75CD",
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
        self.play(Write(VGroup(tangent,tangent_label)))
        
        self.tangent_label=tangent_label
         
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
    
    

    def get_curve(self,func,on_surface=False ,**kwargs):
        config = dict()
        config.update(self.default_graph_style)
        config.update({
            "t_min": 0,
            "t_max": PI/2,
        })
        config.update(kwargs)
        r=1
        curve=ParametricFunction(
            lambda t: self.coords_to_point(
                r*np.cos(t), 
                r*np.sin(t),
            ),
            **config,
        )
        return curve
        
    
     #-------------------------------------------------------       
    def trasform_to_graphs(self):        
        on_surface_graph=(self.get_graph(
            self.Func,on_surface=True
        ))
        on_surface_graph.set_style(
            stroke_width=5,
            stroke_color=YELLOW,
        ) 
        
        line_graph=(self.get_graph(
            self.Func,on_surface=False
        ))
        line_graph.set_style(
            stroke_width=5,
            stroke_color=PINK,
        )
        
        self.on_surface_graph=on_surface_graph
        self.line_graph=line_graph
        graph_area=self.get_area(graph=True) 
        
        into_graph=[
            ReplacementTransform(
            self.values_on_surface,
            on_surface_graph
            ),
            ReplacementTransform(
            self.line_of_int,
            line_graph
            ),
            ReplacementTransform(
            self.area,
            graph_area
            ),
        ]
            
    def get_area(self):
        
        area =Polygon(
            *[
            on_surface.get_point_from_function(t)
                for t in np.arange(0,PI,0.01)
            ],
            *[
             on_base.get_point_from_function(t)
                for t in np.arange(PI,0,-0.01)
            ],
            stroke_width=0,
            fill_color=TEAL_A,
            fill_opacity=.6,
        )

        return area
        
     
    
                    
  #uploaded by Somnath Pandit.FSF2020_Line_Integrals
